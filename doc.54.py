# Q54.
# Write a Python program to create a key-value list pairings in a given dictionary.
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary
# Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]




a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['ZacharySimon']}
b=list(a.keys())
i=0
d={}
c=[]
while i<len(a):
    z=b[i],a[b[i]]
    # d[a[i]]=z[i]
    c.append(z)
    i=i+1
print(c)


