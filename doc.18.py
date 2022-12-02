# Write a Python program to get the maximum and minimum value in a dictionary


my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


# by using loop:
marks={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}
v = marks.values()
maxi = max(v)
mini = min(v)
print("Maximum :",maxi)
print("Minimum :",mini)


# by using while loop:
a={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}
i=0
b=list(a.values())
max=0
min=b[0]
while i<len(a):
    if b[i]>max:
        max=b[i]
    elif b[i]<min:
        min=b[i]
    i=i+1
print(max)
print(min)