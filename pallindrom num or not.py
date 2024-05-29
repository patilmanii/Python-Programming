#pallindrome num

def is_palindrome(number):
    num_str = str(number)
    
    reversed_str = num_str[::-1]
    
    return num_str == reversed_str

number = int(input("Enter a number: "))

if is_palindrome(number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
