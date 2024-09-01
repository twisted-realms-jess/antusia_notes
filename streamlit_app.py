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
# st.write(
#     """Search for notes using the search bar below:
#     """
# )

# Function to load data
def load_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.read_csv(StringIO(response.text))
        return df
    else:
        return st.error('Failed to load data from GitHub.')

# Load character data
character_df = load_data('https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/characters.csv')
character_list = character_df['Search Term'].unique()
character_categories = character_df['Category'].unique()
#character_details = pd.Series(df.Note.values,index=df.Subcategory).to_dict()

# Load session data
session_df = load_data('https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/sessions.csv')
session_list = session_df['Session'].unique()

# Search item input
search_item = st.text_input("Search for a topic: ")

# Search item display
if search_item:
    if search_item in character_list:
        st.header(search_item + ":")
        filtered_df = character_df.loc[character_df['Search Term'] == search_item]
        for category in character_categories:
            st.subheader(category + ":", divider="gray")
            details = filtered_df[filtered_df['Category'] == category]
            character_details = pd.Series(details.Note.values,index=details.Subcategory).to_dict()
            for key, value in character_details.items():
                st.write(key + " = " + value)
        #st.dataframe(filtered_df.set_index(filtered_df.columns[0]),use_container_width=True)
    if search_item in session_list:
        st.subheader(search_item + ":")
        filtered_df = session_df.loc[session_df['Session'] == search_item]
        #st.dataframe(filtered_df.set_index(filtered_df.columns[0]))
        for note in filtered_df['Notes']:
            st.write("- " + note)
    
