class interval(object):

	input = []
	temp = []
# Make the constructor function in order to take correct input

	def __init__(self, input_interval):
		input = separateIntervals(input_interval)
		if (input_interval[0] == '[' and input_interval[-1] == ']') and (int(input[0])>int(input[1])):
			print 'The upper bound ' + input[1] + ' must be greater than the lower bound ' + input[0]
		elif (input_interval[0] == '[' and input_interval[-1] == ')') and (int(input[0])>=int(input[1])):
			print 'The upper bound ' + input[1] + ' must be greater than the lower bound ' + input[0]
		elif (input_interval[0] == '(' and input_interval[-1] == ']') and (int(input[0])>=int(input[1])):
			print 'The upper bound ' + input[1] + ' must be greater than the lower bound ' + input[0]
		elif (input_interval[0] == '(' and input_interval[-1] == ')') and (int(input[0])>=int(input[1])):
			print 'The upper bound ' + input[1] + ' must be greater than the lower bound ' + input[0]
		elif input_interval[0] == '[' and input_interval[-1] == ']':
			print '"[%s,%d]" represents the numbers %s through %d inclusive'%(int(input[0]),int(input[1]),int(input[0]),int(input[1]))
		elif input_interval[0] == '[' and input_interval[-1] == ')':
			print '"[%s,%d)" represents the numbers %s through %d'%(int(input[0]),int(input[1]),int(input[0]),int(input[1])-1)
		elif input_interval[0] == '(' and input_interval[-1] == ']':
			print '"(%s,%d]" represents the numbers %s through %d'%(int(input[0]),int(input[1]),int(input[0])+1,int(input[1]))
		elif input_interval[0] == '(' and input_interval[-1] == ')':
			print '"(%s,%d)" represents the numbers %s through %d'%(int(input[0]),int(input[1]),int(input[0])+1,int(input[1])-1)
		else:
			print 'Enter the correct format for the interval!'

		self._input_interval = input_interval
		self._input = input 	# has the upper and lower bound of interval in a list eg [2, 9]



	def mergeIntervals(int1, int2):
		values1 = separateIntervals(int1)
		values2 = separateIntervals(int2)

		if int(values1[0])>int(values1[1]) or int(values2[0])>int(values2[1]):
			print 'The upper bound must be greater than the lower bound'
		elif int(values2[0])>int(values1[1]) or int(values1[0])>int(values2[1]) :
			print 'The interval does not overlap and cannot be merged'
		elif ((int(values2[0])==int(values1[1]) and (int2[0]=='(' or int1[0]==')')) or (int(values1[0])==int(values2[1]) and (int2[0]==')' or int1[0]=='('))):
			print 'The interval does not overlap and cannot be merged'
		else:
			if int(values2[1])>int(values1[1]):
				return int1[0] + values1[0] + ',' + values2[1] + int2[-1]
			elif int(values1[1])>int(values2[1]):
				return int2[0] + values2[0] + ',' + values1[1] + int1[-1]


def mergeOverlapping(intervals):
	sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
	merged = []

	for higher in sorted_by_lower_bound:
    		if not merged:
        		merged.append(higher)
    		else:
        		lower = merged[-1]
        		# test for intersection between lower and higher:
        		# we know via sorting that lower[0] <= higher[0]
        		if higher[0] <= lower[1]:
            			upper_bound = max(lower[1],higher[1])
            			merged[-1] = (lower[0],upper_bound)  # replace by merged interval
        		else:
            			merged.append(higher)
	return merged
		
def insert(intervals, newint):
	temp = separateIntervals(newint)
	intervals.append((int(temp[0]),int(temp[1])))
	newIntervals = mergeOverlapping(intervals)
	return newIntervals

# This function is to separate the input interval that will be given by the user

def separateIntervals(input_interval):
	temp = input_interval[1:-1]
	input = temp.split(',')
	return input

# Write a function that will take in the inout from the user in proper format

def takeInput():
	temp         = []
	listOfValues = []
	finalMerged  = []
	finalList    = []

	print 'Please type the list of intervals in proper format. For example: [1,5], [2,6), (8,10], [8,18]'
	inputInterval = raw_input('List of Intervals?')

	temp = inputInterval.split(', ')
	try:
		for num in temp:
			tempTuple = separateIntervals(num)
			listOfValues.append((int(tempTuple[0]),int(tempTuple[1])))
		finalMerged = mergeOverlapping(listOfValues)

		print finalMerged

	except:
		print 'You have entered a wrong format. Try again!'
		inputInterval = raw_input('List of Intervals?')

	print 'Enter an interval to be inserted. Type q to quit.'
	while inputInterval != 'q':
		inputInterval = raw_input('Interval?')
		try:
#			inputInterval = raw_input('Interval?')
			finalList = insert(finalMerged, inputInterval)
			print finalList
		except:
			print 'Please entet the correct format. For example: [1,5] or [2,6) or (8,10] or [8,18]'
#			inputInterval = raw_input('Interval?')
	

if __name__ == "__main__":

	takeInput()
				
					

