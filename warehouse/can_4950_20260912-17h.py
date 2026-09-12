"""
Campbell's Soup Can #4950
Produced: 2026-09-12 17:10:59
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import time
import sys

quote = "I'm not afraid of death; I'm just not thrilled by the idea of being forgotten, and I also wish the afterlife had a better coffee selection."

YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

border = "*" * 60

print(YELLOW + BOLD + border + RESET)
sys.stdout.write(YELLOW + BOLD + "* " + RESET)
for char in quote:
    sys.stdout.write(CYAN + char + RESET)
    sys.stdout.flush()
    time.sleep(0.05)
sys.stdout.write(YELLOW + BOLD + " *" + RESET)
print()
print(YELLOW + BOLD + border + RESET)