import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("YEET")

    query_id = "c96f0ab3-0f21-40bf-883a-90b566ed4320"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)


    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    

    st.dataframe(df)

    st.markdown("""
    """)
    

    st.sidebar.header("Choose Columns:")
    columns = st.sidebar.multiselect(
        "Select the columns to plot",
        options = df.columns,
        default = df.columns.max()
    )


    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "FIRST_TX",
        y = columns,
        color = "CLAIMER",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df)

    # ------------------------------------------------

# https://app.flipsidecrypto.com/velocity/queries/c96f0ab3-0f21-40bf-883a-90b566ed4320