def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


rangeBegin = int(input())
rangeEnd = int(input())

primeCount = 0
smallestPrime = None
largestPrime = None

for number in range(rangeBegin, rangeEnd + 1):
    if is_prime(number):
        primeCount += 1
        if smallestPrime is None:
            smallestPrime = number
        largestPrime = number
        

totalNumbers = rangeEnd - rangeBegin + 1
if primeCount == 0:
    percentageOfPrimes = 0.0
else:
   percentageOfPrimes = (primeCount / totalNumbers) * 100

if(primeCount is None):
    print(f'Number of primes: 0')
    print(f'Smallest prime: None')
    print(f'Largest prime: None')
    print(f'Percentage of numbers that are prime: {percentageOfPrimes}')
else:
    print(f"Number of primes: {primeCount}")
    print(f"Smallest prime: {smallestPrime}")
    print(f"Largest prime: {largestPrime}")
    print(f"Percentage of numbers that are prime: {percentageOfPrimes:.1f}")