# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num): # Define the function
 if num % 2 == 0:
  return True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

answer = is_even(num)
# YOUR CODE HERE
if answer is True:
    print("Even!")
else:
    print("Odd!")