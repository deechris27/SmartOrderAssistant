# 🩺 Smart Order Assistant for B2B Pharma

An AI-powered order assistant POC built to showcase how **Generative AI** can enhance B2B pharma applications by providing a natural language interface for ordering medical supplies.

---

## 🚀 Features
✅ Accepts natural language orders like:  
> *"Order 3 syringes and 5 face shields"*  
✅ Matches products against the inventory database  
✅ Generates a detailed order summary  
✅ Frontend chat interface with React + Vite  
✅ Backend API with Python FastAPI  
✅ Database with SQLite and SQLAlchemy  
✅ Integrates with **Claude/Anthropic API** for natural language understanding  
✅ Ready to extend with SAP or ERP integrations

---

## 🌟 Business Value

💊 **Improves User Experience**  
B2B buyers (hospitals, clinics) can place orders conversationally instead of navigating complex product catalogs.

📈 **Faster Order Entry**  
Reduce manual errors and streamline large, repeated orders for medical consumables.

🤖 **Enhance Existing Platforms**  
Integrate easily with existing pharma ordering apps, adding AI-powered natural language ordering on top of your current workflows.

🔒 **Reduce Training Costs**  
Lower the learning curve for new buyers or staff by letting them type natural sentences instead of remembering product codes.

---

## 🛠 Tech Stack

**Frontend**  
- React (with Vite) for blazing-fast dev & build times
- Axios for HTTP calls

**Backend**
- Python 3.10+
- FastAPI REST API
- SQLAlchemy ORM
- SQLite database (PostgreSQL-ready for production)

**AI**
- Anthropic Claude API for LLM-powered natural language understanding
- (Works with OpenAI or other LLMs by swapping the integration)

**Dev Tools**
- Node 20+
- Python virtual environments
- Uvicorn for local FastAPI dev

---

## 📂 Project Structure

smartorderassistant/
├─ backend/
│ ├─ main.py # FastAPI entrypoint
│ ├─ chatbot.py # Claude integration & logic
│ ├─ db.py # SQLAlchemy models & session
│ ├─ seed_db.py # Seed products into DB
│ └─ inspect_db.py # Debug tool to view products
└─ frontend/
└─ smart-order-ui/ # React + Vite app

