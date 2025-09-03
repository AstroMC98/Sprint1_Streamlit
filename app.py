import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import os

# Set page title
st.set_page_config(page_title="My First Streamlit Project", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("What Page Should I Open", ["Overall", "Introduction", "Methodology"])
