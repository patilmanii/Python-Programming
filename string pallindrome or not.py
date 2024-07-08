string=input("Enter a String : ")
rev=""
for i in string:
    rev=i+rev
    
if string==rev:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
