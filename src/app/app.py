import streamlit as st
import pandas as pd
import random
import time

# Page configuration
st.set_page_config(
    page_title="Crop Recommendation AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E8B57;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .recommendation-box {
        background-color: #f0f8f0;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 6px solid #2E8B57;
        margin: 1rem 0;
    }
    .feature-input {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .mock-badge {
        background-color: #ffd700;
        color: #000;
        padding: 0.3rem 0.6rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    .stSlider > div {
        color: #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

# Mock crop database
CROP_DATABASE = {
    "Black": ["Sugarcane", "Cotton", "Wheat", "Rice"],
    "Red": ["Groundnut", "Millet", "Pulses", "Oilseeds"],
    "Brown": ["Maize", "Soybean", "Wheat", "Barley"],
    "Yellow": ["Potato", "Tobacco", "Oilseeds", "Pulses"],
    "White": ["Opium", "Medicinal Plants", "Tea", "Coffee"],
    "Gray": ["Rice", "Jute", "Sugarcane", "Vegetables"]
}

# Mock recommendation logic
def get_mock_recommendation(data):
    crops = CROP_DATABASE.get(data["soil_color"], ["Wheat", "Maize", "Rice"])
    if data["ph_level"] < 5.5:
        crops += ["Potato", "Tea", "Blueberries"]
    elif data["ph_level"] > 7.5:
        crops += ["Alfalfa", "Cabbage", "Spinach"]
    else:
        crops += ["Vegetables", "Fruits", "Grains"]
    
    if data["rainfall"] > 1500:
        crops += ["Rice", "Sugarcane", "Jute"]
    elif data["rainfall"] < 500:
        crops += ["Millet", "Sorghum", "Groundnut"]
    
    if data["temperature"] > 30:
        crops += ["Cotton", "Sugarcane", "Rice"]
    elif data["temperature"] < 10:
        crops += ["Wheat", "Barley", "Oats"]
    
    return random.sample(list(set(crops)), min(3, len(crops)))

# Sidebar
with st.sidebar:
    # GitHub logo with custom TopPNG image and label
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1rem;">
        <a href="https://github.com/IgYaHiko/College_drag" target="_blank" style="text-decoration: none; color: inherit;">
            <img src="https://cdn.iconscout.com/icon/free/png-512/free-github-logo-icon-svg-download-png-461797.png?f=webp&w=512" width="50" style="vertical-align: middle;">
            <span style="font-weight: bold; margin-left: 5px; vertical-align: middle;"></span>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Existing sidebar content
    st.title("⚙️ College Drag")
    st.markdown("---")
    st.header("📊 Status")
    st.warning("🔄 Model Training in Progress")
    st.info("This interface shows mock crop recommendations.")
    st.markdown("---")
    st.header("ℹ️ About")
    st.markdown("""
        - Soil properties (color, pH, nutrients)
        - Climate conditions (temperature, rainfall)
        - Agricultural best practices
        *Real AI recommendations coming soon!*
    """)
    with st.expander("📈 Training Progress"):
        st.markdown("""
        - 🟡 Data Preprocessing: Complete
        - 🟡 Model Architecture: Ready
        - 🔵 Model Training: In Progress
        - ⚪ Model Validation: Pending
        - ⚪ Deployment: Pending
        *Estimated completion: Soon!*
        """)


# Main Header
st.markdown('<h1 class="main-header">🌱 Crop Recommendation System</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:20px"><span class="mock-badge">MOCK DEMO</span></div>', unsafe_allow_html=True)

# Input Form
with st.form("crop_form"):
    st.subheader("🌿 Soil Properties")
    soil_color = st.selectbox("Soil Color", ["Black", "Red", "Brown", "Yellow", "White", "Gray"])
    col1, col2 = st.columns(2)
    with col1:
        nitrogen = st.slider("Nitrogen (N)", 0, 200, 75)
        phosphorus = st.slider("Phosphorus (P)", 0, 200, 50)
    with col2:
        potassium = st.slider("Potassium (K)", 0, 200, 100)
        ph_level = st.slider("pH Level", 3.0, 10.0, 6.5, 0.1)
    
    st.subheader("🌤️ Climate Conditions")
    col1, col2 = st.columns(2)
    with col1:
        rainfall = st.slider("Annual Rainfall (mm)", 0, 5000, 1000)
    with col2:
        temperature = st.slider("Temperature (°C)", -10, 50, 20)
    
    submitted = st.form_submit_button("🌾 Get Recommendation")

# Display Results
if submitted:
    recommendations = get_mock_recommendation({
        "soil_color": soil_color,
        "ph_level": ph_level,
        "rainfall": rainfall,
        "temperature": temperature
    })
    
    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    st.subheader("💡 Recommended Crops")
    for i, crop in enumerate(recommendations, 1):
        st.write(f"{i}. {crop}")
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("👆 Fill in the form to get mock crop recommendations.")
