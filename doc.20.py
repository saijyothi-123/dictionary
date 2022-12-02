# Write a Python program to check a dictionary is empty or not.
# Checking if a dictionary is empty by checking its length
empty_dict = {}
if len(empty_dict) == 0:
    print('This dictionary is empty!')
else:
    print('This dictionary is not empty!')



empty_dict = {}
if empty_dict:
    print("Dictionary is not empty!")
else:
    print("Dictionary is empty!")
# Returns: Dictionary is empty!


dict1 = {}

if dict1:
    print("dict1 Not Empty")
else:
    print("dict1 is Empty")

if bool(dict1):
    print("dict1 Not Empty")
else:
    print("dict1 is Empty")


a = []
if a:
  print("List is empty")
else:
  print("Not empty")
