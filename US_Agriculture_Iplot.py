#Author Tucker Ferguson
#Date 6/13/2020
#
# Note: For this code to run successfully you must have an up-to-date installation of both cufflinks and iplot
#
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import chart_studio.plotly as py
import plotly.graph_objs as go
import cufflinks as cf
#%matplotlib inline

init_notebook_mode(connected=True)
cf.go_offline()
df = pd.read_csv('2011_US_AGRI_Exports')

data = dict(type = 'choropleth',
           colorscale = 'ylorbr',
           locations = df['code'],
           z = df['total exports'],
           locationmode = 'USA-states',
           text = df['text'],
           marker = dict(line = dict(color='rgb(255,255,255)',width = 2)),
           colorbar = {'title':'Millions USD'}
           )
layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )
clmap = go.Figure(data = [data], layout = layout)
iplot(clmap)