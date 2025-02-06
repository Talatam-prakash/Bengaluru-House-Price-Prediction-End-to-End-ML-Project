import json
import numpy as np
 
 
with open('columns.json','rb') as file:
    columns=json.load(file)

location= 'others'  
print(len(columns['data_columns']))
print(columns['data_columns'].index(location))
