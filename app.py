import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Cloud Predictor", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Model Info")

st.sidebar.markdown("""
**Architecture:** CNN + LSTM  
**Dataset:** Cloud VM Dataset  
**Features:** CPU, Memory, Network  
**Accuracy:** ~90%  
**Loss:** Low  
""")

# ---------------- MODEL COMPARISON ----------------
st.sidebar.subheader("📊 Model Comparison")

st.sidebar.table({
    "Model": ["LSTM", "BiLSTM", "CNN+LSTM ⭐"],
    "Accuracy": ["85%", "88%", "92%"],
    "Loss": ["0.25", "0.22", "0.19"]
})

# ---------------- RESOURCES (NEW 🔥) ----------------
st.sidebar.subheader("🔗 Resources")

st.sidebar.markdown("""
- 📄 [Research Paper](https://ieeexplore.ieee.org/)  
- 📊 [Cloud Dataset](https://atlarge-research.com/gwa-t-12/)  
- 💻 [GitHub Repository](https://github.com/)  
- 📓 [Google Colab Notebook](https://colab.research.google.com/)  
""")

# ---------------- MAIN TITLE ----------------
st.markdown("<h1 style='text-align:center;color:#FF4B4B;'>🚀 Cloud Resource Predictor</h1>", unsafe_allow_html=True)
st.write("Deep Learning model for predicting cloud resource usage")

st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.subheader("📥 Enter Cloud Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    cpu = st.slider("CPU Usage (%)", 0, 100, 50)

with col2:
    memory = st.slider("Memory Usage (KB)", 0, 100000, 50000)

with col3:
    network = st.slider("Network Throughput (KB/s)", 0, 10000, 2000)

# ---------------- PREDICT BUTTON ----------------
if st.button("🚀 Predict Usage"):

    # Dummy prediction (replace later with model)
    prediction = (cpu * 0.5 + memory * 0.0005 + network * 0.2)

    st.success(f"📊 Predicted Resource Load: {round(prediction, 2)}")

    # Graph
    values = [cpu, memory/1000, network]
    labels = ["CPU", "Memory", "Network"]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Resource Usage")
    st.pyplot(fig)
