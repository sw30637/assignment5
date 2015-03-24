'''
Created on Mar 8, 2015
@author: Adam Biesenbach
'''

# Import the regular expressions package, which we use to pull out the numbers in the interval form a string. 
import re   

# Create a new class for handling interval errors. 
class IntervalException(Exception): pass

class interval: 
    """A class that represents the range of integers between an upper bound and a lower bound, with some constraints."""
    # this next bit defines the 'constructor.' and the objects which are accesible when the class is initialized.
    def __init__(self, Range):
        
        self.Range = str(Range)    
        # Pull out the numbers in the range using the RE findall function. Here "-*\d+" tells python 
        # to create a list attribute called NumbersInRange where each element in the list either starts with 
        # a negative sign, or doesn't and is a number of any length.
        self.NumbersInRange = [int(x) for x in re.findall(r"-*\d+", Range)]
        
        # Same RE here, except we're creating a list of the brackets from the string. Notice that we had to use the
        # escape sequence "\" to be able to loop for the special character "]".
        self.Brackets = re.findall(r"[()[\]]", Range)
              
    # In this next section, I define the rules that the constructor must abide by, as set out in the question prompt. 
    # Then I assign the attribute variables that I'll use in lter programs. 
              
        def EmptySetHandling():
            if self.NumbersInRange == []:
                raise IntervalException("Empty interval.")
       
        def DoubleBracketsErrorHandling():       
            if self.NumbersInRange[0]>self.NumbersInRange[1]:
                raise IntervalException("must have lower<=upper with bounds given in one or more intervals.")
            else:
                self.FirstNumber=int(self.NumbersInRange[0])    
                self.LastNumber= int(self.NumbersInRange[1])
            
        def MixedbracketsErrorhandling():
            if (self.Brackets[0]=='[' and self.Brackets[1]==')') or (self.Brackets[0]=='(' and self.Brackets[1]==']'):
                if self.NumbersInRange[0]>=self.NumbersInRange[1]:
                    raise IntervalException("must have lower<upper with bounds given in one or more intervals.")
                else:
                    if (self.Brackets[0]=='[' and self.Brackets[1]==')'):     
                        self.FirstNumber=int(self.NumbersInRange[0])
                        self.LastNumber=int(self.NumbersInRange[1])-1
                    elif (self.Brackets[0]=='(' and self.Brackets[1]==']'):
                        self.FirstNumber=int(self.NumbersInRange[0])+1
                        self.LastNumber=int(self.NumbersInRange[1])    
   
        def DoubleParenthesisErrorHandling():
            if self.Brackets[0]=='(' and self.Brackets[1]==')':
                if self.NumbersInRange[0]>=self.NumbersInRange[1]-1:
                    raise IntervalException("must have lower<upper-1 with bounds given in one or more intervals.")
                else:
                    self.FirstNumber=int(self.NumbersInRange[0])+1
                    self.LastNumber=int(self.NumbersInRange[1])-1     
 
        def IntervalErrorHandling():  
            if len(self.NumbersInRange)< 2 or (self.Range[0]!='[' and self.Range[0]!='(') or \
             (self.Range[-1]!=']' and self.Range[-1]!=')'):
                raise IntervalException("must have a valid range.")

        def AllBracketTypeErrorHandling():
            """This is just a wrapper for the error handling functions."""
            IntervalErrorHandling()
            EmptySetHandling()
            DoubleBracketsErrorHandling()
            MixedbracketsErrorhandling()
            DoubleParenthesisErrorHandling()

        AllBracketTypeErrorHandling()
