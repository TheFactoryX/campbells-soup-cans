"""
Campbell's Soup Can #817
Produced: 2025-12-09 13:05:44
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

# ---- ANSI color helpers ----
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
MAGENTA = '\033[95m'

# ---- The Woody‑Allen style quote ----
QUOTE = (
    f"{YELLOW}I’m not afraid of death; I simply refuse to attend the eternal funeral of my own ego.{RESET}"
)

# ---- Visual frame and short animation ----
def print_frame(text):
    """Print text inside a colorful ASCII box."""
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    top = f"{CYAN}╔" + "═" * width + "╗{RESET}"
    bottom = f"{CYAN}╚" + "═" * width + "╝{RESET}"
    print(top)
    for line in lines:
        print(f"{CYAN}║{RESET}  {line.ljust(width - 2)}  {CYAN}║{RESET}")
    print(bottom)

def animate_stare(duration=2.0, interval=0.2):
    """A tiny animated stare before the quote appears."""
    stars = ['\\', '|', '/', '-']
    end_time = time.time() + duration
    while time.time() < end_time:
        for s in stars:
            sys.stdout.write(f"\r{MAGENTA}{BOLD}   {s} thinking...{RESET}")
            sys.stdout.flush()
            time.sleep(interval)
    sys.stdout.write("\r" + " " * 30 + "\r")  # clear line

def main():
    animate_stare()
    print_frame(QUOTE)

if __name__ == "__main__":
    main()
