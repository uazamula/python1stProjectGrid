from bs4 import BeautifulSoup
import requests
from csv import writer
page_to_scrape= requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text,"html.parser")
quotes=soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"itemprop":"author"})
print(authors)
file=open('scraped.csv','w')
writer(file).writerow(['цитата', "автор"])
for quote, author in zip(quotes,authors):
    print(quote.text, '-', author.text)
    writer(file).writerow([quote.text, author.text])
file.close()