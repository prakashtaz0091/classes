# Exercise - 1
---
Programming is not just about typing code; it is first about understanding the problem, doing necessary rough work, figuring out the solution logic, writing clear steps (algorithms), and only then writing the code based on those steps.

Here are the core concepts you need to understand to solve your selected questions:

## 1. Number Classifier (Positive, Negative, Zero)
- To solve this, you must understand how numbers relate to zero on a number line.
- **Positive Numbers**: These are numbers greater than 0. They represent having something (like 5 apples) or moving forward. On a number line, they are to the right of zero.
- **Negative Numbers**: These are numbers less than 0. They represent owing something (like -5 dollars debt) or moving backward. On a number line, they are to the left of zero. They always have a minus sign (-).
- **Zero**: This is the neutral point. It is neither positive nor negative. It represents "nothing" or the starting line.
- **The Logic**: Your program needs to check: Is the number bigger than 0? Is it smaller than 0? Or is it exactly 0? Only one of these can be true.

## 2. Triangle Validity (Angles and Types)
- This question requires understanding the rules that make a shape a triangle and how to compare sides or angles.
- **The 180-Degree Rule**: In flat geometry, the three angles inside any triangle must add up to exactly 180 degrees. If the sum is 179 or 181, it is not a valid triangle; the lines would never meet to close the shape.
- **Equilateral Triangle**: "Equi" means equal. All three angles are exactly the same (which means they must all be 60 degrees).
- **Isosceles Triangle**: This type has at least two angles that are the same. (Note: An equilateral triangle is technically also isosceles, but in simple logic, we often check if exactly two match or if all three match first).
- **Scalene Triangle**: "Scalene" means no symmetry. None of the three angles are equal to each other.
- **The Logic**: First, add the three inputs. If the sum is not 180, stop (invalid). If it is 180, check: Are all three equal? If yes, Equilateral. If not, are any two equal? If yes, Isosceles. If neither, Scalene.

## 3. Multiplication Table (Repeated Addition)
- This concept turns multiplication into a loop of addition.
- **Multiplication Meaning**: Multiplying $5 \times 3$ is just adding 5, three times ($5 + 5 + 5$). A multiplication table is simply a list of these repeated additions for numbers 1 through 10.
- **The Multiplier (1 to 10)**: This is your counter. You start at 1, then go to 2, then 3, all the way to 10.
- **The Pattern**: For a chosen number (let's say 7), the table is:
```
7 x 1 = 7
7 x 2 = 14
...up to...
7 x 10 = 70
```
- **The Logic**: You need a loop that counts from 1 to 10. Inside the loop, you take the user's number and multiply it by the current count number, then print the result.

## 4. Sum of Evens (Filtering and Accumulating)
- This question teaches you how to pick specific items from a group and keep a running total.
- **Even Numbers**: An even number is any integer that can be divided by 2 with no remainder. Examples: 2, 4, 6, 8, 10. If you try to divide an odd number (like 5) by 2, you get a remainder (2.5 or 2 remainder 1).
- **The Range (1 to 50)**: This is your group of numbers to check. You must look at every single number from 1 up to 50.
- **Running Total (Accumulator)**: Imagine a bucket that starts empty (value 0). Every time you find an even number, you add it to the bucket. The bucket gets heavier (the total grows) step-by-step.
- **The Logic**: Start a total variable at 0. Loop through numbers 1 to 50. Inside the loop, ask: "Is this number divisible by 2?" If yes, add it to your total. If no, do nothing. After the loop finishes, print what is in the bucket.

## 5. Input Validation (Looping until Correct)
- This concept is about refusing to move forward until the user follows the rules.
- **Valid Range (1 to 10)**: This defines the "safe zone." Only numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 are allowed. Anything less than 1 or greater than 10 is "out of bounds."
- **The Infinite Wait**: A while loop can run forever if the condition is always true. Here, you want the loop to keep running while the input is invalid.
- **Breaking the Loop**: The break command is like an emergency exit. Once the user finally gives you a good number, you don't want to ask again. You use break to jump out of the loop immediately.
- **The Logic**: Start a loop that runs forever (or while the input is bad). Ask the user for a number. Check: Is it between 1 and 10? If no, print "Invalid" and the loop repeats automatically. If yes, print "Accepted" and hit the break button to stop the loop.
