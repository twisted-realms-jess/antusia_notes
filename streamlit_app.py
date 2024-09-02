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

# Load session data
session_df = load_data('https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/sessions.csv')
session_list = session_df['Session'].unique()

# Load place data
place_df = load_data('https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/places.csv')
place_list = place_df['Place'].unique()

# Load image data
image_df = load_data('https://raw.githubusercontent.com/twisted-realms-jess/antusia_notes/main/images.csv')
image_list = image_df['Search Term'].unique()

# Search item input
search_item = st.text_input("Search for a topic: ")

# Search item display
if search_item:
    st.header(search_item + ":")
    if search_item in image_list:
        image_url = f"./images/" + search_item.lower() + ".jpeg"
        st.image(image_url, width=2)

if search_item:
    if search_item in character_list:
        filtered_df = character_df.loc[character_df['Search Term'] == search_item]
        character_categories = filtered_df['Category'].unique()
        for category in character_categories:
            st.subheader(category + ":", divider="gray")
            details = filtered_df[filtered_df['Category'] == category]
            character_details = pd.Series(details.Note.values,index=details.Subcategory).to_dict()
            for key, value in character_details.items():
                st.write(key + " = " + value)
    elif search_item in place_list:
        filtered_df = place_df.loc[place_df['Place'] == search_item]
        place_categories = filtered_df['Category'].unique()
        for category in place_categories:
            st.subheader(category + ":", divider="gray")
            details = filtered_df[filtered_df['Category'] == category]
            for note in details['Note']:
                st.write("- " + note)
    elif search_item in session_list:
        filtered_df = session_df.loc[session_df['Session'] == search_item]
        for note in filtered_df['Notes']:
            st.write("- " + note)
    
