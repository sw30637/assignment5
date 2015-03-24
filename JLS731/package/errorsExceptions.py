'''
Created on Mar 18, 2015
Created by Joseph Song (JLS731)
These exceptions capture specific errors rather than using catchall
'''


class incorrectInputException(Exception):
    """ Raises error message when interval input is incorrect """
    def __str__(self):
        return 'Invalid Input'  
    
class incorrectBoundException(Exception):
    """ Raises error message when the bounds are incorrectly defined """
    def __str__(self):
        return 'Invalid Bound'

class noOverlapException(Exception):
    """ Raises error message when two intervals do not overlap """
    def __str__(self):
        return 'Intervals do not overlap' 
