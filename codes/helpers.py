
MENU = """
============================
Student Result System
1. Calculate Total
2. Calculate Percentage
3. Check Pass / Fail
4. Exit
============================
"""
PASS_MARKS = 40

def display_choices():
    print(MENU)

def ask_marks():
    m1 = int(input(" Math : "))
    m2 = int(input(" Science : "))
    m3 = int(input(" English : "))
    m4 = int(input(" Computer : "))
    m5 = int(input(" Nepali : "))
    return m1, m2, m3, m4, m5

def show_pass_fail(all_marks):
    for marks in all_marks:
        if marks < PASS_MARKS:
            print("Failed the exam")
            break
    else:
        print("Passed the exam")


COLORS = {
    # Foreground Colors (Text)
    'Black': '30m',
    'Red': '31m',
    'Green': '32m',
    'Yellow': '33m',
    'Blue': '34m',
    'Magenta': '35m',
    'Cyan': '36m',
    'Light Gray': '37m',
    
    # Bright (High-Intensity) Colors
    'Dark Gray': '90m',
    'Bright Red': '91m',
    'Bright Green': '92m',
    'Bright Yellow': '93m',
    'Bright Blue': '94m',
    'Bright Magenta': '95m',
    'Bright Cyan': '96m',
    'White': '97m'
}

def color_print(message, color, end="\n"):
    print(f"\033[{color}{message}\033[1m", end=end)
