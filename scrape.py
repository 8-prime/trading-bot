import requests
import pandas as pd
from bs4 import BeautifulSoup


'''
Takes an integer specifiying how many of the top changers are to be returned
Takes Yahoo finance and parses for a list which is the list of the top gainers and then returns the first n entries
'''
def get_daily_top_n (top_n):
    URL = 'https://finance.yahoo.com/screener/predefined/day_gainers?guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAJPzhFJgI--8KNKwgdiM8Kk7WMl_EHqQdXXO5CTmur7k9dFFg15hppLMOhEDIO1kXDNbZHUeWbHd_C0YlFu7OQAvpyolavIM_C0mLJMi0KYNalp-jWYFz70rGmTjS96gm-8ZuMwPME_JOKIJPtZdeTnDHaBUvfar2oqZfEND0wIl&_guc_consent_skip=1596900194'
    page = requests.get(URL)

    df_list = pd.read_html(page.text)
    df = df_list[0]
    return(df['Symbol'][:top_n])