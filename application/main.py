import imp
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
import matplotlib.pyplot as plt
import dash
from dash import dcc
from dash import html
from dash import dash_table
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
 worlds['Rank'] = ['1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd','1st', '2nd', '3rd']
 worlds = worlds.fillna(method='ffill')
 print(worlds)

 data = {'Year':['2021','2021' ,'2021' ,'2020','2020','2020','2019','2019','2019','2018','2018','2018','2017','2017','2017','2016','2016','2016','2015','2015','2015','2014','2014','2014','2013','2013','2013','2012','2012','2012','2011','2011','2011' ], 
        'Team':['EDward Gaming','DAMWON Gaming','Gen.G Esports','DAMWON Gaming','Suning','Top Esports','FunPlus Phoenix','G2 Esports','Invictus Gaming','Invictus Gaming','Fnatic','G2 Esports','Samsung Galaxy','SK Telecom T1','Royal Never Give Up','SK Telecom T1','Samsung Galaxy','ROX Tigers','SK Telecom T1','KOO Tigers','Origen','Samsung White','Star Horn Royal Club','Samsung Blue','SK Telecom T1 K','Royal Club','NaJin Black Sword','Taipei Assassins','Azubu Frost','Moscow Five','Fnatic','against All authority','Team SoloMid'], 
        'CashPrize_en_USD':[489500,333750,178000,556250,389375,200250,834375,300375,155750,2418750,870750,451500,1723722,620540,321761,2028000,760500,380250,1000000,250000,150000,1000000, 250000,150000,1000000,250000,150000,1000000,250000,150000, 50000,25000,10000], 
        } 
  
 df = pd.DataFrame(data) 

 data1 = {'Team':['Azubu Frost','DAMWON Gaming','EDward Gaming','Fnatic','FunPlus Phoenix','G2 Esports','Gen.G Esports','Invictus Gaming','KOO Tigers','Moscow Five','NaJin Black Sword','Origen','ROX Tigers','Royal Club','Royal Never Give Up','SK Telecom T1','SK Telecom T1 K','Samsung Blue','Samsung Galaxy','Samsung White','Star Horn Royal Club','Suning','Taipei Assassins','Team SoloMid','Top Esports','against All authority'],  
        'Times_in_the_top_3':[1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,3,1,1,2,1,1,1,1,1,1,1],
        } 
  
 lf = pd.DataFrame(data1) 

 data2 = {'Team':['Azubu Frost','DAMWON Gaming','EDward Gaming','Fnatic','FunPlus Phoenix','G2 Esports','Gen.G Esports','Invictus Gaming','KOO Tigers','Moscow Five','NaJin Black Sword','Origen','ROX Tigers','Royal Club','Royal Never Give Up','SK Telecom T1','SK Telecom T1 K','Samsung Blue','Samsung Galaxy','Samsung White','Star Horn Royal Club','Suning','Taipei Assassins','Team SoloMid','Top Esports','against All authority'],  
        'Total_Cash_Won':[250000,890000,489500,920750,834375,751875,178000,2574500,250000,150000,150000,150000,380250,250000,321761,3648540,1000000,150000,2484222,1000000,250000,389375,1000000,10000,200250,25000],
        } 
 tf = pd.DataFrame(data2)

 graph_best_team = plt.subplots(figsize=(50,10))
 graph_best_team=plt.bar(lf['Team'],lf['Times_in_the_top_3'],1.0,color='b')
 plt.savefig('graph1.png')

 plt.clf()
 graph_More_Cash_Won = plt.subplots(figsize=(50,10))
 graph_More_Cash_Won=plt.bar(tf['Team'],tf['Total_Cash_Won'],1.0,color='r')
 plt.savefig('graph2.png')

 app = dash.Dash(__name__)

 app.layout = html.Div(children=[  

        html.H1(children='Dashboard sur les meilleurs equipes de LOL', style={'textAlign': 'center'}),#titre g??n??ral du dashboard
        #Partie pr??sentation du projet / bases de donn??es
        dcc.Tabs(style={'borderTop':'3px solid #212121', 'borderRadius':'6px', 'boxShadow':'2px 2px 30px #dfe4ea'}, colors={'background':'#dfe4ea'}, id="tabs", children=[   #cr??ation des diff??rents "onglets"
            dcc.Tab(label="Pr??sentation", children=[   #premier onglet
                html.Div(children=[
                    html.H1(children='Pr??sentation du projet', style={'textAlign' :'center','background-color':'#dfe4ea'}),#titre de la page
                    dcc.Textarea(
                        id='pr??sentation',#id 
                        title='Pr??sentation du dashboard',#titre en haut de la page
                        value='Bienvenue!\n\n Nous vous pr??sentons ici un Dashboard sur les meilleurs equipes du jeu vid??o LOL',
                        style={'fontFamily':'Arial','width':'100%', 'height':'1000', 'textAlign':'left', 'background-color':'#dfe4ea', 'font-size':'medium', 'font-style':'normal', 'resize':'none', 'border':'none'},
                        readOnly='readOnly',#en lecture seule
                        draggable='false',
                        rows='9'#9 lignes
                    ),

                    html.H1(children='Base de donn??e import??e : Liste des pays', style={'textAlign':'left'}),#premi??re dataframe
                    dash_table.DataTable( #affichage de la base de donn??e 
                        data=worlds.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in worlds.columns],
                        page_action='native',
                        fixed_rows={'headers': True},
                        style_table={'overflowY': 'auto'},
                        page_current= 0,
                        page_size= 10,
                        filter_action="native"
                    ),

                ])
            ]),
            #Partie graphiques
            dcc.Tab(label="Analyse par les graphiques", children=[   #deuxi??me onglet
                html.Div(children=[
                    html.H1(children='Diff??rents graphiques', style={'textAlign' :'center', 'background-color':'#dfe4ea'}),#titre de la page
                        dcc.Textarea(
                        id='graph',
                        title='Graphiques',
                        value='Voici les graphiques permettant une analyse des donn??es.',
                        style={'fontFamily':'Arial','width':'100%', 'height':'1000', 'textAlign':'left', 'background-color':'#dfe4ea', 'font-size':'medium', 'font-style':'normal', 'resize':'none','border':'none'},
                        readOnly='readOnly',
                        draggable='false',
                        rows='2'
                    ),
                        dcc.Graph(#affichage du quatri??me graph
                            id='graph1',
                            figure= graph_best_team,
                            style={'boxShadow':'2px 2px 30px #581845e', 'borderRadius':'10px'}
                        ),
                         dcc.Graph(#affichage du quatri??me graph
                            id='graph2',
                            figure=graph_More_Cash_Won,
                            style={'boxShadow':'2px 2px 30px #581845', 'borderRadius':'10px'}
                        ),
                       
                ]),
            ]),
           
                    
    ])
 ])

 app.run_server(debug=True)

 return None

  

if __name__== "__main__":
   main()
