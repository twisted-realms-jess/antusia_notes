# Description: the script that runs the streamlit app
# Created by: Jess Williamson
# Created on: 19/08/2024

# Import python packages
import streamlit as st
import pandas

# Set up the app header
st.title("Welcome to the Antusia notes app!")
st.write(
    """Search for notes using the search bar below
    """
)

search_item = st.text_input("Search: ")

if search_item:
    st.subheader(search_item + ":")
