# 🚀 NovaBI – AI Business Intelligence Assistant

## Overview

NovaBI is an AI-powered Business Intelligence Assistant built using Streamlit, Monday.com API, and Google Gemini AI.

The application helps founders and business executives retrieve business insights from live Monday.com boards through natural language queries.

---

## Features

- Live Monday.com API Integration
- AI-powered Business Intelligence using Gemini AI
- Interactive Chat Assistant
- Dashboard with Business KPIs
- Leadership Report Generation
- Automatic Data Cleaning
- Handles Missing Values
- Cross-board Analysis (Deals & Work Orders)
- Deployed using Streamlit Community Cloud

---

## Technology Stack

- Python
- Streamlit
- Monday.com GraphQL API
- Google Gemini AI
- Pandas
- Plotly
- Requests

---

## Project Structure

```
NovaBI/
│
├── app.py
├── modules/
│   ├── chat.py
│   ├── dashboard.py
│   └── leadership.py
│
├── services/
│   ├── monday_api.py
│   ├── ai_agent.py
│   ├── analysis.py
│   └── cleaner.py
│
├── data/
├── static/
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/nikhitakammar/NovaBI.git

cd NovaBI

pip install -r requirements.txt

streamlit run app.py
```

---

## Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
MONDAY_API_TOKEN=YOUR_API_TOKEN
```

---

## Live Demo

Streamlit App

https://novabi-wa6reqshxrwo5re9a7zrr2.streamlit.app

---

## GitHub Repository

https://github.com/nikhitakammar/NovaBI

---

## Author

Nikhita Kammar

AI & ML Engineer
