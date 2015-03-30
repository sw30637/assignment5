class interval:
    """Represents the range of integers between a lower bound and an upper bound"""

    def __init__(self, interval_input):
        self.interval_input = str(interval_input)
        comma_index = self.interval_input.index(',')
        self.lower_bound = 0
        self.lower_bracket = ''
        self.upper_bound = 0
        self.upper_bracket = ''

        if self.interval_input[0] == '(':
            self.lower_bound = int(self.interval_input[1:comma_index])+1
            self.lower_bracket = '('
        elif self.interval_input[0] == '[':
            self.lower_bound = int(self.interval_input[1:comma_index])
            self.lower_bracket = '['
        else:
            print "Invalid interval"
        if self.interval_input[-1:] == ')':
            self.upper_bound = int(self.interval_input[comma_index+1:-1])-1
            self.upper_bracket = ')'
        elif self.interval_input[-1:] == ']':
            self.upper_bound = int(self.interval_input[comma_index+1:-1])
            self.upper_bracket = ']'
        else:
            print "Invalid interval"



# task 2
def mergeIntervals(int1, int2):
    """Merges two intervels when they have overlap"""

    sorted_by_lower_bound = sorted([int1, int2], key = lambda x: x.lower_bound )
    lower = sorted_by_lower_bound[0]
    higher = sorted_by_lower_bound[1]
    if lower.upper_bound >= higher.lower_bound:
        lower_bracket = lower.lower_bracket
        if lower_bracket == '(':
            lower_bound = lower.lower_bound -1
        elif lower_bracket == '[':
            lower_bound = lower.lower_bound

        upper_bound = max(lower.upper_bound, higher.upper_bound)
        merged = interval( lower_bracket + str(lower_bound)+','+str(upper_bound)+']')
    else:
        print "The intervals do not have overlap"
    return merged



#task 3
def mergeOverlapping(intervals):
    """takes a list of intervals and merges all overlapping intervals."""
    sorted_by_lower_bound = sorted(intervals, key = lambda x: x.lower_bound )
    overlapped_intervals = []
    for i in range(len(sorted_by_lower_bound)-1):
        if sorted_by_lower_bound[i].upper_bound<= sorted_by_lower_bound[i+1].lower_bound:
            overlapped_intervals.append(sorted_by_lower_bound[i])
        else:
            sorted_by_lower_bound[i+1] = mergeIntervals(sorted_by_lower_bound[i], sorted_by_lower_bound[i+1])
    return overlapped_intervals.append(sorted_by_lower_bound[i+1])



#task 4
def insert(intervals, newint):
    """takes a list of non-overlapping intervals; 
    and insert a single interval into the list of intervals, 
    merging the result if necessary."""
    intervals.append(newint)
    mergeOverlapping(intervals)



#task 5
def print_interval(int1):
    if int1.lower_bracket == '[':
        lower_bound = int1.lower_bound 
    else:
        lower_bound = int1.lower_bound -1
    if int1.upper_bracket == ']':
        upper_bound = int1.upper_bound
    else:
        upper_bound = int1.upper_bound+1
    print int1.lower_bracket+str(lower_bound)+','+str(upper_bound)+int1.upper_bracket

    
intervals = raw_input("List of intervals? ")
newint = raw_input("Interval? ")
for an_interval in insert(intervals, newint):
    print an_interval



