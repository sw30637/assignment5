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
#  Interval.py  
#  This gets called by main.py
#
##########################################################################################



import sys
from operator import itemgetter

##############################
# Class Interval
##############################  
class Interval:
    
    #initializing
    def __init__(self, intervals):
         #self.int1 = int1
         #self.int2 = int2
         self.intervals =  intervals


    ################################################
    # function mergeIntervals
    # mergeIntervals takes two intervals and compare if these overlap
    # if overlap, exception should be thrown and return both values
    # calls numCompare to compare
    ################################################
    def mergeIntervals(self, int1, int2):
        firstnum =  int1.split(",")
        secondnum =  int2.split(",")
        first_openSymbol = firstnum[0][0]
        first_openNumber = int(firstnum[0][1:])
        first_closeNumber = int(firstnum[1][0:-1])
        first_closeSymbol =  firstnum[1][-1]
        second_openSymbol = secondnum[0][0]
        second_openNumber = int(secondnum[0][1:])
        second_closeNumber =int(secondnum[1][0:-1])
        second_closeSymbol =  secondnum[1][-1]

        # in order to use smaller open number of two sets to be compared 
        # this calls function numCompare
        if first_openNumber<=second_openNumber:
            return self.numCompare (int1, int2, first_openSymbol,first_openNumber,first_closeNumber,first_closeSymbol,second_openSymbol,second_openNumber,second_closeNumber,second_closeSymbol)
        else:
            return self.numCompare (int2, int1, second_openSymbol,second_openNumber,second_closeNumber,second_closeSymbol,first_openSymbol,first_openNumber,first_closeNumber,first_closeSymbol)
     
     
     
     ################################################
     # function numCompare
     # numCompare is called from mergeIntervals and compares values and return values back to mergeIntervals
     ################################################
    def numCompare(self, int1, int2, first_openSymbol,first_openNumber,first_closeNumber,first_closeSymbol,second_openSymbol,second_openNumber,second_closeNumber,second_closeSymbol):    
        try:
            
            ################################################
            #case 1: first open number is between second numbers
            ################################################
            if (first_openNumber>second_openNumber) and (first_openNumber<second_closeNumber):  
                
                if first_closeNumber<second_closeNumber: 
                     # case 1a: Both of the first numbers are in second number  // int1 is in int2
                    return second_openSymbol+str(second_openNumber)+","+str(second_closeNumber)+second_closeSymbol
                    
                elif first_closeNumber>second_closeNumber:  
                     # case 1b: The first open number falls in second number, and
                     # close number is bigger than second number  // second open ~ first close
                    return second_openSymbol+str(second_openNumber)+","+str(first_closeNumber)+ first_closeSymbol
                    
                else:
                    # case 1c: The first open number falls in second number, and
                     # close number is same as second number  // second open ~ first/second close
                    if (first_closeSymbol=="]") or (second_closeSymbol=="]"):
                        return second_openSymbol+str(second_openNumber)+","+str(first_closeNumber)+ "]"
                    else:
                         return second_openSymbol+str(second_openNumber)+","+str(first_closeNumber)+ ")"
                         
            ################################################             
            # case 2: the first open numbers of both intervals can be equal
            ################################################             
            elif (first_openNumber==second_openNumber):
                
                if (first_closeNumber==second_closeNumber):
                    #case 2a: both numbers can be equal
                    if (first_openSymbol=="[") or (second_openSymbol=="["):
                        if (first_closeSymbol=="]") or (second_closeSymbol=="]"):
                            return "["+ str(first_openNumber)+","+str(first_closeNumber)+"]"
                        else:
                            return "["+ str(first_openNumber)+","+str(first_closeNumber)+")"
                    else: 
                        if (first_closeSymbol=="]") or (second_closeSymbol=="]"):
                            return "("+ str(first_openNumber)+","+str(first_closeNumber)+"]"
                        else:
                            return "("+ str(first_openNumber)+","+str(first_closeNumber)+")"
                    
                elif (first_closeNumber>second_closeNumber):
                    #case 2b: first close number is bigger   //first open ~first close
                    if (first_openSymbol=="[") or (second_openSymbol=="["):
                            return "["+ str(first_openNumber)+","+str(first_closeNumber)+first_closeSymbol
                    else: 
                            return "("+ str(first_openNumber)+","+ str(first_closeNumber)+first_closeSymbol
                        
                else:
                    #case 2c: first close number is smaller   //first open ~second close
                    if (first_openSymbol=="[") or (second_openSymbol=="["):
                            return "["+ str(first_openNumber)+","+ str(second_closeNumber)+second_closeSymbol
                    else: 
                            return "("+ str(first_openNumber)+","+ str(second_closeNumber)+second_closeSymbol
                             
                             
            ################################################                 
            #case 3: first open and second close are equal    
            ################################################ 
            elif (first_openNumber==second_closeNumber):
                if (first_openSymbol=="[") or (second_openSymbol=="["):
                    return "["+ str(second_openNumber)+","+ str(first_closeNumber)+first_closeSymbol
                elif (first_openSymbol=="(") and (second_closeSymbol==")"):
                        raise Exception(int1, int2)      #do not overlap in this case; exception thrown
                else: 
                    return "("+ str(second_openNumber)+","+ str(first_closeNumber)+first_closeSymbol
                    
                    
            ################################################    
            #case 4: the first open number is not in second numbers, so let's compare first close number
            ################################################        
            else:   
                if (first_closeNumber>second_openNumber) and (first_closeNumber<second_closeNumber):
                    #case 4a: the first close number is in second number
                    return first_openSymbol+str(first_openNumber)+","+ str(second_closeNumber)+ second_closeSymbol
                
                elif (first_closeNumber>second_openNumber) and (first_closeNumber>second_closeNumber):
                    #case 4b: the first close number is larger than second numbers
                    return first_openSymbol+str(first_openNumber)+","+ str(first_closeNumber)+ first_closeSymbol
        
                elif first_closeNumber==second_openNumber:
                    #case 4c: first close number and second open number are equal
                    if (first_closeSymbol==")") and (second_openSymbol=="("):
                        raise Exception(int1, int2)      #do not overlap in this case; exception thrown
                    else:    #otherwise, first open ~second close
                        return first_openSymbol+str(first_openNumber)+","+ str(second_closeNumber)+second_closeSymbol

                elif first_closeNumber==second_closeNumber:
                    #case4d: first close number and second close number are equal
                    if (first_closeSymbol=="]") or (second_closeSymbol=="]"):
                        return first_openSymbol+str(first_openNumber)+","+ str(second_closeNumber)+"]"
                    else: 
                        return first_openSymbol+str(first_openNumber)+","+str(second_closeNumber)+")"
                
                elif (first_closeNumber+1)==second_openNumber:  
                    #case4e: bracket detection of ] and [   e.g (1,5] and [6,9)
                    if (first_closeSymbol=="]") and (second_openSymbol=="["):
                        return first_openSymbol+str(first_openNumber)+","+ str(second_closeNumber)+second_closeSymbol
                    else:
                        raise Exception(int1, int2)
                    
                ################################################    
                #otherwise, exception should be thrown and return both integers
                ################################################    
                else:
                    raise Exception(int1, int2)
                
        except Exception:
            #print "Intervals do not overlap:", int1, int2
            return int1, int2


    ################################################
    # function mergeOverlapping
    # mergeOverlapping compares a list of intervals and returns the intervalsList
    ################################################
    def mergeOverlapping(self, intervals):
        global intervalsList   
        tempList=[]
        this_length = len(intervals) 
        
        tempHolder = intervals[0] 
        for line in xrange(1,(this_length),1):        #range starts from 1 instead of 0 because tempHolder = intervals[0] 
                addThis=(self.mergeIntervals(tempHolder,intervals[line]))
                
                if len(addThis)==2:     #in case if the return is tuple (int1, int2)
                     tempList.append(addThis[0])
                     tempHolder = addThis[1]
                     if line == this_length-1:
                           tempList.append(tempHolder)
                else:                  #otherwise, if one value is returned    
                     tempHolder = addThis    
                     if line == this_length-1:
                           tempList.append(addThis)
                           
        intervalsList = tempList  
        return intervalsList


    ################################################
    # function insert
    # insert function inserts newint from userinput
    ################################################
    def insert(self, intervals, newint):
        global intervalsList
        intList=[]            
        mergedList = self.mergeOverlapping(intervals)   #merge the intervals
        this_length = len(mergedList)
        tempHolder = newint

        for line in xrange(0,(this_length),1):
                 addThis=(self.mergeIntervals(tempHolder,mergedList[line]))
                 
                 if len(addThis)==2:     #in case if it is tuple (int1, int2)
                     intList.append(addThis[0])
                     tempHolder = addThis[1]
                     if line == this_length-1:
                           intList.append(tempHolder)
                           
                 else:                  #otherwise, if one value is returned. typically, len(addThis) is over 5 if so
                     tempHolder = addThis    
                     if line == this_length-1:
                           intList.append(addThis)
                           
        intervalsList=intList
        
