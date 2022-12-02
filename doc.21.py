# Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
# {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

a =[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
b=[]
i=0
while i<len(a):
    for j in a[i]:
        if a[i][j] not in b:
            b.append(a[i][j])
    i=i+1
print(b)


# print all unique values in a dictionary.
a = {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
list =[] 
for val in a.values(): 
  if val in list: 
    continue 
  else:
    list.append(val)

print (list)