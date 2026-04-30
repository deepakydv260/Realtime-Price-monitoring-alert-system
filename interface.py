import streamlit as st
from PIL import Image
import pandas as pd
import requests
import plotly.express as px


img = Image.open("Logo of project.png")
st.image(img,width = 700)

st.set_page_config(page_title="Fake Store Insights",page_icon="🌐",layout="wide")
st.title("Fake Store API - Interactive DASHBOARD")
Api="https://fakestoreapi.com/products"

@st.cache_data
def load_data():
    response = requests.get(Api)
    data=response.json()
    df= pd.DataFrame(data)
    return df

df= load_data()

st.subheader("Dataset Overview")
st.dataframe(df,use_container_width=True)

#basic cleaning
df['price'] = df['price'].astype(float)
df['category'] = df['category'].astype(str)

#slider
st.sidebar.header("🚦Filters")
categories= st.sidebar.multiselect(
    "Select Category",
    df['category'].unique(),default=df['category'].unique())
filtered_df= df[df['category'].isin(categories)]

#kpi
st.header("Key Insights")
col1,col2,col3= st.columns(3)

col1.metric("Total Product",len(filtered_df))
col2.metric("Average Price",f"${filtered_df['price'].mean():.2f}")
col3.metric("Highest Price",f"${filtered_df['price'].mean():.2f}")                  

#visuals
st.header("👾Key Insights")
#barchart :- categories count
cate_count= filtered_df["category"].value_counts().reset_index()
fig_bar = px.bar(cate_count,x="category",y="count",title="products count by category")
st.plotly_chart(fig_bar,use_container_width= True)

#price distribution
fig_hist=px.histogram(filtered_df,x='price',nbins=20,title="price Distribution")
st.plotly_chart(fig_hist,use_container_width=True)

#scatter Prive vs Id
fig_scatter= px.scatter(filtered_df,x="id",y="price",
                        color="category",title="price by Product ID")
st.plotly_chart(fig_scatter,use_container_width=True)

#table view
st.header("Filtered Product")
st.dataframe(filtered_df,use_container_width=True)

#download button
csv= filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered Data(csv)",csv,
                   "filtered_data.csv","text/csv")

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