import streamlit as st
import justify
import json 
import pandas as pd

# add the title
st.title("Smart Social Scan", anchor="main")
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

# read post_justified.json file
df_result = justify.read_json('post_justified.json')
# Display the DataFrame in Streamlit

col1, col2 = st.columns(2)
with col1:
    # count the rows in a card
    st.subheader("#posts justified:")
    metric_value = len(df_result)

    # Use HTML and CSS for full customization
    st.markdown(f"<span style='color:red; font-size:50px; font-weight:bold'>{metric_value}</span>", unsafe_allow_html=True)
    # st.metric(label="Total Posts Justified", value=len(df_result), border=True)

with col2:
    # display the impact score in a column
    st.subheader("Impact Score Distribution:")
    st.bar_chart(df_result['impact_score'],horizontal=True, color = "#FF0000")

# Display the justification results
st.write("Justification Results:")
st.dataframe(df_result.sort_values(by='impact_score', ascending=False).reset_index(drop=True), use_container_width=True)