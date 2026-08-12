#for loop
#Input a number
num = int(input("enter a number:"))
factorial = 1
# calculate factorial
for i in range(1, num + 1):
    factorial = factorial * i
print("factorial =",factorial)    
