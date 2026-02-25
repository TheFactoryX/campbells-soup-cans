"""
Campbell's Soup Can #2429
Produced: 2026-02-25 16:20:46
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
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

def type_effect(text, delay=0.03, color="\033[93m"):
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

box_width = 60
inner_width = box_width - 4

quote = (
    "I've achieved immortality through anxiety - I die a little bit "
    "every time I contemplate my own mortality. The only thing worse than "
    "dying is having to plan my own funeral. And the caterer will never "
    "get my favorite dish right - they always forget the extra matzo ball soup!"
)
author = "— Woody Allen (probably while staring at a clock)"

# Format content lines
content_lines = [
    "",
    *textwrap.wrap(quote, width=inner_width),
    "",
    author.center(inner_width),
    ""
]
content_lines = [line.ljust(inner_width)[:inner_width] for line in content_lines]

# Create ASCII art character
woody_ascii = [
    "   .-''-.   ",
    "  / .  . \\  ",
    " |  (o)(o) | ",
    "  \\   ^   /  ",
    "   '-___-'   ",
    "   \033[90mNEUROTIC\033[0m  ",
    "  \033[90mANXIETY\033[0m  "
]

# Print box with animated typing effect
print("\033[94m╔" + "═" * (box_width - 2) + "╗\033[0m")

for i, line in enumerate(content_lines):
    sys.stdout.write("\033[94m║ \033[0m")
    sys.stdout.flush()
    
    if i in [0, len(content_lines)-1] or not line.strip():
        print(line + "\033[94m ║\033[0m")
    else:
        type_effect(line, 0.025)
        print("\033[94m ║\033[0m")

print("\033[94m╚" + "═" * (box_width - 2) + "╝\033[0m\n")

# Print ASCII art with blinking effect
for _ in range(3):
    for frame in woody_ascii:
        sys.stdout.write("\r" + " " * 70 + "\r")
        sys.stdout.write(frame)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * 70 + "\r")
        sys.stdout.flush()
        time.sleep(0.1)

sys.stdout.write("\r")
for frame in woody_ascii:
    print(frame)
time.sleep(0.5)

# Final punchline with flicker effect
punchline = "Existence is painful. And expensive."
for _ in range(5):
    sys.stdout.write(punchline + "      \r")
    sys.stdout.flush()
    time.sleep(0.15)
    sys.stdout.write(" " * len(punchline) + "      \r")
    sys.stdout.flush()
    time.sleep(0.1)
print("\033[93m" + punchline + "\033[0m")

# Clean up with a sigh
time.sleep(0.7)
print("\033[90m*another existential sigh*\033[0m")