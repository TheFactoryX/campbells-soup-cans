"""
Campbell's Soup Can #3425
Produced: 2026-04-24 10:45:16
Worker: inclusionAI: Ling-2.6-flash (free) (inclusionai/ling-2.6-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# ANSI color codes
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"
RED     = "\033[31m"
GREEN   = "\033[32m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
BLINK   = "\033[5m"

def typewriter_effect(text, delay=0.03):
    """Simulate a slow, nervous Woody Allen typing."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_wooden_frame(lines):
    """Draw a rustic wooden ASCII frame around the quote."""
    max_len = max(len(l) for l in lines)
    border = "+" + "-" * (max_len + 2) + "+"
    print(f"{BOLD}{CYAN}{border}{RESET}")
    for line in lines:
        print(f"{CYAN}| {line.ljust(max_len)} |{RESET}")
    print(f"{BOLD}{CYAN}{border}{RESET}")

def animated_background():
    """Print a slowly shifting background of cosmic dread."""
    bg_chars = [".", ",", "~", ":", ";", "∷", "․"]
    for i in range(40):
        ch = bg_chars[i % len(bg_chars)]
        color = [CYAN, MAGENTA, YELLOW][i % 3]
        print(f"\r{color}{ch * 80}{RESET}", end="", flush=True)
        time.sleep(0.05)
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Cosmic prelude
    animated_background()
    print(f"\n{BLINK}{BOLD}{MAGENTA}    ⚠  EXISTENTIAL CRISIS INITIATED  ⚠{RESET}\n")
    time.sleep(1)
    
    # The quote
    quote = (
        "I've looked at the universe from both sides—"
        "from the cosmic vastness and from my checking account—"
        "and let me tell you, the universe does not return my calls."
    )
    
    # Woody's nervous preamble
    preamble = [
        f"{YELLOW}*{RESET} Contemplating the human condition… {RED}*,*{RESET}",
        f"{YELLOW}*{RESET} Calculating probable doom… {RED}*,*{RESET}",
        f"{YELLOW}*{RESET} Adjusting neurosis levels… {RED}*,*{RESET}",
    ]
    
    for line in preamble:
        print(f"\n{line}")
        time.sleep(0.6)
    
    print(f"\n{GREEN}┌─────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│{RESET} {BOLD}{CYAN}WOODY'S TRUTH:{RESET} {YELLOW}{quote}{RESET}")
    print(f"{GREEN}└─────────────────────────────────────┘{RESET}\n")
    
    # Afterthought
    afterthought = (
        f"{MAGENTA}In the grand scheme, we're all just"
        f" slightly delayed background processes"
        f" in an unresponsive universe."
    )
    
    print(f"\n{YELLOW}About this life…{RESET}")
    typewriter_effect(afterthought, delay=0.02)
    
    # Footer
    footer = f"\n{BLINK}{RED}☠ Existence is optional. Committing to it is not.{RESET}"
    draw_wooden_frame([footer])

if __name__ == "__main__":
    main()