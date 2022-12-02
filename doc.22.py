# Write a Python program to create and display all combinations of letters, selecting each
# letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

a= {'1':['a', 'b'], '2':['c', 'd']}
b= list(a.values())
for i in b[0]:
    for j in b[1]:
        print(i+j)



a= {'1':['a', 'b'], '2':['c', 'd']}
b= list(a.values())
i=0
while i<len(a):
    for j in b[0]:
        for k in b[1]:
            print(j+k)
        i=i+1
    
    
        
d= {'1':['a', 'b'], '2':['c', 'd']}
for x in d['1']:
    for y in d['2']:
        print(x + y)
        
        
