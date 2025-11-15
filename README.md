# Credit-Card-Fraud-Detection-Using-Machine-Learning
This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The dataset is highly imbalanced, and the goal is to build a robust model capable of identifying fraud with high precision and recall.
📝 Project Overview

Credit card fraud is a major problem in financial institutions.
This project aims to:

Analyze transaction patterns

Handle imbalanced data

Train multiple machine learning models

Compare accuracy, precision, recall, F1-score

Identify the best-performing model for fraud detection

📂 Dataset

Source: Kaggle – Credit Card Fraud Detection Dataset

Rows: 284,807 transactions

Fraudulent: Only 492 (0.172%)

Features:

V1 to V28 — PCA-transformed features

Time, Amount — original features

Class — target (1 = fraud, 0 = non-fraud)

⚙️ Technologies Used

Python

NumPy

Pandas

Matplotlib / Seaborn

Scikit-learn

Imbalanced-learn (SMOTE)

Jupyter Notebook

📊 Machine Learning Models Tested

Logistic Regression

Decision Tree

Random Forest

XGBoost / LightGBM (optional)

SVM

ANN (if included)

🧠 Steps Performed

Data Loading & Understanding

Exploratory Data Analysis (EDA)

Handling Imbalanced Data (SMOTE / Undersampling)

Feature Scaling

Model Training

Hyperparameter Tuning

Model Evaluation

Comparison of Models

Final Model Selection

📈 Evaluation Metrics

Accuracy

Precision

Recall

F1-score

Confusion Matrix

ROC-AUC Score

⚠ Fraud detection is a recall-critical problem — catching fraud is more important than reducing false alarms.

🔍 Results

Example (replace with your actual values):

Model	Accuracy	Precision	Recall	F1-Score
Logistic Regression	0.94	0.72	0.65	0.68
Random Forest	0.99	0.91	0.84	0.87
XGBoost	0.999	0.94	0.91	0.92

Best Model: Random Forest / XGBoost (Your choice)

🚀 How to Run

Clone repository:

git clone https://github.com/yourusername/credit-card-fraud-detection.git


Install dependencies:

pip install -r requirements.txt


Run the notebook:

jupyter notebook credit_card_fraud_detection.ipynb


Or run Python script:

python fraud_detection.py

📦 Project Structure
├── data/
│   └── creditcard.csv
├── notebooks/
│   └── EDA.ipynb
│   └── Model_Training.ipynb
├── fraud_detection.py
├── requirements.txt
└── README.md

🛡️ Important Note

This dataset contains highly sensitive financial patterns.
Use the model only for educational and research purposes.

🙌 Author

Chaitanya Jamdar
📧 Feel free to connect or ask questions!
