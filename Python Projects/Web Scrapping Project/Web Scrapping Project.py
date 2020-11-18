# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:26:19 2020

@author: Nick
"""


import requests
from bs4 import BeautifulSoup
import csv


BASE_URL = 'http://drd.ba.ttu.edu/isqs6339/hw/hw1/'
URL = 'http://drd.ba.ttu.edu/isqs6339/hw/hw1/index.php'
res = requests.get(URL)


#Obtaining Status Code
if res.status_code == 200:
    print('This Request Is Good')
else:
    print('The Request is BAD, Received The Code ' + str(res.status_code))


soup = BeautifulSoup(res.content, 'html.parser')
trs = soup.find_all('tr')

i = 0
links = []
for tr in trs:
    if(i != 0):
        links.append(tr.find('a').attrs['href'])
        i = 1
    else:
        i = 1

#Opening CSV and storing data
file1 = open('file1.csv', 'w', encoding="utf-8")
file2 = open('file2.csv', 'w', encoding="utf-8")
file3 = open('file3.csv', 'w', encoding="utf-8")
for link in links:
    id = link.split('=')[1]
    res = requests.get(BASE_URL + link)
    soup = BeautifulSoup(res.content, 'html.parser')

    phone = soup.find(id='PhonePrimary')
    model = phone.find_all('span', class_='val')[0].text
    product_size = phone.find_all('span', class_='val')[1].text
    color = phone.find_all('span', class_='val')[2].text
    storage = phone.find_all('span', class_='val')[3].text
    network = phone.find_all('span', class_='val')[4].text
    os = phone.find_all('span', class_='val')[5].text

    camera = soup.find(id='PhoneSecondary')
    points = camera.find_all('span', class_='val')[0]
    front = points.find_all('li')
    points = camera.find_all('span', class_='val')[1]
    back = points.find_all('li')
    battery = camera.find_all('span', class_='val')[2].text


#Writing CSV
    display1 = csv.writer(file1)
    display1.writerow([id, model, product_size, color, battery, storage, network, os])
    
    display2 = csv.writer(file2)
    for front_camera in front:
        display2.writerow([id, model, front_camera.text])

    display3 = csv.writer(file3)
    for back_camera in back:
        display3.writerow([id, model, back_camera.text])

file1.close()
file2.close()
file3.close()
    
