"""
Campbell's Soup Can #2033
Produced: 2026-02-04 07:56:50
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
COL = {
    "reset": "\033[0m",
    "red":   "\033[31m",
    "green": "\033[32m",
    "yellow":"\033[33m",
    "blue":  "\033[34m",
    "magenta":"\033[35m",
    "cyan":  "\033[36m",
    "white": "\033[37m",
}
def c(text, **kwargs):
    """Wrap text in ANSI colors."""
    parts = []
    for k in kwargs:
        parts.append(COL.get(k, ""))
    parts.append(text)
    parts.append(COL["reset"])
    return "".join(parts)

# The Woody Allen line we want to display
quote = (
    "Life is full of misery, loneliness, and suffering.\n"
    "It also has a happy ending, but only if you're lucky enough to get to the punchline."
)

# Create a simple decorative frame
top    = ("+" + "-" * 66 + "+\n")
middle = ("| " + (" " * 64) + " |")
bottom = ("+" + "-" * 66 + "+")

# Speed of “typing” effect (seconds per character)
delay = 0.03

def slow_print(s, **kwargs):
    for ch in s:
        sys.stdout.write(c(ch, **kwargs))
        sys.stdout.flush()
        time.sleep(delay)

def clear_screen():
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

print("\n" + top, end="")
print(c(middle, cyan=1), end="")
print(c(middle, cyan=1), end="")
print(c(middle, cyan=1), end="")
print(c(middle, cyan=1), end="")
print(c(middle, cyan=1), end="")
print(c(middle, cyan=1), end="")
print(c(middle, cyan=1), end="")
clear_screen()
print(top, end="")

slow_print(c(top[0], red), end="")          # just to show colour works
for i, line in enumerate(quote.split("\n")):
    # Print each line centered inside the frame with a color gradient
    clear_screen()
    print(top, end="")
    print(c(f"| {line.strip().center(64)} |", magenta), end="")
    time.sleep(0.8)

# Final personality line
clear_screen()
final = "   ...and then he realized the universe was just a bad stand‑up set."
slow_print(c(final, yellow), end="")
time.sleep(2)
clear_screen()
print(top, end="")
slow_print(c("   FIN.  ", green), end="")

# Keep the terminal open for a moment before exiting (optional)
time.sleep(3)