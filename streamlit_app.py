# Description: the script that runs the streamlit app
# Created by: Jess Williamson
# Created on: 19/08/2024

# Import python packages
import streamlit as st
import pandas as pd
from ruamel.yaml import YAML
import requests

# Set up the app header
st.title("Welcome to the Antusia notes app!")
st.write(
    """Search for notes using the search bar below
    """
)

# Load notes data 
url = 'https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/notes.json'
response = requests.get(url)
st.write(response.text)
#response_df = st.dataframe(data=response.json(), use_container_width=True)

search_item = st.text_input("Search: ")

if search_item:
    st.subheader(search_item + ":")
    
