# 👋 WaveByeAI – Telco Customer Churn Prediction App

[![Streamlit App](https://img.shields.io/badge/Live%20App-Click%20Here-brightgreen)](https://wavebyeai-je9rjsptrybwwzlrcnxbrr.streamlit.app/)
[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange)](https://streamlit.io/)
[![XGBoost Powered](https://img.shields.io/badge/Model-XGBoost-blue)](https://xgboost.readthedocs.io/en/stable/)

> Predict whether a telecom customer will **stay** or **churn** — all with one click.  
Built using `XGBoost`, `scikit-learn`, `Streamlit`, and a whole lot of love.

---

## 🧠 Project Overview

**WaveByeAI** is a machine learning-powered app that helps telecom companies detect customer churn before it happens. With just a few inputs, you’ll know if a customer is **likely to stay** or if it’s time to **wave bye 👋**.

---

## 🔮 Try the Live App

👉 Click here to test it:  
🔗 https://wavebyeai-je9rjsptrybwwzlrcnxbrr.streamlit.app/

---

## 📁 Project Structure

```bash
.
├── app.py                     # Streamlit frontend
├── model.ipynb                # Model training notebook
├── cleaning.ipynb             # Data cleaning notebook
├── insights.ipynb             # Data visualization and EDA
├── requirements.txt           # All required Python libraries
├── xgboost_churn_model.joblib # Trained XGBoost model
└── files/
    ├── Churn.csv              # Raw dataset
    └── cleaned_Churn.csv      # Cleaned dataset
