# Q41.Write a Python program to filter the height and width of students, which are stored in a
# dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
# 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,66)}
i=0
b=list(a.values())
c=list(a.keys())
d={}
while i<len(a):
    j=0
    while j<len(b[i]):
        if b[i][j]>6.0 and b[i][j]>=70:
            d[c[i]]=b[i]
        j=j+1
    i=i+1
print(d)
