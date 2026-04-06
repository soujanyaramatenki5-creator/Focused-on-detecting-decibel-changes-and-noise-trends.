import streamlit as st
from data_genrator import generate_noise_data
from preprocess import add_features
from predction import train_model, predict_future
from anamoly import detect_anomalies
from cluster import cluster_patterns
from plot import plot_time_series
st.set_page_config(page_title="Noise Tool", layout="wide")
# Load Data
if 'data' not in st.session_state:
    st.session_state.data = generate_noise_data()
df = st.session_state.data
st.title("🔊 Noise Analysis Tool")
# Show Data
st.write(df.head())
# Plot
fig = plot_time_series(df)
st.pyplot(fig)
# Prediction
if st.button("Predict"):
    df_feat = add_features(df)
    features = ['hour_sin', 'hour_cos', 'day_sin', 'day_cos',
                'lag_1', 'lag_6', 'lag_12', 'lag_24']

    model = train_model(df_feat, features)
    preds = predict_future(model, df_feat, features, 24)

    st.write("Predictions:", preds)

# Anomaly
if st.button("Detect Anomalies"):
    anomaly_df = detect_anomalies(df)
    st.write(anomaly_df.head())

# Clustering
if st.button("Cluster Patterns"):
    clusters = cluster_patterns(df)
    st.write(clusters)