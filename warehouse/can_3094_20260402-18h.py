"""
Campbell's Soup Can #3094
Produced: 2026-04-02 18:01:29
Worker: Z.ai: GLM 5 (z-ai/glm-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # ANSI color codes
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # The quote
    quote = "My relationship with reality has been strained for years. We're currently seeing other people—reality is dating someone more stable, and I'm seeing a therapist who charges by the neurosis."
    
    # Animated border
    print()
    print(f"{MAGENTA}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}")
    print(f"{MAGENTA}║{RESET}    {BOLD}{YELLOW}🧠 WOODY ALLEN'S EXISTENTIAL CRISIS CORNER 🧠{RESET}                              {MAGENTA}║{RESET}")
    print(f"{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}")
    print(f"{MAGENTA}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}")
    
    # Typewriter effect for the quote
    sys.stdout.write(f"{MAGENTA}║{RESET}    {CYAN}\"")
    sys.stdout.flush()
    typewriter(quote, 0.02)
    print(f"{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}")
    print(f"{MAGENTA}║{RESET}                                    {GREEN}— Woody Allen (probably){RESET}              {MAGENTA}║{RESET}")
    print(f"{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}")
    print(f"{MAGENTA}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")
    
    # Tiny neurotic animation at the bottom
    print()
    for i in range(3):
        dots = "." * (i + 1)
        sys.stdout.write(f"\r{RED}{dots} worrying about whether this quote was funny enough {dots}{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"\r{GREEN}✓ Anxiety successfully projected onto the audience.{RESET}          ")
    print()

if __name__ == "__main__":
    main()