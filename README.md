# 🎯 Smart Study Recommendation System

An end-to-end **AI/ML-powered Smart Study Recommendation System** that recommends what a student should study next based on their **past performance, learning behavior, and recency of study**.

This system is designed for:
- Students preparing for competitive or academic exams
- Self-learners following structured roadmaps or online courses

The project starts with a **rule-based recommendation engine** and is later upgraded to an **ML-powered recommender**, exposed through a **FastAPI REST API**.

---

## 🚀 Project Goals

- Ingest and store student–topic interaction data  
- Engineer meaningful features that capture learning behavior  
- Build a **rule-based recommender (V1)**  
- Upgrade to an **ML-based recommender (V2)**  
- Expose recommendations via a **REST API**  
- Log user feedback for future model improvement  

---

## 🧠 System Inputs & Outputs

### ✅ Inputs (per user-topic interaction)

| Feature | Description |
|--------|------------|
| user_id | Unique student ID |
| subject | Subject name (Math, Physics, CS, etc.) |
| topic | Specific topic |
| last_score | Latest test/quiz score (0–100) |
| attempts | Number of attempts on this topic |
| time_spent_minutes | Total time spent studying |
| difficulty_rating | Self-rated difficulty (1–5) |
| last_studied_days_ago | Days since last study |
| label_or_priority | Optional ML target (for training) |

---

### ✅ Outputs

- A **ranked list of recommended topics** per user
- Each recommendation contains:
  - subject
  - topic
  - priority_score
  - reason for recommendation

---

## ⚙️ Tech Stack

- **Language:** Python  
- **ML Libraries:** pandas, numpy, scikit-learn  
- **API Framework:** FastAPI  
- **Database (MVP):** CSV files  
- **Model Storage:** Pickle  
- **Version Control:** Git + GitHub  

---

## 🧩 High-Level Architecture

Student Data (CSV)
↓
Data Loader
↓
Feature Engineering
↓
Rule-Based Model (V1)
↓
ML Model (V2)
↓
Recommendation Engine
↓
FastAPI Backend
↓
Client / Frontend

## 📁 Project Structure

smart-study-recommender/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_feature_engineering.ipynb
│ └── 03_model_training.ipynb
│
├── src/
│ ├── init.py
│ ├── config.py
│ ├── data_loader.py
│ ├── features.py
│ ├── train_model.py
│ ├── recommend.py
│ └── api/
│ ├── init.py
│ ├── main.py
│ └── schemas.py
│
├── models/
│ ├── model.pkl
│ └── scaler.pkl
│
├── tests/
├── frontend/ # Optional (future)
├── docs/ # Optional (diagrams, design)
│
├── README.md
├── requirements.txt
└── .gitignore

## 🧪 Recommendation Versions

### ✅ Version 1: Rule-Based System
A simple interpretable scoring formula:

priority_score =
w1 * (1 - normalized_score) +
w2 * recency +
w3 * difficulty_rating


- Weights are configurable
- Returns top-N topics for a user

---

### ✅ Version 2: ML-Based System
Supervised learning model to predict study priority using:

- RandomForestRegressor
- GradientBoostingRegressor

Evaluation metrics:
- RMSE / MAE (Regression)
- Precision@K (Ranking Quality)

---

## 🌐 API Endpoints (FastAPI)

### ✅ Health Check
`GET /health`

Response:
```json
{ "status": "ok" }

POST /recommendations

Request:

{
  "user_id": "user_1",
  "top_n": 5
}

Response:

{
  "user_id": "user_1",
  "recommendations": [
    {
      "subject": "Math",
      "topic": "Derivatives",
      "priority_score": 0.92,
      "reason": "Low recent score, high difficulty, not studied for 12 days"
    }
  ]
}

POST /feedback

{
  "user_id": "user_1",
  "subject": "Math",
  "topic": "Derivatives",
  "feedback_rating": 4,
  "useful": true
}

stored in:


git clone <repo_url>
cd smart-study-recommender
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\Activate.ps1 (Windows)
pip install -r requirements.txt
uvicorn src.api.main:app --reload


📌 Project Roadmap

✅ Project initialization

✅ Architecture & documentation

⏳ Synthetic data generation

⏳ EDA & feature engineering

⏳ Rule-based recommender

⏳ ML recommender

⏳ API integration

⏳ Testing & deployment

👨‍💻 Author

Shantanu Bawane
Data Science | Machine Learning | AI Engineering

## 🔌 API Usage Examples

### 1️⃣ JavaScript (Browser / Frontend)

## 🔌 API Usage Examples

### 1️⃣ JavaScript (Browser / Frontend)

```javascript
async function getRecommendations() {
  const response = await fetch("http://127.0.0.1:8000/recommendations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      user_id: "user_1",
      top_n: 5
    })
  });

  const data = await response.json();
  console.log(data);
}

getRecommendations();


✅ This shows how a **real frontend** would call your AI API.

---

## ✅ 2. cURL Example (Terminal Testing)

```markdown
### 2️⃣ cURL (Terminal)

```bash
curl -X POST "http://127.0.0.1:8000/recommendations" \
  -H "Content-Type: application/json" \
  -d '{ 
    "user_id": "user_1", 
    "top_n": 5 
  }'



  
 
 
  
  
  
  
  
  

 
  
















