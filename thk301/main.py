#########################################################################################
# Tae Kim
# Assignment 5
#
#
#Write a program that prompts the user for a list of intervals, 
#reads a string from the user, and creates a list containing these intervals. 
#Once this string has been read, the program should continue prompting for intervals from the user,
#insert the interval into the list, and display the list at the end of each operation. 
#
#
#  main.py
#
#
##########################################################################################


import sys
from operator import itemgetter
import Interval as itv      #import Class Interval


##############################
# Initial User Input
##############################  
list_input =raw_input("List of intervals?")   #read a list of intervals //there should be a space after each interval

tempList=[]               #create tempList to convert string of input into list
for line in xrange(len(list_input.split(", "))):   #list_input is string, so slicing the string
    tempList.append(list_input.split(", ")[line])

if len(tempList)<2:           #in case the user only type in one value.  Ask the user to add more in order to build a list of intervals
    another_list_input=raw_input("Hey, amigo. Type in at least one more interval:")
    for line in xrange(len(another_list_input.split(", "))):
        tempList.append(another_list_input.split(", ")[line])
        
intervalsList=tempList                       #intervalsList stores intervals here to be used globally
itv.mergeResult = itv.Interval(list_input)     #itv is using Class Interval --> import Interval as itv

interval_Input = raw_input("Interval?")  
interval_Input = interval_Input.strip()             #remove white spaces on the first and the last in case users add extra spaces
interval_Input = interval_Input.replace(" ", "")    #remove white spaces in between in case different users type in differently


##############################
# Deligate the Tasks
##############################  
try:
  while interval_Input !="quit":        #if quit, finish the program
    if (interval_Input[0] == "(" or interval_Input[0] == "["):  #it must start with symbol, if not, invalid interval; simple and effective way
        itv.mergeResult.insert(intervalsList, interval_Input)   #calls insert function in Class Intervals
        
        intervalsList = itv.intervalsList   #intervalsList is equal to returned list from Class Intervals
              
        # print out results 
        print "Ranges are :", intervalsList
        interval_Input = raw_input("Interval?")
        interval_Input = interval_Input.strip()             #remove white spaces on the first and the last in case users add extra spaces
        interval_Input = interval_Input.replace(" ", "")    #remove white spaces in between in case different users type in differently
    
    else:           
        print "Invalid interval"
        interval_Input = raw_input("Interval?")
        interval_Input = interval_Input.strip()             #remove white spaces on the first and the last in case users add extra spaces
        interval_Input = interval_Input.replace(" ", "")    #remove white spaces in between in case different users type in differently


##############################
# Error Handlings
##############################   

except IndexError:  #in case of IndexError
    print "Index is out of range. e.g. (1,3) or [2,4]. You typed: ", interval_Input
    sys.exit(1)

except ValueError:  #in case of ValueError
    print "Please type in valid interval next time. e.g. (1,3) or [2,4]. You typed: ", interval_Input
    sys.exit(1)

except SystemExit:
   sys.exit(1)