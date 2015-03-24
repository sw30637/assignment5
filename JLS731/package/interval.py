'''
Created on Mar 18, 2015
Created by Joseph Song (JLS731)
Filename: interval.py
Description: Defines 'interval' class and the three functions (mergeIntervals, mergeOverlapping, and insert)

'''

from errorsExceptions import * 


class interval:
    """interval class: Input an (string) interval and grab the relevant attributes to use in other functions and catch any errors"""
    def __init__(self, string):
        leftBrace = string[0]
        intervalValues = string[1:-1]
        rightBrace = string[-1]
        
        try:
            lowerBound, upperBound = intervalValues.split(',')
            self.lowerBound = int(lowerBound)
            self.upperBound = int(upperBound)  
            assert leftBrace in ["[","("]
            assert rightBrace in ["]",")"]          
        except:
            raise incorrectInputException()
        self.leftBraceInclusive = (leftBrace=="[") 
        self.rightBraceInclusive = (rightBrace=="]")
        if ((self.leftBraceInclusive and self.rightBraceInclusive and self.lowerBound > self.upperBound)\
            or (not self.leftBraceInclusive and self.rightBraceInclusive and self.lowerBound >= self.upperBound)\
            or (not self.leftBraceInclusive and not self.rightBraceInclusive and self.lowerBound >= self.upperBound-1)):
            raise incorrectBoundException()

    #Need the "lowerValue" and "upperValue" to use in later parts of the assignment
    def lowerValue(self):
        """ Creates the actual lower bound """
        if self.leftBraceInclusive:
            return self.lowerBound
        else:
            return self.lowerBound+1

    def upperValue(self):
        """ Creates the actual upper bound """
        if self.rightBraceInclusive:
            return self.upperBound
        else:
            return self.upperBound-1
        
        
    def __repr__(self):
        """ Spits out the interval as a string again """
        if self.leftBraceInclusive:
            left = "["
        else:
            left = "("
        if self.rightBraceInclusive:
            right = "]"
        else:
            right = ")"
        return left + str(self.lowerBound) + "," + str(self.upperBound) + right
        

def merge_intervals(int1, int2):
    """ Takes two intervals, and if the intervals overlap returns a merged interval. If no overlap, exception is thrown"""
    interval1 = interval(int1)
    interval2 = interval(int2)
    
    maxInt1 = interval1.upperBound
    maxInt2 = interval2.upperBound
    minInt1 = interval1.lowerBound
    minInt2 = interval2.lowerBound
    
    maxBound = (maxInt1, maxInt2)
    minBound = (minInt1, minInt2)
    
    maxVals = (interval1.upperValue(),interval2.upperValue())
    minVals = (interval1.lowerValue(),interval2.lowerValue())

    if min(maxVals) >= max(minVals)-1:
        
        minIndex = minBound.index(min(minBound))
        maxIndex = maxBound.index(max(maxBound))
        
        if minIndex == 0:
            leftBrace = int1[0]
        if minIndex == 1:
            leftBrace = int2[0]
        if maxIndex == 0:
            rightBrace = int1[-1]
        if maxIndex == 1:
            rightBrace = int2[-1]
        newInterval = leftBrace + str(minBound[minIndex]) + ',' + str(maxBound[maxIndex]) + rightBrace
        return newInterval
    else:
        raise noOverlapException()

def mergeOverlapping(intervals):
    """ Takes a list of intervals and merges all overlapping intervals"""
    newList = []
    for i in xrange(0,len(intervals)):
        newList.append(interval(intervals[i]))
    newList = sorted(newList, compareLowerBound) #Reorder by the lower bound
    mergeList = []
    firstItem = str(newList[0])
    for nextItem in newList[1:]:
        nextItem = str(nextItem)
        try:
            firstItem = merge_intervals(firstItem, nextItem)
        except:
            mergeList.append(firstItem)
            firstItem = nextItem
    mergeList.append(firstItem)
    for j in xrange(0,len(mergeList)):
        mergeList[j] = interval(mergeList[j])
    return mergeList

def insert(intervals, newint):
    """ Takes two argument: list of non-overlapping intervals and a single interval and inserts newint in the approprate spot and merges accordingly"""
    intervals.append(newint)
    newIntervals = mergeOverlapping(intervals)
    return newIntervals
    
def compareLowerBound(int1,int2):
    """ Compares lower bounds of two intervals: we use this to sort"""
    return cmp(int1.lowerValue(),int2.lowerValue())

