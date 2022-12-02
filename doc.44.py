# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# 84}, {'Science': 95, 'Language': 80}]


a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=list(a.values())
c=list(a.keys())
i=0
d={}
e={}
f={}
g={}
while i<len(a): 
    j=0
    while j<len(b[i]):
        d[c[i]]=b[i][0]
        k=0
        while k<len(b[i]):
            e[c[i]]=b[i][1]   
            l=0
            while l<len(b[i]):
                f[c[i]]=b[i][2] 
                g[c[i]]=b[i][3]
                z=(d,e,f,g)
                l=l+1
            k=k+1  
        j=j+1
    i=i+1
print(list(z))