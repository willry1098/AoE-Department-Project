# Get this figure: fig = py.get_figure("https://plot.ly/~bbs2133/1/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~bbs2133/1/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Plot 1", fileopt="extend")
# Get z data of first trace: z1 = py.get_figure("https://plot.ly/~bbs2133/1/").get_data()[0]["z"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "z": ["130.1727273", "65.00909091", "80.49090909", "115.3", "53", "68.16363636", "66.14545455", "92.17272727", "78.00909091", "84.78181818", "46.82727273", "84.58181818", "61.03636364", "100.2909091", "64.85454545", "83.67272727", "122.5545455", "109.3727273", "84.80909091", "66.4", "63.22727273", "92.28181818", "55.71818182", "113.8727273", "87.90909091", "81.71818182", "67.51818182", "92.06363636", "78.50909091", "58", "72.32727273", "47.31818182", "90.64545455", "58.42727273", "92.75454545", "114.1090909", "93.82727273", "77.3", "77.30909091", "96.38181818", "55.42727273", "128.2090909", "68.53636364", "83.36363636", "55.22727273", "72.51818182", "78.84545455", "130.8818182", "70.74545455", "79.15454545"], 
  "autocolorscale": False, 
  "colorbar": {"title": "Persciptions"}, 
  "colorscale": [
    [0, "rgb(190, 207, 182)"], [0.35, "rgb(125, 178, 143)"], [0.5, "rgb(40, 144, 126)"], [0.6, "rgb(16, 125, 121)"], [0.7, "rgb(24, 97, 108)"], [1, "rgb(28, 71, 93)], 
  "locationmode": "USA-states", 
  "locations": ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"], 
  "locationssrc": "bbs2133:0:ce8e2e", 
  "marker": {"line": {
      "color": "rgb(255,255,255)", 
      "width": 2
    }}, 
  "name": "z", 
  "showscale": True, 
  "text": ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"], 
  "textsrc": "bbs2133:0:128c77", 
  "type": "choropleth", 
  "uid": "f6ed89", 
  "zauto": True, 
  "zmax": 130.8818182, 
  "zmin": 46.82727273, 
  "zsrc": "bbs2133:0:d594b6"
}
data = Data([trace1])
layout = {
  "geo": {
    "lakecolor": "rgb(255, 255, 255)", 
    "projection": {
      "scale": 0.994240573556, 
      "type": "albers usa"
    }, 
    "scope": "usa", 
    "showlakes": True
  }, 
  "hovermode": "closest", 
  "title": "Average Opioid Prescriptions per 100 People: 2005-2015"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)