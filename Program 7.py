# Program to find the sum of digits of a given number:

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    num //= 10
    sum += digit

print("Sum of digits:", sum)
