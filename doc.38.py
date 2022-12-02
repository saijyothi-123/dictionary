# Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


a={'c1': 'Red', 'c2': 'Green', 'c3':None}
b=list(a.values())
c=list(a.keys())
i=0
d={}
while i<len(a):
    if b[i] == None:
        pass
    else:
        d[c[i]]=b[i]

    i=i+1
print(d)



# my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue'}
# keys = my_dictionary.items()
# for r in keys:
#   if my_dictionary[r] == None:
#     del my_dictionary[r]
# print(my_dictionary)




# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
# print("Original Dictionary:")
# print(dict1)
# print("New Dictionary after dropping empty items:")
# dict1 = {key:value for (key, value) in dict1.items() if value is not None}
# print(dict1)


