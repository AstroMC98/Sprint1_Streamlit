import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import os

# Set page title
st.set_page_config(page_title="My First Streamlit Project", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("What Page Should I Open", ["Overall", "Introduction", "Methodology"])


# Ensure directories exist
data_dir = "data"
image_dir = "images"
plot_dir = "plots"

# Overall Section
if menu == "Overall" :
  st.title("Overall Summary")
  st.write("This is an overview of the project.")

  overall_image_path = os.path.join(image_dir, "mochi.png")
  st.image(overall_image_path, caption="Mochi", use_column_width=True)

  X_VALUES = range(10)
  Y_VALUES = [i**2 for i in X_VALUES]

  fig, ax = plt.subplots()
  ax.plot(X_VALUES,Y_VALUES)
  ax.set_title("Sample Plot")
  st.pyplot(fig)
