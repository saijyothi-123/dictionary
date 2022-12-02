# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

a='w3resource'
d={}
for i in a:
    d[i]=a.count(i)
print(d)

# while loop:
a='w3resource'
b=[]
d={}
i=0
count=0
while i<len(a):
    if a[i].isalpha() or a[i].isdigit():
        d[a[i]]=a.count(a[i])
        b.append(a[i])
    i=i+1
print(d)



# o/p: {0:1, 1:1, 2:2, 3:2, 4:1, 5:1, 6:1, 7:1, 8:1, 9:2}
a='w3resource'
b=[]
d={}
i=0
count=0
while i<len(a):
    if a[i].isalpha() or a[i].isdigit():
        d[i]=a.count(a[i])
        b.append(a[i])
    i=i+1
print(d)


