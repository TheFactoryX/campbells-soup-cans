"""
Campbell's Soup Can #2251
Produced: 2026-02-15 23:42:44
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

reset = "\033[0m"
border_color = "\033[95m"   # Bright magenta
text_color = "\033[96m"      # Bright cyan
accent_color = "\033[93m"    # Bright yellow

def print_with_typing(text, delay=0.03, color=text_color):
    for char in text:
        print(color + char + reset, end='', flush=True)
        time.sleep(delay)
    print()

inner_width = 50
top_border = "╔" + "═" * inner_width + "╗"
bottom_border = "╚" + "═" * inner_width + "╝"

quote = "I'm not afraid of death; I'm afraid of the paperwork\nthat comes with it... and the coffee in the afterlife\nis probably just as bad as the coffee here."

lines = []
for part in quote.split('\n'):
    lines.append(part.center(inner_width))

ascii_art = [
    accent_color + "    ☕    " + reset,
    accent_color + "   (  )   " + reset,
    accent_color + "  (    )  " + reset,
    accent_color + " (______) " + reset
]

print("\n" * 3)
for line in ascii_art:
    print(line.center(inner_width + 10))
print("\n" + border_color + " " * 10 + "Woody Allen-Style Existential Dread" + reset)
print("")
print(border_color + top_border + reset)

print(border_color + "║" + reset, end='', flush=True)
print_with_typing(" " * (inner_width), 0.001, reset)
print(border_color + "║" + reset)

for i, line in enumerate(lines):
    print(border_color + "║", end='', flush=True)
    print_with_typing(line, 0.025 if i != 1 else 0.05)
    print(border_color + "║" + reset, end='\n', flush=True)
    if i == 0:
        time.sleep(0.2)
        print(border_color + "║" + reset + accent_color + "    (sweats nervously about the paperwork)" + reset.center(20) + border_color + "║" + reset)
        time.sleep(0.7)

print(border_color + "║" + reset, end='', flush=True)
print_with_typing(" " * (inner_width), 0.001, reset)
print(border_color + "║" + reset)

print(border_color + bottom_border + reset)
print_with_typing("\nWhy did the neurotic philosopher cross the road?\nTo overanalyze the existential implications of chickenhood.", 0.015, accent_color)
print(reset + "\n" + " " * 15 + "─" * 20 + " The End " + "─" * 20 + "\n")