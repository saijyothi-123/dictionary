# 51.Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}




a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
d={}
for i in a:
    lis=[]
    for k in a[i]:
        if k%2==0:
            lis.append(k)
    d[i]=lis
print(d)


a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
b=list(a.values())
c=list(a.keys())
i=0
dict1={}
while i<len(c):
    list1=[]
    j=0
    while j<len(b[i]):
        if b[i][j]%2==0:
            list1.append(b[i][j])
        j=j+1
    dict1[c[i]]=list1
    i=i+1
print(dict1)