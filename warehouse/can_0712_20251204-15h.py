"""
Campbell's Soup Can #712
Produced: 2025-12-04 15:38:13
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful, single‑file Python script that prints a funny Woody Allen‑style
philosophical quote with colors, ASCII art and a tiny typing animation.
"""

import sys
import time
import itertools

# ---------- ANSI colour codes ----------
RESET = '\033[0m'
BLUE = '\033[94m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'

# ---------- Utility functions ----------
def slow_print(text, delay=0.04, color=RESET):
    """Prints `text` one character at a time with a short delay."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def spinner_animation(durations=20, delay=0.07):
    """Shows a simple spinner for a short time."""
    for _ in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write(f"\r{YELLOW}Loading the universe like an existential dread...{_}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
        durations -= 1
        if durations <= 0:
            break
    sys.stdout.write('\r' + ' ' * 60 + '\r')   # clear the line

# ---------- ASCII art ----------
ART = f"""
{CYAN}   .-""""-.
  / -   -  \\
 |  .-. .-.|
 |  \\o/ \\o/|
  \\  \\\\//  /
  '------'{RESET}
"""

# ---------- The Woody Allen quote ----------
QUOTE = ("I often wonder whether the universe is a cosmic joke, and if so "
         "am I the punchline that keeps asking, ‘Did I bring my own joke?’ "
         "The only certainty is that I keep losing my keys and my sense of purpose.")


def main():
    # Print the colorful ASCII art
    print(ART)

    # Show a tiny spinner to build suspense
    spinner_animation()

    # Print the quote inside a decorative box with a slow‑type effect
    quote_lines = QUOTE.split(' ')
    # Wrap the quote to 60 chars per line for aesthetics
    wrapped = []
    line = ""
    for word in quote_lines:
        if len(line) + len(word) + 1 <= 60:
            line += word + " "
        else:
            wrapped.append(line.strip())
            line = word + " "
    wrapped.append(line.strip())

    # Build the boxed output
    border = f"{MAGENTA}┌" + "─" * 62 + "┐{RESET}\n"
    boxed = border
    for w in wrapped:
        boxed += f"{MAGENTA}│{RESET}{CYAN}  {w.ljust(60)}  {MAGENTA}│{RESET}\n"
    boxed += f"{MAGENTA}└" + "─" * 62 + "┘{RESET}\n"

    slow_print(boxed, delay=0.03, color=RESET)

if __name__ == "__main__":
    main()