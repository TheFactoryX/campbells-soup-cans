"""
Campbell's Soup Can #2430
Produced: 2026-02-25 18:13:50
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# [96m colored box with a Woody Allen‑style philosophical quote [0m
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

quote = ("I'm not afraid of death; I just don't want to be there when it happens. "
         "Also, I keep postponing pretending I understand the meaning of life.")

middle = f"{CYAN}* {YELLOW}{quote}{RESET} *{RESET}"
width = len(middle)
top = f"{CYAN}{'*'*width}{RESET}"

print(top)
print(middle)
print(top)