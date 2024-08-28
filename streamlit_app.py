# Description: the script that runs the streamlit app
# Created by: Jess Williamson
# Created on: 19/08/2024

# Import python packages
import streamlit as st
import pandas as pd
import requests

# Set up the app header
st.title("Welcome to the Antusia notes app!")
st.write(
    """Search for notes using the search bar below
    """
)

# Load notes data 
url = 'https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/notes.csv'
response = requests.get(url)

if response.status_code == 200:
    df = pd.read_csv(StringIO(response.text))
    print(df)
else:
    st.error(“Failed to load data from GitHub.”)

# st.write(response.text)
# response_df = st.dataframe(data=response.text, use_container_width=True)

# search_item = st.text_input("Search: ")

# if search_item:
#     st.subheader(search_item + ":")
    
