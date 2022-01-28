import imp
from application import app
from flask import appcontext_popped, render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px
from cgi import test
from cgitb import text
from cmath import nan
from os import name
import string
from numpy import nan
import pandas as pd
import requests
import string
#import pymongo
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup


def main():
 ############ Scraping League of legends Worlds championship

 url = 'https://liquipedia.net/leagueoflegends/S-Tier_Tournaments'
 response = requests.get(url)
 worldslink = []
 if response.ok :
   soup = BeautifulSoup(response.text, 'lxml')
   href = [elt['href'] for elt in soup.findAll('a') if elt.get('href')  ]
   for elt in href :
      if 'World_Championship/' in elt :
         worldslink.append('https://liquipedia.net' + elt)   
 del worldslink[0]

 with open('url.csv', 'w') as fileurl :
   for links in worldslink : 
      fileurl.write(links + '\n')
 with open('teams.csv','w') as file :
   file.write('Year, Team, CashPrize \n')
   with open('url.csv', 'r') as fileurl :
      for row in fileurl :
         url = row.strip()
         response =  requests.get(url)
         if response.ok : 
            soup = BeautifulSoup(response.text, 'lxml')
            ## Year of championship
            year = soup.find('a', {'class': 'mw-selflink selflink'}).text

            position1 = soup.find('tr', {'class' : 'background-color-first-place'}).find('td').text
            position2 = soup.find('tr', {'class' : 'background-color-second-place'}).find('td').text
            position3 = soup.find('tr', {'class' : 'background-color-third-place'}).find('td').text
            
            first = soup.find('tr', {'class' : 'background-color-first-place'}).find('span', {'class': 'team-template-text'}).find('a').text
            # first = position1 + first
            cashprize1 = soup.find('tr', {'class' : 'background-color-first-place'}).find('td').findNext('td').text
            cashprize1 = cashprize1.replace(',',' ')
            cashprize1 = cashprize1.replace('$',' USD ')
            
            second = soup.find('tr', {'class' : 'background-color-second-place'}).find('span', {'class': 'team-template-text'}).find('a').text
            cashprize2 = soup.find('tr', {'class' : 'background-color-second-place'}).find('td').findNext('td').text
            cashprize2 = cashprize2.replace(',',' ')
            cashprize2 = cashprize2.replace('$',' USD ')

            third = soup.find('tr', {'class' : 'background-color-third-place'}).find('span', {'class': 'team-template-text'}).find('a').text
            cashprize3 = soup.find('tr', {'class' : 'background-color-third-place'}).find('td').findNext('td').text  
            cashprize3 = cashprize3.replace(',',' ')
            cashprize3 = cashprize3.replace('$',' USD ')   
   
            
                        
            file.write(year+','+first+','+cashprize1+','+second+','+cashprize2+','+third+','+cashprize3+ '\n')

 ############## Dataframe
 worlds=pd.read_csv('teams.csv')
 print(worlds)

 return None



if __name__== "__main__":
   app.run()