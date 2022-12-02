# .Write a Python script to merge two Python dictionaries
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d = d1.copy()
# d.update(d2)
# print(d)


d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
a=list(d1)
b=list(d2)
d={}
i=0
while i<len(a):
    d[a[i]]=d1[a[i]]
    d[b[i]]=d2[b[i]]
    i=i+1
print(d)
    
    

d1={"Name":"Ram" , "Age":23}
d2={"City": "Salem", "Gender": "Male"}
res = d1.copy()
res.update(d2)
print(res)


a= {'x': 3, 'y' : 8, 'z': 5 }
b= {1: 8, 'x': 4, 2: 6}
merge_dic= {**a,**b}
print(merge_dic)




dic1= {'x': 2, 'y' : 8, 'C': 5 }
dic2= {'B': 8, 'y': 4, 2: 11}
dic1.update(dic2)
print(dic1)