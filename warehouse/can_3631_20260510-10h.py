"""
Campbell's Soup Can #3631
Produced: 2026-05-10 10:37:50
Worker: Baidu: Qianfan-OCR-Fast (free) (baidu/qianfan-ocr-fast:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
from colorama import init, Fore, Style

# Initialize colorama for colored output in both Windows and Terminal
init()

# Create ASCII art at the top
ART = r"""
  ___
 /'_/ /\ \__. 
 `\_//`..` >)
     /'`.  
    ( o.o )
     \_"|/
"""

# Create a fun color palette using a rainbow
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def draw_line(color):
    print(f"{color}––––––––––––––––––––––––––––––––––––––––––––––––––––{Style.RESET_ALL}")

# Print the art with color variations
print(f"{ART.center(80)} {Style.RESET_ALL}")

# Draw a separator
draw_line(Fore.CYAN)

# Print a sequence of quotes with color animations
quotes = [
    "I'm sure the world was always a beautiful place but now I don't come out of the bathroom without the impression that Proust had a good one.",
    "Most of the enemies I have experienced in my lifetime have been caused by clarifying questions which their answers failed to warrant.",
    "If you don't like something, you're either not happy with it or can't take it. I can't take it."
]

indices = [0, 3, 1]  # Changing the quote order with insane neuroticism
time.sleep(1)

for char_num in range(80):
    for index in indices:
        if char_num < len(quotes[index]):
            color = colors[char_num % len(colors)]
            print(f"{color}{quotes[index][char_num]}{Style.RESET_ALL}", end="")
    print(f"{Fore.MAGENTA}@{Style.RESET_ALL}", end="")
    time.sleep(0.05)  # Slow down the animation

# Final quote that will appear slowly
print(f"{Fore.YELLOW}\nThe entire enterprise of constructing a defense mechanism, I admit, strikes me as splendidly\nmiserable. But who has the time?", Style.RESET_ALL)

# Wait before ending
time.sleep(2)