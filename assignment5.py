class interval():
	def __init__(self,interval):

		lower = int(interval[1:interval.index(",")])
		upper = int(interval[(interval.index(",")+1) : -1])
		self._leftbound = interval[0]
		self.lower = lower
		self.upper = upper
		self._rightbound = interval[-1]
		if interval[0] == '[' and interval[-1] == ']':
			if lower > upper:
				raise ValueError ('Lower (%s) must not be greater than the upper(%d)'%(lower,upper))
		elif interval[0] == '(' and interval[-1] == ']':
			if lower > upper or lower == upper:
				raise ValueError('Lower(%s) must be smaller than the upper(%d)'%(lower,upper))
		elif interval[0] == '[' and interval[-1] ==')':
			if lower > upper or lower == upper:
				raise ValueError('Lower(%s) must be smaller than the upper(%d)'%(lower,upper))
		elif interval[0] == '(' and interval[-1] ==')':
			if lower >= upper:
				raise ValueError('Lower(%s) must be smaller than the upper(%d)'%(lower,upper))
	
	def __repr__(self):
		lower = self.lower
		upper = self.upper
		leftbound = self._leftbound
		rightbound = self._rightbound
		if self._leftbound == '[' and self._rightbound == ']':

			return "[%s,%d]"%(lower,upper)
		elif self._leftbound == '(' and self._rightbound == ']':
			return '(%s,%d]'%(lower,upper)
		elif self._leftbound == '[' and self._rightbound == ')':
			return '[%s,%d)'%(lower,upper)
		elif leftbound == '(' and rightbound == ')':
			return '(%s,%d)'%(lower,upper)
		else:
			raise SyntaxError('Please check the format of the interval.')
	def print_interval():
		lower = self.lower
		upper = self.upper
		leftbound = self._leftbound
		rightbound = self._rightbound
		if self._leftbound == '[' and self._rightbound == ']':
			
			return '"[%s,%d]" represents the numbers %s through %d'%(lower,upper,lower,upper)
		elif self._leftbound == '(' and self._rightbound == ']':
			return '"(%s,%d]" represents the numbers %s through %d'%(lower,upper,lower+1,upper)
		elif self._leftbound == '[' and self._rightbound == ')':
			return '"[%s,%d)" represents the numbers %s through %d'%(lower,upper,lower,upper-1)
		elif leftbound == '(' and rightbound == ')':
			return '"(%s,%d)" represents the numbers %s through %d'%(lower,upper,lower+1,upper-1)
		else:
			raise SyntaxError('Please check the format of the interval.')
	

	def mergeIntervals(int1,int2):
	# if up.upper <down.upper:
	# 	raise SyntaxError('Please change the position of down and up')
		a = max(int1.upper,int2.upper)
		if a == int1.upper > int2.upper:
			up=int1
			down = int2
		elif a == int2.upper > int1.upper:
			up = int2
			down = int1
		elif a == int1.upper == int2.upper:
			if int2._rightbound == ')' :
				up = int1
				down = int2
			elif int1._rightbound == ')':
				up = int2
				down = int1

		if up.lower > down.upper:
			raise Exception('The two intervals do not overlap')
		elif up.lower == down.upper:
			if up._leftbound == '[' and down._rightbound == ']':
				# print down._leftbound + str(down.lower)+','+str(up.upper)+up._rightbound
				return down._leftbound + str(down.lower)+','+str(up.upper)+up._rightbound
			
			else:
				raise Exception('The two intervals do not overlap')
		elif up.lower < down.upper and up.lower > down.lower:
			# print down._leftbound+str(down.lower)+','+str(up.upper),up._rightbound
			return  down._leftbound+str(down.lower)+','+str(up.upper)+up._rightbound
		elif up.lower == down.lower:
			if down._leftbound == up._leftbound == '[':
				return up
			elif down._leftbound =='(' or up._leftbound == '(':
				# print '('+str(up.lower)+','+str(up.upper),up._rightbound
				return  '('+str(up.lower)+','+str(up.upper),up._rightbound
		elif up.lower < down.lower:
			# print up._leftbound+str(up.lower)+','+str(up.upper),up._rightbound
			return up

		elif up.lower == down.lower:
			if down._leftbound == up._leftbound == '(':
				return up
			elif down._leftbound =='[' or up._leftbound == '[':
				# print '['+str(up.lower)+','+str(up.upper),up._rightbound
				return  '['+str(up.lower)+','+str(up.upper),up._rightbound
def mergeOverlapping(Intervals):
	si = sorted(Intervals, key = lambda Int: Int.lower)
		
	mergedList = []
	for Int in si:
		if not mergedList:
			mergedList.append(Int)
		else:
			b = mergedList.pop()
			if b.upper >= Int.upper and b.lower < Int.lower:
				mergedList.append(b)
			elif b.upper >= Int.lower and b.lower < Int.lower:
				new_Int = interval('(%s,%d)'%(b.lower,Int.upper))
				mergedList.append(new_Int)
			else:
				mergedList.append(b)
				mergedList.append(Int)

	return mergedList

def insert(intervals, newint):

	intervals.append(newint)
	newinterval_List = mergeOverlapping(intervals)
	return newinterval_List


def program():
	inputstring = raw_input('List of intervals?')
	# if ' ' not  in inputstring:
	# 	raise ValueError('There must be a space after each interval comma')
	# else:
	count = 0
	while 	count == 0:
		try:
			intervalList= inputstring.split(', ')
			break
		except ValueError:
			print('Please check the format of the string')

	a = []
	for ele in intervalList:
		b = interval(ele)
 		a.append(b) 
	k = mergeOverlapping(a)
	var = 1
	intervallist = []
	intstr = raw_input('Interval?')
	while var == 1:
		if intstr[0] == '(' or intstr[0] == '[':
			e = interval(intstr)
			m = insert(k,e)
			intstr = raw_input('Interval?')
		if intstr == 'Q' or intstr == 'quit' or intstr == 'q':
			break
		else:
			print 'invalid interval'
			intstr = raw_input('Interval?') 
	print m 
	return m 

if __name__ == '__main__':
	program()
# a = interval('[4,7]')
# b = interval('[5,10]')
# c = interval('(11,19)')
# d = interval('(1,20)')
# k = [a,b,c,d]
# e = interval('(-1,21)')
# m = mergeOverlapping(k)
# print m 
# n = insert(m,e)
# print n 

