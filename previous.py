import pandas as pd
import streamlit as st
import plotly.offline as py
import plotly.figure_factory as ff
import plotly.graph_objects as go
#the dataset incloudes the covid-19 vaccination status around the world
#it can be downloaded from URL: https://www.kaggle.com/gpreda/covid-world-vaccination-progress
df = pd.read_csv("country_vaccinations.csv")
st.title('Uber pickups in NYCf')
st.bar_chart(df['daily_vaccinations'])
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.country, y=df.total_vaccinations, mode = 'lines+markers'))
fig.update_layout(
    title="Total vaccinations per country",
    xaxis_title="Country",
    yaxis_title="Total vaccinations",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="blue"
    )
)
