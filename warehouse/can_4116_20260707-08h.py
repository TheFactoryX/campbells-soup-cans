"""
Campbell's Soup Can #4116
Produced: 2026-07-07 08:43:04
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

def animate_text(text, delay=0.015, color="\033[93m"):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m")

glasses = """
\033[91m   ╭───╮   ╭───╮
   │ o │   │ o │
   ╰───╯   ╰───╯
     ╲  .  ╱
      ╲___╱\033[0m
"""

quote = "I'm not afraid of the inevitability of death; I'm afraid that when I get there, they'll ask for my credentials and I'll have forgotten my wallet. It's always the small humiliations that make the infinite void so unbearable."

wrapped = textwrap.wrap(quote, width=62)
max_len = max(len(line) for line in wrapped)

box_color = "\033[94m"

print(glasses)
print("\n" + box_color + "╔" + "═" * (max_len + 2) + "╗\033[0m")

for line in wrapped:
    padding = " " * (max_len - len(line))
    sys.stdout.write(box_color + "║\033[0m ")
    animate_text(line, 0.015, "\033[93m")
    sys.stdout.write(padding + " " + box_color + "║\033[0m\n")
    time.sleep(0.1)

time.sleep(0.3)
print(box_color + "╚" + "═" * (max_len + 2) + "╝\033[0m")
print("\n\033[90m- Attributed to Woody Allen (if he were cosmically anxious)\033[0m")