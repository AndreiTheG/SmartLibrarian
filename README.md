# 📚 Smart Librarian - DavaX - AI with RAG & Tool Completion 

An intelligent chatbot acting as a digital librarian, allowing interaction through text, voice, and LLMs, using a modern interface and scalable backend.

---

## 🧰 Technologies Used

- **fastapi** – The main web framework
- **uvicorn** – Runs the FastAPI app as a local web server
- **pydantic** – Data validation & serialization
- **sqlalchemy** – Providing SQL and ORM (Object Relational Mapping) features for database access  
- **chromadb** – Storing and querying the embeddings for LLM apps using RAG approach  
- **openai** – Providing tools to interact with OpenAI API  
- **speech_recognition** – Used for speech-to-text conversion  
- **pyttsx3** – Used for text-to-speech conversion  

---

## 📘 Tutorial for Using the Librarian Chatbot Application

### 🔹 Step 1 – Clone the repository in PyCharm

Clone the repo from GitHub into PyCharm using the command:

```bash
git clone https://github.com/AndreiTheG/SmartLibrarian.git
```

---

### 🔹 Step 2 – Create a virtual environment and install required packages

```bash
pip install fastapi uvicorn pydantic sqlalchemy chromadb openai speech_recognition pyttsx3
```

---

### 🔹 Step 3 – Install frontend frameworks (React + Vite)

Make sure you have Node.js installed, then run:

```bash
npm create vite@latest frontend --template react
cd frontend
npm install
```

---

### 🔹 Step 4 – Set the OpenAI API key

Set the key in your terminal:

```bash
export OPENAI_API_KEY=your_api_key_here
```

---

## 🧠 Application Structure

### 🔸 Step 5.1 – Running `main.py`

Run the FastAPI server and define the `/chat` route.

### 🔸 Pasul 5.2 – Modele Pydantic

Create the `model` folder and add:

- `ChatRequest.py`
- `SummaryBook.py`
- `SummaryBookModel.py`

### 🔸 Step 5.3 – `Database.py` Script

Create the SQLite database with book data.

### 🔸 Step 5.4 – Define API Routes

- `POST` – Insert book data and messages
- `GET` – Retrieve data by ID

### 🔸 Pasul 5.5 – Run `load_db_to_chroma.py`

```bash
python backend/chatbot/load_db_to_chroma.py
```

### 🔸 Step 5.6 – Start the CLI

```bash
python -m backend.chatbot.cli_bot
```

---

## 🌐 Frontend

### 🔸 Step 6.1 – Install Axios

```bash
npm install axios
```

### 🔸 Step 6.2 – Create Chat.jsx + integrate with App.jsx

Use the endpoint `http://localhost:8000/chat`.

---

### 🔸 Step 7 – Enable CORS in FastAPI

Add in `main.py`:

```python
origins = ["http://localhost:5173"]
```

---

## 🚀 Running the Application

### ▶️ Backend

```bash
uvicorn backend.main:app --reload
```

### ▶️ Frontend

```bash
npm run dev
```

Access [http://localhost:5173](http://localhost:5173)

---

## 📚 Main Features

- 🔍 Insert and retrieve book summaries 
- 🤖 Chatbot interaction (text + voice)  
- 📈 Vectorization in ChromaDB  
- 🧠 Generate summaries and recommendations using GPT  

---

## ✅ Recommendations

- Run backend and frontend in parallel 
- Reload Chroma database if you add new books  
- The app is easily extendable for other LLM/UI integrations

## Application Interface:
![Alt text](./Chatbot_interface.png)
