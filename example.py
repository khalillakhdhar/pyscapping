# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:50:11 2024

@author: khali
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
# Making a GET request
r = requests.get('https://formation.elitetechnologygroupe.com/index.php/2024/06/12/python-for-data-science/')
# check status code for response received
# success code - 200
soup = BeautifulSoup(r.content, 'html.parser')

# print content of request
#print(r.content)
print(soup.title)
titres=[]
programmes=[]

articles=soup.find_all('h3')
art2=soup.find_all('p')
#print(art2)

for art in art2:
    programme=art.get_text(strip=True)
    if("Jour" in programme):
        programmes.append(programme)
#print(programmes)

for article in articles:
    titre=article.get_text(strip=True)
    if("Semaine" in titre):
        titres.append(titre)
print(titres)
df=pd.DataFrame(
    {
     'Titres':titres,
     "Programmes":programmes
     })
df.to_csv("Elite tech website.csv",index=False)