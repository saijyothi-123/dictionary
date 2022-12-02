Q52. Write a Python program to find the specified number of maximum values in a given
# dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']



a={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
b=list(a.values())
d=list(a.keys())
x={}
c=[]
i=0
while i<len(a):
    b.sort(reverse=True)
    # z=d[i],b[i]
    # c.append(z)
    x[a[d[i]]]=[d[i],b[i]]
    i=i+1
print(x)
    
