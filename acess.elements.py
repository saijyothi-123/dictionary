d={}
d[0]="welcome"
d[1]="how","are","you"
d["name"]={"first":"indu","last":"harijana"}
print(d["name"])


d={}
d[0]="welcome"
d[1]="how","are","you"
d["name"]={"first":"indu","last":"harijana"}
print(d["name"]["first"])


d={}
d[0]="welcome"
d[1]="how","are","you"
d["name"]={"first":"indu","last":"harijana"}
print(d.get(1))