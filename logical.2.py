# print the value in the table

a={"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}
a,b,c=a.keys()
print(a,b,c)
x,y,z=a.values()
d=x,y,z
i=0
while i<len(d):
    print(x[i],y[i],z[i])
    i=i+1