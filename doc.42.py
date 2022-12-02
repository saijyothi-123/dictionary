# Q42.
# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False


a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
b=list(a.values())
c=list(a.keys())
i=0
while i<len(a):
    if b[i]==12:
        print ("True")
    elif b[i]==10:
        print("false")
    i=i+1


