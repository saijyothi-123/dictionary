# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
print(dic4)




a={1:10, 2:20}
b={3:30, 4:40}
c={5:50, 6:60}
d = {}
i=0
x=list(a)
y=list(b)
z=list(c)
while i<len(a):
    d[x[i]]=a[x[i]]
    d[y[i]]=b[y[i]]
    d[z[i]]=c[z[i]]
    i=i+1
print(d)

