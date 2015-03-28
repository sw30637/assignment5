'''
Created on Mar 27, 2015

@author: ds-ga-1007
'''
class interval:
    def __init__(self, itv):
        self.itvlist = itv.split(",")

        #the first character of the first item is the open bracket, and the last character of the second item is the close bracket
        self.openingBracket = self.itvlist[0][0]
        self.closingBracket = self.itvlist[1][-1]
        
        #get the real lower bound that the interval represents
        if bracketIsInclusive(self.openingBracket):
            self.lower = int(self.itvlist[0][1:])
        elif bracketIsExclusive(self.openingBracket):
            self.lower = int(self.itvlist[0][1:]) + 1

        #get the real upper bound that the interval represents
        if bracketIsInclusive(self.closingBracket):
            self.upper = int(self.itvlist[1][:-1])
        elif bracketIsExclusive(self.closingBracket):
            self.upper = int(self.itvlist[1][:-1]) - 1


def bracketIsInclusive(bracket):
    '''check if bracket is inclusive'''
    if bracket == "[" or bracket == "]":
        return True
    else:
        return False
        
def bracketIsExclusive(bracket):
    '''check if bracket is exclusive'''
    if bracket == "(" or bracket == ")":
        return True
    else:
        return False
    
#Question 2
def mergeIntervals(int1, int2):
    '''merge two interval strings if overlap, else return the original intervals'''
    itv1 = interval(int1)
    itv2 = interval(int2)
    if intervalValid(itv1.openingBracket, itv1.closingBracket, itv1.lower, itv1.upper) & intervalValid(itv2.openingBracket, itv2.closingBracket, itv2.lower, itv2.upper): 
        #sort by lower bound then determine if they overlapse
        if overLap(itv1.upper, itv2.lower):
            if isLarger(itv1.upper, itv2.upper) == itv2.upper:
                mergedInterval = itv1.itvlist[0] + "," + itv2.itvlist[1]
            elif isLarger(itv1.upper, itv2.upper) == itv1.upper:
                mergedInterval = itv1.itvlist[0] + "," + itv1.itvlist[1]
            elif isLarger(itv1.upper, itv2.upper) == False:
                mergedInterval = itv1.itvlist[0] + "," + itv1.itvlist[1]
        else:
            return False
      
        return mergedInterval
    else:
        raise Exception()
    
    

def isSmaller(bound1, bound2):
    '''check the lower bound of each interval and return the lower one'''
    if bound1 < bound2:
        return bound1
    elif bound1 > bound2:
        return bound2
    elif bound1 == bound2:
        return False
    
def isLarger(bound1, bound2):
    '''check the upper bound of each interval and return the lower one'''
    if bound1 > bound2:
        return bound1
    elif bound1 < bound2:
        return bound2
    elif bound1 == bound2:
        return False    

def overLap(upper, lower):
    '''check if the upper bound of the 1st interval is larger or == to the lower bound of the 2nd interval, if yes, they overlap'''
    if upper >= lower-1:
        return True
    else:
        False
        
#Question 3
def mergeOverLapping(intervals):
    '''takes a list of intervals and merges all overlapping intervals''' 
    
    #sort the intervals
    ###Ask Prof. to Clearify###
    intervals.sort(key = lambda x: interval(x).lower)
    
    output = []
    itvToMerge = intervals[0]
    
    #does not start at 0 because that is itvToMerge
    for item in range(1, len(intervals)):
        #check if merge happened
        if mergeIntervals(itvToMerge, intervals[item]) != False:
            #add the result of mergeIntervals to temporary output
            tempOutput = mergeIntervals(itvToMerge, intervals[item])
            #set itvToMerge to the temp output, which is our newly merged interval
            itvToMerge = tempOutput
            if item == len(intervals)-1:
                output.append(tempOutput)
        else:
            #append itvToMerge to output
            output.append(itvToMerge)
            #set itvToMerge to the second item of the temp output, which is our newly merged interval
            itvToMerge = intervals[item]
            if item == len(intervals)-1:
                output.append(intervals[item]) 
                
    return output

def insert(intervals, newint):
    '''takes a list of intervals & a single interval, place it in the list and merge if necessary'''
    itv = interval(newint)
    if intervalValid(itv.openingBracket, itv.closingBracket, itv.lower, itv.upper):
        intervals.append(newint)
        intervals.sort(key = lambda x:interval(x).lower)
        outPut = mergeOverLapping(intervals)
        return outPut
    else:
        raise Exception()

def intervalValid(openingBracket, closingBracket, lower, upper):
    '''ensure the interval is valid'''
    #if opening bracket is inclusive "[" and closing is also inclusive "]", lower must <= upper
    if openingBracket == "[" and closingBracket == "]" and lower <= upper:
        valid = True
    #if one bracket is inclusive "[" and the other is exclusive ")", lower must < upper
    elif (openingBracket == "(" and closingBracket == "]") or (openingBracket == "[" and closingBracket == ")") and lower < upper:
        valid = True
        #if both are exclusive, lower must < upper - 1
    elif openingBracket == "(" and closingBracket == ")" and lower <= upper-1:
        valid = True
    else:
        valid = False
    return valid
