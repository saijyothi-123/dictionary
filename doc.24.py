# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
# 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})




a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
b={}
for d in a:
    if d['item'] not in b:
        b[d['item']] = d['amount']
    else:
        b[d['item']] += d['amount'] 
print(b) 
