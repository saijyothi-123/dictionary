# 3.Write a Python program to sum all the items in a dictionary

a={"x":2,"y":100,"c":50}
b=list(a)
i=0
sum=0
while i<len(a):
    sum=sum+a[b[i]]
    i=i+1
print(sum)
# o/p:152


def Sum(dict):
    sum= 0
    for i in dict.values():
        sum= sum + i
    return sum
dict = {"p":1,"y":5,"t":10,"h":6,"o":3,"n":11}
print(Sum(dict))
# o/p:36


def Sum(dict):
    sum= 0
    i=0
    a=list(dict)
    while i<len(dict):
        sum= sum + dict[a[i]]
        i=i+1
    return sum
dict = {"p":1,"y":5,"t":10,"h":6,"o":3,"n":11}
print(Sum(dict))
# o/p:36
