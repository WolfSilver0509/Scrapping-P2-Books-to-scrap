#name = input('What is your name?\n')
#print('Hi, %s.' % name)

#Import des librairies
import requests
from bs4 import BeautifulSoup
import unidecode

import csv

# rentrer l'url d'une page produit dans "l'URL"
url = ' http://books.toscrape.com/catalogue/sharp-objects_997/index.html'

#On crée une reponse qui va recuperer l'url si tout est ok (200 )
response = requests.get(url)

if response.ok:


    soup = BeautifulSoup(response.text, 'lxml')
    product_page_url= url
    table= soup.findAll('td')
    title = soup.find('h1').text
    universal_product_code = table[0].text
    price_including_tax = table[2].text.replace('£', '')
    price_excluding_tax = table[3].text.replace('£', '')
    number_available = table[5].text.removeprefix('In stock (').removesuffix('available)')
    product_description_unicode = soup.select_one('article > p').text
    product_description = unidecode.unidecode(product_description_unicode)
    #category
    review_rating = soup.find('p', class_='star-rating').get('class').pop()
    #image_url
    image = soup.find('div',class_="item active")

    book = {"product_page_url":product_page_url,
            "title":title,
            "product_description":product_description,
            "universal_product_code":universal_product_code,
            "price_including_tax":price_including_tax,
            "price_excluding_tax":price_excluding_tax,
            "review_rating":review_rating,
            "image":image,}
            #"number_available":number_available}

    print(book)

# Créer une liste pour les en-têtes
#en_tete = ["title", "product_description"]
en_tete = ["product_page_url","title"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(en_tete)
 
