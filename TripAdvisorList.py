from bs4 import BeautifulSoup
import requests
import csv
import time

url = 'https://www.tripadvisor.es/RestaurantSearch-g187514-oa0-madrid.htm'
urlTrozos = url.split('-')

search = 0

# Crea el CSV
csv_file = open('listaRestaurantes.csv', 'w', newline='')
csv_file2 = open('paginasconerror.csv', 'w', newline='')


# Escribe los títulos en el csv
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Url'])

csv_writer = csv.writer(csv_file2)
csv_writer.writerow(['Url'])

while search < 10680:
    busqueda = 'oa' + str(search)
    urlFull = urlTrozos[0] + '-' + urlTrozos[1] + '-' + busqueda + '-' + urlTrozos[3]
    print(urlFull)
    source = requests.get(urlFull)
    source0 = source.text
    soup = BeautifulSoup(source0, 'lxml')

    print(source.status_code)
    if source.status_code != 200:

        csv_writer.writerow([urlFull])
    

    for restaurante in soup.find_all('div', class_='restaurants-list-ListCell__infoWrapper--3agHz'):
        if restaurante.find("div", class_='ui_merchandising_pill sponsored_v2'):
            continue
        else:
            urlRest = restaurante.find('a', class_='restaurants-list-ListCell__restaurantName--2aSdo')['href']
            urlRestFull = 'https://tripadvisor.es' + urlRest
            print(urlRestFull)

        csv_writer.writerow([urlRestFull])

    search = search + 30
    time.sleep(10)
#

csv_file.close()
