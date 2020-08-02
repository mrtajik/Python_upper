"""
Advance 
"""
 
#sum,min,max, slicing lists
# .join() 
# int to string conversion
#generator expressions
# Python code to illustrate generator expression 
generator = (num ** 2 for num in range(100)) 
for num in generator: 
	print(num) 


#zip function
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))