
# Write a Python program to remove duplicates from Dictionary.


a = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}
b = []
d = dict()
for key, val in a.items():
    if val not in b:
        b.append(val)
        d[key] = val

print(d)



a = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}
b=list(a)
c=[]
d={}
i=0
while i<len(a):
    if a[b[i]] not in c:
        c.append(a[b[i]])
        d[b[i]]=a[b[i]]
    i=i+1
# print(c)
print(d)



