# Question 1

def isSmallerEqual(arg1, arg2):
    """
    Summary:
        Takes 2 arguments. 
        Returns True if arg1 < arg2, and False otherwise
    """
    return arg1 <= arg2

def boundsParser(string):
    return string[1:(len(string)-1)].split(",")

class IntervalStringException(Exception):
    """
    Summary:
        Defines an exception for an interval class input in the wrong format.
    """
    def __str__(self):
        return "The input string representation of an interval is wrong! It should be of the form Sa,bS, where a and b are integers, and S is [,(,), or ]\n"

class IntervalInputException(Exception):
    """
    Summary:
        Defines an exception for an interval where the lower bound is larger than the upper bound.
    """
    def __str__(self):
        return "Your lower bound does not match your upper bound"

class interval:
    """
    Summary:
        Class with 3 attributes: lower and upper (integer), and stringRepresentation (string).
        Can throw IntervalStringException and IntervalInputException.
    """
    def __init__(self, string):
        try:
            bounds = boundsParser(string)
            self.lowerIntegerInString = int(bounds[0])
            self.upperIntegerInString = int(bounds[1])
        except:
            raise IntervalStringException()
        
        if string[0] == "[":
            self.lower = self.lowerIntegerInString
        elif string[0] == "(":
            self.lower = self.lowerIntegerInString + 1
        else:
            raise IntervalStringException()
        if string[len(string)-1] == "]":
            self.upper = self.upperIntegerInString
        elif string[len(string)-1] == ")":
            self.upper = self.upperIntegerInString - 1
        else:
            raise IntervalStringException()
        if isSmallerEqual(self.lower, self.upper):
            self.stringRepresentation = string
        else: 
            raise IntervalInputException()
    
    def __repr__(self):
        return '"' + self.stringRepresentation + '"' + " represents the numbers " + str(self.lower) + " through " + str(self.upper)




# Question 2

class NoIntersectionException(Exception):
    def __str__(self):
        return "Your intervals do not intersect!"

def mergeable(int1, int2):
    """
    Summary:
        Takes 2 intervals of interval class as arguments and returns a boolean to show if they overlap.
    """
    return not (int1.upper < int2.lower or int1.lower > int2.upper)

    
def mergeIntervals(int1, int2):
    """
    Summary:
        Takes 2 intervals (of interval class or a string representation) as arguments. 
        Returns an object of interval class if intervals overlap. Otherwise, raises NoIntersectionException.
    """
    # Convert arguments to interval class if necessary
    if not isinstance(int1, interval):
        int1 = interval(int1)
    if not isinstance(int2, interval):
        int2 = interval(int2)
    
    if mergeable(int1, int2):
        # Define the start value and the type of the opening bracket 
        if int1.lowerIntegerInString <= int2.lowerIntegerInString:
            start = int1.lowerIntegerInString
            startSymbol = int1.stringRepresentation[0]
        else:
            start = int2.lowerIntegerInString
            startSymbol = int2.stringRepresentation[0]
        # Define the end value and the type of the closing bracket 
        if int1.upperIntegerInString >= int2.upperIntegerInString:
            end = int1.upperIntegerInString
            endSymbol = int1.stringRepresentation[len(int1.stringRepresentation)-1]
        else:
            end = int2.upperIntegerInString
            endSymbol = int2.stringRepresentation[len(int2.stringRepresentation)-1]
        # Make the final string and return it
        string = startSymbol + str(start) + "," + str(end) + endSymbol
        return interval(string)
    else:
        raise NoIntersectionException()
        
        

# Question 3

def mergeOverlapping(intervals):
    """
    Summary:
        Takes a list of intervals as an argument. 
        Merges overlapping intervals and returns a list of non-overlapping intervals. 
    Logic: loop over the list, keeping track of what intervals have been already merged. 
        Take the first non-merged interval and check if it can be merged with one of the later intervals in the list. 
        If yes, loop over the list again. Keep looping while new merges happen. 
        When no more merges happen, store the result in the output and take the next non-merged element of the list.
    Local variables: 
        output - list to be returned by the function
        current - current element of the list that is checked for merges with subsequent elements of the list
        alreadyMerged - list of boolean values keeping track of interval already merged
        newLoopNeeded - boolean value needed to keep looping over the list if a merge happens. Gets True if a merge happens. 
    """
    # Check  every element. Make it of interval class if necessary
    for i in range(len(intervals)): 
        if not isinstance(intervals[i], interval):
            intervals[i] = interval(intervals[i])
    
    output = []
    alreadyMerged = [False]*len(intervals)
    
    # Go over all intervals that have not yet been merged. 
    for i in range(len(intervals)):
        if alreadyMerged[i] == False:
            current = intervals[i]
            alreadyMerged[i] = True
            # newLoopNeeded is used to start a new loop over all intervals if a merge happens
            # Motivation: other intervals can be merged after a merge happens
            newLoopNeeded = False
            # Loop over non-merged intervals located after the current one in the list
            for j in range(i+1, len(intervals)):
                if alreadyMerged[j] == False:
                    if mergeable(current, intervals[j]):
                        # If mergeable, require a new loop and merge
                        newLoopNeeded = True
                        current = mergeIntervals(current, intervals[j])
                        alreadyMerged[j] = True
            # Loop over all non-merged intervals while merges happen
            while (newLoopNeeded == True):
                newLoopNeeded = False
                for m in range(len(intervals)):
                    if alreadyMerged[m] == False:
                        if mergeable(current, intervals[m]):
                            newLoopNeeded = True
                            current = mergeIntervals(current, intervals[m])
                            alreadyMerged[m] = True      
            # When no merges happen with the current interval, append it to the output list
            output.append(current)
    
    return output


# Question 4
def insert(intervals, newint): 
    """
    Summary: 
        Takes 2 arguments: list of non-overlapping intervals and an interval. 
        Returns a list of merged intervals (when possible).
    """
    # Check every element in the input list. Make it of interval class if necessary
    for i in range(len(intervals)):
        if not isinstance(intervals[i], interval):
            intervals[i] = interval(intervals[i])
    # Check newint argument and make it of interval class if necessary
    if not isinstance(newint, interval):
        newint = interval(newint)
    
    # Make a copy of intervals. Append newint
    allIntervals = list(intervals)
    allIntervals.append(newint)
    
    return mergeOverlapping(allIntervals)