n=int(input("Enter the no of terms of fibonacci series to find:"))
a=0
b=1
x=0
i=1
print(a)
print(b)
while i<=(n-2):
    x=a+b
    print(x)
    a=b
    b=x
    i+=1
