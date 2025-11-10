# 🌾 Crop Recommendation System

A simple machine learning project that recommends the most suitable crop to grow based on soil and environmental conditions such as nitrogen (N), phosphorus (P), potassium (K), temperature, humidity, pH, and rainfall.

---

## 🚀 Project Overview

This project uses a **Random Forest Classifier** to predict which crop is best suited for a given set of agricultural parameters.  
It helps farmers and researchers make data-driven decisions for better productivity and resource optimization.

---

## 🧩 Folder Structure
```bash
crop-recommendation/
│
├── data/ # Contains datasets (raw and processed)
│ └── Crop_recommendation.csv
│
├── models/ # Saved machine learning models
│ └── crop_model.pkl
│
├── notebooks/ # Jupyter/VSCode notebooks for analysis
│ └── crop_recommendation.ipynb
│
├── src/ # All source code (scripts for data & model)
│ ├── data_preprocessing.py
│ ├── train_model.py
│ ├── predict.py
│ └── utils.py
│
├── venv/ # Virtual environment (ignored in git)
│
├── requirements.txt # Dependencies list
└── README.md # Project documentation
```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/crop-recommendation.git
cd crop-recommendation
