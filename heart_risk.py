# import streamlit as st
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# # ---------- Background Image + Title Color ----------
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://img.freepik.com/premium-photo/human-heart-is-wonder-nature_34950-7012.jpg");
#         background-size: cover;
#         background-position: center;
#         background-attachment: fixed;
#     }

#     /* Title */
#     h1 {
#         color: #87CEEB;
#     }

#     /* Subheaders */
#     h3 {
#         color: #87CEEB;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ---------- Title ----------
# st.title("❤️ Heart Risk Prediction App")

# # ---------- Load Dataset ----------
# df = pd.read_csv("heart_risk.csv")

# # ---------- Dataset Preview ----------
# st.subheader("Dataset Preview")
# st.write(df.head())

# # ---------- Features and Target ----------
# X = df[['Age','Cholesterol','BloodPressure','Sugar','MaxHeartRate','Smoking']]
# y = df['Risk']

# # ---------- Train Model ----------
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# model = LogisticRegression()
# model.fit(X_train, y_train)

# # ---------- Input Section ----------
# st.subheader("Enter Patient Details")

# col1, col2 = st.columns(2)

# with col1:
#     age = st.number_input("Age", 1, 100, 40)
#     chol = st.number_input("Cholesterol", 100, 400, 200)
#     bp = st.number_input("Blood Pressure", 80, 200, 120)

# with col2:
#     sugar = st.number_input("Sugar", 70, 200, 100)
#     hr = st.number_input("Max Heart Rate", 60, 220, 150)
#     smoking = st.selectbox("Smoking", [0,1])

# # ---------- Prediction ----------
# if st.button("Predict Risk"):

#     data = [[age, chol, bp, sugar, hr, smoking]]
#     prediction = model.predict(data)

#     if prediction[0] == 1:
#         st.error("⚠️ High Heart Risk")
#     else:
#         st.success("✅ Low Heart Risk")




import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# ---------- Background Image + All Text Sky Blue ----------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/human-heart-is-wonder-nature_34950-7012.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* All Text Color */
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: #87CEEB !important;
    }

    /* Input text color */
    .stNumberInput label, .stSelectbox label {
        color: #87CEEB !important;
    }

    /* Dataset table text */
    .stDataFrame {
        color: #87CEEB;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Title ----------
st.title("❤️ Heart Risk Prediction App")

# ---------- Load Dataset ----------
df = pd.read_csv("heart_risk.csv")

# ---------- Dataset Preview ----------
st.subheader("Dataset Preview")
st.write(df.head())

# ---------- Features and Target ----------
X = df[['Age','Cholesterol','BloodPressure','Sugar','MaxHeartRate','Smoking']]
y = df['Risk']

# ---------- Train Model ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# ---------- Input Section ----------
st.subheader("Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 100, 40)
    chol = st.number_input("Cholesterol", 100, 400, 200)
    bp = st.number_input("Blood Pressure", 80, 200, 120)

with col2:
    sugar = st.number_input("Sugar", 70, 200, 100)
    hr = st.number_input("Max Heart Rate", 60, 220, 150)
    smoking = st.selectbox("Smoking", [0,1])

# ---------- Prediction ----------
if st.button("Predict Risk"):

    data = [[age, chol, bp, sugar, hr, smoking]]
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Heart Risk")
    else:
        st.success("✅ Low Heart Risk")