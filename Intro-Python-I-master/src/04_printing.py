"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:

# x is 10, y is 2.25, z is "I like turtles!"

print("x is %d, y is %.2f, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing
print("x is {}, y is {}, z is {}".format(10, 2.25, "I like turtles!"))

# Finally, print the same thing using an f-string
print(f"x is {10}, y is {2.25}, z is {z}")