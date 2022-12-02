
# write the sum of the list from the dictionary

d={"a":[4,8,6],"b":[4,1],"c":[8,3]}
for i in d:
    g=d[i]
    l=[]
    sum=0
    j=0
    while j<len(g):
        sum=sum+g[j]
        j+=1
    l.append(sum)
    d[i]=l
print(d)


# for loop:
d={"a":[4,8,6],"b":[4,1],"c":[8,3]}
for i in d:
    sum=0
    for j in d[i]:
        sum+=j
    d[i]=[sum]
print(d)