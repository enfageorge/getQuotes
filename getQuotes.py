import requests
from bs4 import BeautifulSoup


tag=input("What topic would you like quotes in?")
pageno=1
link = "https://www.goodreads.com/quotes/tag/"+tag+"?page="+str(pageno)
result = requests.get(link)
#print result.text

soup = BeautifulSoup(result.text,'lxml')
#print soup.text

# kill all script and style elements

for script in soup(["script", "style"]):
    script.extract()

samples = soup.find_all("div", "quoteText")
print("Top 20 quotes on ",tag," are")
for quote in samples:
    print (quote.text)
#Write the quotes to a file
with open('quotefile.txt', 'w') as file:
    for quote in samples:
        file.write(str(quote.text.encode("utf-8")))
