# Program to check if a given number is an Armstrong number:

num = int(input("Enter a number: "))
temp = num
sum = 0
order = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
