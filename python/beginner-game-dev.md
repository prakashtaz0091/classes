# Python for Future Game Developers
### A Beginner Programming Course for Young Coders (Ages 12–13)

---

This course is designed to take a complete beginner from *"I've never written a line of code"* to *"I can write small programs and I'm ready to start making games in Godot."*

**Philosophy of this course:**
- We teach **procedural** programming first (no classes, no OOP). That comes later, in Godot.
- Every concept is tied to **games**: health bars, scores, coins, enemies, inventories.
- We prioritize **doing** over reading. Each lesson should have the student typing and running code within the first 5 minutes.
- Mistakes are **expected and good**. A big part of teaching here is normalizing errors as part of how programming works, not a sign of failure.
- Keep sessions short, energetic, and full of small wins.

**How to use this document:** Each lesson is self-contained. Read the Teacher Notes before the lesson — they contain the analogies and questions that make the concept click for a 12–13 year old. Live-code in front of the student whenever possible; don't just hand them finished code.

---

## Course Roadmap

| # | Lesson | Big Idea |
|---|--------|----------|
| 1 | What is Programming? | Computers follow exact instructions |
| 2 | Variables | Storing information (like a character's stats) |
| 3 | Input | Letting the player talk to the program |
| 4 | Basic Math | Updating scores, health, coins |
| 5 | Decisions (if/else) | The game reacts differently depending on what's true |
| 6 | Comparisons & Logic | Asking yes/no questions about the game state |
| 7 | Loops | Repeating actions without repeating code |
| 8 | Lists | Holding many things at once (inventory, enemies) |
| 9 | Functions | Reusable actions like `attack()` or `heal()` |
| 10 | Small Projects | Put it all together |

---

# Lesson 1: What is Programming?

## Objective
The student will understand what a program is, see what Python code looks like, run their first program, and use `print()` to display messages.

## Explanation

A **program** is just a list of exact instructions for a computer to follow, in order. The computer doesn't guess what you mean — it does *exactly* what you tell it, nothing more, nothing less.

Think about a video game: every time a character jumps, picks up a coin, or loses health, there's code behind it telling the computer exactly what to do.

**Python** is one of the languages we use to write these instructions. It's a great starting language because it reads almost like English.

The very first thing most programmers learn is how to make the computer **say something**. In Python, we use a command called `print()`.

```python
print("Hello, world!")
```

This tells Python: "Display the text Hello, world! on the screen." That's it. That's a real program.

## Example Code

```python
# This is a comment - Python ignores anything after a #
# Comments are notes for humans, not instructions for the computer

print("Hello, world!")
print("Welcome to your first program.")
print("You are now a programmer.")

# print() can also show numbers
print(100)

# You can print multiple things separated by commas
print("Score:", 100)
```

## Exercises

1. Run the example code above exactly as it is. See what happens.
2. Change the message in the first `print()` to say your own name.
3. Add a new line that prints your favorite game's name.
4. Print three lines that introduce a made-up game character (name, weapon, power).
5. Try removing one of the quotation marks from a `print()` line on purpose. What happens? Read the error message out loud.
6. Print a small "menu" like a game would show:
   ```
   1. Start Game
   2. Options
   3. Quit
   ```

## Challenge

Print a tiny "title screen" for a game you imagine, using at least 5 `print()` lines, including the game's name, a tagline, and a fake "Press Start" message — try to make it look like a banner using dashes or symbols, e.g. `print("==========")`.

## Common Mistakes

- **Forgetting quotation marks** around text: `print(Hello)` causes an error because Python thinks `Hello` is a variable name, not text.
- **Mismatched quotes**: starting with `"` and ending with `'`.
- **Capitalization matters**: `Print()` is not the same as `print()`. Python is case-sensitive.
- **Forgetting parentheses**: `print "Hello"` (this was valid in old Python 2, but not in the Python we use).

## Teacher Notes

- **Analogy**: A program is like a recipe. The computer is a very obedient but very literal chef — if the recipe says "add sugar" but doesn't say how much, the chef won't guess. Programming is about being precise.
- **Analogy**: Compare to a game's dialogue box — every piece of text a character says in a game had to be `print()`-ed (or its equivalent) by a programmer at some point.
- **Question to ask**: "If you were programming a game character to greet the player, what would you want it to say?" Let them write it before showing syntax.
- **Question to ask**: "What do you think happens if I misspell `print`?" Encourage them to guess before running it — this builds intuition for reading error messages without fear.
- Let the student break things on purpose. The error messages are not scary; they're clues.
- Keep this lesson **fast and fun** — the goal is the dopamine hit of "I made the computer do something."

---

# Lesson 2: Variables

## Objective
The student will understand what a variable is and use variables to store numbers, text (strings), and true/false values (booleans), using game-related examples.

## Explanation

A **variable** is a labeled box where you store information so you can use it later. Instead of typing the same value over and over, you give it a name.

In a game, almost everything is a variable: the player's name, their score, their health, how many coins they've collected.

```python
player_name = "Alex"
score = 0
health = 100
```

Here, `player_name`, `score`, and `health` are variables. The `=` sign doesn't mean "equals" like in math class — it means **"store this value in this box."**

Variables can hold different **types** of information:
- **Strings** — text, written in quotes: `"Alex"`, `"Dragon Sword"`
- **Numbers** — for counting and math: `100`, `3.5`
- **Booleans** — only two possible values: `True` or `False`. Great for yes/no game states like "is the player alive?"

```python
player_alive = True
has_key = False
```

## Example Code

```python
# Character stats stored as variables
player_name = "Nova"
health = 100
coins = 0
level = 1
is_alive = True

print(player_name)
print(health)
print(coins)
print(is_alive)

# You can change a variable's value any time
coins = 10
print(coins)

# You can combine variables and text using a comma in print()
print(player_name, "has", health, "health points")
```

## Exercises

1. Create variables for a game character: `name`, `health`, `level`, and `is_alive`. Print all four.
2. Create a variable called `weapon` and set it to a string like `"Sword"`. Print a sentence using it, like: `print(name, "is holding a", weapon)`.
3. Change `health` to a lower number (simulating taking damage) and print it again.
4. Make a `boolean` variable called `has_shield` and print it.
5. Create three variables for an enemy: `enemy_name`, `enemy_health`, `enemy_is_boss` (boolean).
6. Print a short "status report" using at least 4 variables in one sentence.

## Challenge

Create a full character sheet using at least 6 variables (name, health, level, coins, weapon, is_alive), then print it formatted like a game UI, for example:

```
=== CHARACTER SHEET ===
Name: Nova
Level: 1
Health: 100
Coins: 0
Weapon: Sword
Status: Alive
```

## Common Mistakes

- **Quotes vs. no quotes**: `health = 100` (number) vs `health = "100"` (text). These behave very differently later in math operations.
- **Variable names with spaces**: `player name = "Alex"` causes an error. Use underscores: `player_name`.
- **Starting a variable name with a number**: `1health` is invalid. Must start with a letter.
- **Forgetting variables can change**: Some students think a variable is locked forever once set.

## Teacher Notes

- **Analogy**: A variable is like a labeled chest in a game's inventory system. The label (`health`) is the box's name; the value (`100`) is what's inside. You can always open the chest and put something new inside.
- **Analogy**: Booleans are like a single light switch — only ON or OFF, nothing in between. "Is the player alive?" is either `True` or `False`, never "kind of."
- **Question to ask**: "If your character takes 20 damage, what would the code look like to update their health?" (Sets up Lesson 4 nicely.)
- **Question to ask**: "What other things in your favorite game could be stored as variables?" Let them brainstorm — ammo count, stamina, distance traveled, etc.
- Emphasize that **the variable name is chosen by us** — `health` could be called `hp` or `life`, it doesn't matter to Python, but clear names make code easier to read.

## Mini Challenge (End of Lesson)
Have the student design a **stat block** for an original game character entirely from imagination — name, class, 3 stats, 1 boolean — and print it nicely. This becomes "their character" that can be reused in later lessons.

---

# Lesson 3: Input

## Objective
The student will use `input()` to get information from the player and combine it with `print()` to create interactive, personalized output.

## Explanation

So far, our programs only do what we hard-coded. But real games **react to the player**. The `input()` command lets the program ask a question and wait for the player to type an answer.

```python
name = input("What is your name? ")
print("Welcome,", name)
```

`input()` always gives back a **string** (text), even if the player types a number. We'll deal with that detail more in the math lesson — for now, just know: if you want to do math with something the player typed, you'll need to convert it (covered next lesson).

## Example Code

```python
# Ask the player for their name and greet them
player_name = input("Enter your character's name: ")
print("Welcome to the dungeon,", player_name)

# Ask for a class choice
character_class = input("Choose your class (Warrior/Mage/Rogue): ")
print("You have chosen the", character_class, "class!")

# Combine multiple inputs into a short intro
favorite_weapon = input("What weapon do you want to start with? ")
print(player_name, "the", character_class, "draws their", favorite_weapon)
print("The adventure begins...")
```

## Exercises

1. Ask the player for their name and print a personalized welcome message.
2. Ask the player to choose a starting weapon, then print a sentence using it.
3. Ask for the player's favorite color and use it to describe their "magic aura" in a sentence.
4. Ask three separate questions (name, class, weapon) and print a short combined intro paragraph using all three answers.
5. Ask the player to name their pet/companion and print a sentence introducing the companion.

## Challenge

Build a tiny **"Character Creator"**: ask for name, class, weapon, and one boolean-style question answered as yes/no (e.g. "Do you want a shield? (yes/no)"), then print a full formatted character summary using all the answers, similar to the character sheet from Lesson 2 — but built from `input()` instead of hard-coded values.

## Common Mistakes

- **Forgetting input() returns text**: trying to do math directly on it before converting (we'll fix this next lesson — for now, just note it and move on).
- **Unclear prompts**: `input()` with no message inside the parentheses leaves the player confused about what to type. Always include a question string.
- **Mismatched variable names**: storing the answer in one variable name and then printing a different (unset) one.

## Teacher Notes

- **Analogy**: `input()` is like a game's text box where the player types their character's name before starting — the game pauses and waits until the player presses Enter.
- **Big moment**: This is usually the first lesson where the program feels alive — it's no longer just talking *at* the student, it's talking *with* them. Let them enjoy that.
- **Question to ask**: "What's the first thing a game usually asks you when you start a new save file?" (Name, difficulty, character type — all `input()`-style questions.)
- Encourage messy, fun answers — typing silly names is part of the fun and doesn't break anything.

---

# Lesson 4: Basic Math

## Objective
The student will use Python's math operators to update game values like score, health, and coins, and will learn to convert input text into numbers.

## Explanation

Games are full of math: adding score, subtracting health, multiplying damage, splitting loot evenly. Python's operators:

| Symbol | Meaning | Example | Result |
|--------|---------|---------|--------|
| `+` | Add | `5 + 3` | `8` |
| `-` | Subtract | `10 - 4` | `6` |
| `*` | Multiply | `3 * 4` | `12` |
| `/` | Divide | `10 / 2` | `5.0` |
| `%` | Remainder ("modulo") | `10 % 3` | `1` |
| `**` | Power (exponent) | `2 ** 3` | `8` |

`%` is special — it tells you what's "left over" after dividing. It's surprisingly useful in games (e.g., checking if a number is even, or making something happen "every 5th wave of enemies").

A common pattern in games is **updating a variable using itself**:

```python
score = 0
score = score + 10   # score is now 10
score += 10          # shortcut for the line above - score is now 20
```

`+=`, `-=`, `*=` are shortcuts that mean "update this variable based on its current value."

**Converting input to numbers**: Remember, `input()` gives text. To do math with it, wrap it in `int()` (whole numbers) or `float()` (decimal numbers):

```python
damage = input("Enter damage amount: ")   # this is text!
damage = int(damage)                      # now it's a number
health = health - damage
```

## Example Code

```python
health = 100
score = 0
coins = 5

# Player gets hit by an enemy
damage = 15
health = health - damage
print("Health after attack:", health)

# Player collects coins
coins += 10
print("Coins:", coins)

# Player earns points, doubled by a power-up
points_earned = 50
score += points_earned * 2
print("Score:", score)

# Using input with conversion
gold_found = input("How much gold did you find? ")
gold_found = int(gold_found)
coins = coins + gold_found
print("Total coins:", coins)

# Modulo example: every 3rd hit is a critical hit
hit_number = 6
if hit_number % 3 == 0:
    print("Critical hit!")
```
*(Don't worry about the `if` above yet — just notice the `%` in action. We'll fully cover `if` next lesson.)*

## Exercises

1. Start with `health = 100`. Subtract 30 damage, then print the new health.
2. Start with `score = 0`. Add 25 points three separate times using `+=`, printing the score after each.
3. A potion heals 20 HP, but health can't go above 100 conceptually — just add it for now (we'll cap it with `if` next lesson) and print the result.
4. Ask the player how many enemies they defeated using `input()`, convert it to a number, then calculate total score if each enemy is worth 15 points.
5. Use `%` to check whether a number of coins (try `17`) splits evenly between 2 players — print the leftover coin count.
6. Use `**` to calculate damage that doubles every level: if base damage is `5` and the level is `3`, what is `5 * (2 ** 3)`?

## Challenge

Write a "loot split" calculator: ask the player how much gold a party found and how many players are in the party (both via `input()`, converted to numbers). Calculate how much gold each player gets using `/`, and how much gold is left over using `%`. Print both results clearly.

## Common Mistakes

- **Forgetting to convert input()**: trying `damage = input(...)` then `health - damage` causes an error because you can't subtract text from a number.
- **Division always gives a decimal**: `/` returns a "float" even when it divides evenly (`10 / 2` is `5.0`, not `5`). This is fine for now — just flag it as something to notice, not fix.
- **Confusing `=` and `==`**: `health = 100` *sets* health. `health == 100` *asks* if health is 100 — that's a comparison, covered next lesson.
- **Order of operations confusion**: `2 + 3 * 4` follows normal math rules (multiplication first) — remind them parentheses can clarify: `(2 + 3) * 4`.

## Teacher Notes

- **Analogy**: `+=` is like a potion that adds to your health bar instead of replacing it — the old value isn't thrown away, it's built upon.
- **Analogy for `%`**: Think of a clock. After 12, it loops back to 1. `13 % 12` gives `1`, just like 13:00 is 1 o'clock. Great for "every Nth event" logic in games (every 5th enemy is a boss, etc.)
- **Question to ask**: "If your character has 100 health and takes 35 damage twice, what should their health be? Let's write code to check our math."
- This is a great lesson for **prediction games**: ask the student to guess the output *before* running the code. It builds the habit of "tracing through" code mentally — a core programming skill.

---
# Lesson 5: Decisions (if / elif / else)

## Objective
The student will use `if`, `elif`, and `else` to make programs that react differently depending on game conditions, like whether a player has enough coins or is still alive.

## Explanation

Games constantly make decisions: *Is the player alive? Do they have enough coins to buy that sword? Is the level unlocked?*

In Python, we make decisions using `if`. If the condition is true, the code inside runs. If not, it's skipped.

```python
health = 0

if health <= 0:
    print("Game Over!")
```

Notice two important things:
1. The line ends with a **colon** `:`
2. The code that should run *if true* is **indented** (pushed in with a tab or 4 spaces)

We can add more branches with `elif` ("else if") and `else`:

```python
coins = 30
sword_price = 50

if coins >= sword_price:
    print("You bought the sword!")
elif coins >= 20:
    print("Not enough for the sword, but you could buy a potion.")
else:
    print("You can't afford anything yet.")
```

Python checks each condition **top to bottom** and runs the *first* one that's true, then stops checking the rest.

## Example Code

```python
health = 45
coins = 60
level_unlocked = False

# Check if player is alive
if health <= 0:
    print("You have been defeated.")
else:
    print("You are still standing with", health, "health.")

# Check if player can afford an item
item_price = 50
if coins >= item_price:
    print("Purchase successful!")
else:
    print("Not enough coins.")

# Check level access
if level_unlocked == True:
    print("Welcome to Level 2!")
else:
    print("Level 2 is locked. Find the key first.")

# elif chain - grading enemy difficulty by health
enemy_health = 250

if enemy_health > 200:
    print("This is a BOSS enemy!")
elif enemy_health > 50:
    print("This is a tough enemy.")
else:
    print("This is a weak enemy.")
```

## Exercises

1. Make a variable `health = 0` and print `"Game Over"` if health is 0 or below, otherwise print `"You're alive!"`.
2. Make a variable `coins = 25` and an item that costs `30`. Print whether the player can afford it.
3. Make a variable `has_key = False`. If `True`, print `"Door unlocked!"`, otherwise print `"The door is locked."`.
4. Create an `elif` chain that prints `"S Rank"`, `"A Rank"`, `"B Rank"`, or `"Try Again"` based on a `score` variable (you choose the cutoffs).
5. Ask the player for their health using `input()` (convert to a number!) and print a message warning them if health is below 20.
6. Combine ideas: ask for `coins` and an item `price` via input, and tell the player if they can buy it **and** how many coins they'll have left if so.

## Challenge

Build a tiny **"Shop System"**: the player has `coins = 80`. There are three items: Potion (`20`), Shield (`50`), Sword (`100`). Ask the player which item they want to buy (`input()`), then use `if`/`elif`/`else` to check if they can afford it, telling them the result and (if successful) their remaining coins.

## Common Mistakes

- **Forgetting the colon** `:` at the end of the `if` line.
- **Forgetting to indent** the code under `if` — Python uses indentation to know what's "inside" the if-block.
- **Using `=` instead of `==`** inside a condition (`if health = 0` is an error — that's assignment, not comparison).
- **Putting `else` with a condition**: `else` never takes a condition — only `if` and `elif` do.
- **Indentation mismatch**: mixing tabs and spaces causes confusing errors. Stick to one (most editors default to spaces).

## Teacher Notes

- **Analogy**: An `if` statement is like a fork in a choose-your-own-adventure book: "If you have the key, turn to page 12. Otherwise, turn to page 45." The game is always checking which page to "turn to" next.
- **Analogy**: Think of a bouncer at a club checking a condition: "If you're on the list, you get in. Else, you wait outside." Conditions gate access, just like a locked level.
- **Question to ask**: "What are three things in your favorite game that probably use an `if` statement behind the scenes?" (Low health warning, locked doors, "not enough gold" messages, etc.)
- **Question to ask**: "What happens if NONE of the conditions are true and there's no `else`?" (Nothing happens — good for testing their understanding that `else` is the safety net.)
- Live-code a simple branching dialogue tree together — it's a great visual, hands-on way to see decisions in action.

---

# Lesson 6: Comparisons & Logical Operators

## Objective
The student will use comparison operators to ask true/false questions about the game state, and combine multiple conditions using `and`, `or`, and `not`.

## Explanation

Last lesson we used `if` to make decisions, but we kept the conditions simple. Now let's look closely at how we **ask questions** in code.

**Comparison operators** always produce `True` or `False`:

| Symbol | Meaning | Example | Result |
|--------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `3 > 5` | `False` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `4 >= 5` | `False` |

**Logical operators** let us combine multiple conditions into one bigger question:

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be true | `health > 0 and coins >= 50` |
| `or` | At least one must be true | `has_key or has_password` |
| `not` | Flips True/False | `not is_alive` |

```python
health = 80
has_sword = True

# Player can attack only if alive AND armed
if health > 0 and has_sword:
    print("You attack!")

# Player can enter if they have a key OR know the password
has_key = False
knows_password = True
if has_key or knows_password:
    print("Door opens.")

# not flips a boolean
is_poisoned = False
if not is_poisoned:
    print("You feel fine.")
```

## Example Code

```python
health = 60
coins = 75
level = 4
has_shield = True
is_boss_fight = True

# Simple comparisons
print(health > 50)        # True
print(coins == 100)       # False
print(level >= 4)         # True

# Combining with 'and'
if health > 0 and coins >= 50:
    print("You're alive and rich enough to shop!")

# Combining with 'or'
if has_shield or level >= 5:
    print("You feel safe enough to fight.")

# Combining with 'not'
if not is_boss_fight:
    print("This is a normal enemy.")
else:
    print("Boss fight! Stay sharp.")

# Combining multiple operators together
if health > 0 and (coins >= 100 or has_shield):
    print("You're ready for the dungeon.")
```

## Exercises

1. Write 4 comparison statements using game variables of your choice (health, coins, level) and predict the True/False result *before* running them.
2. Create an `if` statement using `and`: the player can enter a boss room only if `health > 50` **and** `has_key == True`.
3. Create an `if` statement using `or`: the player wins a prize if `score >= 1000` **or** `time_left > 60`.
4. Use `not` to check if a player is **not** poisoned, and print a message accordingly.
5. Combine all three (`and`, `or`, `not`) in one condition that decides whether a "Secret Boss" appears.
6. Ask the player for their `health` and `coins` via input (converted to numbers) and tell them if they meet BOTH conditions to enter a special shop (e.g. health > 30 and coins >= 20).

## Challenge

Build a **"Door Puzzle"**: there are three doors. The player can only pick Door 1 if they have a torch AND a map. They can pick Door 2 if they have a key OR know a secret code. They can pick Door 3 only if they do **not** have the "cursed" status. Set up the booleans yourself, ask the player which door they want to try, and print whether they succeed.

## Common Mistakes

- **Confusing `=` and `==`** again — this trips up almost everyone at first. `=` stores, `==` asks.
- **Forgetting `and`/`or` need full conditions on both sides**: `if health > 0 and coins > 50` is correct; `if health and coins > 0` works in Python but doesn't ask what students think it asks — better to write both sides fully while learning.
- **Mixing up `and` vs `or` logic**: students sometimes use `and` when they mean "either is fine" (`or`), which can lock players out unintentionally.
- **Overcomplicating conditions**: encourage breaking very long conditions into smaller `if` statements when it gets confusing — readability matters more than cleverness at this stage.

## Teacher Notes

- **Analogy for `and`**: A treasure chest with TWO locks — you need BOTH keys, not just one.
- **Analogy for `or`**: A door with two paths — going through EITHER path gets you to the other side; you don't need both.
- **Analogy for `not`**: A "curse reversal" potion — it just flips whatever the current status is.
- **Question to ask**: "If I need a key AND a torch to open a door, but I only have the torch, can I open it?" (No — reinforces `and` requires both.)
- **Question to ask**: "What real game mechanic uses an 'or' condition?" (e.g., "press A or Space to jump.")
- This lesson pairs perfectly with truth-table style thinking — you can even draw a quick 2x2 grid on paper showing True/True, True/False, False/True, False/False for `and` vs `or` if the student likes visual structure.

---
# Lesson 7: Loops

## Objective
The student will use `while` and `for` loops (with `range()`) to repeat actions without copy-pasting code, using examples like countdowns, coin collection, and repeated attacks.

## Explanation

So far, if we wanted something to happen 5 times, we'd have to write the same line 5 times. Loops let the computer repeat instructions for us.

### `while` loops
A `while` loop keeps running **as long as a condition is true**:

```python
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Go!")
```

This is perfect for things that depend on a changing game state — like "keep attacking while the enemy's health is above 0."

**Careful**: if the condition never becomes false, you get an **infinite loop** that never stops! Always make sure something inside the loop is changing the condition.

### `for` loops with `range()`
A `for` loop is great when you know **how many times** something should repeat:

```python
for i in range(5):
    print("Collecting coin #", i)
```

`range(5)` generates the numbers `0, 1, 2, 3, 4` (5 numbers, starting at 0). We don't need to manually track a countdown variable — Python handles it.

```python
for i in range(1, 6):
    print(i)   # prints 1, 2, 3, 4, 5
```

`range(start, stop)` lets you control where counting begins and ends (it stops *before* reaching `stop`).

## Example Code

```python
# while loop: countdown before a battle starts
countdown = 3
while countdown > 0:
    print(countdown, "...")
    countdown -= 1
print("Battle Start!")

# while loop: attack until enemy is defeated
enemy_health = 30
attack_damage = 10

while enemy_health > 0:
    enemy_health -= attack_damage
    print("You attack! Enemy health is now", enemy_health)
print("Enemy defeated!")

# for loop: collecting 5 coins
for coin_number in range(1, 6):
    print("Collected coin", coin_number)

# for loop: simulate 4 turns of combat
for turn in range(1, 5):
    print("Turn", turn, ": You swing your sword!")
```

## Exercises

1. Write a `while` loop that counts down from 10 to 1, then prints `"Liftoff!"`.
2. Write a `for` loop using `range(5)` that prints `"Coin collected!"` five times.
3. Write a `while` loop that reduces an enemy's health (starting at `50`, losing `15` per hit) until it reaches 0 or below, printing the health each time.
4. Write a `for` loop using `range(1, 11)` that prints each number — then add an `if` inside the loop that prints `"Bonus round!"` only when the number is divisible by 5 (hint: use `%`).
5. Simulate collecting coins in a `for` loop from `range(1, 8)`, keeping a running total with a variable that starts at `0` and updates each loop using `+=`.
6. Write a `while` loop that keeps asking the player to `input()` a password until they type the correct one (e.g. `"open sesame"`).

## Challenge

Simulate a full **mini battle**: the player has `health = 100` and the enemy has `enemy_health = 100`. Use a `while` loop that continues **as long as both** the player and the enemy have health above 0. Each loop, subtract a fixed damage amount from each side and print both health totals. When the loop ends, check who is still alive (`> 0`) and print who won.

## Common Mistakes

- **Infinite loops**: forgetting to update the loop's condition variable inside a `while` loop (e.g., forgetting `countdown -= 1`). If the program seems frozen, that's usually why — teach the student to recognize this and stop the program (often Ctrl+C, or the IDE's stop button).
- **Off-by-one confusion with `range()`**: forgetting that `range(5)` goes from `0` to `4`, not `1` to `5`.
- **Indentation issues inside loops**, same as with `if` statements.
- **Re-initializing variables inside the loop by accident**, resetting progress instead of accumulating it (e.g. putting `coins = 0` *inside* the loop instead of before it).

## Teacher Notes

- **Analogy**: A `while` loop is like a boss fight that keeps going "while the boss still has health" — nobody knows exactly how many hits it'll take, just that it ends when health hits 0.
- **Analogy**: A `for` loop with `range()` is like a wave-based enemy spawner that says "spawn exactly 5 enemies," — you know the exact number ahead of time.
- **Question to ask**: "What's something in a game that happens a *known* number of times?" (for loop) "What's something that happens *until a condition changes*?" (while loop) This distinction is the heart of the lesson.
- **Demonstrate an infinite loop on purpose** (in a safe, controlled way) so the student sees what it looks like and learns how to stop it. This demystifies a very common beginner fear.
- Loops are often where things start to feel like "real programming" — celebrate this milestone.

---

# Lesson 8: Lists

## Objective
The student will create lists, access and change items inside them, add and remove items, and loop through them — using examples like inventory, weapons, and high scores.

## Explanation

A **list** is a single variable that holds many values in order — perfect for an inventory, a party of characters, or a leaderboard.

```python
inventory = ["Sword", "Shield", "Potion"]
```

Each item has a **position**, called an **index**, starting at `0`:

| Index | 0 | 1 | 2 |
|-------|---|---|---|
| Item | "Sword" | "Shield" | "Potion" |

```python
print(inventory[0])   # "Sword"
print(inventory[2])   # "Potion"
```

**Adding items** — use `.append()`:
```python
inventory.append("Bow")
```

**Removing items** — use `.remove()`:
```python
inventory.remove("Shield")
```

**Changing an item** by index:
```python
inventory[0] = "Magic Sword"
```

**Looping through a list** — use a `for` loop:
```python
for item in inventory:
    print(item)
```

You can also check a list's length with `len()`:
```python
print(len(inventory))   # how many items are in the list
```

## Example Code

```python
# Player's inventory
inventory = ["Sword", "Shield", "Potion"]
print(inventory)

# Access specific items by index
print("First item:", inventory[0])
print("Last item:", inventory[2])

# Add a new item
inventory.append("Bow")
print("After adding bow:", inventory)

# Remove an item
inventory.remove("Shield")
print("After removing shield:", inventory)

# Loop through the inventory
for item in inventory:
    print("You have:", item)

# A list of enemies
enemies = ["Goblin", "Skeleton", "Dragon"]
for enemy in enemies:
    print("A wild", enemy, "appears!")

# A list of high scores
high_scores = [950, 870, 800, 650]
print("Top score:", high_scores[0])
print("Number of scores recorded:", len(high_scores))

# Adding a new high score
high_scores.append(1000)
print(high_scores)
```

## Exercises

1. Create a list called `weapons` with at least 4 weapon names. Print the whole list, then print just the first and last items.
2. Add a new weapon to the list using `.append()` and print the updated list.
3. Remove one weapon using `.remove()` and print the updated list.
4. Create a list called `enemies` and loop through it with a `for` loop, printing `"A wild [enemy] appears!"` for each one.
5. Create a list of high scores. Use `len()` to print how many scores are recorded.
6. Change the value at index `0` of any list directly (e.g. `weapons[0] = "Magic Staff"`) and print the result.
7. Combine a `for` loop and an `if` statement: loop through a list of enemy health values and print `"Boss!"` if the health is above `100`, otherwise print `"Normal enemy."`

## Challenge

Build an **Inventory Manager**: start with an empty list `inventory = []`. Use `input()` in a loop (you can use a `for` loop with a fixed number of turns, like `range(5)`) to let the player add 5 items one at a time using `.append()`. After the loop, print the full inventory and how many items it contains using `len()`.

## Common Mistakes

- **Index out of range**: trying to access `inventory[5]` in a list that only has 3 items causes an error. Remind them indexes start at `0`.
- **Forgetting `.append()` needs parentheses** and the new item inside them: `inventory.append "Bow"` is invalid — must be `inventory.append("Bow")`.
- **Trying to remove an item that doesn't exist** in the list (e.g. misspelled) causes an error.
- **Confusing the item's value with its index**: `inventory.remove(0)` tries to remove the *value* `0` from the list, not the item *at position* `0`. (That's a subtlety worth mentioning if it comes up.)

## Teacher Notes

- **Analogy**: A list is exactly like an inventory bag in a game — slots in order, items you can add, remove, or rearrange.
- **Analogy**: The index is like a numbered shelf in that bag — slot 0 is the first shelf, not the "zeroth" shelf in a confusing sense, just "where counting starts" in programming.
- **Question to ask**: "If your inventory bag has 3 items, what's the index of the last one?" (Index 2, not 3 — reinforces zero-based counting.)
- **Question to ask**: "What in your favorite game is basically a list?" (Inventory, party members, quest log, leaderboard, skill tree options.)
- This is a great lesson to bring in a **visual diagram** — draw boxes in a row, numbered 0, 1, 2... and physically point to which box is being accessed, appended, or removed.

---
# Lesson 9: Functions

## Objective
The student will understand why functions exist, create their own simple functions with parameters and return values, using examples like `attack()`, `heal()`, and `calculate_score()`.

## Explanation

By now, the student has probably written some code that repeats similar ideas — like printing a battle message every time damage happens. A **function** lets us package up a set of instructions and give it a name, so we can reuse it any time, just by calling that name.

```python
def attack():
    print("You swing your sword!")
    print("The enemy takes damage.")

attack()       # calling the function runs the code inside it
attack()       # we can call it again without rewriting anything
```

`def` means "define a function." The function's name follows, then parentheses, then a colon. Everything indented underneath is the function's code.

### Parameters — giving functions information

Functions become much more powerful when we can pass them information:

```python
def attack(weapon):
    print("You attack with your", weapon, "!")

attack("Sword")
attack("Bow")
```

`weapon` is a **parameter** — a placeholder for whatever value gets passed in when the function is called.

### Return values — getting information back

Sometimes we want a function to calculate something and **give us back** a result, instead of just printing:

```python
def calculate_score(enemies_defeated):
    return enemies_defeated * 10

total = calculate_score(5)
print(total)   # 50
```

`return` sends a value back out of the function, which we can then store in a variable or use elsewhere — unlike `print()`, which just displays something and doesn't give the value back to use later.

## Example Code

```python
# A simple function with no parameters
def cheer():
    print("You leveled up! Great job!")

cheer()

# A function with one parameter
def heal(amount):
    print("You healed for", amount, "HP!")

heal(20)
heal(50)

# A function with a parameter AND a return value
def calculate_damage(base_damage, multiplier):
    return base_damage * multiplier

critical_hit = calculate_damage(10, 3)
print("Critical hit damage:", critical_hit)

# Using a function's result inside game logic
health = 100
damage_taken = calculate_damage(5, 2)
health -= damage_taken
print("Health after attack:", health)

# A function that uses an if statement inside it
def check_status(health):
    if health <= 0:
        return "Defeated"
    elif health < 30:
        return "Critical condition"
    else:
        return "Healthy"

print(check_status(80))
print(check_status(10))
print(check_status(0))
```

## Exercises

1. Write a function called `greet_player()` that prints a welcome message. Call it twice.
2. Write a function called `heal(amount)` that prints a healing message using the parameter. Call it with three different amounts.
3. Write a function called `take_damage(current_health, damage)` that returns the new health after subtracting damage. Store and print the result.
4. Write a function called `calculate_score(coins, enemies_defeated)` that returns a total score (you decide the formula, e.g. `coins * 5 + enemies_defeated * 20`).
5. Write a function called `is_alive(health)` that returns `True` if health is above 0, and `False` otherwise. Test it with a few different values.
6. Write a function called `level_up_message(level)` that returns a different string depending on the level (use `if`/`elif`/`else` inside the function).

## Challenge

Write three functions that work together to simulate one round of combat:
- `attack(damage)` → prints an attack message and returns the damage dealt.
- `apply_damage(health, damage)` → returns the new health after damage.
- `check_status(health)` → returns "Alive" or "Defeated" depending on health.

Then, write a few lines of code *outside* the functions that uses all three together: simulate an attack, apply the damage to a starting health of `100`, and print the final status.

## Common Mistakes

- **Forgetting `return`** and expecting the function's result to "just work" — without `return`, a function gives back `None`, and using that in calculations causes confusing errors.
- **Confusing `print()` inside a function with `return`**: printing shows something on screen, but doesn't let other code *use* the value afterward.
- **Forgetting to call the function**: defining `def attack():` but never writing `attack()` means the code inside never actually runs.
- **Indentation errors**: forgetting to indent the function's body under the `def` line.
- **Mismatched parameter count**: calling `heal(20, 30)` when the function was only defined with one parameter.

## Teacher Notes

- **Analogy**: A function is like a special move in a game — you only have to "program" the special move once, then you can use it (call it) as many times as you want during the fight.
- **Analogy for parameters**: Think of a function like a vending machine slot — you put something in (the parameter), and the machine does something based on what you gave it.
- **Analogy for return values**: `return` is like a vending machine handing you back a snack — `print()` is more like a machine just showing a message on a screen without actually giving you anything to hold.
- **Question to ask**: "If I wanted my character to be able to attack 100 times in a game, would I want to write the attack code 100 times, or just once?" (This is the entire motivation for functions in one question.)
- **Question to ask**: "What's the difference between a function that *prints* a result and one that *returns* a result?" Encourage experimenting with both to feel the difference directly.
- This is one of the most important conceptual leaps in the whole course — functions are the bridge to thinking in reusable, modular pieces, which is exactly how Godot's own built-in functions (like `move_and_slide()`) will feel later.

---

# Lesson 10: Small Projects

## Objective
The student will combine everything learned so far — variables, input, math, decisions, comparisons, loops, lists, and functions — to build complete, working mini programs from start to finish.

## How to Run This Lesson

This is less of a single "lesson" and more of a **project arc** — plan for **several sessions** here, picking projects in order of difficulty. Each project below lists which earlier concepts it reinforces, a suggested starter structure (not a full solution — let the student build it), extension ideas, and teacher notes specific to that project.

**General teaching approach for this whole lesson:**
- Resist the urge to write the code for the student. Ask guiding questions instead ("What variable would track the player's guesses?").
- Let the student get something working end-to-end first, *then* improve it — a clunky working program beats a perfect unfinished one.
- After each project, ask: *"What part of this used something we learned in Lesson ___?"* This builds the connection between isolated concepts and real programs.

---

### Project 1: Guess the Number

**Concepts reinforced**: variables, input, comparisons, loops, conditionals

**Idea**: The computer picks a secret number (use the `random` module, introduced here for the first time — it's the one exception allowed beyond core syntax). The player keeps guessing until they get it right, with hints like "Too high!" or "Too low!"

**Starter structure** (a skeleton, not the full solution):
```python
import random

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = input("Guess the number (1-100): ")
    guess = int(guess)

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it!")
```

**Extension ideas**: Count how many guesses it took using a variable that increases each loop; limit the player to a maximum number of attempts.

**Teacher Notes**: This is a great first project because the `while` loop's purpose feels obvious immediately — "keep guessing until correct" is intuitive. Introduce `random.randint(a, b)` simply as "Python's way of rolling a die between two numbers."

---

### Project 2: Simple Calculator

**Concepts reinforced**: input, math operators, functions, decisions

**Idea**: Ask the player for two numbers and an operation (`+`, `-`, `*`, `/`), then perform the calculation and print the result.

**Starter structure**:
```python
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

result = calculate(a, b, op)
print("Result:", result)
```

**Extension ideas**: Add `%` and `**` as operations; loop so the player can do multiple calculations before quitting (e.g., type "quit" to stop).

**Teacher Notes**: This reinforces that functions can return different things from different `if` branches — a subtle but important idea for game logic later (e.g., a function that decides loot drops).

---

### Project 3: Rock, Paper, Scissors

**Concepts reinforced**: input, conditionals, comparisons, logical operators, `random`, loops

**Idea**: The player chooses rock, paper, or scissors; the computer picks randomly; the program decides the winner.

**Starter structure**:
```python
import random

choices = ["rock", "paper", "scissors"]
player_choice = input("Choose rock, paper, or scissors: ")
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("You lose!")
```

**Extension ideas**: Wrap the whole thing in a `while` loop so the player can play multiple rounds; keep score across rounds using variables.

**Teacher Notes**: The `elif` chain here is long, and that's intentional — it's a good moment to ask: "Is there a shorter way to write this?" without necessarily teaching a shorter way yet (e.g. it foreshadows what dictionaries or more advanced logic *could* simplify later, without requiring it now).

---

### Project 4: Text Adventure

**Concepts reinforced**: input, conditionals, booleans, functions, loops

**Idea**: A simple "choose your own path" story — the player makes choices that lead to different outcomes (find treasure, fall in a trap, escape a monster).

**Starter structure**:
```python
def start_adventure():
    print("You stand before two doors.")
    choice = input("Do you go LEFT or RIGHT? ").lower()

    if choice == "left":
        print("You find a treasure chest!")
    elif choice == "right":
        print("A monster jumps out! You run away.")
    else:
        print("You hesitate too long and the floor collapses!")

start_adventure()
```

**Extension ideas**: Chain multiple decision points together (after the first choice, present a second); track an `inventory` list that updates based on choices; track `health` that can reach 0 and end the game.

**Teacher Notes**: This is a great showcase project for parents/family — it feels like a "real game" despite using only concepts already taught. Encourage creativity in the story over code complexity.

---

### Project 5: Mini RPG Battle Simulator

**Concepts reinforced**: variables, functions, loops, lists, conditionals, comparisons

**Idea**: A simplified turn-based battle between the player and an enemy, using stats and functions built across the whole course.

**Starter structure**:
```python
def attack(name, damage):
    print(name, "attacks for", damage, "damage!")
    return damage

player_health = 100
enemy_health = 80

while player_health > 0 and enemy_health > 0:
    enemy_health -= attack("Player", 15)
    if enemy_health <= 0:
        print("Enemy defeated! You win!")
        break
    player_health -= attack("Enemy", 10)
    if player_health <= 0:
        print("You were defeated...")
        break

    print("Player HP:", player_health, "| Enemy HP:", enemy_health)
```
*(Note: `break` immediately exits a loop. It's a tiny, intuitive addition worth showing here in context — "stop the battle loop right now because someone already won.")*

**Extension ideas**: Add a list of multiple enemies the player must defeat in sequence; add an inventory of potions the player can use mid-battle; add random variation to damage using `random.randint()`.

**Teacher Notes**: This project is the closest thing to an actual (very simple) game in the whole course — treat it as a milestone moment. It's also a natural bridge to Godot, where turn-based or real-time combat will use very similar logic, just with visuals attached.

---

### Project 6: Quiz Game

**Concepts reinforced**: lists, loops, conditionals, functions, variables (score tracking)

**Idea**: Ask the player a series of questions (stored in lists), track correct answers, and print a final score.

**Starter structure**:
```python
questions = ["What is 2 + 2?", "What is the capital of France?", "What color is the sky?"]
answers = ["4", "Paris", "Blue"]
score = 0

for i in range(len(questions)):
    player_answer = input(questions[i] + " ")
    if player_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The answer was", answers[i])

print("Final score:", score, "out of", len(questions))
```

**Extension ideas**: Add a timer-style scoring bonus (e.g., extra points if answered within a guessed "fast" category); randomize question order using `random.shuffle()`.

**Teacher Notes**: This project is an excellent showcase of **parallel lists** (questions and answers matching by index) — a subtle but powerful idea. Ask the student: "Why does the order of the answers list matter so much?"

---

### Project 7: Inventory Simulator

**Concepts reinforced**: lists, functions, loops, conditionals

**Idea**: Build a small menu-driven program letting the player add items, remove items, and view their inventory, using a loop that keeps the "menu" running until they choose to quit.

**Starter structure**:
```python
inventory = []

def show_menu():
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View inventory")
    print("4. Quit")

running = True
while running:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Item to add: ")
        inventory.append(item)
    elif choice == "2":
        item = input("Item to remove: ")
        if item in inventory:
            inventory.remove(item)
        else:
            print("You don't have that item.")
    elif choice == "3":
        print("Inventory:", inventory)
    elif choice == "4":
        running = False
        print("Goodbye!")
    else:
        print("Invalid choice.")
```
*(`item in inventory` is a small, intuitive new piece of syntax — "is this value inside this list?" — worth a one-line explanation in the moment.)*

**Extension ideas**: Limit inventory to a maximum size; add item categories (weapons vs potions) using two separate lists.

**Teacher Notes**: This menu-loop pattern (`while running:` controlled by a boolean) is extremely common in real games and tools — point that out explicitly. It's a great "feels like a real app" moment.

---

### Project 8: Coin Collector Simulation

**Concepts reinforced**: loops, lists, functions, random, conditionals

**Idea**: Simulate a player moving through several "rooms," collecting coins randomly placed in each, with a running total and a final report.

**Starter structure**:
```python
import random

rooms = ["Cave", "Forest", "Tower", "Dungeon"]
total_coins = 0

for room in rooms:
    coins_found = random.randint(0, 20)
    total_coins += coins_found
    print("You explored the", room, "and found", coins_found, "coins!")

print("Total coins collected:", total_coins)
```

**Extension ideas**: Add a chance of finding a "trap" room that costs coins instead (`if random.random() < 0.2:`); add a list that records which rooms had traps for a final summary report.

**Teacher Notes**: This project is a nice gentle reintroduction to `random` combined with loops and accumulation — useful preparation for "random loot drop" systems that are extremely common in Godot game design.

---
# A Note on Object-Oriented Programming (OOP)

## Why OOP is Not in This Course

You may notice this course never introduces `class`, objects, or inheritance — even though Godot's GDScript leans on these ideas. **This is intentional.**

OOP is a way of *organizing* code — it's not a new kind of logic. Underneath every class and object, the actual thinking is still: variables, conditionals, loops, lists, and functions. If a student doesn't yet have those fundamentals comfortable and automatic, adding classes on top just adds confusing extra syntax without adding real understanding.

Trying to teach OOP to someone who hasn't internalized "what is a variable" or "why do functions exist" tends to produce **memorized syntax without real comprehension** — exactly what this course is trying to avoid.

## When OOP Becomes Useful

OOP becomes genuinely useful once a program has **many similar things that each need their own data and behavior** — for example:
- Multiple enemies, each with their own health, position, and attack pattern
- Multiple players or characters that share behavior but have different stats
- Game objects (coins, doors, power-ups) that all need to "do something" when the player touches them

At that point, writing one giant set of separate variables (`enemy1_health`, `enemy2_health`, `enemy3_health`...) becomes messy and repetitive — and that messiness is *exactly* the motivation that makes OOP click. Classes let you define "what every enemy has and can do" once, then create as many enemies as you like from that template.

## When to Introduce It

Introduce OOP **once the student is comfortable and fluent with**:
- Writing their own functions with parameters and return values, without help
- Using loops and lists together naturally (e.g., looping through a list of enemies)
- Completing at least 2–3 of the small projects in Lesson 10 independently

In practice, this usually means: **right around the start of Godot**, since Godot's own structure (`Node`, scenes, scripts attached to objects) will *naturally* reintroduce the idea of "a thing with its own data and behavior" in a much more visual, intuitive way than abstract Python classes would. Many students find OOP far easier to understand once they can *see* it (a Godot scene with a sprite and a script) rather than only reading about it in text.

**Suggested first OOP example, when the time comes**: rewrite the Mini RPG Battle Simulator project (Lesson 10) using a `Character` class with `health` and an `attack()` method. The student will already deeply understand *what* this code needs to do — the only new thing will be the `class` packaging around it.

---

# Recommended Teaching Schedule

This course works well at a relaxed, sustainable pace. Avoid rushing — confidence matters more than speed.

| Week | Lessons Covered | Sessions |
|------|------------------|----------|
| 1 | Lesson 1: What is Programming? | 1 session |
| 2 | Lesson 2: Variables | 1 session |
| 3 | Lesson 3: Input | 1 session |
| 4 | Lesson 4: Basic Math | 1–2 sessions |
| 5 | Lesson 5: Decisions | 1–2 sessions |
| 6 | Lesson 6: Comparisons & Logic | 1 session |
| 7 | Lesson 7: Loops | 2 sessions |
| 8 | Lesson 8: Lists | 1–2 sessions |
| 9 | Lesson 9: Functions | 2 sessions |
| 10–13 | Lesson 10: Small Projects | 1 project per session, ~8 sessions total |
| 14 | Capstone Project | 1–2 sessions |

**Pace guideline**: 1–2 sessions per week is ideal for this age group. This spreads the course over roughly **3–4 months**, which is enough time for ideas to settle without losing momentum.

## Estimated Duration Per Lesson

| Lesson | Estimated Time |
|--------|-----------------|
| 1. What is Programming? | 30–40 minutes |
| 2. Variables | 40–50 minutes |
| 3. Input | 30–40 minutes |
| 4. Basic Math | 45–60 minutes |
| 5. Decisions | 45–60 minutes |
| 6. Comparisons & Logic | 40–50 minutes |
| 7. Loops | 50–60 minutes (across 2 sessions) |
| 8. Lists | 50–60 minutes |
| 9. Functions | 60 minutes (across 2 sessions) |
| 10. Each Small Project | 40–60 minutes per project |
| Capstone | 60–90 minutes (across 1–2 sessions) |

*(These are guidelines, not strict limits — let curiosity extend a session if the student is engaged, and don't hesitate to split a lesson across two shorter sessions if focus is fading.)*

---

# Suggested Homework

Homework should be **light, optional-feeling, and low-pressure** — the goal is light repetition, not grinding.

| After Lesson | Suggested Homework |
|---------------|---------------------|
| 1 | Print a short "About Me" using 3–4 `print()` lines. |
| 2 | Create variables for 2 different game characters (not just one) and print both. |
| 3 | Build a tiny input-based "Would You Rather" game with 2 questions. |
| 4 | Calculate the total cost of 3 imaginary shop items using variables and math. |
| 5 | Write 3 `if`/`else` statements about anything from a favorite game. |
| 6 | Write one `and`, one `or`, and one `not` condition about made-up game stats. |
| 7 | Write a `for` loop that prints a multiplication table for any number 1–12. |
| 8 | Create a list of 5 favorite game characters and loop through printing them with a custom message. |
| 9 | Write 2 new functions not covered in class (e.g. `give_xp()`, `unlock_level()`). |
| 10 | Pick one small project and add ONE extension idea on your own. |

---

# Mini Revision Quizzes

These are meant to be **quick, casual, and verbal or written** — not formal tests. Use them as a 5-minute check-in at the start of the *next* lesson to refresh memory.

### Quiz: After Lesson 2 (Variables)
1. What symbol do we use to store a value in a variable?
2. What are the three types of values we learned about?
3. True or False: once you set a variable, you can never change it.

### Quiz: After Lesson 4 (Math)
1. What does `%` do?
2. What's the shortcut for `score = score + 10`?
3. What do you need to do before doing math on something from `input()`?

### Quiz: After Lesson 6 (Comparisons & Logic)
1. What's the difference between `=` and `==`?
2. If `health = 0`, what does `health > 0` evaluate to?
3. Give an example of when you'd use `and` instead of `or`.

### Quiz: After Lesson 8 (Lists)
1. What index is the *first* item in a list?
2. What command adds an item to a list?
3. What command tells you how many items are in a list?

### Quiz: After Lesson 9 (Functions)
1. What keyword do we use to send a value back out of a function?
2. What's the difference between `print()` and `return` inside a function?
3. Why are functions useful, in your own words?

---

# Final Capstone Project: Before Godot

## "The Last Stand" — A Complete Mini Text-Based RPG

This project pulls together **every single concept** from the course: variables, input, math, decisions, comparisons, logic, loops, lists, and functions.

### Project Brief (give this to the student as a creative brief, not a spec):

> Build a small text-based game called **The Last Stand**. The player creates a character, explores a few rooms collecting coins and items, may encounter enemies that must be fought using a battle system, and the game ends with either victory or defeat.

### Suggested Requirements (adjust freely based on student ability):

- [ ] Character creation using `input()` (name, starting stats)
- [ ] An inventory system using a **list**
- [ ] At least one **function** for attacking and one for healing
- [ ] A **loop** that lets the player explore multiple rooms (using a list of room names)
- [ ] **Random** chance of encountering an enemy in each room
- [ ] A battle system using a `while` loop that ends when either side's health reaches 0
- [ ] Decision points using `if`/`elif`/`else` (e.g., choosing to fight or flee)
- [ ] A final outcome message (win/lose) based on the character's ending health

### How to Run This With the Student

- Don't hand over a template. Instead, ask: *"What do we need first? What comes after that?"* and let them sketch an outline (even on paper) before coding.
- Expect this to take more than one sitting — that's normal and healthy for a capstone.
- Bugs will happen constantly here. This is the best moment in the whole course to model **calm debugging**: read the error, find the line, ask "what did I expect vs. what actually happened?"
- When finished, have the student **demo it** to a parent or sibling. This presentation moment is a huge confidence and motivation boost.

---

# "Ready for Godot?" Checklist

Before moving into Godot and GDScript, the student should be able to confidently say **yes** to most of these:

- [ ] I can read a short piece of code and explain what it does, step by step.
- [ ] I can create variables and know the difference between numbers, strings, and booleans.
- [ ] I can use `input()` to get information from a user.
- [ ] I can write and predict the result of basic math operations, including `%`.
- [ ] I can write `if` / `elif` / `else` statements to make decisions in code.
- [ ] I understand comparison operators (`==`, `<`, `>`, etc.) and logical operators (`and`, `or`, `not`).
- [ ] I can write a `while` loop and explain why it might run forever if I'm not careful.
- [ ] I can write a `for` loop using `range()`.
- [ ] I can create a list, access items by index, add items, remove items, and loop through it.
- [ ] I can write my own function with parameters and a return value.
- [ ] I have completed at least 3 small projects from Lesson 10 mostly on my own.
- [ ] I have completed the final capstone project ("The Last Stand").
- [ ] I feel comfortable reading error messages instead of being afraid of them.

**If most boxes are checked**, the student has a strong procedural programming foundation. They are ready to start exploring **Godot and GDScript**, where these exact same ideas (variables, conditionals, loops, functions) will reappear in a visual, game-native environment — and where `class`-like structures (via Godot's `Node` and scene system) will finally have a natural, hands-on context to be introduced.

**Welcome to game development.** 🎮
