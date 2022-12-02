# Write a Python program to remove a key from a dictionary.


x = {'a':1,'b':2,'c':3,'d':4}
print(x)
if 'a' in x: 
    del x['a']
print(x)



a= {'a':1,'b':2,'c':3,'d':4}
print(a)
key=input("enter the key")
if key in a.keys(): 
    del a[key]
else:
    print("key is not in dict")
print(a)



x = {"name":"jyothi","age":22,"course":"python"}
print(x)
if 'age' in x: 
    del x['age']
print(x)


