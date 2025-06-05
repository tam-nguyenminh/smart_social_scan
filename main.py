import streamlit as st
import justify
import json 
import pandas as pd

# add the title
st.title("Smart Social Scan", anchor="main")

# intro
st.subheader("Project 🧴")
st.image("equippos.png", use_container_width=False)

st.subheader("Voice of the Customer 📢🤖")
st.image("graphvoc.png", use_container_width=False)

# add the description
st.write("This is a tool to scan social media posts for potential risks and provide justifications for those risks.")
secret_key = st.secrets["secret_key"]

# add the input file as json

st.write("Please upload a JSON file containing social media posts data.")
uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

if uploaded_file is not None:
    # Read the uploaded file
    try:
        input_data = uploaded_file.read()
        st.write("File uploaded successfully!")
        # st.json(input_data)  # Display the JSON content

    except Exception as e:
        st.error(f"Error reading file: {e}")

# add the json file to justify.py
    st.write("Processing the uploaded data...")
    # Here you would typically call your justify.py logic
    # df_result = justify.call_prompt(input_data, secret_key)
    # Example of displaying a message after processing
    st.success("Justification completed successfully!")

