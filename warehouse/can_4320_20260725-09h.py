"""
Campbell's Soup Can #4320
Produced: 2026-07-25 09:59:38
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def main():
    # Woody Allen‑style philosophical quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # ANSI color codes for a colorful, eye‑catching presentation
    BOLD   = "\033[1m"
    YELLOW = "\033[33m"
    CYAN   = "\033[36m"
    RESET  = "\033[0m"

    # Build a simple bordered box around the quote
    max_len = len(quote)
    width   = max_len + 4                     # padding on each side
    top    = f"{BOLD}{YELLOW}{'*' * width}{RESET}"
    middle = f"{BOLD}{CYAN}| {quote} |{RESET}"
    bottom = f"{BOLD}{YELLOW}{'*' * width}{RESET}"

    # Small pause for a dramatic effect
    time.sleep(0.5)

    print(top)
    print(middle)
    print(bottom)

if __name__ == "__main__":
    main()