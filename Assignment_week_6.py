# Soal Nomor 3
ON = lambda binary_func: lambda func: lambda val1: lambda val2: binary_func(func(val1))(func(val2))

EQUAL = lambda x: lambda y: x == y
LEN = len

result = ON(EQUAL)(LEN)("saya")("ganteng")
print(result)

# Soal nomor 4
Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

# Recursive sum function
SUM = Y(lambda f: lambda n: 0 if n == 0 else n + f(n - 1))

print(SUM(5))
print(SUM(10))

# Soal nomor 5
Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

# Helper functions
HEAD = lambda s: s[0] if s else ""
TAIL = lambda s: s[1:] if s else ""
LEN = lambda s: len(s)

# Reverse function using Y-Combinator
REVERSE = Y(lambda f: lambda s: "" if LEN(s) == 0 else f(TAIL(s)) + HEAD(s))

print(REVERSE("kenapa"))
print(REVERSE("abcde"))

#Soal nomor 6
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Map
halved = list(map(lambda x: round(x / 2), numbers))
#Filter
evens = list(filter(lambda x: x % 2 == 0, halved))
#Reduce
result = reduce(lambda acc, x: acc - x, evens)

print(f"Halved: {halved}")
print(f"Evens: {evens}")
print(f"Result: {result}")

#soal nomor 7
from functools import lru_cache
import time

#Tanpa Menggunakan cache
def fib_slow(n):
    if n < 2: 
        return n
    return fib_slow(n-1) + fib_slow(n-2)

#Menggunakan cache
@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2: 
        return n
    return fib_fast(n-1) + fib_fast(n-2)

#Testing performanya
start = time.time()
print(fib_slow(35))
print(f"Without cache: {time.time() - start:.4f}s")

start = time.time()
print(fib_fast(35))
print(f"With cache: {time.time() - start:.4f}s")

#Cek info cache-nya
print(fib_fast.cache_info())

#soal nomor 8
from itertools import chain

nested = [[5,6], [7], [0, 3, 4]]

flat = list(chain.from_iterable(nested))
print(flat)

#soal nomor 9
def cache(func):
    memo = {}
    
    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    
    return wrapper

@cache
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
print(fib(10))
