# 23.Write a Python program to find the highest 3 values of corresponding keys in a
# dictionary.


# a={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}
# x=list(a.values())
# x.sort(reverse=True)
# x=x[:3]
# print(x)


a={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}
x=list(a.values())
x.sort()
y=x[:-4 :-1]
# print(x)
print(y)



a={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}
x=list(a.values())
b=[]
i=0
while i<len(a):
    x.sort(reverse=True)
    z=x[i]
    b.append(z)
    c=b[:3]
    i=i+1
print(b)
print(c)