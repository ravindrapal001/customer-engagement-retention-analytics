
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Customer Retention Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Engagement & Product Utilization Analytics")
st.subheader("Customer Retention Strategy Dashboard")

# Locate the CSV in the same folder as this script
data_path = Path(__file__).parent / "European_Bank.csv"

if data_path.exists():
    df = pd.read_csv(data_path)

    st.success("Dataset loaded successfully!")

    st.metric("Total Customers", f"{len(df):,}")

    if "Exited" in df.columns:
        st.metric("Churn Rate", f"{df['Exited'].mean():.2%}")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

else:
    st.error("European_Bank.csv was not found.")
