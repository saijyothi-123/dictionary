# Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Output:
# key value count
# 1 10 1
# 2 20 2
# 3 30 3
# 4 40 4
# 5 50 5
# 6 60 6


# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5, 'x': 2}

# for k, v in my_dict.items():
#     print('key:', k, 'value:', v, 'item:', (k, v))



# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key  value  count")
# for count, (key, value) in enumerate(dict_num.items(), 1):
#     print(key,'   ',value,'    ', count)



dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n = 0
print("Key    Value    Count")
for key, value in dict_num.items():
    n+=1
    print(" "+str(key)+"      "+str(value)+"        "+str(n))
    
    

# a= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# b=list(a)
# d=list(a.values())
# print(d)
# c=0
# print(b)
# i=0
# while i<len(a):
#     if b:
#         c+=1
#     i=i+1
# print(c)
    
