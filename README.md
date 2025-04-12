# 💻 TraceFi Frontend (Streamlit)

**TraceFi** is a blockchain OSINT tool that allows users to visually explore and trace the flow of cryptocurrency across wallets.

This repository contains the **Streamlit-based** frontend that connects to the TraceFi backend and displays wallet metadata, transaction history, and graph visualizations.

---

## 🛠️ Tech Stack

- Python 3.11
- [Streamlit](https://streamlit.io/)
- REST API integration
- Docker (optional)
- `.env` support

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.10+
- `pip` / `venv`
- Docker (optional)

---

### 🧱 Local Setup (no Docker)

```bash
git clone https://github.com/yourusername/tracefi-frontend.git
cd tracefi-frontend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

# Optional: edit .env to match your backend URL
# BACKEND_URL=http://localhost:8000

streamlit run app.py
```

Visit: http://localhost:8501

---

### 🐳 Docker Setup

```bash
docker build -t tracefi-frontend .
docker run -p 8501:8501 --env BACKEND_URL=http://localhost:8000 tracefi-frontend
```

---

### 🔗 API Dependency

Make sure the TraceFi Backend is running and accessible at the URL defined in .env.

---

### 📌 Coming Soon

- Wallet graph explorer
- Entity enrichment panel
- Flow charts with timestamps