"""
Campbell's Soup Can #1091
Produced: 2025-12-21 22:34:17
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

# ANSI color codes
RESET  = "\033[0m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
MAGENTA= "\033[35m"

def typewrite(text: str, delay: float = 0.05) -> None:
    """Print text one character at a time with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def typewrite_colored(words, delay: float = 0.07) -> None:
    """Print a list of words, cycling through a set of colors."""
    colors = [CYAN, YELLOW, MAGENTA]
    for i, word in enumerate(words):
        color = colors[i % len(colors)]
        typewrite(f"{color}{word}{RESET} ", delay)

def main() -> None:
    quote = ("I think the universe owes me an answer, "
             "but it's still waiting for my existential question mark.")
    words = quote.split(' ')
    width = len(quote)

    # Top border
    sys.stdout.write(f"{CYAN}┌{'─'*width}┐{RESET}\n")
    time.sleep(0.2)

    # Left border + quote
    sys.stdout.write(f"{CYAN}│{RESET}")
    typewrite_colored(words)
    sys.stdout.write(f"{CYAN}│{RESET}\n")
    time.sleep(0.2)

    # Bottom border
    sys.stdout.write(f"{CYAN}└{'─'*width}┘{RESET}\n")

if __name__ == "__main__":
    main()