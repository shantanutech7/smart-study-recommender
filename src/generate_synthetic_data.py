import pandas as pd
import numpy as np
import random
from pathlib import Path

# -------------------------------
# Configuration
# -------------------------------
NUM_ROWS = 1000
OUTPUT_PATH = Path("data/raw/interactions.csv")
random.seed(42)
np.random.seed(42)

# -------------------------------
# Subjects & Topics
# -------------------------------
SUBJECTS_TOPICS = {
    "Math": ["Algebra", "Trigonometry", "Derivatives", "Integrals", "Probability"],
    "Physics": ["Kinematics", "Dynamics", "Thermodynamics", "Optics", "Electromagnetism"],
    "CS": ["Python Basics", "Data Structures", "Algorithms", "Databases", "Machine Learning"]
}

USER_IDS = [f"user_{i}" for i in range(1, 51)]  # 50 users

# -------------------------------
# Helper Function: Priority Label
# -------------------------------
def compute_priority_label(score, recency, difficulty):
    """
    Higher priority if:
    - Low score
    - High recency
    - High difficulty
    """
    normalized_score = score / 100
    priority = (
        0.5 * (1 - normalized_score) +
        0.3 * (recency / 60) +
        0.2 * (difficulty / 5)
    )
    return round(priority, 3)

# -------------------------------
# Data Generation
# -------------------------------
rows = []

for _ in range(NUM_ROWS):
    user_id = random.choice(USER_IDS)
    subject = random.choice(list(SUBJECTS_TOPICS.keys()))
    topic = random.choice(SUBJECTS_TOPICS[subject])

    last_score = round(np.random.uniform(30, 100), 2)
    attempts = np.random.randint(1, 10)
    time_spent_minutes = round(np.random.uniform(15, 600), 2)
    difficulty_rating = np.random.randint(1, 6)
    last_studied_days_ago = np.random.randint(0, 61)

    label_or_priority = compute_priority_label(
        last_score,
        last_studied_days_ago,
        difficulty_rating
    )

    rows.append([
        user_id,
        subject,
        topic,
        last_score,
        attempts,
        time_spent_minutes,
        difficulty_rating,
        last_studied_days_ago,
        label_or_priority
    ])

# -------------------------------
# Create DataFrame
# -------------------------------
columns = [
    "user_id",
    "subject",
    "topic",
    "last_score",
    "attempts",
    "time_spent_minutes",
    "difficulty_rating",
    "last_studied_days_ago",
    "label_or_priority"
]

df = pd.DataFrame(rows, columns=columns)

# -------------------------------
# Ensure Output Folder Exists
# -------------------------------
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# -------------------------------
# Save CSV
# -------------------------------
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Synthetic dataset generated successfully!")
print(f"📁 Saved at: {OUTPUT_PATH}")
print("\nPreview:")
print(df.head())
