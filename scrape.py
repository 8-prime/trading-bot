import requests
import bs4 as bs



URL = 'https://finance.yahoo.com/screener/predefined/day_gainers?guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAJPzhFJgI--8KNKwgdiM8Kk7WMl_EHqQdXXO5CTmur7k9dFFg15hppLMOhEDIO1kXDNbZHUeWbHd_C0YlFu7OQAvpyolavIM_C0mLJMi0KYNalp-jWYFz70rGmTjS96gm-8ZuMwPME_JOKIJPtZdeTnDHaBUvfar2oqZfEND0wIl&_guc_consent_skip=1596900194'
page = requests.get(URL)

soup =  BeautifulSoup(page.content, 'html.parser')
