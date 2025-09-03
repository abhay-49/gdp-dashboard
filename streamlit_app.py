import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Child Weight Gain Dashboard",
    page_icon=":baby:",
)

# Title
st.title("📊 Child Weight Gain Dashboard")

# -----------------------
# Sample Data (replace later with Excel upload)
# -----------------------
data = {
    "Year": [2000, 2005, 2010, 2015, 2020],
    "Normal_WeightGain": [12, 14, 15, 16, 18],
    "Comorbid_WeightGain": [8, 9, 10, 11, 13],
}
df = pd.DataFrame(data)

# -----------------------
# Show Raw Data
# -----------------------
st.header("Raw Data")
st.dataframe(df)

# -----------------------
# Graphs
# -----------------------
st.header("Weight Gain Trends Over Time")
st.line_chart(df.set_index("Year")[["Normal_WeightGain", "Comorbid_WeightGain"]])

st.header("Comparison in 2020")
year2020 = df[df["Year"] == 2020][["Normal_WeightGain", "Comorbid_WeightGain"]]
st.bar_chart(year2020.T)
