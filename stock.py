import yfinance as yf
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from datetime import date
import requests
from datetime import date, timedelta
import time

# Initial Setup
st.set_page_config(page_title="Stock Prices", page_icon=":chart_with_upwards_trend:", layout="wide")
today = date.today()

# Sidebar Setup
st.sidebar.header("Options")
my_form = st.sidebar.form(key = "form1")
tickerSymbol = my_form.text_input(label = "Enter ticker symbol")
submit = my_form.form_submit_button(label = "Submit Symbol")

if not tickerSymbol:
    st.Title("Please enter a ticker symbol into the sidebar")
else:
    st.Title(f"Your ticker is {tickerSymbol}")
    
