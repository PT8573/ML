import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ---------- Lottie Animation Loader ----------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---------- Animations ----------
healthy_animation = load_lottie("https://assets2.lottiefiles.com/packages/lf20_tutvdkg0.json")
risk_animation = load_lottie("https://assets2.lottiefiles.com/packages/lf20_jbrw3hcz.json")


# ---------- Background Style ----------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/human-heart-is-wonder-nature_34950-7012.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    html, body, p, div, span {
        color: #87CEEB;
    }

    h1, h2, h3 {
        color: #87CEEB !important;
    }

    label {
        color: #87CEEB !important;
        font-weight: bold;
    }

    .stButton>button {
        background-color: #87CEEB;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        height: 45px;
        width: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------- Title ----------
st.markdown("<h1 style='text-align:center;'>❤️ AI Heart Risk Prediction App</h1>", unsafe_allow_html=True)


# ---------- Load Dataset ----------
df = pd.read_csv("heart_risk_dataset.csv")


# ---------- Show Dataset ----------
st.subheader("Dataset Preview")
st.write(df)


# ---------- Features ----------
X = df[['Age','Cholesterol','Blood_Pressure','Sugar','Heart_Rate','Smoking']]
y = df['Heart_Risk']


# ---------- Train Model ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)


# ---------- Accuracy ----------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.subheader("Model Accuracy")
st.success(f"Accuracy: {accuracy:.2f}")


# ---------- Healthy Example ----------
st.subheader("Healthy Human Example")

healthy_data = {
    "Age":30,
    "Cholesterol":180,
    "Blood_Pressure":115,
    "Sugar":90,
    "Heart_Rate":72,
    "Smoking":0
}

st.write(healthy_data)


# ---------- User Input ----------
st.subheader("Enter Your Health Details")

age = st.number_input("Age", 20, 100, 30)
chol = st.number_input("Cholesterol", 100, 400, 180)
bp = st.number_input("Blood Pressure", 80, 200, 115)
sugar = st.number_input("Sugar", 70, 200, 90)
heart_rate = st.number_input("Heart Rate", 50, 200, 72)
smoking = st.selectbox("Smoking (0 = No, 1 = Yes)", [0,1])


# ---------- Prediction ----------
if st.button("Predict"):

    sample = [[age, chol, bp, sugar, heart_rate, smoking]]
    prediction = model.predict(sample)

    if prediction[0] == 1:

        st.error("⚠ High Heart Risk Detected 💔")

        st_lottie(healthy_animation, height=300)

        st.warning("Please consult a doctor and maintain a healthy lifestyle.")

        # ---------- Diet Chart ----------
        st.subheader("Recommended Heart Healthy Diet")

        diet_data = {
            "Meal": ["Morning", "Breakfast", "Lunch", "Evening Snack", "Dinner"],
            "Recommended Food": [
                "Warm water + Lemon / Green Tea",
                "Oats + Fruits + Boiled Eggs",
                "Brown Rice / Roti + Vegetables + Dal",
                "Nuts (Almonds, Walnuts) + Green Tea",
                "Light Salad + Soup / Grilled Vegetables"
            ]
        }

        diet_df = pd.DataFrame(diet_data)

        st.table(diet_df)

    else:

        st.success("✅ Your Heart Looks Healthy❤️")

        
        st_lottie(risk_animation, height=300)

        st.info("Keep maintaining a healthy diet and exercise regularly.")