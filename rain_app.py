# app.py
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('/Users/titassaha/code/rain_model.pkl')

st.title("Rain Prediction App 🌧️☀️")

with st.container():
    st.write("This is a simple weather prediction app. Enter weather details and click on predict below.")
    st.subheader("Enter today's weather data: ") 

# User input
    pressure = st.slider("Pressure (hPa)", min_value=800.0, max_value=1100.0, value=1013.0)
    temperature = st.slider("Temperature (°C)", min_value=-50.0, max_value=60.0)
    humidity = st.slider("Humidity (%)", min_value=0.0, max_value=100.0)
    cloud = st.slider("Cloud", min_value = 1, max_value = 100)
    sunshine = st.slider("Sunshine", min_value = 0, max_value =1)
    winddirection = st.slider("Wind Direction (degrees)", min_value=0.0, max_value=360.0)
    windspeed = st.slider("Windspeed (km/h)", min_value=0.0, max_value=200.0)

st.markdown("   ")
st.markdown("""
    <style>
    div.stButton > button:first-child {git add rain_app.py
        font-size: 20px;
        height: 3em;
        width: 40%;
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("Predict"):
    input_data = np.array([[pressure, temperature, humidity, cloud, sunshine, winddirection, windspeed]])
    prediction = model.predict(input_data)
    result = "Prediction : 🌧️ Rain" if prediction[0] == 1 else "Prediction: ☀️ No Rain"
    st.markdown(
        f"<h4 style='text-align: left; color: green;'>{result}</h4>",
        unsafe_allow_html=True
)
    
st.markdown("   \n   ")

st.write("See full code here: https://github.com/t-saha/Streamlit-Projects/tree/main")
    
st.markdown("---")
st.markdown("---")
st.markdown("---")
