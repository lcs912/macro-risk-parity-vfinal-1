import yfinance as yf

def get_data():

    df = yf.download(["SPY","QQQ","TLT","GLD"], period="1y")["Close"]

    return df.dropna()
