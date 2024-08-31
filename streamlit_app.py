# Description: the script that runs the streamlit app
# Created by: Jess Williamson
# Created on: 19/08/2024

# Import python packages
import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Set up the app header
st.title("Welcome to the Antusia notes app!")
st.write(
    """Search for notes using the search bar below
    """
)

# Load notes data 
def load_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.read_csv(StringIO(response.text))
        return df
    else:
        return st.error('Failed to load data from GitHub.')

character_df = load_data('https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/characters.csv')
# st.write(character_df)
character_list = character_df['Search Term'].unique()

session_df = load_data('https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/sessions.csv')
# st.write(session_df)
session_list = session_df['Session'].unique()

search_item = st.text_input("Search: ")

if search_item:
    if search_item in character_list:
        st.subheader(search_item + ":")
        filtered_df = character_df.loc[character_df['Search Term'] == search_item]
        st.dataframe(filtered_df.set_index(filtered_df.columns[0]))
    if search_item in session_list:
        st.subheader(search_item + ":")
        filtered_df = session_df['Notes'].loc[session_df['Session'] == search_item]
        st.dataframe(filtered_df.set_index(filtered_df.columns[0]))
    
