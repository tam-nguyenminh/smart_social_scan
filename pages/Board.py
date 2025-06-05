import streamlit as st

import json 
import pandas as pd
import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import justify

# a must to put set_page_config at the top of the pyfile
st.set_page_config(layout='centered')


st.title('Alert Board')
st.image("gif alert small ngang.gif", use_container_width=True)
df_result = justify.read_json('post_justified.json')
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