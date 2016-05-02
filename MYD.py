import math

def mind_your_decisions_puzzle(sqrt_coefficient,max_recursion_depth,default_value_after_max_recursion):

	if sqrt_coefficient>max_recursion_depth: #If statement meant to stop infinite recursion
		return default_value_after_max_recursion #After a certain number of recursions
		
	else:
		x=math.sqrt(1+sqrt_coefficient*sqrt_puz(sqrt_coefficient+1,max_recursion_depth,default_value_after_max_recursion)) 
		#Sqrt(1 + 2 * Sqrt(1 + 3 * Sqrt(1 + 4 * .... This function will solve the equation recursively
		return x
		
mind_your_decisions_puzzle(2,900,2) 
#With a high enough recursion limit, the default_value_after_max_recursion won't matter
