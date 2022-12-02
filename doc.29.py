# Write a Python program to sort a list alphabetically in a dictionary
my_dict = {"a": [2, 3, 5],
           "b": [1, 8, 4],
           "c": [9, 0, 1]}

for i in my_dict.values():
    i.sort()
print(my_dict)



a = {"a": [2, 3, 5],
           "b": [1, 8, 4],
           "c": [9, 0, 1]}
i=0
d={}
b=list(a)
while i<len(a):
    a[b[i]].sort()
    d[b[i]]=a[b[i]]
    i=i+1
print(d)