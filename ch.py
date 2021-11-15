import pandas as pd 
df = pd.read_csv('amazon_earbuds.csv')
df.drop_duplicates(subset=['Asin'], inplace = True) # now we have 250  rows instead of 381 as at the beginning
data_asin = list(df.Asin)
data_asin[0:5]
import requests
from bs4 import BeautifulSoup

#Now create link to product with ASIN and get the link to page contains all customer reviews
def get_review(asin):
    url="https://www.amazon.de/dp/"+asin #get product link
    header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36 Edg/95.0.1020.44'}
    r = requests.get(url, headers = header) #down page
    content = r.content
    soup=BeautifulSoup(content,"html.parser")
    #search link to page contains all customer reviews
    i = soup.find('a',{'data-hook':'see-all-reviews-link-mobile'})
        #search and append reviews to dataFrame
    link = i['href']
    if link is None:
        pass
    else:
        #search reviews on all pages
        review_data = pd.DataFrame(columns=['Rating', 'Review Title','Review Content'])
        for i in range(50):
            url_review ='https://www.amazon.de'+link+'&pageNumber='+str(i)
            re = requests.get(url, headers = header)
            content_r = re.content
            soup_r=BeautifulSoup(content_r,"html.parser")
            for j in soup_r.find_all('div',{'data-hook':'mobley-review-content'}):
                ratings = j.find_all('i',{'data-hook':'review-star-rating'})
                titles = j.find_all('span',{'data-hook':'review-title'})
                reviews = j.find_all('div',{'class':'a-row a-spacing-small cr-full-content aok-hidden'})
                for element in ratings:
                    if element is not None:
                        rating = element.text
                    else:
                        rating = 'unknown'
                for element in titles:
                    if element is not None:
                        title = element.text.strip()
                    else:
                        title = 'unknown' 
                for element in reviews:
                    if element is not None:
                        review = element.text.strip()
                    else:
                        review_content = 'unknown'
                review_data = review_data.append({'Rating':rating, 'Review Title':title,'Review Content':review},ignore_index=True)
        return review_data
result = pd.DataFrame()
for i in range(10):
    df = get_review(data_asin[i])
    result = result.append(df)
result.to_csv('allreviews.csv', index=False, encoding='utf-8')