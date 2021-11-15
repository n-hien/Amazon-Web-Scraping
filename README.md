# Amazon Product Analysis

<h2>Web Scraping</h2>
- Libraries: request, BeautifulSoup, pandas<br>
- Function <a href = 'https://github.com/n-hien/Amazon-Product-Analysis/blob/main/earbudsScraper.py'> get_data </a> is used to get the data from each page, and append it to dataFrame<br>
- Then, loop through all pages and save dataset in .csv file
<h2>Product Price Analysis</h2>
- Libraries:matplotlib, pandas, seaborn <br>
- Firstly, duplicates in the "Asin" column will be removed <br>
- Then,the datatypes of price, Rating and Number of Rating will be converted to numeric for analysis purpose<br>
- Using dataFrame.describe() and boxplot to see the distribution of product price
<p><div style="background-color: grey;">
 -----------------<br>
count    250.00000 <br>
mean      73.25436 <br>
std       72.46441 <br>
min        6.79000 <br>
25%       29.99000 <br>
50%       41.19000 <br>
75%       92.49000 <br>
max      619.80000 <br>
Name: Price, dtype: float64<br>
  -----------------</div>
</p>
<p align="center">
  <img src="boxplot.png">
</p>
- Filter the top 20 products based on Rating and draw a scatter plot of these top 20 products
<p align="center">
  <img src="scatterplot.png">
</p>
- We maybe want to buy the product with Asin-B09J8HTDHX

<h2>Product Review Analysis</h2>
- Libraries: request, BeautifulSoup, pandas, nltk<br>
- Function <a href='https://github.com/n-hien/Amazon-Product-Analysis/blob/main/ReviewScraper.ipynb'> get_review</a> is used to get all reviews of products <br>
<p align="center">
  <img src="reviews.PNG">
</p>
<p align="center">
  <img src="wcloud.png">
</p>

