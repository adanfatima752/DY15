def fibonacci_memo(n, cache=None, cache_limit=1000):
    """
    Calculates the n-th Fibonacci number using memoization. If the cache grows too large,
    it switches to an iterative method.
    
    :param n: The position in the Fibonacci sequence (0-indexed).
    :param cache: A dictionary for memoization. Defaults to None, initializing an empty cache.
    :param cache_limit: The maximum size of the cache before switching to an iterative method.
    :return: The n-th Fibonacci number.
    """
    # Initialize cache if not provided
    if cache is None:
        cache = {}

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Check if value is already in the cache
    if n in cache:
        return cache[n]

    # If cache is too large, use iterative approach
    if len(cache) > cache_limit:
        return fibonacci_iterative(n)

    # Recursive calculation with memoization
    cache[n] = fibonacci_memo(n - 1, cache, cache_limit) + fibonacci_memo(n - 2, cache, cache_limit)
    
    return cache[n]

def fibonacci_iterative(n):
    """
    Calculates the n-th Fibonacci number using an iterative approach.
    
    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The n-th Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

# Example usage:
n = 35
fibonacci_number = fibonacci_memo(n)
print(f"The {n}-th Fibonacci number is: {fibonacci_number}")
