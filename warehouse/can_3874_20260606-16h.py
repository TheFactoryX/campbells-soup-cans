"""
Campbell's Soup Can #3874
Produced: 2026-06-06 16:19:39
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

blue = '\033[34m'
red = '\033[91m'
bold = '\033[1m'
reset = '\033[0m'

print(f"{blue}  _____________  {reset}")
print("| WOODY ALL'N |")
print("| QUOTE 42 |")
print(f"{blue}  _____________  {reset}\n")

quote = "Expectations are like a bad choice made at a bar: you know they’ll punch you in the face eventually, but what’s the alternative?"
print(f"{bold}{red}'{quote}'{reset}\n")

word = "Expectations"
length = len(word)
print(f"{red}{word}{reset}", end='\r')  # Initial bold red display
time.sleep(0.3)

# Blink animation (3 cycles)
for _ in range(3):
    print(f"{' ' * length}", end='\r')  # Clear with spaces
    time.sleep(0.3)
    print(f"{red}{word}{reset}", end='\r')  # Reappear in red
    time.sleep(0.3)

# Final static display
print(f"{reset}{bold}'{quote}'{reset}")