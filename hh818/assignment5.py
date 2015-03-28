'''
Created on Mar 27, 2015

@author: ds-ga-1007
'''
if __name__ == "__main__":
    import intervalPackage
    
    #set a list for the intervals for the user to input
    while True:
        try:
            userInput = raw_input("List of intervals? Please format it as [5,8), (6,10), [3,6)")
            intervalsList = userInput.split(", ")
            
            mergedList = intervalPackage.mergeOverLapping(intervalsList)
            print mergedList
            break
        except:
            print "Invalid Intervals List"
        
    #set the a loop until user type in valid intervals
    while True:
        newInt = raw_input("Interval?")
        try:
            if newInt == "quit":
                break
            else:
                mergedList = intervalPackage.insert(mergedList, newInt)
                print mergedList
            
        except:
            print "Invalid Interval"