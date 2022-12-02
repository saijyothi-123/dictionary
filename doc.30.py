# 30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary: {'S 001': ['Math', 'Science'], 'S 002': ['Math',
# 'English']}
# New dictionary: {'S001': ['Math', 'Science'], 'S002': ['Math',
# 'English']}


# my_dict = {'o n e': 1,'t w o': 2,'t h r e e': 3}

# new_dict = {key.replace(' ', ''): value for key, value in my_dict.items()}
# print(new_dict)

# # 👇️ {'one': 1, 'two': 2, 'three': 3}



# a= {'S 001': ['Math', 'Science'], 'S 002': ['Math','English']}
# b={}
# for i in a:
#     if "" in i:
#         c=i.replace(" ","")
#         b[c]=a[i]
# print(b)




# a= {'S 001': ['Math', 'Science'], 'S 002': ['Math','English']}
# b=list(a)
# print(b)
# d={}
# i=0
# while i<len(a):
#     if "" in b[i]:
#         c=b[i].replace(" ","")
#         d[c]=a[b[i]]
#     i=i+1
# print(d)



my_dict = {'a b c': [2, 3, 5],
           'b d e': [1, 8, 4],
           'c f g': [9, 0, 1]}

for key in my_dict:
    new_key = key.replace(' ', '')
    my_dict[new_key] = my_dict.pop(key)
print(my_dict)

