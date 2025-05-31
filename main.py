import streamlit as st
import justify

# add the title
st.title("Smart Social Scan", anchor="main")
# add the description
st.write("This is a tool to scan social media posts for potential risks and provide justifications for those risks.")

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
    justify.read_key_value('smart_social_scan/secrete.json')
    # Example of displaying a message after processing
    st.success("Justification completed successfully!")