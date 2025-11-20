# Real-Life + Fun Simulation Problems

All problems focus on:

- function behavior
- print vs return
- None checking
- if/else flow
- logic building

---

# 1. Candy Machine Simulator

A shop sells one candy for 10 rupees.

Write a function `buy_candy(money)` that:

- If the student gives 10 or more rupees → return `"Candy bought!"`
- If the money is less than 10 → print `"Not enough money"`

After calling the function:

- If the function returned something, print: `"Customer got the candy"`
- If nothing returned, print: `"No candy given"`

---

# 2. PUBG/FreeFire Health Booster

A player’s health is from 0 to 100.

Create a function `heal(health)`:

- Print `"Healing..."` every time the function runs
- If health is 100 or more → return nothing (returns None)
- Else → return `"Healed"`

After calling:

- If a value was returned → print `"Healing successful"`
- If it returned None → print `"Player already at full health"`

---

# 3. ATM Withdrawal Machine

Write a function `withdraw(balance, amount)`:

- If amount is greater than balance → print `"Insufficient balance"`
- Otherwise → return the new balance (balance - amount)

After calling:

- If it returned a value, print `"New balance: <value>"`
- If it didn’t return a value, print `"Transaction failed"`

---

# 4. School Attendance System

Create a function `mark_attendance(name, present)`:

- If `present` is True → return `"Marked Present"`
- If `present` is False → print `"Student is absent"`

After calling:

- If return value exists → print `"Attendance saved"`
- Else → print `"Attendance not saved"`

---

# 5. Mobile Battery Checker

Create a function `battery_status(level)`:

- If battery level is less than 20 → print `"Low battery"`
- Otherwise return `"Battery OK"`

After calling:

- Print `"Phone is functioning normally"` if a value is returned
- Otherwise print `"Phone battery warning"`

---

# 6. Restaurant Billing System

Create a function `calculate_bill(items)`
(Here, items is a list of item prices, for example [100, 50, 130])

The function should:

- If the list is empty → print `"No items selected"`
- Otherwise → return the total sum

After calling:

- If value returned → print `"Total bill is: <value>"`
- Otherwise → print `"Cannot generate bill"`

---

# 7. Weather Alert System

Create a function `check_temp(temp)`:

- If temp > 40 → print `"Too hot! Stay hydrated"`
- If temp < 0 → print `"Freezing cold! Dress warmly"`
- Otherwise → return `"Weather is normal"`

Then check if the function returned a value and display it.

---

# 8. Game XP Reward System

Create a function `reward(xp)`:

- If xp is greater than 1000 → return `"Level Up!"`
- Otherwise → print `"Earn more XP to level up"`

After calling:

- If return value exists → print `"Congratulations!"`
- Otherwise → print `"Try again"`

---

# 9. Delivery Service Simulator

A company only delivers within 50 km.

Write function `delivery_status(distance)`:

- If distance > 50 → print `"Delivery not available"`
- Else → return `"Delivery on the way"`

After calling:

- If return value exists → print `"Order placed successfully"`
- Else → print `"Order failed"`

---

# 10. Traffic Light System

Create a function `traffic(color)`:

- If color is `"red"` → print `"Stop"`
- If `"yellow"` → print `"Get ready"`
- If `"green"` → return `"Go"`

After calling:

- If value returned → print `"Drive"`
- Otherwise → print `"Wait"`

---

# 11. YouTube Video Loader

Create a function `load_video(speed)`:

- If speed < 2 Mbps → print `"Buffering..."`
- Else → return `"Playing Video"`

After calling:

- If returned → print `"Enjoy your video!"`
- Else → print `"Internet slow, please wait"`

---

# 12. Grocery Checkout

Create a function `checkout(amount)`:

- If amount is 0 → print `"Your cart is empty"`
- Else → return `"Payment successful"`

After calling:

- If returned → print `"Thank you for shopping!""`
- Else → print `"Could not checkout"`

---

# 13. Password Strength Checker

Create a function `check_password(password)`:

- If password length is less than 8 → print `"Weak password"`
- Else → return `"Strong password"`

After calling, print:

- `"Secure"` if returned value exists
- `"Please choose stronger password"` otherwise

---

# 14. Bus Booking System

Create a function `book_ticket(seats)`:

- If seats == 0 → print `"Sold out"`
- Else → return `"Ticket booked"`

After calling, check if the function returned something.

---

# 15. Nepali Mobile Recharge Simulator

Create a function `recharge(amount)`:

- If amount < 10 → print `"Minimum recharge is 10"`
- Else → return `"Recharge successful"`

After calling:

- If returned → print `"Balance Updated"`
- Else → print `"Recharge failed"`

---

# 16. Water Bottle Level Checker

Create a function `check_water(level)`:

- If level == 0 → print `"Bottle empty"`
- If level < 50 → print `"Need refill soon"`
- If level >= 50 → return `"Water level OK"`

Use return checking.

---

# 17. Movie Ticket Counter

Function `buy_ticket(age)`:

- If age < 5 → print `"Free entry"`
- If age between 5–17 → return `"Child ticket"`
- If age 18 or more → return `"Adult ticket"`

After calling, check if returned or only printed.

---

# 18. Laptop Battery Saver Mode

Function `power_mode(level)`:

- If level < 20 → print `"Switching to battery saver"`
- Else → return `"Normal mode"`

---

# 19. Fitness App Calories Counter

Function `calories_burned(minutes)`:

- If minutes == 0 → print `"Workout not started"`
- Else → return minutes \* 5

Check if returned.

---

# 20. Coffee Vending Machine

Function `make_coffee(coins)`:

- Coffee costs 15 rupees
- If coins < 15 → print `"Not enough coins"`
- Else → return `"Coffee ready"`

---
