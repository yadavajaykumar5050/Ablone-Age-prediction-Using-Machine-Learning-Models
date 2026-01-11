import streamlit as st
import numpy as np
import pickle

# Load model (and scaler if used)
model = pickle.load(open("model.pkl", "rb"))
# scaler = pickle.load(open("scaler.pkl", "rb"))  # uncomment if used

# Page config
st.set_page_config(
    page_title="Abalone Age Prediction",
    page_icon="🐚",
    layout="centered"
)

# Custom styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='color:yellow; text-align:center;'>Abalone Age Prediction Model</h1>", unsafe_allow_html=True)

# Image
st.image("img.jpg", use_container_width=True)

st.markdown("---")

# Input form
with st.form("abalone_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        sex = st.selectbox("Sex", ["Male", "Female", "Infant"])
    with col2:
        length = st.number_input("Length", min_value=0.0, step=0.01)
    with col3:
        diameter = st.number_input("Diameter", min_value=0.0, step=0.01)

    col4, col5, col6 = st.columns(3)

    with col4:
        height = st.number_input("Height", min_value=0.0, step=0.01)
    with col5:
        whole_weight = st.number_input("Whole Weight", min_value=0.0, step=0.01)
    with col6:
        shucked_weight = st.number_input("Shucked Weight", min_value=0.0, step=0.01)

    col7, col8 = st.columns(2)

    with col7:
        viscera_weight = st.number_input("Viscera Weight", min_value=0.0, step=0.01)
    with col8:
        shell_weight = st.number_input("Shell Weight", min_value=0.0, step=0.01)

    submit = st.form_submit_button("🐚 Get Abalone Age")

# Prediction
if submit:
    sex_map = {"Male": 0, "Female": 1, "Infant": 2}
    sex_val = sex_map[sex]

    features = np.array([[ 
        sex_val,
        length,
        diameter,
        height,
        whole_weight,
        shucked_weight,
        viscera_weight,
        shell_weight
    ]])

    # If scaler is used
    # features = scaler.transform(features)

    prediction = model.predict(features)

    st.markdown("---")
    st.success(f"### 🐚 Predicted Abalone Age: *{int(prediction[0])} years*")
    st.info("This age is predicted based on the input measurements provided.")