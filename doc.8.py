# Write a Python program to check whether a given key already exists in a dictionary


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
x=int(input("enter the key"))
is_key_present(x)




d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
a=int(input("enter the num"))
if a in d:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')





d = {"apple": 10, "ball": 20, "cool":"icecream", "nice":"nicey", "bangalore": "cool city"} 
a=input("enter the num")
if a in d:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')



