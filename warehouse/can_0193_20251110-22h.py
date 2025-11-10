"""
Campbell's Soup Can #193
Produced: 2025-11-10 22:33:59
Worker: Anthropic: Claude Opus 4.1 (anthropic/claude-opus-4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import sys

# ANSI color codes
PURPLE = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

def typewriter(text, delay=0.05):
    """Simulate typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_neurotic_box():
    """Draw a shaky, neurotic box"""
    box_chars = ['╔', '═', '╗', '║', '╚', '╝', '~', '≈']
    
    # Top border with nervous shake
    print(f"{CYAN}  ", end="")
    for i in range(60):
        if random.random() > 0.9:
            print(f"{DIM}~{RESET}{CYAN}", end="")
        else:
            print("═", end="")
    print(f"{RESET}")
    
    # Neurotic thought bubbles
    print(f"{DIM}{BLUE}   ○ ◯ ◌{RESET}")
    print(f"{DIM}{BLUE}  ◯ ◌ ○{RESET}")
    print(f"{DIM}{BLUE} ○ ◌{RESET}")
    
    # ASCII Woody
    print(f"{YELLOW}  👓{RESET}")
    print(f"{YELLOW}  /|\\  {DIM}<-- existential dread{RESET}")
    print(f"{YELLOW}  / \\{RESET}")
    
def main():
    # Clear screen
    print("\033[2J\033[H")
    
    # Title with anxiety
    print(f"\n{BOLD}{PURPLE}{'=' * 65}{RESET}")
    print(f"{BOLD}{WHITE}     WOODY ALLEN'S PHILOSOPHICAL ANXIETY GENERATOR™{RESET}")
    print(f"{BOLD}{PURPLE}{'=' * 65}{RESET}\n")
    
    # Draw neurotic elements
    draw_neurotic_box()
    
    print(f"\n{DIM}{CYAN}*adjusts glasses nervously*{RESET}\n")
    time.sleep(1)
    
    # The quote with dramatic buildup
    print(f"{YELLOW}{'─' * 65}{RESET}")
    print()
    
    # Typewriter effect for the quote
    quote = "My therapist says I have a preoccupation with vengeance.\n" + \
            "               We'll see about that."
    
    print(f"{BOLD}{GREEN}", end="")
    typewriter("  \"", delay=0.1)
    
    print(f"{RESET}{WHITE}", end="")
    typewriter("     My relationship with reality is purely platonic—", delay=0.08)
    
    time.sleep(0.5)
    print(f"{DIM}{RED}        *nervous laugh*{RESET}")
    time.sleep(0.5)
    
    print(f"{WHITE}", end="")
    typewriter("     we see each other, but we're not really committed.", delay=0.08)
    
    print(f"{BOLD}{GREEN}", end="")
    typewriter("  \"", delay=0.1)
    
    print(f"\n{YELLOW}{'─' * 65}{RESET}")
    
    # Footer with neurotic additions
    time.sleep(1)
    print(f"\n{DIM}{PURPLE}        — Woody Allen", end="")
    print(f" (probably while lying on a couch){RESET}")
    
    # Random anxious thoughts floating around
    thoughts = [
        f"{DIM}{BLUE}(what if existence is just a cosmic joke?){RESET}",
        f"{DIM}{RED}(did I leave the stove on?){RESET}",
        f"{DIM}{CYAN}(why do we park in driveways?){RESET}"
    ]
    
    time.sleep(1.5)
    print(f"\n{random.choice(thoughts)}")
    
    # Final existential crisis
    print(f"\n{BOLD}{PURPLE}{'=' * 65}{RESET}")
    print(f"{DIM}{WHITE}  Press Ctrl+C to escape existential dread (spoiler: you can't){RESET}")
    print(f"{BOLD}{PURPLE}{'=' * 65}{RESET}\n")

if __name__ == "__main__":
    main()