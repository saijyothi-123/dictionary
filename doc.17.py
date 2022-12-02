# Write a Python program to sort a dictionary by key.

# ascending order(keys)

a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x=list(a)
print(x)
d={}
i=0
while i<len(a):
    x.sort()
    d[x[i]]=a[i]
    i=i+1
print(d)


# decending order(keys):
a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x=list(a)
d={}
i=0
while i<len(a):
    x.sort(reverse=True)
    d[x[i]]=a[x[i]]
    i=i+1
print(d)

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))
	

# key_value={}

# key_value[5] = 10      
# key_value[3] = 8
# key_value[6] = 77
# key_value[4] = 23
# key_value[2] = 9     
# key_value[1] = 43
 
# print("sorting on the basis of keys")

# for i in sorted(key_value) :
    # print ((i, key_value[i]), end =" ")

