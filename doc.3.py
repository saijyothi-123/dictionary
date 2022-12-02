# Q3.Write a Python script to generate and print a dictionary that contains a number (between 1
# and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# for loop:
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 


# while loop:
n=int(input("Input a number "))
d = dict()
i=1
while i<=n:
    d[i]=i*i
    i=i+1
print(d) 
          