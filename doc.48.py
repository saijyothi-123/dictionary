# Q48.Write a Python program to find the length of a given dictionary values.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}




a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
b=list(a.values())
i=0
d={}
while i<len(a):
    d[b[i]]=len(b[i])
    i=i+1
print(d)




a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
b=list(a.values())
i=0
d={}
while i<len(a):
    d[b[i]]=len(b[i])
    i=i+1
print(d)

