import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from db import SessionLocal, Product

load_dotenv()

llm = ChatAnthropic(
    model_name="claude-3-haiku-20240307",
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True,
)

def process_user_command(message: str):
    """
     1. Send user message to Claude (Langchain conversation) to get a structured response.
     2. Parse the structured response (e.g action and product list)
     3. Query the DB for those products
     4. Return an order summary.
    """

    system_prompt = (
        "You are a helpful B2B order assistant."
        "when the user types a messages, you must respond in JSON format only with two fields:\n"
        "- action: string (e.g., 'reorder_previous', 'new_order')\n"
        "- items: array of objects with product_name and quantity.\n"
        "Example response:\n"
        "{\"action\":\"new_order\",\"items\":[{\"product_name\":\"gloves\",\"quantity\":5}]}"
    )

    full_prompt = f"{system_prompt}\n\nUser: {message}"

    raw_response = conversation.predict(input=full_prompt)

    print("[Debug] Raw response from claude:", raw_response)


    try:

        import json
        parsed = json.loads(raw_response)
        action = parsed.get("action", "")
        items = parsed.get("items", [])
        print("[DEBUG] Parsed items:", items)

    except Exception as e:
        print("[Error] could not parse Claude response:", e)
        return "Sorry, I could not understand your request. Please try again."
    

    db = SessionLocal()
    order_lines = []
    for item in items:
        product_name = item["product_name"]
        qty = item["quantity"]

        products = db.query(Product).filter(Product.name.ilike(f"%{product_name.lower()}%")).all()
        if products:
          for prod in products:
            if prod.stock >= qty:
                order_lines.append(f"{qty} x {prod.name} @ ${prod.price: .2f} each")

            else:
                order_lines.append(f"Sorry, only {prod.stock} units of {prod.name} available.")
            break
        else:
            order_lines.append(f"Product '{product_name}' not found in catalog")

    db.close()

    if order_lines:
        return f"Order summary:\n" + "\n".join(order_lines)
    else:
        return "No matching products found."