import { useState } from "react";
import axios from "axios";

export default function Chat() {
  const [input, setInput] = useState("");
  const [history, setHistory] = useState([]);

  // 🔊 Give the message GPT
  const speakText = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    speechSynthesis.speak(utterance);
  };

  // 🎤 Register the voice input
  const handleVoiceInput = () => {
    const recognition = new window.SpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = false;

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setInput(transcript);
    };

    recognition.onerror = (event) => {
      console.error("🎤 Voice recognition error:", event.error);
    };

    recognition.start();
  };

  // 🔁 Send the text message
  const handleSubmit = async () => {
    if (!input.trim()) return;

    const updatedHistory = [...history, { role: "user", content: input }];

    try {
      const res = await axios.post("http://localhost:8000/chat", {
        message: input,
        history: updatedHistory,
      });

      const reply = res.data.response;

      setHistory([
        ...updatedHistory,
        { role: "assistant", content: reply }
      ]);

      speakText(reply); // 🔊 GPT Voice
      setInput("");
    } catch (err) {
      console.error(err);
    }
  };

  // 🔁 Reset local historical (frontend)
  const handleReset = () => {
    setHistory([]);
    setInput("");
    speechSynthesis.cancel();
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "700px", margin: "0 auto" }}>
      <h2>🤖 Smart Librarian</h2>

      {/* 💬 Displayed historical */}
      <div style={{ marginBottom: "1rem" }}>
        {history.map((msg, index) => (
          <div
            key={index}
            style={{
              background: msg.role === "user" ? "#1565c0" : "#388e3c",
              padding: "0.75rem",
              marginBottom: "0.5rem",
              borderRadius: "5px"
            }}
          >
            <strong>{msg.role === "user" ? "You" : "Assistant"}:</strong>
            <p style={{ margin: 0 }}>{msg.content}</p>
          </div>
        ))}
      </div>

      {/* Input + controls */}
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask me about a book..."
        rows={3}
        style={{ width: "100%", fontSize: "1rem" }}
      />
      <br />
      <button onClick={handleSubmit} style={{ marginRight: "0.5rem" }}>Send</button>
      <button onClick={handleVoiceInput} style={{ marginRight: "0.5rem" }}>🎤 Speak</button>
      <button onClick={handleReset}>🔁 Reset</button>
    </div>
  );
}
