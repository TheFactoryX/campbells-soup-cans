"""
Campbell's Soup Can #3901
Produced: 2026-06-10 01:30:32
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, color‑driven Woody‑Allen‑style existential joke,
flying straight into your terminal like a one‑liner comic strip.
"""

import sys
import time
import shutil

# ANSI escape codes for colors
RED   = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE  = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN  = "\x1b[36m"
WHITE = "\x1b[37m"
RESET = "\x1b[0m"

# The quote
QUOTE = (
    "I am not a philosopher; I am a chain‑of‑thought that keeps breaking "
    "the rule that if you stop, you die. So I keep going until I trip on my "
    "own existential existentialism."
)

# Decorative ASCII art "box" that fills the terminal width
def make_box(text: str) -> str:
    cols, _ = shutil.get_terminal_size(fallback=(80, 24))
    # Pad text to center
    lines = text.split("\n")
    left_padding = (cols - max(len(line) for line in lines)) // 2
    padded_lines = [(" " * left_padding) + line for line in lines]
    border = "-" * (max(len(line) for line in padded_lines) + 4)
    boxed = f"{MAGENTA}+{border}+\n"
    for l in padded_lines:
        boxed += f"{MAGENTA}|  {l}  |\n"
    boxed += f"{MAGENTA}+{border}+{RESET}"
    return boxed

# Typewriter effect
def typewriter(text: str, color: str = CYAN, delay: float = 0.02):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    # Clear screen
    sys.stdout.write("\x1b[2J\x1b[H")
    # Print header with colors
    title = f"{YELLOW}  ██████╗  ██████╗ ████████╗ {RESET}"
    subtitle = f"{BLUE}  ██╔══██╗██╔═══██╗╚══██╔══╝ {RESET}"
    footer = f"{GREEN}  ██████╔╝██║   ██║   ██║    {RESET}"
    print(title + subtitle + footer)
    print("\n")

    # Prepare quote in box
    boxed_quote = make_box(QUOTE)
    print(colored(ascii_art(boxed_quote), GREEN))
    print("\n")
    # Animated reveal of a smaller punchline
    punchline = "Maybe I should just write this program and call it a tragedy."
    typewriter(punchline, YELLOW)

def ascii_art(text: str) -> str:
    # Convert to a simple ASCII art style
    art = ""
    for ch in text:
        if ch == "\n":
            art += "\n"
        else:
            art += ch if ch == " " else ch
    return art

if __name__ == "__main__":
    main()