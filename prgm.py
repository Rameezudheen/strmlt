import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Demo")
st.markdown("## Streamlit  ")

url_link = "https://www.google.com/search?channel=fs&client=ubuntu&q=youtube"
st.markdown(url_link)
dat = pd.read_csv('auto_data.csv')
dt = dat.head(10)
st.table(dt)
st.header("Visualisation ")
st.subheader("Bar Plot")
dt.plot(kind='bar')
st.pyplot()
st.subheader("Displot")
sns.displot(dt['displacement'])
st.pyplot()
st.subheader("JointPlot")
sns.jointplot(x='displacement',y='mpg',data=dt,kind='scatter')
st.pyplot()
st.subheader("Rugplot")
sns.rugplot(dt['horsepower'])
st.pyplot()
status = st.radio("What is your status",('Active','Inactive'))
if status == 'Active':
	st.text("Status is Active")
else:
	st.warning("Not Active Yet")
occupation = st.selectbox("interested area",['programming','debugging','testing','documentation'])
st.write("You selected this option",occupation)
name = st.text_input("Enter Name","Type Here...")
if st.button('Submit'):
    result = name.title()
    st.success(result)
else:
    st.write("Press the above button..")
st.sidebar.header("Dashboard")
st.sidebar.text("Details")

