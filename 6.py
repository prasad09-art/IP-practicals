num = int(input ("enter a number :"))
original  = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("reversed number=", reverse)

if original == reverse:
    print("the number is a Palindrome.")
else:
    print("the number is not palindrome.")
