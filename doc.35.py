# Write a Python program to count the number of items in a dictionary value that is a list.
# dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Sample output: 5

dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in dict:
    for j in dict[i]:
        if dict[i]:
            count+=1
print(count)


a = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
i=0
b=list(a.values())
# print(b)
while i<len(a):
    j=0
    while j<len(b[i]):
        if b[i]:
            count+=1
        j=j+1
    i=i+1
print(count)
