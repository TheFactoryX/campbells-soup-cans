"""
Campbell's Soup Can #4757
Produced: 2026-08-22 03:56:16
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Woody Allen philosophical quote with colorful ASCII box

inner_width = 44

top_bottom = "+" + "-" * inner_width + "+"

def make_line(text):
    padding = inner_width - len(text) - 2
    if padding < 0:
        padding = 0
    return f"| " + text + " " + " " * padding + "|"

def colored(txt, color):
    return f"\033[{color}m{txt}\033[0m"

quote1 = colored("I’m not afraid of death; I just don’t want", 33)
quote2 = colored("miss the punchline.", 33)

line1 = make_line(quote1)
line2 = make_line(quote2)

print(top_bottom)
print(line1)
print(line2)
print(top_bottom)