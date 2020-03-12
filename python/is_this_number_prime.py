isprime = lambda number: all(number % i > 0 for i in range(2,int(number**.5)+1))
# This program checks whether a number is prime or not.