def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_num + 1) if is_prime[p]]
    return primes, set(primes)

def count_prime_pairs(N, primes, prime_set):
    if N < 4:
        return 0
    count = 0
    for p in primes:
        if p > N // 2:
            break
        if (N - p) in prime_set:
            count += 1
    return count

def main():
    input_numbers = list(map(int, input().split()))
    max_input = max(input_numbers)
    primes, prime_set = sieve_of_eratosthenes(max_input)
    
    results = [count_prime_pairs(N, primes, prime_set) for N in input_numbers]
    print(" ".join(map(str, results)))

main()