import pandas as pd 
import requests
from bs4 import BeautifulSoup

no_pages = 7
search_key = 'damenuhr+silber'
getfile = 'amazon_damenuhr.csv'
def get_data(pageNo): 
    ##download the contents of webpage and store in data
    header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36 Edg/95.0.1020.44'}
    url= 'https://www.amazon.de/s?k='+search_key+'&page='+str(pageNo)
    r = requests.get(url, headers = header)
    content = r.content
    soup=BeautifulSoup(content,"html.parser")

    data = pd.DataFrame(columns=['Asin','Product Name','Price','Rating','Number of Rating'])
    ##extract data e.g.: product name, price, rating, asin (Amazon Standard Identification Number)
    for i in soup.find_all('div',attrs={'class':['s-result-item s-asin sg-col s-widget-spacing-small sg-col-6-of-12','s-result-item s-asin AdHolder sg-col s-widget-spacing-small sg-col-6-of-12']}):
        asin= i['data-asin']  #extract asin
        names = i.find_all('h2')
        prices = i.findAll('span', attrs={'class':'a-price-whole'})
        ratings = i.findAll('span', attrs={'class':'a-icon-alt'})
        users_rated = i.findAll('span', attrs={'class':'a-size-mini a-color-base s-light-weight-text'})
        for element in names:
            if element is not None:
                name = element.text
            else:
                name = 'unknown'
        for element in prices:
            if element is not None:
                price = element.text
            else:
                price = 'unknown'
        for element in ratings:
            global rating 
            if element is not None:
                rating = element.text
            else:
                rating = 'unknown'
        for element in users_rated:
            global rated
            if element is not None:
                rated = element.text
            else:
                rated = '0'
        if asin is not None:
            data = data.append({'Asin':asin,'Product Name':name,'Price':price,'Rating':rating,'Number of Rating':rated},ignore_index=True)
    return data


result = pd.DataFrame()
for i in range(1,no_pages+1):
    df = get_data(i)
    result = result.append(df)
result.to_csv(getfile, index=False, encoding='utf-8')