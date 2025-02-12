import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


st.title("Hello World")
st.header("This is a header with a divider", divider="gray")
st.header("One", divider=True)
col1,col2=st.columns(2)
with col1:
    x = st.slider("Choose X value",1,10)
with col2:
    st.write(":blue[***You choose x =***]",x)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=("a","b","c"))
st.table(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)
st.line_chart(chart_data)
st.dataframe(chart_data)
st.metric(label="Revenue", value="$500K", delta="-5%")
