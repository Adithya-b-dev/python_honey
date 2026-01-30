
income=float(input("Enter your income"))

def income_tax(income):
    tax=0
    
    if income<=250000:
        tax=0
    elif income<=500000:
        tax=(income-250000)*0.05
    elif income<=1000000:
        tax=(250000*0.05)+(income-500000)*0.20
    else:
        tax=(250000*0.05)+((income-500000)*0.20)+income-1000000*0.30

    return tax
tax = income_tax(income)

print("Income Tax to be paid:", tax)
