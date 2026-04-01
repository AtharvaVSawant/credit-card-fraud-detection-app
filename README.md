# 💳 Credit Card Fraud Detection ML App

## 📌 Project Overview

This project is an **end-to-end Machine Learning application** designed to detect fraudulent credit card transactions.

It compares multiple models, including **Random Forest** and **XGBoost**, and uses **SMOTE (Synthetic Minority Oversampling Technique)** to handle class imbalance.

The final model is deployed using **Streamlit** for real-time predictions.


## 🚀 Features

- Detects fraudulent transactions in real-time  
- Interactive web interface using Streamlit  
- Handles imbalanced data using SMOTE  
- Model comparison (Random Forest vs XGBoost)  
- Displays prediction probability  

## Dataset 
- kaggle Link : https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## 🧠 Machine Learning Pipeline

### 🔹 Data Preprocessing

- Feature scaling using StandardScaler  
- Handling class imbalance using SMOTE  

### 🔹 Models Used

- Random Forest Classifier ✅ (Best performing)  
- XGBoost Classifier  

### 🔹 Model Selection

Random Forest was selected as the final model due to:

- Better performance on validation data  
- More stable predictions  
- Lower overfitting compared to XGBoost  



## 🛠️ Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- XGBoost  
- Imbalanced-learn (SMOTE)  
- Pandas / NumPy  



## 📂 Project Structure
- app.py                    # Streamlit app 
- creditcardfraud.ipynb     # Model training & analysis 
- rf_model.pkl              # Final trained model 
- scaler.pkl                # Data scaler 
- features.pkl              # Feature list 
- requirements.txt          # Dependencies 
- README.md                 # Documentation



## 📬 Contact

For any queries, please contact:  
atharvasawant3183@gmail.com 

https://www.linkedin.com/in/atharvavsawant/



