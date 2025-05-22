import React, { useState } from 'react';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [chatLog, setChatLog] = useState([]);
  const [loading, setLoading] = useState(false); // NEW: loading state

  const sendMessage = async () => {
    if (!question.trim()) return;

    const userMessage = { user: 'You', text: question };
    setChatLog([...chatLog, userMessage]);
    setQuestion('');
    setLoading(true); // Show loading

    try {
      const response = await fetch(`http://127.0.0.1:8000/chat/${encodeURIComponent(question)}`);
      const data = await response.json();

      // Simulate delay (e.g., 1.5 seconds)
      setTimeout(() => {
        setChatLog((prevLog) => [...prevLog, { user: 'Bot', text: data.answer }]);
        setLoading(false); // Hide loading
      }, 1500);
    } catch (error) {
      console.error('Error:', error);
      setChatLog((prevLog) => [...prevLog, { user: 'Bot', text: "Sorry, something went wrong." }]);
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h1>Chatbot</h1>
      <div className="chat-box">
        {chatLog.map((msg, idx) => (
          <div key={idx} className={`chat-msg ${msg.user === 'You' ? 'user' : 'bot'}`}>
            <strong>{msg.user}:</strong> {msg.text}
          </div>
        ))}
        {loading && (
          <div className="chat-msg bot">
            <strong>Bot:</strong> <em>Typing...</em>
          </div>
        )}
      </div>
      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask something..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
