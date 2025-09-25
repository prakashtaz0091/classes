# Practice Questions

---

## **1. Comprehensions (List, Dict, Set)**

1. **Generate a list of squares of numbers 1 to 10**
   **Steps:**

   - Start with a list of numbers from 1 to 10.
   - For each number, multiply it by itself.
   - Store the result in a new list.

2. **Generate a list of even numbers 1 to 20**
   **Steps:**

   - Loop through numbers 1 to 20.
   - Check if the number is divisible by 2.
   - If yes, include it in a new list.

3. **Convert a list of words into their lengths**

   ```python
   words = ["python", "java", "c", "golang"]
   ```

   **Steps:**

   - Loop through each word.
   - Count the number of characters in the word.
   - Store the lengths in a new list.

4. **Create a dictionary with word as key and length as value**
   **Steps:**

   - Loop through each word in the list.
   - Use word as key, length as value.
   - Store them in a dictionary.

5. **Create a set of unique vowels from `"comprehension"`**
   **Steps:**

   - Loop through each character of the string.
   - Check if the character is a vowel (`a, e, i, o, u`).
   - Add it to a set (duplicates automatically removed).

6. **Flatten nested list `[[1,2],[3,4],[5,6]]`**
   **Steps:**

   - Loop through each sublist.
   - Loop through each element in sublist.
   - Add element to a new flat list.

7. **Reverse each string in a list of names**
   **Steps:**

   - Loop through each string in the list.
   - Reverse it using slicing.
   - Store the reversed string in a new list.

---

## **2. Map and Filter**

1. **Use map to get squares of numbers**
   **Steps:**

   - Define a function or lambda to square a number.
   - Apply it to each element of the list using `map`.
   - Convert result to list.

2. **Use map to convert strings to uppercase**
   **Steps:**

   - Define a function or lambda to make string uppercase.
   - Apply to each string using `map`.
   - Convert result to list.

3. **Use filter to get even numbers**
   **Steps:**

   - Define a function or lambda to check if number % 2 == 0.
   - Apply `filter` on the list.
   - Convert result to list.

4. **Use filter to get words longer than 3 characters**
   **Steps:**

   - Define a function or lambda to check word length > 3.
   - Apply `filter` on the list.
   - Convert result to list.

5. **Combine map and filter: filter even numbers then square them**
   **Steps:**

   - First use `filter` to select even numbers.
   - Then use `map` to square each filtered number.
   - Convert result to list.

6. **Filter names starting with `"a"`**
   **Steps:**

   - Define function or lambda: check if string starts with `"a"`.
   - Apply `filter`.

7. **Add 10% tax to prices using map**
   **Steps:**

   - Define a function/lambda: multiply each price by 1.10.
   - Apply `map` to all prices.
   - Convert result to list.

---

## **3. Decorators (Basic Level)**

1. **Decorator to print start and end messages**
   **Steps:**

   - Define a decorator function that accepts another function.
   - Inside, print `"Function is starting..."`.
   - Call the original function.
   - Print `"Function has ended."`.

2. **Decorator to calculate execution time**
   **Steps:**

   - Use `time.time()` before and after calling the function.
   - Subtract start from end to get duration.
   - Print the duration.

3. **Decorator to check if user is logged in**
   **Steps:**

   - Use a global `is_logged_in` variable.
   - Inside decorator, check value.
   - If True → run function; else → print `"Access Denied"`.

4. **Decorator to convert output to uppercase**
   **Steps:**

   - Call the original function.
   - Capture its return value.
   - Convert string to uppercase.
   - Return the modified value.

5. **Decorator to print function arguments**
   **Steps:**

   - Inside decorator, capture `*args` and `**kwargs`.
   - Print them before calling function.
   - Call the original function.

---

## **4. Generators (Basic Level)**

1. **Generator for numbers 1 to 5**
   **Steps:**

   - Use `yield` inside a loop from 1 to 5.
   - Use a `for` loop to print generated values.

2. **Generator for squares of numbers 1 to 10**
   **Steps:**

   - Loop through numbers 1 to 10.
   - `yield` number squared.

3. **Generator for even numbers up to n**
   **Steps:**

   - Loop from 1 to n.
   - Check if number is even.
   - `yield` if even.

4. **Infinite sequence of natural numbers**
   **Steps:**

   - Use `while True:` loop.
   - Start from 1 and keep increasing.
   - `yield` each number.
   - Stop manually when testing.

5. **Generator for characters of a string**
   **Steps:**

   - Loop through string.
   - `yield` each character.

6. **Generator for Fibonacci sequence**
   **Steps:**

   - Initialize first two numbers: 0,1.
   - `yield` each number.
   - Calculate next = sum of last two.
   - Repeat up to n terms.
