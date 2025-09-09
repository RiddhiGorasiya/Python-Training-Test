class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit

    def generate(self):
        a, b = 0, 1
        while a <= self.limit:
            yield a
            a, b = b, a + b

limit = 100
fib_gen = FibonacciGenerator(limit)

print(f"Fibonacci numbers up to {limit}:")
for num in fib_gen.generate():
    print(num)