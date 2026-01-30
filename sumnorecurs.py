arr = list(map(int, input("Enter the numbers in the array for sum: ").split()))

def sum1(lower,upper):
    if lower>upper:
        return 0

    else:
       return  lower+sum1(lower+1,upper)
