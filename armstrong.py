num=int(input("Enter the number "))
l=len(str(num))
armstrong=0
for i in str(num):
   armstrong+=int(i)**l

if armstrong==num:
    print("The number",num,"is armstrong")
else:
    print("The number",num,"is not armstrong")
    
