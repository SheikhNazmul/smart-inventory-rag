# 🤖 Simple GenAI Text Assistant

A beginner-friendly Generative AI application built with **Python, Streamlit, and the OpenAI API**. Users can enter a prompt and generate an AI response with adjustable creativity.

## ✨ Features

- Prompt-based text generation
- Streamlit web interface
- Selectable OpenAI model
- Adjustable creativity/temperature
- Environment-variable API key handling
- Basic error and input validation

## 🧰 Tech Stack

- Python
- Streamlit
- OpenAI API
- Git/GitHub

## 📁 Project Structure

```text
smart-inventory-rag/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/SheikhNazmul/smart-inventory-rag.git
cd smart-inventory-rag
```

### 2. Install dependencies

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Set `OPENAI_API_KEY` as an environment variable. Never commit a real API key to GitHub.

Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

macOS/Linux:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

### 4. Start the app

```bash
streamlit run app.py
```

## 💼 Portfolio Value

This project demonstrates practical Generative AI integration, API usage, prompt handling, UI development, configuration management, and secure secret handling. It is intentionally simple so the code is easy to understand and extend.

## 🔮 Possible Extensions

- Chat history and multi-turn conversations
- Streaming responses
- Prompt templates
- RAG with a vector database
- Document upload and question answering
- Authentication and usage limits

## 👨‍💻 Author

**Sheikh Nazmul Islam NiR**  
AI/ML Engineer • Python Developer

- GitHub: https://github.com/SheikhNazmul
- LinkedIn: https://www.linkedin.com/in/sheikh-nazmul-islamm-1a649b296
