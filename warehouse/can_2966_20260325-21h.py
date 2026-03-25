"""
Campbell's Soup Can #2966
Produced: 2026-03-25 21:53:44
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI escape codes
reset = '\033[0m'
blue = '\033[38;5;14m'
red = '\033[38;5;9m'
white = '\033[38;5;15m'
black_bg = '\033[48;5;0m'

# Animated thinking face
frames = ['(_.)', '(oO)', '(_<)']
for frame in frames:
    print(f'   {frame}\r', end='', flush=True)
    time.sleep(0.2)
print()

# Print the main content
print(f"{blue}                                   {reset}")
print(f"{blue}  PAPER MOON PHILOSOPHY           {reset}")
print(f"{blue}  --------------------------------{reset}")

# The quote box (red border, black background, white text)
border = red + '*' * 60 + reset + '\n'
inner_bg = black_bg + white

# Print the box content
print(border)
print(inner_bg + " *" + f" {red}{reset}"
      " I'm not afraid of love, I'm afraid of marriage. Not because of the money   "
      " {blue}{reset}"
      " — spending eternity with someone is like getting stuck sweating\n"
      f" {white}  in a New York apartment without air conditioning*{reset} *\n")
print(border)