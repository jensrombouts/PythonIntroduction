import shapefile

import pandas as pd

sf_school = shapefile.Reader('C:/Users/jrombouts/Desktop/python training/Wegsegment_selection/Schools_Flanders.shp')
sf_wegsegment = shapefile.Reader('C:/Users/jrombouts/Desktop/python training/Wegsegment_selection/Wegsegment_selection.shp')

shapes_wegsegment = sf_wegsegment.shapes()
shapes_school = sf_school.shapes()

print(sf_school.fields)

headers = []

for element in sf_school.fields:
    for i, name in enumerate(element):
        if i == 0:
            headers.append(name)

print(headers)

headers = headers[1:]

data = []

for record in sf_school.records():
    data.append(record)

print(data)

content = pd.DataFrame(data=data,columns=headers)

print(content.head())






