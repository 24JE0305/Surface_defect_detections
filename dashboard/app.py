import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Defect Detection System", layout="wide")

st.title("🔍 Surface Defect Detection Dashboard")
st.markdown("Real-time defect detection analytics powered by YOLOv8 + PostgreSQL")

# fetch data from API
try:
    response = requests.get("http://127.0.0.1:8000/detections")
    data = response.json()
except:
    st.error("API not running. Start it with: uvicorn api.main:app --reload")
    st.stop()

if len(data) == 0:
    st.warning("No detections in database yet.")
    st.stop()

# convert to dataframe
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['confidence'] = df['confidence'].round(3)

# top metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Detections", len(df))
col2.metric("Unique Defect Types", df['defect_class'].nunique())
col3.metric("Avg Confidence", f"{df['confidence'].mean():.2%}")

st.divider()

# bar chart
st.subheader("Detections by Defect Class")
class_counts = df['defect_class'].value_counts()
st.bar_chart(class_counts)

st.divider()

# confidence per class
st.subheader("Average Confidence per Class")
avg_conf = df.groupby('defect_class')['confidence'].mean().round(3)
st.bar_chart(avg_conf)

st.divider()

# raw detections table
st.subheader("All Detections")
st.dataframe(
    df[['id', 'timestamp', 'defect_class', 'confidence', 'image_path']],
    use_container_width=True
)