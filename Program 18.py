# Program to find the first 100 prime numbers among 1000 numbers:

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in range(2, 1001) if is_prime(num)]
first_100_prime_numbers = prime_numbers[:100]
print(first_100_prime_numbers)






