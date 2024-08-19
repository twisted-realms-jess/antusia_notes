# Description: the script that runs the streamlit app
# Created by: Jess Williamson
# Created on: 19/08/2024

# Import python packages
import streamlit as st
import pandas
from ruamel.yaml import YAML

# Set up the app header
st.title("Welcome to the Antusia notes app!")
st.write(
    """Search for notes using the search bar below
    """
)

yaml = YAML()
input_file = 'notes.yaml'

for key, value in yaml.load(open(input_file)).items():
    print(str(key))

search_item = st.text_input("Search: ")

if search_item:
    st.subheader(search_item + ":")
    
