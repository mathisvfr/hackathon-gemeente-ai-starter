# 🚀 Hackathon Quick Start Guide

Welkom bij de hackathon! Deze guide helpt je snel aan de slag te gaan.

## Stap 1: Kopieer de repository

Download of clone deze repository naar je lokale machine.

## Stap 2: Configureer je GreenPT API Key

### Backend configuratie

```bash
cd "3. Platform/backend"
cp .env.example .env
```

Open het `.env` bestand en vul je GreenPT API key in:
```
GREENPT_API_KEY=jouw_api_key_hier
```

### Frontend configuratie (optioneel)

```bash
cd "3. Platform"
cp .env.example .env
```

## Stap 3: Installeer dependencies

### Backend (Python)
```bash
cd "3. Platform/backend"
python -m venv venv

# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### Frontend (Node.js)
```bash
cd "3. Platform"
npm install
```

## Stap 4: Start de applicatie

### Terminal 1 - Backend
```bash
cd "3. Platform/backend"
# Activeer venv (zie stap 3)
python start.py
```

### Terminal 2 - Frontend
```bash
cd "3. Platform"
npm run dev
```

## 🎉 Klaar!

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📚 Projectstructuur

```
├── 1. Datasets/          # Dataset met scraped content
├── 2. Best Practices/    # Best practices documentatie
├── 3. Platform/          # Hoofdapplicatie
│   ├── backend/          # Python FastAPI backend
│   ├── src/              # React frontend
│   └── ...
└── 4. Feedback/          # Feedback documentatie
```

## 🆘 Hulp nodig?

- Bekijk [SETUP_GREENPT.md](3.%20Platform/SETUP_GREENPT.md) voor gedetailleerde setup instructies
- Bekijk de README bestanden in elke map voor meer informatie
- Vraag je hackathon begeleiders!

Veel succes! 💪
