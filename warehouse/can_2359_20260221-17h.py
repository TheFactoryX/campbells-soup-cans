"""
Campbell's Soup Can #2359
Produced: 2026-02-21 17:42:35
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

reset = '\033[0m'
yellow = '\033[93m'
red = '\033[91m'
white = '\033[97m'
blue = '\033[94m'
bold = '\033[1m'

width = 60
inside_width = width - 4

quote_lines = [
    "I'm not afraid of death; I'm afraid of the traffic",
    "on the way to the afterlife. (And yes, the coffee's terrible there too.)"
]

colored_lines = []
for i, line in enumerate(quote_lines):
    if i == 0:
        colored_line = red + " (•̃_•̃) " + reset + white + line + reset
    else:
        colored_line = blue + line + reset
    colored_lines.append(colored_line.ljust(inside_width))

top_bottom = yellow + bold + '═' * width + reset

print(top_bottom)
time.sleep(0.1)

for line in colored_lines:
    print(yellow + bold + '║' + reset + ' ' + line + ' ' + yellow + bold + '║' + reset)
    time.sleep(0.2)

print(top_bottom)
time.sleep(0.1)

print(f"{white}{' ' * 15}— Woody Allen, probably{reset}")
print(f"{yellow}{' ' * 20}© 2023 Existential Deli{reset}")
time.sleep(0.3)
print(f"{blue}{' ' * 18}Press any key to overthink...{reset}")