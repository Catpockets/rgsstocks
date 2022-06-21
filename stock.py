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
todaylastyear = today - timedelta(days=365)

# Sidebar Setup
st.sidebar.header("Options")
my_form = st.sidebar.form(key = "form1")
tickerSymbol = my_form.text_input(label = "Enter ticker symbol")
st.sidebar.write(f"Today is: {today}")
start_date = my_form.date_input("Starting Date", value=pd.to_datetime(todaylastyear, format="%Y-%m-%d"))
end_date = my_form.date_input("Ending Date Date", value=pd.to_datetime(today, format="%Y-%m-%d"))

submit = my_form.form_submit_button(label = "Submit Symbol")
st.markdown(
"""
<style>
.stApp {
    background-color: #0D1117;
    color: #FFFFFF;
    }
div.css-ocqkz7 e1tzin5v4 {
    background-color: #EEEEEE;
</style>


""", unsafe_allow_html=True
)


if not tickerSymbol:
    st.header("Please enter a ticker symbol into the sidebar")
elif tickerSymbol == '69':
    st.header("Nice")
    st.video("https://youtu.be/dQw4w9WgXcQ")
elif tickerSymbol == '420':
    st.header("Drugs are Bad...")
    st.video("https://youtu.be/dAHoxaphbEs")
else:
    st.header(f"Your ticker is {tickerSymbol}")
    
    # Load animations from Lottie
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json")

    # Use local CSS
    #def local_css(file_name):
    #    with open(file_name) as f:
    #        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    #local_css("/style/style.css")

    # Ticker data feed
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
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

    # Header Selection

    with st.container():
        st.write("---") # Dividert
        st.subheader("Analyst: Randell G Smith :chart_with_upwards_trend:")
        st.title("Ticker Stock analysis using Streamlit")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("""
            This is a test application to demo the power of streamlit as a viable python coding so
            The live dataset is Yahoo Finance Python API (yfinance) and is a live datastream of st
            This application attempts to connect to live data feeds and plot out stock market perf

            This application will take user input in sidebar and automatically pull data from API 
            """)

        with right_column:
            st_lottie(lottie_coding, height=250, key="coding")

    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", float_close, percentchange)

    # Body Body
    with st.container():
        st.write("---") # Dividert
        st.header("Ticker Information")
        st.write(f"Name: {longName}")
        st.image(logourl)
        left_column, right_column = st.columns(2)
        with left_column:

            st.write(f"Last Close: {last_close:.2f}")
            st.write(f"Day Low Trade: {dayLow}")
            st.write(f"Day High Trade: {dayHigh}")
            st.write(f"Market Cap: {numshares}")
            st.write(f"Profit Margins: {profitMargins}")

        with right_column:
            st.write(f"Gross Margins: {grossMargins}")
            st.write(f"Operating Cash Flow: {operatingCashflow}")
            st.write(f"Total Cash: {totalCash}")
            st.write(f"Total Debt: {totalDebt}") 

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
