k# 🛡️ PhishGuard AI

AI-powered phishing URL detection and threat intelligence platform built using FastAPI, React, Machine Learning, PostgreSQL, Docker, and cybersecurity APIs.

---

# 🚀 Project Overview

PhishGuard AI is a real-time phishing detection system that analyzes suspicious URLs using:

- Machine Learning
- Threat Intelligence APIs
- SSL Analysis
- WHOIS Analysis
- Risk Scoring Engine
- Browser Extension Detection

The system classifies URLs into:

- ✅ Safe
- ⚠️ Suspicious
- ❌ Phishing

with real-time confidence and risk analysis.

---

# 🧠 AI & Machine Learning

The AI module is trained on phishing datasets containing:

- benign URLs
- phishing URLs
- malware URLs
- defacement URLs

The ML model learns phishing patterns using:

- URL length
- suspicious keywords
- special characters
- domain structure
- SSL presence
- domain age
- entropy patterns

Current ML pipeline:

- Feature Extraction
- XGBoost Classification
- Confidence Prediction
- Hybrid Threat Scoring

---

# ⚙️ Tech Stack

## Frontend

- React.js
- Tailwind CSS
- Recharts
- Axios

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication

## Database

- PostgreSQL

## AI / ML

- Python
- Scikit-learn
- XGBoost
- Pandas
- NumPy

## DevOps

- Docker
- Docker Compose

## Threat Intelligence APIs

- VirusTotal API
- WHOIS Lookup
- SSL Certificate Validation

---

# ✨ Features

## 🔍 URL Scanning

Real-time phishing URL detection.

---

## 📊 Threat Analytics Dashboard

- Total scans
- Threat detection count
- Safe URL ratio
- Pie chart analytics

---

## 🧠 AI-Based Classification

Classifies URLs into:

- Safe
- Suspicious
- Phishing

using machine learning.

---

## 🔐 SSL Certificate Analysis

Checks if website uses valid HTTPS encryption.

---

## 🌐 WHOIS Domain Analysis

Checks:

- domain age
- suspicious domains
- recently registered domains

---

## ☣️ VirusTotal Integration

Uses threat intelligence feeds for malicious URL reputation analysis.

---

## 🧹 Clear Stats System

Users can reset all dashboard statistics and database history.

---

## 🧩 Browser Extension Support

Chrome extension support for real-time phishing alerts while browsing.

---

# 🏗️ System Architecture

```text
User URL Input
       │
       ▼
Frontend Dashboard (React)
       │
       ▼
FastAPI Backend
       │
 ┌───────────────┬───────────────┬───────────────┐
 ▼               ▼               ▼
ML Model     VirusTotal      WHOIS + SSL
(XGBoost)      API            Intelligence
       │
       ▼
Hybrid Risk Scoring Engine
       │
       ▼
Final Threat Classification
       │
       ▼
PostgreSQL Database

phishguard-ai/
│
├── backend/
│   ├── app/
│   ├── ml/
│   ├── models/
│   ├── services/
│   └── api/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── pages/
│
├── docker-compose.yml
│
└── README.md


Start Project
docker compose up --build

Frontend
http://localhost:5173

Backend API
http://localhost:8000

Swagger Documentation
http://localhost:8000/docs


🧪 Example Test URLs

✅ Safe URLs
https://google.com
https://github.com
https://onlinesbi.sbi

❌ Phishing URLs
http://verify-bank-login.cc
http://free-crypto-bonus.ru

⚠️ Suspicious URLs
http://secure-login-check.net
http://account-verification-alert.org
http://banking-update-portal.info
http://signin-security-check.xyz
http://wallet-authentication.live
