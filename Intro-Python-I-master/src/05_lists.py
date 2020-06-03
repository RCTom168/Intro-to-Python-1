# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4) # Append the number 4 to the end of x
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y) # Extend the new x by adding the y values to the end
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4) # Remove the integer in position 4
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99) # Place the number 99 in position 5
print(x)

# Print the length of list x
# YOUR CODE HERE
print("The length of list x is:", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print("The Product is:", i*1000,  '\n', "-"*85) # Multiplies each value in x[] by 1000