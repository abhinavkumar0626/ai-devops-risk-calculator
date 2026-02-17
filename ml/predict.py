import joblib
import sys
import json

model = joblib.load("ml/model.pkl")

# Example input
input_data = {
    "files_changed": int(sys.argv[1]),
    "additions": int(sys.argv[2]),
    "deletions": int(sys.argv[3]),
    "duration": int(sys.argv[4])
}

prediction = model.predict([[
    input_data["files_changed"],
    input_data["additions"],
    input_data["deletions"],
    input_data["duration"]
]])

print("Risk:", "HIGH" if prediction[0] == 1 else "LOW")
