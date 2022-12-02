# Write a Python program to map two lists into a dictionary



keys = ['white', 'black', 'software']
values = ['shirt','jean', 'developer']
x= dict(zip(keys, values))
print(x)




# while loop:
keys = ['white', 'black', 'software']
values = ['shirt','jean', 'developer']
d={}
i=0
while i<len(keys):
    d[keys[i]]=values[i]
    i=i+1
print(d)

