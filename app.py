import streamlit as st
import pandas as pd
import joblib

# Load the trained XGBoost model
model = joblib.load("xgboost_churn_model.joblib")

# App title
st.title("📞 Telco Customer Churn Prediction")
st.markdown("Will you as a customer **churn** or stay? Let's find out! ")


def user_input():
    gender = st.selectbox("Gender", [0, 1],1)  # 0: Female, 1: Male
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1],1)
    Partner = st.selectbox("Has Partner", [0, 1],1)
    Dependents = st.selectbox("Has Dependents", [0, 1],1)
    PhoneService = st.selectbox("Has Phone Services",[0,1],0)
    MultipleLines = st.selectbox("Multiple Lines", [0, 1],1)
    InternetService = st.selectbox("Internet Service (0: None, 1: DSL, 2: Fiber)", [0, 1, 2],2)
    OnlineSecurity = st.selectbox("Online Security", [0, 1],0)
    OnlineBackup = st.selectbox("Online Backup", [0, 1],0)
    DeviceProtection = st.selectbox("Device Protection", [0, 1],0)
    TechSupport = st.selectbox("Tech Support", [0, 1],1)
    StreamingTV = st.selectbox("Streaming TV", [0, 1],1)
    StreamingMovies = st.selectbox("Streaming Movies", [0, 1],1)
    Contract = st.selectbox("Contract (0: Month-to-month, 1: One year, 2: Two year)", [0, 1, 2],0)
    PaperlessBilling = st.selectbox("Paperless Billing", [0, 1],0)
    PaymentMethod = st.selectbox("Payment Method (0: Bank, 1: Credit, 2: Electronic, 3: Mailed)", [0, 1, 2, 3],2)
    tenure = st.slider("Tenure (months)", 0, 72, 30)
    MonthlyCharges = st.slider("Monthly Charges", 0.0, 150.0, 50.0)
    TotalCharges = st.slider("Total Charges", 0.0, 10000.0, 5000.0)
    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,  
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,          
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input()


st.subheader("📋 Customer Data")
st.write(input_df)

# Prediction
if st.button("Predict Churn"):
    proba = float(model.predict_proba(input_df)[0][1])  #  Cast to float
    threshold = 0.4
    prediction = int(proba > threshold)

    st.metric(label="🎯 Churn Probability", value=f"{proba * 100:.2f}%")
    st.progress(proba)

    if prediction == 1:
        st.error(f"⚠️ This customer is **likely to churn** (Probability: {proba * 100:.2f}%)")
        st.markdown("💡 _Suggested Action: Consider offering a retention discount or reaching out via support._")
    else:
        st.success(f"✅ This customer is **likely to stay** (Probability: {(1 - proba) * 100:.2f}%)")
        st.markdown("🙌 _Looks good! Keep providing great service to maintain loyalty._")

