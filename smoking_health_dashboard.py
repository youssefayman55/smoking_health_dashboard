# importing libraries
import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Smoking Health Dashboard",
                   page_icon= None,
                   layout= "wide",
                   initial_sidebar_state="expanded")
# loading data
data = pd.read_csv('smoking_health_data_final.csv')

# sidebar
st.sidebar.header("Smoking Health Dashboard")
st.sidebar.image('download.jpeg')
st.sidebar.write("This dashboard is using smoking health data from kaggle website for educational purposes")

st.sidebar.write("")
st.sidebar.write("Filter your data :")
categorical_filter = st.sidebar.selectbox("Categorical Filtering" , [None ,"sex" ,"current_smoker"])
numerical_filter = st.sidebar.selectbox("Numerical Filtering" , [None ,"age" ,"heart_rate"])

st.sidebar.write("")
st.sidebar.markdown("Made with  :heart_eyes: by Eng.[Youssef Ayman](https://www.linkedin.com/in/youssef-ayman-4440342a4/)")


# body 

# row a
a1 , a2 , a3 , a4 = st.columns(4)

a1.metric("max age " , data["age"].max())
a1.metric("min age " , data["age"].min())

a2.metric("max heart_rate " , data["heart_rate"].max())
a2.metric("min heart_rate " , data["heart_rate"].min())

a3.metric("max blood_pressure " , data["blood_pressure"].max())
a3.metric("min blood_pressure " , data["blood_pressure"].min())

a4.metric("max chol " , data["chol"].max())
a4.metric("min chol " , data["chol"].min())

# row b
st.subheader("blood_pressure vs. heart_rate")
figure1 = px.scatter(data_frame= data ,
                    x = "blood_pressure" ,
                    y= "heart_rate",
                    color= categorical_filter,
                    size= numerical_filter
                   )
st.plotly_chart(figure1 , use_container_width= True)

# row c
st.subheader("chol vs. heart_rate")
figure2 = px.scatter(data_frame= data ,
                    x = "chol" ,
                    y= "heart_rate",
                    color= categorical_filter,
                    size= numerical_filter
                    )
st.plotly_chart(figure2 , use_container_width= True)

#row d

c1 , c2 , c3 = st.columns((4,3,3))

with c1 :
    st.write("sex vs. current_smoker")
    fig1 = px.bar(data_frame=data , x= "sex" , y= "current_smoker" ,color= categorical_filter )
    st.plotly_chart(fig1 , use_container_width= True)

with c2 :
    st.write("current_smoker vs. age")
    fig2 = px.pie(data_frame=data , names= "current_smoker" , values= "age" ,color= categorical_filter )
    st.plotly_chart(fig2 , use_container_width= True)

with c2 :
    st.write("current_smoker vs. current_smoker")
    fig3 = px.pie(data_frame=data , names= "current_smoker" , values= "chol" ,color= categorical_filter , hole= 0.4 )
    st.plotly_chart(fig3 , use_container_width= True)