'''Defining class interval that represents the range of integers between a lower and upper bound. Either of the bounds of an interval can be “inclusive” or “exclusive” and can be positive or negative. The bounds must always meet the requirement that lower <= upper if both bounds are inclusive, lower < upper if one bound is exclusive and one inclusive, or lower < upper-1 if both are exclusive. When the class is printed, intervals are displayed using square brackets [ ] for inclusive bounds or parenthesis ( ) for exclusive bounds.'''
class interval(object):
	def __init__(self, input_string):
		#input_string is the interval written in string form
		#list_from_string will split the string into a lower and upper portion
		list_from_string = input_string.split(",")
		#open_bracket is the first character of the first item in the new list
		open_bracket = list_from_string[0][0]
		#close_bracket is the last character of the last item in the new list
		close_bracket = list_from_string[-1][-1]

		lower = int(list_from_string[0][1:])
		upper = int(list_from_string[1][:-1])

		global valid
		valid = True #initialize boolean that will check if string is valid string

		#checks if string format conforms to requirements
		if (open_bracket == '[') & (close_bracket == ']') & (lower <= upper):
			pass
		elif (open_bracket == '(') & (close_bracket == ')') & (lower < upper-1):
			pass
		elif lower < upper:
			pass
		else:
			valid = False

		self.lower = lower
		self.upper = upper
		self.open = open_bracket
		self.close = close_bracket

		if open_bracket == '[':
			self.first_num = lower
		else:
			self.first_num = lower+1

		if close_bracket == ']':
			self.last_num = upper
		else:
			self.last_num = upper-1

	def __repr__(self):
		if valid == True:
			return self.open + str(self.lower) + "," + str(self.upper) + self.close
		else:
			return "Invalid interval"


'''function mergeIntervals(int1, int2) that takes two intervals, and if the intervals overlap returns a merged interval.'''
def mergeIntervals(int1, int2):
	overlap = True #initialize overlap, assuming true
	if ((int1.last_num < int2.first_num) & (int1.first_num < int2.first_num)) or ((int2.last_num < int1.first_num) & (int2.first_num < int1.first_num)):
		overlap = False
	# if ((int1.first_num == int2.first_num) & (int1.last_num == int2.last_num)):
	# 	overlap = False

	if int1.first_num < int2.first_num:
		open_bracket = int1.open
		lower = int1.lower
	else:
		open_bracket = int2.open
		lower = int2.lower

	if int1.last_num > int2.last_num:
		close_bracket = int1.close
		upper = int1.upper
	else:
		close_bracket = int2.close
		upper = int2.upper

	if overlap == True:
		merged_int_string = open_bracket + str(lower) + "," + str(upper) + close_bracket
		merged_int = interval(merged_int_string)
		return merged_int
	else:
		return None

'''function mergeOverlapping(intervals) that takes a list of intervals and merges all overlapping intervals.'''
def mergeOverlapping(intervals):
	#intervals is a list of string intervals
	#let return_list be an empty list to append merged intervals into
	return_list = []

	return_list.append(intervals[0])
	while len(intervals)>1:
		del intervals[0]

		merged = mergeIntervals(return_list[0], intervals[0])
		if merged != None:
			return_list[0] = merged
		else: return_list.append(intervals[0])

	return return_list

'''function insert(intervals, newint) that takes two arguments: a list of non-overlapping intervals; and a single interval. The function should insert newint into intervals, merging the result if necessary.'''
def insert(intervals, newint):
	appended_list = intervals
	appended_list.insert(0, newint)
	return mergeOverlapping(appended_list)

'''function string_reader(string) takes a string input and turns it into a list of interval objects'''
def string_reader(string):
	list_from_string = string.split(", ")
	intervals_list = []
	for item in list_from_string:
		intervals_list.append(interval(item))
	return intervals_list

'''ran into issues with program-writing'''

interval_list = raw_input("List of intervals?")

interval_list = string_reader(interval_list)

newint = interval(raw_input("Interval?"))

interval_list = insert(interval_list, newint)

print interval_list