from bs4 import BeautifulSoup
import requests

result = requests.get('https://filmix.ac/films/fantastiks/112868-5w-novie-chelovek-muravey-2015.html')

soup = BeautifulSoup(result.text,'html.parser')

name = soup.find('h1',{'class':'name'}).next_element

describe = soup.find('div',{'class':'full-story'}).next_element

res = soup.find('span',{'class':'item-content'}).next_element.next_element.next_element.next_element


print(f"Name of film : {name}; {describe}, and director this film is {res}")