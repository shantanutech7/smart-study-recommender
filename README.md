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


### ✅ cURL example
```md
```bash
curl -X POST "http://127.0.0.1:8000/recommendations" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"user_1","top_n":5}'


⚠️ You must have:
- **Three backticks before**
- **Three backticks after**
- Language name immediately after the first three backticks

---

## ✅ ✅ 2. Also check for these mistakes and fix them:
- ❌ Using only **one or two backticks**
- ❌ Forgetting to **close** a code block
- ❌ Writing `javascript` or `bash` without ``` before it

---

## ✅ ✅ 3. After fixing in VS Code:
1. Save `README.md`
2. Commit & push again:

```powershell
git add README.md
git commit -m "Fix README markdown formatting"
git push

