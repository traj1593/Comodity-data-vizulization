'''
Program: Commodity Data Visualization
Filename: commodityDataVisualization-tRaj-00.py
Author: Tushar Raj
Description: Importing the CSV file and filtering the record as per need and then drawing the graph using the matplotlib
Revisions: No revisions made
'''

import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.ticker as mtick

#There are no literal constraint
#There are no class defined
#There are no functions defined

print("**** Commodity Data Visualization ****\n\n")

file = csv.reader(open('produce_csv.csv','r')) #Opening the produce csv and reading it
data = [i for i in file] #iterating each line and storing it as list

modList = [] #creating the empty list to store modified list
for i in data: #iterating through the the list
    changedList=list()
    for j in i:
        if "$" in j:
            changedList.append(float(j.replace("$",""))) # replacing the $ sign with null vlaue
        elif "/" in j: 
            changedList.append(datetime.strptime(j,'%m/%d/%Y')) #changing the sting format of date into date format
        else:
            changedList.append(j)  
    modList.append(changedList) # appending the changed list into master list

locations = modList.pop(0)[2:] #removing the header
records = [] # creating an empty list
for row in modList: 
    newRow = row[:2] #storing the first 2 row in new variable
    for loc,price in zip(locations,row[2:]): # location and prices and appended with the first first two rows
        records.append(newRow + [loc,price]) # new data is added to record
        


select = list(filter(lambda x:x[0] == "Oranges" and x[2] == "Chicago", records)) #filtering out the data for Oranges in Chicago

dates = [x[1] for x in select] #picking up the date from the data
prices = [x[3] for x in select] #picking up the Chicago price from the data

#merging them for plotting
dpMerge = [ [d,p] for d,p in zip(dates,prices)]
dpMerge.sort(key = lambda a:a[0]) #sorting w.r.t first column

#creating text graph
for x in dpMerge:
    print(f'{datetime.strftime(x[0],"%m-%d-%Y")} {int(25*x[1])*"="}')



fig = plt.figure() #initiating the figure
ax = fig.add_subplot() #just adding the subplots

ax.plot(dates,prices,label="Oranges in Chicago") #plotting the graph


ax.set_xlabel('date') #adding X-axis
ax.set_ylabel('price in dollars') #adding Y-axis

fmt = '${x:,.2f}' #add "$" sign to Y axis values

tick = mtick.StrMethodFormatter(fmt) #defining the format
ax.yaxis.set_major_formatter(tick) #establishing the format for Y-axis label


plt.legend() # to show legend
plt.show() # to show graphs

print("\n\n**** Commodity Data Visualization Ended ****")
