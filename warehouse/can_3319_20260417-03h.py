"""
Campbell's Soup Can #3319
Produced: 2026-04-17 03:45:32
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import itertools

# ANSI color codes
RESET = "\x1b[0m"
BG_BLUE = "\x1b[44m"
FG_WHITE = "\x1b[97m"
FG_YELLOW = "\x1b[93m"
FG_LIGHT_GRAY = "\x1b[37m"

# Quote in Woody Allen style
QUOTE = (
    "I confess: the universe is just a painfully anxious sitcom, "
    "and I'm the earnest character who keeps saying 'I have nothing to offer— "
    "except levels of neuroticism!'."
)

# Box dimensions
WIDTH = max(len(line) for line in QUOTE.split('\n')) + 4
BOX_TOP = f"{FG_WHITE}{BG_BLUE}+{'-' * (WIDTH - 2)}+{RESET}"
BOX_BOTTOM = f"{FG_WHITE}{BG_BLUE}+{'-' * (WIDTH - 2)}+{RESET}"
BOX_PADDING = f"{FG_WHITE}{BG_BLUE}|{' ' * (WIDTH - 2)}|{RESET}"

def type_write(text, delay=0.05):
    """Print text with a typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != '\n':
            time.sleep(delay)
    sys.stdout.write('\n')

def main():
    # Clear screen
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()

    # Print top of the box
    sys.stdout.write(BOX_TOP + "\n")
    # Empty line inside box
    sys.stdout.write(BOX_PADDING + "\n")

    # Display the quote with a slight delay per character
    type_write(FG_YELLOW + QUOTE + RESET, delay=0.04)

    # Empty line inside box
    sys.stdout.write(BOX_PADDING + "\n")
    # Bottom of the box
    sys.stdout.write(BOX_BOTTOM + "\n")

    # Pause briefly before exiting
    time.sleep(1)

if __name__ == "__main__":
    main()