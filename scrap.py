from bs4 import BeautifulSoup
import requests
from csv import writer

Url= "https://www.apartments.com/woodbridge-va/"
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
page = requests.get(url=Url,headers=header)


soup = BeautifulSoup(page.content, 'html5lib')


lists = soup.find('section', class_="placards placardsv2")

with open('./Desktop/housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Address', 'Price', 'Beds']
    thewriter.writerow(header)

    for list in lists.find_all('li', class_="mortar-wrapper"):
        title = list.find('span', class_="js-placardTitle title").text
        location = list.find('div', class_="property-address js-url").text
        price = list.find('p', class_="property-pricing").text
        area = list.find('p', class_="property-beds").text

        info = [title, location, price, area]
        print(info)
        thewriter.writerow(info)
