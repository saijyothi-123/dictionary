# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y




x= {'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
i=0
c=list(x.values())
d=list(y.values())
e=list(x.keys())
while i<len(x):
    if c[i]==1 and d[i]==1:
        print(e[i],":",c[i],"is present in both x and y")
    i=i+1
    
    
  
    
    
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))
	
