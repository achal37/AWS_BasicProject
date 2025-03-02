import streamlit as st
import joblib
import numpy as np

# Load model and scaler
knn_model = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")

# Streamlit UI Configuration
st.set_page_config(page_title="📱 Mobile Price Prediction", layout="wide")

# Title and Description
st.title("Mobile Price Prediction")
st.markdown("### Enter the mobile specifications below to predict the price category.")

# Add styling
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout with two sections
st.markdown("## 🔧 Hardware Specifications")
col1, col2 = st.columns(2)

with col1:
    battery = st.number_input("Battery Power (mAh)", min_value=0, step=1)
    px_height = st.number_input("Pixel Height", min_value=0, step=1)
    px_width = st.number_input("Pixel Width", min_value=0, step=1)
    sc_h = st.number_input("Screen Height", min_value=0, step=1)
    sc_w = st.number_input("Screen Width", min_value=0, step=1)
    clock_speed = st.number_input("Processor Clock Speed (GHz)", min_value=0.1, step=0.1)
    cores = st.number_input("Number of Processor Cores", min_value=1, step=1)
    ram = st.number_input("RAM (MB)", min_value=0, step=1)

with col2:
    rom = st.number_input("Internal Storage (GB)", min_value=0, step=1)
    mobile_weight = st.number_input("Mobile Weight (g)", min_value=0, step=1)
    mobile_depth = st.number_input("Mobile Depth (cm)", min_value=0.1, step=0.1)
    primary_camera = st.number_input("Primary Camera (MP)", min_value=0, step=1)
    front_camera = st.number_input("Front Camera (MP)", min_value=0, step=1)
    talk_time = st.number_input("Talk Time (Hours)", min_value=0, step=1)

# Software & Connectivity Features
st.markdown("## 📡 Software & Connectivity Features")
col3, col4 = st.columns(2)

with col3:
    bluetooth = st.selectbox("Bluetooth", [0, 1])
    dual_sim = st.selectbox("Dual SIM", [0, 1])
    four_g = st.selectbox("4G", [0, 1])
    three_g = st.selectbox("3G", [0, 1])

with col4:
    touch_screen = st.selectbox("Touch Screen", [0, 1])
    wifi = st.selectbox("Wi-Fi", [0, 1])

# Compute Derived Features
pixels_dimension = px_height * px_width
screen_dimension = sc_h * sc_w

st.markdown("---")
if st.button("🔮 Predict Price Category", use_container_width=True):
    try:
        # Prepare feature array
        features = np.array([[battery, bluetooth, clock_speed, dual_sim, front_camera, four_g,
                              rom, mobile_depth, mobile_weight, cores, primary_camera, ram,
                              talk_time, three_g, touch_screen, wifi, pixels_dimension, screen_dimension]])

        # Scale input
        features_scaled = scaler.transform(features)

        # Predict price category
        prediction = knn_model.predict(features_scaled)[0]

        # Display result
        st.success(f"💰 **Predicted Price Category:** {prediction}")

    except Exception as e:
        st.error(f"❌ Error: {e}")

