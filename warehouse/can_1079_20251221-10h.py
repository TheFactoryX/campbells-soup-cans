"""
Campbell's Soup Can #1079
Produced: 2025-12-21 10:36:17
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
A whimsical, color‑filled Woody‑Allen‑style philosophical quip.
Runs natively with no external libraries.
"""

import sys
import time
import random
import textwrap

# ---------- ANSI colour codes ----------
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"
GREEN   = "\033[32m"
# ---------- Quote ----------
QUOTE = (
    "I think the meaning of life is to be an existential punchline "
    "that never gets a punchback. Still, I keep guessing for a reason."
)

# ---------- Frame helpers ----------
FRAME_CHAR = "█"
WIDTH = 80  # inner width of the frame

def _styled(text: str, color: str = "") -> str:
    return f"{BOLD}{color}{text}{RESET}"

def _frame_line(content: str = "") -> str:
    """Return a single line of the frame, padded to the inner width."""
    pad_len = WIDTH - len(content)
    if pad_len < 0:  # in case content is longer
        content = content[:WIDTH]
        pad_len = 0
    return f"{FRAME_CHAR}{content}{' ' * pad_len}{FRAME_CHAR}"

def _print_line(line: str):
    """Print a single line of text within the frame."""
    sys.stdout.write(f"{_frame_line(line)}\n")
    sys.stdout.flush()

# ---------- Animation helpers ----------
def _type_text(text: str, min_delay: float = 0.02, max_delay: float = 0.06):
    """Simulate typing animation for a given string."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))

def _animate_delayed_print(line: str):
    """Print a line with typing animation inside the frame."""
    sys.stdout.write(FRAME_CHAR)
    _type_text(line)
    remaining = WIDTH - len(line)
    if remaining > 0:
        sys.stdout.write(" " * remaining)
    sys.stdout.write(FRAME_CHAR + "\n")
    sys.stdout.flush()

# ---------- Main rendering ----------
def main():
    # Top border
    sys.stdout.write(f"{FRAME_CHAR * (WIDTH + 2)}\n")
    sys.stdout.flush()

    # Header
    header = _styled(" Woody‑Allen‑ish Existential Musings ", GREEN)
    header_line = header.center(WIDTH, " ")
    _print_line(header_line)

    # Empty separator
    _print_line("")

    # Quote wrapped into multiple lines
    wrapper = textwrap.TextWrapper(width=WIDTH)
    wrapped_lines = wrapper.wrap(QUOTE)

    for line in wrapped_lines:
        _animate_delayed_print(line)

    # Empty separator
    _print_line("")

    # Bottom line
    _print_line("-" * WIDTH)

    # Bottom border
    sys.stdout.write(f"{FRAME_CHAR * (WIDTH + 2)}\n")
    sys.stdout.flush()

    # Bye note in fun colour
    print(_styled("Courage? Rare. Existence? Continuous. Thank you for reading.", MAGENTA))

if __name__