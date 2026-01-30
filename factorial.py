i=1
fact =1

n=int(input('enter the no to find factorial of : '))

while i<=n:
    fact*=i
    i+=1

print("The factorial of ", n, "is", fact)
