import pandas as pd
import plotly.express as px
import streamlit as sl

df = pd.read_csv(r"c:\Users\Cronoss\Documents\Dashboards\Data\vgsales.csv") # load the Dataset
df[["Rank", "Name"]] # Select the columns Rank and Name


