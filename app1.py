import streamlit as st
import plotly.express as px

st.title("My Web App")
numbers = st.text_input("Enter multiple numbers separated by space")
num_list = list(map(int,numbers.split()))
# line graph
st.area_chart(num_list, use_container_width=True)
# bar chart
st.bar_chart(num_list, use_container_width=True)

x = st.text_input("Enter numbers separated by space for x")
y = st.text_input("Enter numbers separated by space for y")
x_list = list(map(int,x.split()))
y_list = list(map(int,y.split()))
if len(x_list) != len(y_list):
    st.error("Length of x and y must be same")
else:
    st.plotly_chart(px.scatter(x=x_list, y=y_list, title="Scatter Plot"))
    c1, c2 = st.columns(2)
    c1.plotly_chart(px.histogram(x=x_list, title="Histogram X"), use_container_width=True)
    c2.plotly_chart(px.histogram(x=y_list, title="Histogram Y"), use_container_width=True)