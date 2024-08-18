def prime_sieve(limit):
    """
    Generator function that yields prime numbers up to the specified limit
    using an optimized version of the Sieve of Eratosthenes.
    
    :param limit: The upper limit up to which to generate prime numbers.
    :yield: The next prime number.
    """
    # Dictionary to store primes and their corresponding multiples
    sieve = {}
    cache = []
    
    for num in range(2, limit + 1):
        if num not in sieve:
            # num is a prime number, yield it and cache it
            yield num
            cache.append(num)
            
            # Mark multiples of the prime starting from num*num
            sieve[num * num] = [num]
        else:
            # num is not prime, it's a multiple of known primes
            for prime in sieve[num]:
                sieve.setdefault(prime + num, []).append(prime)
            del sieve[num]
    
    # Use cached primes for future calls if needed
    for cached_prime in cache:
        if cached_prime <= limit:
            yield cached_prime

# Example usage:
limit = 50
primes = list(prime_sieve(limit))
print(f"Prime numbers up to {limit}: {primes}")
