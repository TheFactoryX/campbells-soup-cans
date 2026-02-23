"""
Campbell's Soup Can #2390
Produced: 2026-02-23 10:12:29
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not afraid of death; I just don't want to be there when it happens. And by 'there', I mean the future. It's always so... tomorrowish."

width = 60
border_color = "\033[94m"
quote_color = "\033[93m"
reset = "\033[0m"
content_width = width - 2
padding = (content_width - len(quote)) // 2
total_move = 1 + padding

print(f"{border_color}  (o o)  {reset}")
print(f"{border_color}  (   ),{reset}")
print(f"{border_color}   \" \"   {reset}")
print()

print(border_color + "┌" + "─" * (width-2) + "┐" + reset)
print(border_color + "│" + " " * (width-2) + "│" + reset)
print(border_color + "└" + "─" * (width-2) + "┘" + reset)

print(f"\033[2A\033[{total_move}C", end='', flush=True)
print(quote_color, end='', flush=True)
for char in quote:
    print(char, end='', flush=True)
    time.sleep(0.03)
print(reset)
print()