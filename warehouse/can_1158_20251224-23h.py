"""
Campbell's Soup Can #1158
Produced: 2025-12-24 23:31:18
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

# ANSI colour codes
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'

# Border for the quote
WIDTH = 60
TOP_BORDER = f"{YELLOW}{BOLD}╔{'═' * WIDTH}╗{RESET}"
BOTTOM_BORDER = f"{YELLOW}{BOLD}╚{'═' * WIDTH}╝{RESET}"

# The Woody‑Allen‑style quote (one line)
QUOTE = (
    "I think the best way to avoid existential dread is to write "
    "your life's sitcom and then laugh at its irony."
)

def type_out(text, delay=0.05):
    """Print *text* to the console one character at a time."""
    for ch in text:
        sys.stdout.write(CYAN + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    # Print the colourful border and the animated quote
    sys.stdout.write(TOP_BORDER + '\n')
    sys.stdout.flush()
    type_out(QUOTE)
    sys.stdout.write(BOTTOM_BORDER + '\n\n')
    sys.stdout.flush()

    # ASCII laughing face (in magenta)
    art_lines = [
        "  ______",
        " /    \\\\",
        "| (•_•) |",
        " \\__|__/",
        "   / \\\\",
    ]
    laugh_art = f"{MAGENTA}{BOLD}\n" + "\n".join(art_lines) + f"\n{RESET}"
    sys.stdout.write(laugh_art + '\n')
    sys.stdout.flush()

if __name__ == "__main__":
    main()
