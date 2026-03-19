s=input("Enter a string: ")
rev=''
for i in range(-1,-len(s)-1,-1):
    rev=rev+s[i]

if s.lower()==rev.lower():
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
