#while loop
#Intput a number
num = int(input("Enter a number: "))
factorial = 1
i = 1
#calculate factorial
while i <=num:
    factorial = factorial * i
    i = i + i
print("factorial =", factorial) 
