
def fizz_buzz(numEntered):
	# if the number is divisible by  3 & 5
	if(numEntered%3 ==0 and numEntered%5==0):
		return "FizzBuzz"
	else:
		# if number is divisible by 3 only
		if(numEntered%3 == 0):
			return "Fizz"	
		#if num is divisble by 5 only
		elif(numEntered%5 == 0):
			return "Buzz"	
		#number not divisible by neither 3 nor 5
		else:
			return numEntered