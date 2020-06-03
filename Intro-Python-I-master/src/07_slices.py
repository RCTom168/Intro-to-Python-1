"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1]) # The number 4 is in the 1 slot

# Output the second-to-last element: 9
print(a[4]) # The number 9 is in the 4 slot
print(a[-2]) # This is more specific to "second-to-last"

# Output the last three elements in the array: [7, 9, 6]
print(a[3:]) # 7, 9, & 6 are in the last 3 slots

# Output the two middle elements in the array: [1, 7]
print(a[2:4]) # 1 & 7 are in slots 2 & 3, 4 isn't counted

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:]) #Starts at the 1 slot and moves forward

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:5]) # Starts at the front and stops before the last one

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])