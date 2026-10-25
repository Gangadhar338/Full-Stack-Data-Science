import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")
data = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "region": ["North", "South", "North", "South"],
    "sales": [1200, 950, 1450, 1300],
})
regions = st.multiselect("Region", sorted(data["region"].unique()), default=sorted(data["region"].unique()))
filtered = data[data["region"].isin(regions)]
st.metric("Total sales", f"{filtered['sales'].sum():,.0f}")
st.dataframe(filtered, use_container_width=True)
if not filtered.empty:
    st.bar_chart(filtered.set_index("month")["sales"])
else:
    st.info("Select at least one region to view data.")
