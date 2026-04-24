import streamlit as st
from PIL import Image

img = Image.open("Logo of project.png")
st.image(img,width = 700)

st.title("Realtime-Price-Monitoring-alert_system")

st.header("Daily Price Tracking")
st.header("Historical storage")
st.header("Daily Price")
st.header("Price Comparison")
st.header("Alert system for Price Charge")
st.header("Automated Pipeline")
st.markdown("---")

st.subheader("Database Connective")
st.success("Proceed Successfully")
st.info("Find The Formal Information")
st.warning("You are going to high risk scenario")
st.error("Account has been blocked for 24 hours")