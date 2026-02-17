# AI DevOps Risk Predictor

This project predicts CI/CD deployment failure risk using ML.

## Features
- GitHub Actions CI
- Failure risk prediction
- RandomForest ML model
- Synthetic dataset generation

## How to Run

Generate dataset:
python scripts/generate_dataset.py

Train model:
python ml/train.py

Predict:
python ml/predict.py 10 200 50 400
