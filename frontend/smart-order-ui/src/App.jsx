import { useState } from 'react'
import axios from 'axios';
import './App.css'

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if(!input.trim()) return;

    setMessages([...messages, {sender: 'User', text: input }]);

    try {
      const res = await axios.post('http://127.0.0.1:8000/chat', {'message': input});
      const reply = res.data.response;
      setMessages(msgs => [...msgs, {sender: 'Bot', text: reply}]);

    }catch(err){
       console.log(err);
       setMessages(msgs => [...msgs, {sender: 'Bot', text: 'Error Contacting server'}]);

    }

    setInput('');
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') sendMessage();
  };

  return (
    <div className="App">
      <h2>🩺 Pharma Smart Order Assistant</h2>
      <div className="chat-box">
        {messages.map((msg, idx) => (
          <div key={idx} className={msg.sender === 'User' ? 'user-msg' : 'bot-msg'}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <div className="input-area">
        <input
          type="text"
          placeholder="Type your order..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App
