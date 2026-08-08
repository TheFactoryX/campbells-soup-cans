"""
Campbell's Soup Can #4482
Produced: 2026-08-08 15:45:53
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# ANSI color codes
COLORS = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
RESET = '\033[0m'

def typewriter_line(line, width, delay=0.07):
    """Print a single line inside a box with a typewriter effect."""
    sys.stdout.write(f"{COLORS[0]}|{RESET}")
    for ch in line:
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    # Pad the rest of the line to keep the box rectangular
    sys.stdout.write(' ' * (width - len(line)))
    sys.stdout.write(f"{COLORS[0]}|{RESET}\n")

def print_box(lines):
    """Print a list of lines inside a colored box with typewriter animation."""
    width = max(len(line) for line in lines)
    sys.stdout.write(f"{COLORS[0]}+{'-' * width}+{RESET}\n")
    for line in lines:
        typewriter_line(line, width)
    sys.stdout.write(f"{COLORS[0]}+{'-' * width}+{RESET}\n")

def main():
    # A little brain ASCII art to set the mood
    brain = [
        "      .-''''-.",
        "     /  .--.  \\",
        "    /  /    \\  \\",
        "    |  |    |  |",
        "    \\  \\    /  /",
        "     \\  '--'  /",
        "      '-....-'"
    ]

    # The Woody‑Allen‑style philosophical quote
    quote = ("I think the universe is a cosmic joke, "
             "and I'm the punchline that keeps asking why.")

    # Show the brain first
    print_box(brain)
    time.sleep(0.5)

    # Then the quote
    print_box([quote])

if __name__ == "__main__":
    main()
