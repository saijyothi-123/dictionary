# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}



a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x=list(a.values())
y=list(a.keys())
d={}
i=0
while i<len(a):
    x.sort(reverse=True)
    d[a[x[i]]]=x[i]
    i=i+1
print(d)


a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x=list(a.values())
b=[]
i=0
while i<len(a):
    x.sort(reverse=True)
    z=a[x[i]],x[i]
    b.append(z)
    i=i+1
print(b)