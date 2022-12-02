# Python: Print a dictionary line by line
# students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# Sample Output:
# Aex
# class : V
# rolld_id : 2
# Puja
# class : V
# roll_id : 3

students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for i in students:
    print(i)
    for j in students[i]:
        print(j,":",students[i][j])
        
        
        

a= {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}    
b=list(a.values())
c=list(a.keys())
i=0
while i<len(c):
    print(c[i])
    j=0
    x=list(b[i].values())
    y=list(b[i].keys())
    while j<len(x):
        print(y[j],":",x[j])
        j=j+1
    i=i+1

