import unicodecsv
from bs4 import BeautifulSoup
import requests,csv
csv_file = open('results.csv','w')
csv.writer = csv.writer(csv_file)
csv.writer.writerow(['Ad Title','Ad Description'])
'''
post-card-item kt-col-6 kt-col-xxl-4
	kt-post-card__description
	<div class="kt-post-card__description">توافقی</div>
	'''
price = 'توافقی'
response = requests.get('https://divar.ir/s/shiraz',timeout= 5).text
soup = BeautifulSoup(response,'lxml')

post = soup.find('div',class_='post-card-item kt-col-6 kt-col-xxl-4')
title = post.find('div',class_='kt-post-card__title').text
description = post.find('div',class_='kt-post-card__description').text
if price in description:
    csv.writer.writerow([title,description])
print(description, post.prettify())





csv_file.close()