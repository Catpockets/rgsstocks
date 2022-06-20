import yfinance as yf
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from datetime import date
import requests
from datetime import date, timedelta
import time

# Initial Setup
st.set_page_config(page_title="Boeing Stock", page_icon=":airplane:", layout="wide")
today = date.today()


st.sidebar.header("Options")
my_form = st.sidebar.form(key = "form1")
tickerSymbol = my_form.text_input(label = "Enter ticker symbol")
submit = my_form.form_submit_button(label = "Submit Symbol")

# Load animations from Lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_oAtVDo.json")

# Use local CSS
#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#local_css("/style/style.css")

# Header Selection
st.subheader("Analyst: Randell G Smith :chart_with_upwards_trend:")
st.title("Ticker Stock analysis using Streamlit")
st.write("""
This is a test application to demo the power of streamlit as a viable python coding solution with a live data set.
The live dataset is Yahoo Finance Python API (yfinance) and is a live datastream of stock market.
This application attempts to connect to live data feeds and plot out stock market performance.
""")

# Ticker data feed
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2000-5-31', end=today)
tickers = [tickerSymbol]
longName = tickerData.info['longName']
numshares = tickerData.info['marketCap']
profitMargins = tickerData.info['profitMargins']
grossMargins = tickerData.info['grossMargins']
operatingCashflow = tickerData.info['operatingCashflow']
revenueGrowth = tickerData.info['revenueGrowth']
totalCash = tickerData.info['totalCash']
totalDebt = tickerData.info['totalDebt']
dayLow = tickerData.info['dayLow']
dayHigh = tickerData.info['dayHigh']
logourl = tickerData.info['logo_url']

for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_close = data['Close'].iloc[-1]

for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_open = data['Open'].iloc[-1]

float_open = f"${last_open:.2f}"
float_close = f"${last_close:.2f}"
percentchange = f"{last_close / last_open:.2f}%"
#dayLow dayHigh
today = date.today()

col1, col2, col3 = st.columns(3)
col1.metric("Current Price", last_close, percentchange)
#col2.metric("Prior Day Price", priorday, "0")
#col3.metric("Humidity", "86%", "4%")

# Body Body
with st.container():
    st.write("---") # Dividert
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Ticker Information")
        st.write(f"Name: {longName}")
        st.image(logourl)
        st.write(f"Last Close: {last_close:.2f}")
        st.write(f"Day Low Trade: {dayLow}")
        st.write(f"Day High Trade: {dayHigh}")
        st.write(f"Market Cap: {numshares}")
        st.write(f"Profit Margins: {profitMargins}")
        st.write(f"Gross Margins: {grossMargins}")
        st.write(f"Operating Cash Flow: {operatingCashflow}")
        st.write(f"Total Cash: {totalCash}")
        st.write(f"Total Debt: {totalDebt}")       
    with right_column:
        st_lottie(lottie_coding, height=550, key="coding")

# Charts
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.line_chart(tickerDf.Close)
    with right_column:
        st.line_chart(tickerDf.Volume)

# Dataframe
st.header("RAW DATA")
dataf = tickerData.history(period="MAX")
st.write(dataf)
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

# csv = convert_df(dataf)
# 
# st.download_button(
#      label="Download data as CSV"
#      data=csv,
#      file_name='large_df.csv',
#      mime='text/csv',
#  )         
         
# Contact me
with st.container():
    st.write("---")
    st.header("Contact me!")
    st.write("##")

# documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/rgsmith787@gmail.com" method="POST">
        <input type="hidden" name="_capcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()





