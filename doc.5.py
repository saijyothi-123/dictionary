# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x=list(a.values())
b=[]
i=0
while i<len(a):
    x.sort()
    z=a[i],x[i]
    b.append(z)
    i=i+1
print(b)
# o/p- [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]



a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x=list(a.values())
d={}
i=0
while i<len(a):
    x.sort()
    d[a[i]]=x[i]
    i=i+1
print(d)
# o/p-{0:0,2:1,1:2,4:3,3:4}



# by using method:
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)

a = sorted(d.items(), key=lambda item:item[1])
print('Ascending order : ',a)

b = dict( sorted(d.items(), key=lambda item:item[1],reverse=True))
print('Descending order : ',b)



