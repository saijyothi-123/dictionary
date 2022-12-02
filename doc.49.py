# Q49.Python: Access dictionary key’s element by index
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# physics
# math
# chemistry


a = {'physics': 80, 'math': 90, 'chemistry': 86}
b=list(a.keys())
i=0
while i<len(a):
    print(b[i])
    i=i+1