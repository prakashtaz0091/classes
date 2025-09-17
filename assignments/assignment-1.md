# Formula-related Questions

---

**1. Area of a rectangle**

- Formula: `Area = length × width`
- Hints:

  1. Take input for length and width.
  2. Multiply them.
  3. Print the result.

---

**2. Area of a circle**

- Formula: `Area = 3.14 × radius × radius`
- Hints:

  1. Take input for radius.
  2. Multiply radius by itself, then by 3.14.
  3. Print area.

---

**3. Perimeter of a square**

- Formula: `Perimeter = 4 × side`
- Hints:

  1. Take input for side length.
  2. Multiply side by 4.
  3. Print perimeter.

---

**4. Simple Interest**

- Formula: `SI = (P × R × T) ÷ 100`
- Hints:

  1. Take inputs: principal, rate, time.
  2. Apply formula.
  3. Print result.

---

**5. Average of three numbers**

- Formula: `Average = (a + b + c) ÷ 3`
- Hints:

  1. Input three numbers.
  2. Add them.
  3. Divide by 3.
  4. Print average.

---

**6. Celsius to Fahrenheit**

- Formula: `F = (C × 9/5) + 32`
- Hints:

  1. Input Celsius.
  2. Multiply by 9, divide by 5, add 32.
  3. Print result.

---

**7. Fahrenheit to Celsius**

- Formula: `C = (F − 32) × 5/9`
- Hints:

  1. Input Fahrenheit.
  2. Subtract 32, multiply by 5, divide by 9.
  3. Print Celsius.

---

**8. Volume of a cube**

- Formula: `Volume = side³`
- Hints:

  1. Input side.
  2. Multiply side × side × side.
  3. Print volume.

---

**9. Perimeter of a triangle**

- Formula: `Perimeter = a + b + c`
- Hints:

  1. Input three sides.
  2. Add them.
  3. Print perimeter.

---

**10. Body Mass Index (BMI)**

- Formula: `BMI = weight ÷ (height × height)` (height in meters)
- Hints:

  1. Input weight, height.
  2. Multiply height × height.
  3. Divide weight by that value.
  4. Print BMI.

---

**11. Days into weeks and days**

- Formula: `Weeks = days ÷ 7`, `Remaining days = days % 7`
- Hints:

  1. Input total days.
  2. Divide by 7 (get weeks).
  3. Use remainder operator `%` for leftover days.
  4. Print both.

---

**12. Compound Interest**

- Formula: `CI = P × (1 + R/100)^T – P`
- Hints:

  1. Input principal, rate, time.
  2. Apply formula using power (`**`).
  3. Print CI.

---

**13. Square root**

- Formula: `√n = n ** 0.5`
- Hints:

  1. Input number.
  2. Raise to power 0.5.
  3. Print result.

---

**14. Swap two numbers (with temp)**

- Hints:

  1. Input two numbers.
  2. Store first in `temp`.
  3. Assign second to first.
  4. Assign `temp` to second.
  5. Print swapped numbers.

---

**15. Swap two numbers (without temp)**

- Hints:

  1. Input two numbers.
  2. Add them, store in first variable.
  3. Subtract appropriately to get second.
  4. Subtract again to get first.
  5. Print swapped numbers.

---

**16. Find remainder**

- Formula: `Remainder = dividend % divisor`
- Hints:

  1. Input two numbers.
  2. Use `%` operator.
  3. Print remainder.

---

**17. Speed**

- Formula: `Speed = distance ÷ time`
- Hints:

  1. Input distance, time.
  2. Divide distance by time.
  3. Print speed.

---

**18. Circumference of a circle**

- Formula: `Circumference = 2 × 3.14 × radius`
- Hints:

  1. Input radius.
  2. Multiply radius by 2 and 3.14.
  3. Print circumference.

---

**19. Minutes to hours and minutes**

- Formula: `Hours = minutes ÷ 60`, `Remaining = minutes % 60`
- Hints:

  1. Input minutes.
  2. Divide by 60 (get hours).
  3. Use remainder for extra minutes.
  4. Print both.

---

**20. Final price after discount**

- Formula: `Final Price = price − (price × discount / 100)`
- Hints:

  1. Input price, discount %.
  2. Calculate discount amount.
  3. Subtract from price.
  4. Print final price.

---

# Decision-related Questions

---

**21. Positive, negative, or zero**

- Condition: `if number > 0`, `elif number < 0`, `else` zero
- Hints:

  1. Input a number.
  2. Compare it with 0.
  3. Print whether it’s positive, negative, or zero.

---

**22. Even or odd**

- Condition: `if number % 2 == 0` → even, else odd
- Hints:

  1. Input a number.
  2. Find remainder when divided by 2.
  3. Decide based on remainder.

---

**23. Eligible to vote (age ≥ 18)**

- Condition: `if age >= 18` → eligible, else not
- Hints:

  1. Input age.
  2. Compare with 18.
  3. Print eligibility.

---

**24. Largest of three numbers**

- Condition: check `if a > b and a > c`, etc.
- Hints:

  1. Input three numbers.
  2. Compare each one.
  3. Print the largest.

---

**25. Smallest of three numbers**

- Condition: check `if a < b and a < c`, etc.
- Hints:

  1. Input three numbers.
  2. Compare each one.
  3. Print the smallest.

---

**26. Leap year**

- Condition: `(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)`
- Hints:

  1. Input year.
  2. Apply leap year rules.
  3. Print leap year or not.

---

**27. Age group classification**

- Condition:

  - `if age < 13 → child`
  - `elif age < 20 → teenager`
  - `else adult`

- Hints:

  1. Input age.
  2. Compare against ranges.
  3. Print group.

---

**28. Grade based on marks**

- Example ranges:

  - `90+ = A`, `80+ = B`, `70+ = C`, `60+ = D`, else `F`

- Hints:

  1. Input marks.
  2. Use multiple `if-elif` conditions.
  3. Print grade.

---

**29. Equal or not**

- Condition: `if num1 == num2`
- Hints:

  1. Input two numbers.
  2. Compare with `==`.
  3. Print equal or not.

---

**30. Vowel or consonant**

- Condition: check if character in `a, e, i, o, u`
- Hints:

  1. Input one character.
  2. Convert to lowercase.
  3. Check if it is in vowel list.
  4. Else print consonant.

---

**31. Multiple of 5**

- Condition: `if num % 5 == 0`
- Hints:

  1. Input number.
  2. Find remainder when divided by 5.
  3. Decide based on remainder.

---

**32. Divisible by both 3 and 7**

- Condition: `if num % 3 == 0 and num % 7 == 0`
- Hints:

  1. Input number.
  2. Check divisibility by 3 and 7.
  3. Print result.

---

**33. Greater of two numbers**

- Condition: `if a > b`
- Hints:

  1. Input two numbers.
  2. Compare them.
  3. Print which is greater.

---

**34. Income category**

- Example: `<20000 = low`, `20000–50000 = medium`, `>50000 = high`
- Hints:

  1. Input salary.
  2. Use range conditions.
  3. Print category.

---

**35. Senior citizen**

- Condition: `if age >= 60`
- Hints:

  1. Input age.
  2. Compare with 60.
  3. Print senior or not.

---

**36. Number within range 10–50**

- Condition: `if 10 <= num <= 50`
- Hints:

  1. Input number.
  2. Check range.
  3. Print result.

---

**37. Sum greater than 100**

- Condition: `if (a + b) > 100`
- Hints:

  1. Input two numbers.
  2. Add them.
  3. Compare with 100.
  4. Print result.

---

**38. Absolute difference less than 10**

- Condition: `if abs(a − b) < 10`
- Hints:

  1. Input two numbers.
  2. Find difference.
  3. Convert to positive (absolute).
  4. Compare with 10.

---

**39. Password check**

- Condition: `if input_password == stored_password`
- Hints:

  1. Define a stored password.
  2. Input another password.
  3. Compare them.
  4. Print match or not.

---

**40. Season by month**

- Example:

  - `12,1,2 → Winter`
  - `3,4,5 → Spring`
  - `6,7,8 → Summer`
  - `9,10,11 → Autumn`

- Hints:

  1. Input month number.
  2. Use conditions for ranges.
  3. Print season.

---
