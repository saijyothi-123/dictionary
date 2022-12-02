
# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300}


# while loop:
a = {'a': 100, 'b': 200, 'c':300}
b = {'a': 300, 'b': 200, 'd':400}
i=0
x=list(a)
y=list(b)
z={}
while i<len(a):
    if x[i] in y[i]:
        z[x[i]]=a[x[i]]+b[y[i]]
    else:
        z[x[i]]=x[i]=a[x[i]]
        z[y[i]]=y[i]=b[y[i]]
    i=i+1
print(z)


# for loop:
x = {'a': 100, 'b': 200, 'c':300}
y = {'a': 300, 'b': 200, 'd':400}
d={}
for i in x:
    if i=="a":
        e=(x.get(i)+y.get(i))
        d[i]=e
    elif i=="b":
        e=(x.get(i)+y.get(i))
        d[i]=e
    elif i=="c":
        e=x.get(i)
        d[i]=e
for j in y:
    if j=="d":
        e=y.get(j)
        d[j]=e
print(d)
        

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
e={}
for i in d1 :
    if i not in d2 :
        e[i]=d1[i]
    else :
        e[i]=(d1[i]+d2[i])
for x in d2 :
    if x not in e :
        e[x]=d2[x]
print(e)

       