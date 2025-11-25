"""
Campbell's Soup Can #514
Produced: 2025-11-25 14:38:26
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A fun, single‑file Woody Allen–style philosophical quote with colors and typing animation.
"""

import sys
import time

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

# Tiny helper to mimic a typing effect
def typewrite(text: str, delay: float = 0.02, newline: bool = False):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")

def main() -> None:
    # Box styling
    width = 60
    top_border = f"{CYAN}+{'-' * (width - 2)}+{RESET}"
    side_border = f"{CYAN}|{RESET}"
    bottom_border = f"{CYAN}+{'-' * (width - 2)}+{RESET}"

    # Quote in Woody Allen style
    quote = (
        "I keep asking myself what the point of my life is, "
        "and the universe replies, \"It's just a background track in this cosmic jam.\" "
        "If that's not plausible, then perhaps I'm the joke and someone else's mind is my punchline."
    )

    # Break quote into wrapped lines
    words = quote.split()
    lines = []
    line = ""
    for w in words:
        if len(line) + len(w) + 1 <= width - 4:
            line += w + " "
        else:
            lines.append(line.rstrip())
            line = w + " "
    if line:
        lines.append(line.rstrip())

    # Show the output
    typewrite(top_border, newline=True)
    for l in lines:
        formatted = f"{side_border} {l.ljust(width - 4)} {side_border}"
        typewrite(formatted, newline=True)
    typewrite(bottom_border, newline=True)

    # A little playful animation: the quote “jazz hands” to celebrate existence
    jazz_anim = f"{BOLD}{MAGENTA}🎷🕺💃{RESET}"
    for _ in range(3):
        typewrite(jazz_anim + "\r", delay=0.1, newline=False)
        time.sleep(0.1)
    typewrite(jazz_anim + "\n", newline=True)

if __name__ == "__main__":
    main()