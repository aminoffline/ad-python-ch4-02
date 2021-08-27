from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('results.csv', 'w', encoding='utf-8')
csv.writer = csv.writer(csv_file)
csv.writer.writerow(['Ad Title ', 'Ad Description'])

price = 'توافقی'
response = requests.get('https://divar.ir/s/shiraz', timeout=5).text
soup = BeautifulSoup(response, 'lxml')

for post in soup.find_all('div', class_='post-card-item kt-col-6 kt-col-xxl-4'):
    try:
        title = post.find('div', class_='kt-post-card__title').text
        description = post.find('div', class_='kt-post-card__description').text
        if price in description:
            csv.writer.writerow([title, description])
            print(title, description)
    except:
        pass

csv_file.close()
