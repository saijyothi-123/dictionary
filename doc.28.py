# Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}

# list = [1, 2, 3, 4]
# new_dict = current = {}
# for name in list:
#     current[name] = {}
#     current = current[name]
# print(new_dict)
 
 
list = [1, 2, 3, 4]
a = b = {}
i=1
while i<=len(list):
    b[i] = {}
    b = b[i]
    i=i+1
print(a)


