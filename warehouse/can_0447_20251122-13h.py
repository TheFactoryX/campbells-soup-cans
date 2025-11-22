"""
Campbell's Soup Can #447
Produced: 2025-11-22 13:32:40
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
A little Pixar‑ish Woody Allen thought in the terminal.
"""

import time, sys, textwrap

# ================================
# ANSI escape codes
# ================================
RESET   = '\033[0m'
BOLD    = '\033[1m'
YELLOW  = '\033[1;33m'
CYAN    = '\033[1;36m'
MAGENTA = '\033[1;35m'

# ================================
# The quote
# ================================
QUOTE = (
    "Life is a paradox: each time I try to dance, I pull my own feet into an "
    "existential DISASTER, as if the universe has a sarcastic sense of humor. "
    "So I ask: am I absurd, or is absurdity absurd?"
)

# ================================
# Utilities
# ================================
def typewriter(text, delay=0.04):
    """Prints text like a typewriter."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def draw_box(lines, width=60):
    """Draws a box around the given lines."""
    top = f"{BOLD}{YELLOW}┏{'━' * width}┓{RESET}"
    print(top)
    for line in lines:
        # left/right borders
        print(f"{BOLD}{YELLOW}┃{RESET} {line:<{width-2}} {BOLD}{YELLOW}┃{RESET}")
    bottom = f"{BOLD}{YELLOW}┗{'━' * width}┛{RESET}"
    print(bottom)

def show_loading_spinner(seconds=2):
    """A tiny spinner to tease the reader."""
    spinner = ['|', '/', '-', '\\']
    end = time.time() + seconds
    idx = 0
    while time.time() < end:
        sys.stdout.write(f"\r{MAGENTA}Thinking... {spinner[idx % len(spinner)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

# ================================
# Main
# ================================
def main():
    # A little animation before the reveal
    show_loading_spinner(2)

    # Wrap the quote to fit in the box
    wrapped = textwrap.wrap(QUOTE, width=56)  # 56 so +2 spaces fits 60 width
    # Animate each line
    for line in wrapped:
        typewriter(f"{CYAN}–{RESET} {line}", delay=0.05)
        time.sleep(0.1)

    # Draw a box around the quoted text
    draw_box([f"{CYAN}–{RESET} {line}" for line in wrapped], width=60)

if __name__ == "__main__":
    main()
