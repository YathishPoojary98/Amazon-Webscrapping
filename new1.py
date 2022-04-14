from bs4 import BeautifulSoup
import requests
import csv
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
html_text = requests.get('https://www.amazon.in/s?k=phones&ref=nb_sb_noss',headers=headers).text
soup = BeautifulSoup(html_text,'lxml')
names = []
prices = []

for i in soup.find_all('a','a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'):
    string = i.text
    names.append(string.strip())
for j in soup.find_all('span','a-price-whole'):
    strings = j.text
    prices.append(strings.strip())
    

file_name = 'Phones.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No','Phone Name','Prices'])

    for i in range(len(names)):
        writer.writerow([i, names[i], prices[i]])
