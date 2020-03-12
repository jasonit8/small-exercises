def isprime(number):
    if (type(number) != int) or (number < 2):
        return False
    elif number < 4:
        return True
    else:
        primes = [2]
        prime = 3
        while prime <= number**.5:
            primes += [prime] if all(prime % p > 0 for p in primes) else []
            prime += 1
        return all(number % p > 0 for p in primes)

# This program checks whether a number is prime or not.