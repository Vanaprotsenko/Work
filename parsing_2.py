from bs4 import BeautifulSoup
import requests

result = requests.get('https://auto.ria.com/uk/auto_mercedes-benz_c-class_33822154.html')


soup = BeautifulSoup(result.text,'html.parser')

price = soup.find('div',{'class':'price_value'}).next_element.next_element.next_element

name = soup.find('div',{'class':'m-padding'}).next_element.next_element

dvig = soup.find('svg',{'class':'svg svg-match blue'}).next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element


color = soup.find('span',{'class':'car-color'}).next_element

print(f"Model of car is {name}, price is {price}, color thar car is {color}, and your dvigyn{dvig}")