"""
Campbell's Soup Can #4518
Produced: 2026-08-10 15:16:02
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

def typewriter_no_newline(text, delay=0.05):
    """Print text one character at a time with random colors."""
    for ch in text:
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def print_ascii_art():
    """Print a small brain ASCII art with a green color."""
    art = [
        "   .-''''-.",
        "  /        \\",
        " |  O  O   |",
        " |   /\\    |",
        "  \\  --   /",
        "   '-..-'"
    ]
    for line in art:
        sys.stdout.write(f"{COLORS[1]}{line}{RESET}\n")
        time.sleep(0.1)

def print_box_with_typewriter(lines, width):
    """Print a box around the lines and typewriter the content."""
    sys.stdout.write(f"{COLORS[0]}+{'-'*width}+{RESET}\n")
    for line in lines:
        sys.stdout.write(f"{COLORS[0]}|{RESET}")
        typewriter_no_newline(line, delay=0.07)
        sys.stdout.write(f"{COLORS[0]}|{RESET}\n")
    sys.stdout.write(f"{COLORS[0]}+{'-'*width}+{RESET}\n")

def main():
    quote = ("I think the universe is a cosmic joke, "
             "and I'm the punchline that keeps asking why.")
    lines = [quote]
    width = max(len(line) for line in lines)
    print_ascii_art()
    print_box_with_typewriter(lines, width)

if __name__ == "__main__":
    main()
