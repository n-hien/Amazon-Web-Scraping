# Amazon Product Analysis

<h2>Web Scraping</h2>
- libraries: request, BeautifulSoup, pandas<br>
- function <i> get_data </i> is used to get the data from each page, and append it to dataFrame<br>
- then, loop through all pages and save dataset in .csv file
<h2>Product Analysis</h2>
- Firstly, duplicates in the "Asin" column will be removed br>
- Then,the datatypes of price, Rating and Number of Rating will be converted to numeric for analysis purposebr>
- Using dataFrame.describe() and boxplot to see the distribution of product price
<p align="center">
  <img src="boxplot.png">
</p>
- Filter the top 20 products based on Rating and draw a scatter plot of these top 20 products  
<p align="center">
  <img src="scatterplot.png">
</p>




