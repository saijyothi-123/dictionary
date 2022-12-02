# Q6.
# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


d={}
d[0]=10
d[1]=20
d[2]=30
print(d)


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# i/p={1:10,2:20}
# o/p-{1:10,2:20,3:30,4:40}

d={}
for i in range(1,5):
   d[i]=i*10
print(d)


a={1: 10, 2: 20}
i=1
while i<=4:
    a[i]=i*10
    i=i+1
print(a)
    



