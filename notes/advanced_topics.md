## 1. **Comprehensions**

Comprehensions provide a concise way to create collections like lists, sets, or dictionaries in a single line, instead of using loops.

- **List Comprehension**

  ```python
  nums = [1, 2, 3, 4, 5]
  squares = [x**2 for x in nums]
  # [1, 4, 9, 16, 25]
  ```

- **Set Comprehension**

  ```python
  nums = [1, 2, 2, 3, 4]
  unique_squares = {x**2 for x in nums}
  # {16, 1, 9, 4}
  ```

- **Dict Comprehension**

  ```python
  nums = [1, 2, 3]
  square_dict = {x: x**2 for x in nums}
  # {1: 1, 2: 4, 3: 9}
  ```

- **With Condition**

  ```python
  even_squares = [x**2 for x in nums if x % 2 == 0]
  # [4, 16]
  ```

👉 **Advantages:** shorter, readable, and efficient.
👉 **Avoid overuse:** nested comprehensions may reduce readability.

---

## **Lambda Functions**

Lambda functions are small, anonymous functions that are defined using the `lambda` keyword.

- **Basic Lambda Function**

  ```python
  add = lambda x, y: x + y
  print(add(2, 3))  # 5
  ```

- **Lambda with Multiple Arguments**

  ```python
  multiply = lambda x, y, z: x * y * z
  print(multiply(2, 3, 4))  # 24
  ```

- **Lambda with Default Arguments**

  ```python
  divide = lambda x, y=1: x / y
  print(divide(10))  # 10.0
  print(divide(10, 2))  # 5.0
  ```

👉 **Why useful?** Simplify complex logic, reduce code duplication, improve readability.

## 2. **Higher-Order Functions**

A higher-order function is a function that can take other functions as arguments or return them as results.

- **Example: `map`, `filter`, `reduce`**

  ```python
  nums = [1, 2, 3, 4]

  # map
  squares = list(map(lambda x: x**2, nums))
  # [1, 4, 9, 16]

  # filter
  evens = list(filter(lambda x: x % 2 == 0, nums))
  # [2, 4]

    # sorted
  sorted_nums = sorted(nums, reverse=True, key=lambda x: abs(x))
  # [1, 2, 3, 4]

  ```

- **Custom Higher-Order Function**

  ```python
  def apply_twice(func, x):
      return func(func(x))

  print(apply_twice(lambda n: n+2, 5))  # 9
  ```

👉 **Why useful?** Encourages functional programming style, improves reusability.

---

## 3. **Decorator**

A decorator is a function that modifies the behavior of another function without permanently changing it.
It is commonly used for logging, access control, timing, etc.

- **Basic Decorator**

  ```python
  def my_decorator(func):
      def wrapper():
          print("Before function call")
          func()
          print("After function call")
      return wrapper

  @my_decorator
  def say_hello():
      print("Hello!")

  say_hello()
  # Output:
  # Before function call
  # Hello!
  # After function call
  ```

- **Decorator with Arguments**

  ```python
  def repeat(n):
      def decorator(func):
          def wrapper(*args, **kwargs):
              for _ in range(n):
                  func(*args, **kwargs)
          return wrapper
      return decorator

  @repeat(3)
  def greet(name):
      print(f"Hello, {name}")

  greet("Alice")
  # Prints 3 times
  ```

👉 **Why use?** Clean way to add reusable functionality (e.g., logging, authentication).

---

## 4. **Generator**

Generators are functions that yield values one at a time using `yield` instead of returning all at once.
They are memory-efficient (lazy evaluation).

- **Basic Generator**

  ```python
  def my_gen():
      yield 1
      yield 2
      yield 3

  for val in my_gen():
      print(val)
  # 1, 2, 3
  ```

- **With Computation**

  ```python
  def count_up_to(n):
      i = 1
      while i <= n:
          yield i
          i += 1

  for num in count_up_to(5):
      print(num)
  ```

- **Generator Expression**

  ```python
  squares = (x**2 for x in range(5))
  print(next(squares))  # 0
  print(next(squares))  # 1
  ```

👉 **Why use?**

- Saves memory (doesn’t store entire list in memory).
- Useful for large data streams, pipelines.

# Infinite prime generator

```python
def primes_generator():
    """Infinite prime number generator (yields 2,3,5,7,11,...)."""
    primes = []       # discovered primes for trial-division
    candidate = 2
    while True:
        is_prime = True
        # only test divisors up to sqrt(candidate)
        limit = int(candidate**0.5) + 1
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 1 if candidate == 2 else 2  # skip even numbers after 2
```

```python
# Use the generator
prime_number = primes_generator()

# Print the first 10 prime numbers
for _ in range(10):
    print(next(prime_number))
```

# Infinite prime iterator (class)

```python
class PrimeIterator:
    """Infinite iterator that yields prime numbers (implements iterator protocol)."""
    def __init__(self):
        self.primes = []
        self._next = 2

    def __iter__(self):
        return self

    def __next__(self):
        candidate = self._next
        while True:
            is_prime = True
            limit = int(candidate**0.5) + 1
            for p in self.primes:
                if p > limit:
                    break
                if candidate % p == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(candidate)
                # prepare next candidate (skip even numbers after 2)
                self._next = candidate + (1 if candidate == 2 else 2)
                return candidate
            candidate += 1 if candidate == 2 else 2
```

```
# Use the iterator
prime_number = PrimeIterator()

# Print the first 10 prime numbers
for _ in range(10):
    print(next(prime_number))
```
