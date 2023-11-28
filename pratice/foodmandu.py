# library req:
# pip install requests
# pip install bs4

import requests
from  bs4 import BeautifulSoup

# url = "https://foodmandu.com/"
# r = requests.get(url)
# # print(r.text)
# source_code = r.text
# soup = BeautifulSoup(source_code)
# listing_div= soup.findAll("div",{"class":"listing"})
#  print(listing_div)
# for listing in listing_div:
#   print(listing.text.strip())


# url = "https://foodmandu.com/Restaurant/Details/1027"
# r = requests.get(url)
# source_code = r.text
# soup = BeautifulSoup(source_code)
# listing_div= soup.findAll("div",{"class":"ng-scope"})
# ul= soup.findAll("ul",{"class":"menu__items"})
# print(ul)
        
# print(ul)

# for listing in listing_div:
#   print(listing)

url="https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId=1027&show="
r = requests.get(url)
all_menus = r.json()
# print(r.text)

all_menus = all_menus[0]['items']
for menu in all_menus:
  print("name:",menu['name']," price : ",menu["price"])