#crawling
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
stockList = soup.find(id='popularItemList').find_all('li')

dataList = []
for i in stockList:
    company = i.find('a').text
    stock= i.find('span').text
    dataList.append({'company': company, 'stock':stock})
print(dataList)

#for i in stockList:
#   print(i.text)
#   #[{company: '현대차', stock:227000}]


