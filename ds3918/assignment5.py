# Question 5
"""
Summary:
    The first input should be a string representation of intervals separated by a comma and a whitespace. No quotes needed!
    Later inputs should be strings that fit the interval class format. 
    Type "quit" to exit the program
"""
import intervalPackage
from sys import exit

# Prompt the user for the first input
firstInput = raw_input("List of intervals? ")
# If it's not "quit", split into intervals, append to a list ("currentIntervals") and make them of interval class.
if firstInput != "quit":
    firstInputElements = firstInput.split(", ")
    currentIntervals = []
    try:
        for element in firstInputElements:
            currentIntervals.append(intervalPackage.interval(element))
    except:
        print "Some of your intervals was in the wrong format. Try again."
        # firstInputError is used to detect errors in the 1st input and prompt the user to try again
        firstInputError = True
        # Prompt the user for a list of intervals until the input is in the right format
        while firstInputError:
            firstInput = raw_input("List of intervals? ")
            if firstInput != "quit":
                firstInputElements = firstInput.split(", ")
                currentIntervals = []
                try:
                    for element in firstInputElements:
                        currentIntervals.append(intervalPackage.interval(element))
                    firstInputError = False
                except:
                    print "Some of your intervals was in the wrong format. Try again."
            else:
            	exit(0)
    
    # Prompt the user for a single interval
    nextInput = raw_input("Interval? ")
    if nextInput != "quit":
        try:
            nextInputInterval = intervalPackage.interval(nextInput)
            # Insert the new input and print results
            currentIntervals = intervalPackage.insert(currentIntervals, nextInputInterval)
            print currentIntervals
        except:
            print "Invalid interval"
        
        # Prompt the user for intervals until "quit"
        while (nextInput != "quit"):
            nextInput = raw_input("Interval? ")
            if nextInput == "quit":
                exit(0)
            else:
                try:
                    nextInputInterval = intervalPackage.interval(nextInput)
                    currentIntervals = intervalPackage.insert(currentIntervals, nextInputInterval)
                    print currentIntervals
                except:
                    print "Invalid interval"
    
    # If the user wants to quit, empty currentIntervals list
    else: 
        exit(0)