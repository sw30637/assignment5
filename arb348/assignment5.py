'''
Created on Mar 23, 2015
@author: Adam Biesenbach
'''

"""Question: 1 """

# Import the class we made in an earlier part of the assignment and a regular expressions package.
from  assignment5_IntervalClass import interval
from  assignment5_IntervalClass import IntervalException
import re

"""Question: 2 """

def mergeIntervals(int1, int2):    
    """A function that takes in two intervals as arguments and, if they overlap, merges them. If not, it throws an exception."""
   
    # Function CheckIfOverlapping tests to see if sets are overlappping, and returns a 'True' if so.  
    AreSetsOverlapping = CheckIfOverlapping(int1, int2)  
    
    # Based on the output of the previous function, this function will throw an exception if the intervals do not overlap. 
    HandleNonMergeError(AreSetsOverlapping)
    
    # Function MergeOverlappingSets performs the merger, and returns the merged set.     
    if AreSetsOverlapping==True:
        print MergeOverlappingSets(int1, int2)
        return MergeOverlappingSets(int1, int2)
       
def CheckIfOverlapping(int1, int2):      
    """This function creates a flag that tells us if the intervals are overlapping."""
    
    # Here we initialize our previously created interval class, using the arguements provided.    
    FirstInterval=interval(int1)      
    SecondInterval=interval(int2)
    
    # Here we create the flag for overlapping sets. 
    AreSetsOverlapping = ( (min(FirstInterval.NumbersInRange[1], SecondInterval.NumbersInRange[1]) == max( FirstInterval.NumbersInRange[0], SecondInterval.NumbersInRange[0])) and 
    ((FirstInterval.Brackets[1]=="]" and SecondInterval.Brackets[0]=="[") and (FirstInterval.NumbersInRange[1]==SecondInterval.NumbersInRange[0])) or 
    ((SecondInterval.Brackets[1]=="]" and FirstInterval.Brackets[0]=="[") and (SecondInterval.NumbersInRange[1]==FirstInterval.NumbersInRange[0]))) or \
    ( (min(FirstInterval.NumbersInRange[1], SecondInterval.NumbersInRange[1]) > max( FirstInterval.NumbersInRange[0], SecondInterval.NumbersInRange[0])))
    return AreSetsOverlapping       
 
def MergeOverlappingSets(int1, int2):
    """ This function will merge two overlapping intervals."""
    
    # Create a list of the numbers in the intervals provided.
    NumbersInRanges = interval(int1).NumbersInRange+interval(int2).NumbersInRange
    # Create a list of the brackets provided.
    Brackets = interval(int1).Brackets+interval(int2).Brackets
    # Get a list of the max/min numbers in the list being merged, along with their indices.
    MaxNumbersInRange = [[i,x] for i,x in enumerate(NumbersInRanges) if x==max(NumbersInRanges)]
    MinNumbersInRange = [[i,x] for i,x in enumerate(NumbersInRanges) if x==min(NumbersInRanges)]

    # If both intervals have the same max values (i.e. length>1), we need special logic to choose which bracket to use in the merge. 
    bracketsMax = ChooseMaxBrackets(MaxNumbersInRange,Brackets)
    
    # The same procedure used for the maximums is used for the minimums.
    bracketsMin = ChooseMinBrackets(MinNumbersInRange, Brackets)
        
    # Here we construct the merged interval, as a string. 
    MergedInterval = str(bracketsMin) + str(MinNumbersInRange[0][1]) + "," + str(MaxNumbersInRange[0][1]) + str(bracketsMax)
    return MergedInterval  

# A class for error handling when the two sets do not overlap. 
class NonOverlappingError(Exception): pass
""" A error class we created for a non-overlapping interval error."""
    
# Raise an error is non-overlapping sets.
def RaisesErrorIfNotOverlapping(AreSetsOverlapping):
    """This function raises an error if the intervals do not overlap."""
    if AreSetsOverlapping == False:
        raise NonOverlappingError("NonOverlappingError: The two intervals do not overlap.") 

def HandleNonMergeError(AreSetsOverlapping):
    """ This is an error handling function for our merging function."""
    try:
        RaisesErrorIfNotOverlapping(AreSetsOverlapping)
    except NonOverlappingError, e:
        print str(e)    
 
def ChooseMaxBrackets(MaxNumbersInRange, Brackets):
    """ If there is a duplicate of the max value, we need special logic to pick the bracket."""
    if len(MaxNumbersInRange)>1:
        bracketsMax =  re.search(r"]", ''.join([Brackets[x[0]] for x in MaxNumbersInRange]))
        if bracketsMax is not None:
            bracketsMax = bracketsMax.group(0)
        else:
            bracketsMax = ')'
    # Else if there is a unique max, use the bracket from that max.
    else: 
        bracketsMax = [Brackets[x[0]] for x in MaxNumbersInRange][0]     
    return bracketsMax

def ChooseMinBrackets(MinNumbersInRange, Brackets):
    """ If there is a duplicate of the min value, we need special logic to pick the bracket."""
    if len(MinNumbersInRange)>1:
        bracketsMin =  re.search(r"\[", ''.join([Brackets[x[0]] for x in MinNumbersInRange]))
        if bracketsMin is not None:
            bracketsMin = bracketsMin.group(0)
        else:
            bracketsMin = '('
    else: 
        bracketsMin = [Brackets[x[0]] for x in MinNumbersInRange][0]
    return bracketsMin    

"""Question: 3"""

def mergeOverlapping(Ranges):
    """ This function is intended to take a list of intervals, and returns all overlapping intervals."""
 
    # Loop through each element in the list of intervals, and perform the mergeIntervals function on each pairing. 
    MergedIntervalList = LoopOverIntervalsAndMerge(Ranges)
    
    # Present the results of the merger, and return this value.  
    PresentResults(MergedIntervalList)
    return MergedIntervalList
    
def LoopOverIntervalsAndMerge(Ranges):   
    """ Here we perform the merger of the intervals in the list.  """
  
    for Intervals in range(len(Ranges)):
        for TheOtherIntervals in range(1,len(Ranges)):
            print "Merger attempt results for " + str(Ranges[0]) + " , " + str(Ranges[TheOtherIntervals])+":"
            MergedInterval = mergeIntervals(Ranges[0], Ranges[TheOtherIntervals])
            if MergedInterval is not None:
                Ranges.remove(Ranges[TheOtherIntervals])
                Ranges.remove(Ranges[0])
                Ranges.insert(0, MergedInterval)
                break
    return Ranges

def PresentResults(MergedIntervalList):  
    """ A function that prints the results of the merger."""
    
    # If there are merged intervals, print them, else print that no merged exist. 
    if MergedIntervalList !=[]:
        print 'Here is the merged interval list: ' + str(MergedIntervalList)
        return MergedIntervalList
    else:
        print "No Overlapping intervals given."    

"""Question: 4"""

def insert(intervals, newint):
    """ A function that takes two arguments: a list of nonoverlapping intervals and a single interval. The
    function should insert newint into intervals, merging if necessary. you can assume that the initial list 
    was sorted by lower bound, and you should sort the new list by lower bounds as well."""
  
    # Initialize the results list.
    Results = GenerateResultsList(intervals, newint)
    
    # Parse out the intervals from the string into separate elements of a list, then append the new interval.    
    ParsedIntervals = ParseOutIntervals(intervals)
    ParsedIntervals.append(newint)  
    
    #Sort the intervals by the minimum number.
    ListofIntervals = SortIntervalsByStart(ParsedIntervals)    
   
    # Generate the final results file.
    InsertedIntervalResults = GenerateInsertedIntervals(ListofIntervals, Results)
    return InsertedIntervalResults

def GenerateResultsList(intervals, newint):
    """Initialize the results list.  If the list of intervals is empty, return the new interval."""
    Results = []
    if len(intervals) == 0:
        return Results + newint  
    return Results

def ParseOutIntervals(intervals):
    """Parse the input string to pick out the intervals and store them as separate
    string entries in a new list call ListofIntervals."""

    ListofIntervals = []
    
    # Look through the string, and start creating a substring called NewInterval. Continue to create this 
    # substring until a closing bracket is found, and then append this string to the ListofIntervals list 
    # and continue looking for the net interval.
    
    for EachInterval in intervals:
        NewInterval = ""
        #Pick out the intervals from each element in list.
        for elements in range(len(EachInterval)):
            NewInterval+=EachInterval[elements]
            if (EachInterval[elements]==']' or EachInterval[elements]==')'):
                while (EachInterval[0]!='(' and EachInterval[0]!='['):
                    NewInterval=NewInterval[1:]
                ListofIntervals.append(NewInterval)
                NewInterval = ""  
    return ListofIntervals  

def SortIntervalsByStart(ListofIntervals):  
    """ Sort the list of intervals by the first value using this lambda function."""
    ListofIntervals.sort(key = lambda x: interval(x).FirstNumber)
    return ListofIntervals
    
def GenerateInsertedIntervals(ListofIntervals, Results):    
    """if it's not empty, then look in the results list at the next most recent addition, and
       looping over all the elements in our intervals list, check to see that the first number in the interval list is 
       between the first and last numbers of the element in the results list. If it is, then reset the last number
       of that element in the results list to be the max of the two lists."""
    
    # Loop through an index of all the elements of ListofIntervals, our list of the intervals from the string.    
    for i in range(len(ListofIntervals)):
   
        #If results list is empty, put in the first interval from the list.
        if Results==[]:
            Results.append(ListofIntervals[i])
            
        # if it's not empty, then look at the ith interval in the list. If the most recent addition to the results file 
        # contains the starting number of the ith interval member, then check to see if the last number contained in that interval 
        # is less than the last number in the  
        else:
            size=len(Results)
            if interval(Results[size-1]).FirstNumber-1<=interval(ListofIntervals[i]).FirstNumber<=interval(Results[size-1]).LastNumber+1:
                if  interval(ListofIntervals[i]).LastNumber < interval(Results[size-1]).LastNumber:
                    Results[size-1] = str(interval(Results[size-1]).Brackets[0]) + str(interval(Results[size-1]).NumbersInRange[0]) + "," + str(interval(Results[size-1]).NumbersInRange[1]) + str(interval(Results[size-1]).Brackets[1])
                elif interval(Results[size-1]).LastNumber < interval(ListofIntervals[i]).LastNumber:
                    Results[size-1] = str(interval(Results[size-1]).Brackets[0]) + str(interval(Results[size-1]).NumbersInRange[0]) + "," + str(interval(ListofIntervals[i]).NumbersInRange[1]) + str(interval(ListofIntervals[i]).Brackets[1])
                elif interval(Results[size-1]).LastNumber == interval(ListofIntervals[i]).LastNumber:
                    if interval(Results[size-1]).NumbersInRange[1] < interval(ListofIntervals[i]).NumbersInRange[1]:
                        Results[size-1] = str(interval(Results[size-1]).Brackets[0]) + str(interval(Results[size-1]).NumbersInRange[0]) + "," + str(interval(ListofIntervals[i]).NumbersInRange[1]) + str(interval(ListofIntervals[i]).Brackets[1])   
                    else:
                        if interval(ListofIntervals[i]).Brackets[1]==']' or interval(Results[size-1]).Brackets[1]==']':
                            Results[size-1] = str(interval(Results[size-1]).Brackets[0]) + str(interval(Results[size-1]).NumbersInRange[0]) + "," + str(interval(ListofIntervals[i]).NumbersInRange[1]) + ']'
                        else:                   
                            Results[size-1] = str(interval(Results[size-1]).Brackets[0]) + str(interval(Results[size-1]).NumbersInRange[0]) + "," + str(interval(ListofIntervals[i]).NumbersInRange[1]) + ')'                        
            else:
                Results.append(ListofIntervals[i])  
    return Results



"""Question: 5"""

def ReturnInsertedResults():
    """ A master function that returns a lists of intervals with a new interval inserted in."""
    
    # From an initial list provided by the user, handle error to make sure that the intervals are valid.   
    ValidatedIntervalList = ValidateList()   
    # Return the new list that includes the inserted interval.
    ReturnInsertedList(ValidatedIntervalList)
 
def ValidateList():
    """Here is a function to handle exceptions to the intervals list."""         
  
    # Get input from the user. If the string is empty, prompt them again. 
    # If not, take out each of the parsed elements and try to put it into the interval class.
    # If an exception is raised, add it to the exceptions list. If after running the loop, 
    # the length of the errors list is greater than zero, prompt again. 
    
    while True:
    
        Intervals = GetUsersInitialList()    
        
        NumberOfErrors = []   
        if ParseIntervalsFromString(Intervals) != []:
            for element in ParseIntervalsFromString(Intervals):
                try:
                    interval(element)
                except IntervalException:  
                    NumberOfErrors.append(element)
                except IndexError:
                    NumberOfErrors.append(element)
           
            if len(NumberOfErrors)>0:
                print "Invalid Interval."
                continue
            
            return Intervals
            break
      
        else:
            print "Invalid Interval."
            continue 
            
    else:
        return Intervals

def ParseIntervalsFromString(intervals):
    """Parse the input string to pick out the intervals and store them as separate
    string entries in a new list call ListofIntervals."""
   
    ListofIntervals = []
    NewInterval = ""
    
    # Look through the string, and start creating a substring called NewInterval. Continue to create this 
    # substring until a closing bracket is found, and then append this string to the ListofIntervals list 
    # and continue looking for the net interval.
    
    for elements in range(len(intervals)):
        NewInterval+=intervals[elements]
        if (intervals[elements]==']' or intervals[elements]==')'):
            while (NewInterval[0]!='(' and NewInterval[0]!='['):
                NewInterval=NewInterval[1:]
            ListofIntervals.append(NewInterval)
            NewInterval = ""  
    return ListofIntervals  
  
def GetUsersInitialList():
    """Return the raw input from the user containing the initial list of intervals."""
    return raw_input("List of Intervals? ")


def ReturnInsertedList(IntervalsThatPassedInspection):
    """Produce the new list, which includes the the inserted interval."""   
    if IntervalsThatPassedInspection is not None:
        ValidateInsertedInterval(IntervalsThatPassedInspection)

def ValidateInsertedInterval(IntervalsThatPassedInspection):
    """Looks for exceptions in each of the elements of the inserted interval."""  
    while True:
        InsertInterval = GetUsersInsert()
        if InsertInterval=='quit':
            print "exiting program..."
            break
        else:
            try:
                interval(InsertInterval)
            except IntervalException:  
                print "Invalid Interval." 
                continue
            except IndexError:
                print "Invalid Interval."
                continue  
            else:
                ProduceOutput(IntervalsThatPassedInspection, InsertInterval)
                
def GetUsersInsert():
    """Return the raw input from the user containing the interval they wish to insert."""
    return raw_input("Insert? ")
    
def ProduceOutput(IntervalsThatPassedInspection, InsertInterval):
    """Produce the inserted list that will be printed to the screen. Because the insert() function 
    produces a list of strings, we need to convert its output to another string to along the loop to 
    perform."""
    IntervalsThatPassedInspection = ','.join(str(elements) for elements in insert(ParseIntervalsFromString(IntervalsThatPassedInspection), InsertInterval))
    print IntervalsThatPassedInspection


"""" Here's where you can check if the functions work. """    

"""Question 1"""
#rint "Question 1: "
#SampleInterval= interval("(0,5]")
#print SampleInterval

"""Question 2"""
#print "Question 2: " + mergeIntervals("[0,1]", "(0,5]")

"""Question 3"""
#print "Question 3: " 
#mergeOverlapping(["[1,5]", "[2,6)", "(8,10]", "[8,18]"])

"""Question 4"""
#print "Question 4: Here is the inserted list: " 
#print insert(["[6,9)", "[10,20]"], "[1,7]")

"""Question 5"""
ReturnInsertedResults()
