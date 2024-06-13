import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import csv

data = pd.read_csv('C:/Users/kagiklb/Documents/DendrochronologickaDBaApp/Grafy/tacr-chronologie.csv')
list_of_column_names = list(data.columns)

for sites in list_of_column_names:
    if sites == 'year':
        continue;
    #x,y = [],[]
    x = data['year'].astype(str);
    y = data[sites].astype(float);
    #fig = plt.subplots(figsize=(12, 6))
    plt.plot(x, y, color = 'g', #linestyle = 'dashed',
        #     marker = 'o',label = "Weather Data"
             )
    plt.xticks(np.arange(0, len(x)+1, 3),rotation = 25, fontsize=8)
    plt.xlabel('Years')
    plt.ylabel('RWI')
    #plt.title('Chronology', fontsize = 20)
    plt.grid()
    #plt.margins(0.2)
    #plt.legend()
    #plt.show()
    plt.savefig('C:/Users/kagiklb/Documents/DendrochronologickaDBaApp/Grafy/Grafy/'+sites+'.png')
    plt.clf()
"""
x = []
y = []
with open('C:/Users/kagiklb/Documents/DendrochronologickaDBaApp/Grafy/Book3.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[1]))
print(x)
print(y)
fig = plt.subplots(figsize=(12, 6))
plt.plot(x, y, color = 'g', #linestyle = 'dashed',
    #     marker = 'o',label = "Weather Data"
         )
plt.xticks(np.arange(0, len(x)+1, 3),rotation = 25)
plt.xlabel('Years')
plt.ylabel('RWI')
#plt.title('Chronology', fontsize = 20)
plt.grid()
#plt.legend()
#plt.show()
plt.savefig('C:/Users/kagiklb/Documents/DendrochronologickaDBaApp/Grafy/Grafy/obr.png')"""