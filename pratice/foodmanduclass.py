import requests
from bs4 import BeautifulSoup
import csv
class FoodmanduFetch:
    def __init__(self):
        self.url="https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId={restruant_id}&show="
    def scrape_menu(self,restruant_id):
        r=requests.get(self.url.format(restruant_id=restruant_id))
        all_menus = r.json()
# print(r.text)

        all_menus = all_menus[0]['items']
        output =[]
        for menu in all_menus:
         print("name:",menu['name']," price : ",menu["price"])
         tmp={
             "name":menu['name'],
             "price":menu["price"]
         }
         output.append(tmp)
        headers = output[0].keys()   
        with open("foodmandu-menu.csv","w") as file_object:
            dict_writer = csv.DictWriter(file_object, headers)
		    dict_writer.writeheader()
		    dict_writer.writerows(output) 

s= FoodmanduFetch()
s.scrape_menu(1027)
print("--------------------------------")
s.scrape_menu(1028)