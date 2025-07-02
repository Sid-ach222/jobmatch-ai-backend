
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load dataset
df = pd.read_csv("public_hiring_data.csv")

# Convert string of skills into space-separated string (if needed)
df["skills"] = df["skills"].apply(lambda x: " ".join(eval(x)) if isinstance(x, str) and x.startswith("[") else x)

# Define features and label
X = df[["education", "experience_years", "skills", "job_title", "location"]]
y = df["hired"]

# Preprocessing pipeline
numeric_features = ["experience_years"]
categorical_features = ["education", "job_title", "location"]
text_features = "skills"

preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("txt", CountVectorizer(), text_features)
    ]
)

# Full pipeline with classifier
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train-test split and fit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model trained from CSV and saved as model.pkl")
