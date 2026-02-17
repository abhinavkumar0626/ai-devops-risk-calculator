import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/data.csv")

X = df[["files_changed", "additions", "deletions", "duration"]]
y = df["failed"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")

print("Model trained successfully")
