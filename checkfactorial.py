#factorial of a given number
import math
def factorial(num):
	return(math.factorial(num))
num = int(input('Please enter a number to find the factorial: '))
print("The factorial of the given number", num, "is",
	factorial(num))
