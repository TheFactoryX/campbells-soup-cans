"""
Campbell's Soup Can #981
Produced: 2025-12-16 22:34:14
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
quote = "I’m not scared of death; I just don’t want to miss the punchline."
def c(s, col):
    colors = {"red":"\033[91m","yellow":"\033[93m","reset":"\033[0m"}
    return colors[col] + s + colors["reset"]
w = 58
top    = "╔" + "═"*w + "╗"
bottom = "╚" + "═"*w + "╝"
mid    = "║" + " "*w + "║"
def print_line(txt, col):
    print(c(txt, col))
print_line(top, "red")
for i in range(0, len(quote), w):
    segment = quote[i:i+w]
    print_line("║"+segment.ljust(w)+"║", "yellow")
print_line(bottom, "red")