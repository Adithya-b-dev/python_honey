s=input("Enter the string to be encrypted: ")
shift=int(input("Enter the no of terms to be shifted for encryption: "))
code=""

if s.isalpha():
    for char in s:

        if char.isupper():
            code+=chr((ord(char)-ord('A')+shift) %26 +ord('A') )
        else :
            code+=chr((ord(char)-ord('a')+shift) %26 +ord('a') )
            
    print("The encrypted version of ",s," is" ,code ")
else:
    print("Invalid input pyare deshvasiyo :)")
    
