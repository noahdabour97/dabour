## importing libraries
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


## Brief introduction to NBA league
preface = """The National Basketball Association (NBA) is a professional basketball league in North America. The league is composed of 30 teams (29 in the United States and 1 in Canada) and is one of the four major professional sports leagues in the United States and Canada. It is the premier men's professional basketball league in the world"""
print(preface)

## importing dataset
df = pd.read_csv("players.csv",sep=';')



## some information about NBA Players dataset
df.info()

## retuurn the first 5 records
df.head()

## sort dataset by name
df.sort_values('Name',inplace=True)

print('Total Number of NBA players are: ',len(df))

## number of Players by position
## clryifing each position with bar chart
def pos():
    poss = df['Position'].value_counts()
    print(poss)
    plt.title("Position")
    plt.ylabel("Players")
    plt.legend()
    poss.plot(kind='bar',color='green')
    
pos()
    
## player with the highest salary and his details
df.sort_values('Salary').iloc[0]

## information about Teams
print("How many players for each team?")
df.Team.value_counts()
    

## Player's Age info
def age():
    print("The Average of player's age is: ",round(df["Age"].mean(),1))
    print(df["Age"].plot(kind="hist",color="green",bins=[10,20,30,40,50],rwidth=0.95))
    plt.show()
    
age()


## basic Descriptive statistics
df.describe()



