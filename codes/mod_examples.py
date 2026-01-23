import time
import os
from helpers import color_print, COLORS


# timer code
for timer in range(10, 0, -1):
    os.system("clear") # 1. clear existing number/timer
    # print(timer) # 2. show new timer value
    color_print(message=timer, color=COLORS["Bright Green"])
    time.sleep(1) # 3. wait for 1 sec
    
# timer code end
# clean screen/console/terminal before printing the message

os.system("clear")

color_print(message="HAPPY", color=COLORS["Bright Red"], end=" ")
color_print(message="NEW", color=COLORS["Bright Green"], end= " ")
color_print(message="YEAR", color=COLORS["Bright Yellow"], end=" ")

"""
THsi
is multi
line
comment
"""
