# Paisa Saathi AI 💰🤖

**Paisa Saathi AI** is an AI-powered personal finance assistant designed to help users understand financial information, analyze market data, retrieve relevant information, and generate useful insights through a conversational interface.

The application combines **Generative AI, specialized agents, financial APIs, Retrieval-Augmented Generation (RAG), and data visualization** to provide an interactive financial analysis experience.

---

## 🚀 Features

* 🤖 **AI Financial Assistant** — Ask questions about financial markets and receive AI-generated responses.
* 📈 **Stock Analysis** — Retrieve and analyze stock-related information.
* 📰 **Financial News** — Access relevant financial news and information.
* 🔎 **RAG-based Retrieval** — Retrieve relevant information from indexed financial documents/data.
* 📊 **Data Visualization** — Generate charts and visual representations of financial data.
* 🔮 **Prediction** — Perform basic market/price prediction using machine-learning models.
* 🧩 **Multi-Agent Architecture** — Different agents handle different financial tasks.
* 🎙️ **Conversational Interface** — Interact with the assistant through a Streamlit-based UI.

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
              ┌───────────────┐
              │  Streamlit UI │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Backend / API │
              └───────┬───────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Agent Orchestrator│
             └────────┬────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Financial      Retrieval      Analysis /
   Data Agent       Agent        Prediction
        │             │             │
        ▼             ▼             ▼
 Financial APIs    FAISS/RAG     ML Models
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                AI Response
                      │
                      ▼
                Streamlit UI
```

---

## 🛠️ Tech Stack

### Programming & Backend

* Python
* FastAPI
* Streamlit

### AI & Machine Learning

* Google Gemini
* LangChain
* Machine Learning models
* Retrieval-Augmented Generation (RAG)

### Vector Search

* FAISS

### Financial Data

* Yahoo Finance
* Financial/news data sources

### Deployment

* Docker
* Railway

---

## 📂 Project Structure

```text
Paisa-Saathi-AI/
│
├── agents/
│   └── Specialized AI agents
│
├── data_ingestion/
│   └── Data collection and preprocessing
│
├── docs/
│   └── Project documentation
│
├── orchestrator/
│   └── Agent coordination and workflow
│
├── streamlit_app/
│   └── Streamlit user interface
│
├── testing/
│   └── Testing and validation
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker_compose.yaml
└── railway.json
```

---

## ⚙️ How It Works

1. The user enters a financial query through the Streamlit interface.
2. The request is sent to the backend.
3. The agent orchestrator determines which capability is required.
4. The appropriate agent processes the request.
5. Financial APIs, retrieved information, or machine-learning models are used when required.
6. The AI processes the collected information.
7. The final response is returned to the user through the Streamlit interface.

---

## 🧠 RAG Pipeline

The retrieval component uses a **Retrieval-Augmented Generation** approach.

```text
Documents / Financial Data
          │
          ▼
     Data Processing
          │
          ▼
      Text Chunks
          │
          ▼
      Embeddings
          │
          ▼
       FAISS Index
          │
          ▼
    Similarity Search
          │
          ▼
 Relevant Information
          │
          ▼
       Gemini LLM
          │
          ▼
    Final Response
```

This allows the application to retrieve relevant information before generating an answer rather than relying only on the language model's internal knowledge.

---

## 🔐 Environment Variables

Create a `.env` file in the project directory and configure the API keys required by the application.

Example:

```env
GOOGLE_API_KEY=your_api_key
```

Add any additional keys required by the data sources used by your local configuration.

**Do not commit API keys or other secrets to GitHub.**

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/shekhar421/Paisa-Saathi-AI.git
cd Paisa-Saathi-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file and add the required API keys.

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🐳 Running with Docker

Build the Docker image:

```bash
docker build -t paisa-saathi-ai .
```

Run the container:

```bash
docker run -p 8501:8501 paisa-saathi-ai
```

---

## 🎯 Project Goals

The main goals of Paisa Saathi AI are to:

* Simplify access to financial information.
* Provide an interactive AI-based financial assistant.
* Combine financial data with Generative AI.
* Demonstrate the use of multi-agent systems.
* Apply RAG and vector search to financial information.
* Provide useful visualizations for financial analysis.

---

## ⚠️ Disclaimer

Paisa Saathi AI is intended for **educational and informational purposes only**.

The information, predictions, and analysis generated by the application should not be considered financial, investment, or trading advice.

Users should conduct their own research and consult qualified financial professionals before making financial decisions.

---

## 📜 License

This project is released under the **MIT License**.

If this repository contains or derives from third-party open-source components, their respective licenses and attribution requirements continue to apply.
