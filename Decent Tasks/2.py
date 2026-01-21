'''
Write a function that:

Stores results of expensive calculations

Returns cached result if available

cache = {}

def slow_square(n):
    ...
'''
cache = {}
import time

def slow_square(n):
    if n in cache:
        print("Returning cached result")
        return cache[n]

    print("Calculating...")
    time.sleep(2)
    result = n * n
    cache[n] = result
    return result
slow_square(4)
slow_square(4)
if cache is not None:
    print(cache)