'''
Created on Mar 20, 2015
Created by Joseph Song (JLS731)
Filename: assignment5.py
Description: Main program to run assignment 5:
takes user inputs manipulates the intervals
I completed this homework with the help of the Lutz: python book and stackoverflow.com
'''

from interval import *

if __name__ == '__main__':
    
    userInputList = raw_input("List of intervals?")
    userInputListNoSpace = userInputList.replace(" ","") #get rid of any whitespace
    components = userInputListNoSpace.split(',')
    newList = []
    assert len(components)%2 ==0, "Error: Uneven number of components--something is wrong"
    for i in xrange(0,len(components),2):
        newList.append(str(interval(components[i] + "," + components[i+1])))
    userInput = raw_input("Interval?")
    
    while userInput != "quit":
        try:
            newInput = str(interval(userInput))
        except:
            print("Invalid interval")
        else:
            userInputList = insert(newList, newInput)
            print userInputList
        userInput = raw_input("Interval?")
    print("User quit")
