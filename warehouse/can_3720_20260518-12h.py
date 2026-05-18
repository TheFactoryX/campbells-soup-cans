"""
Campbell's Soup Can #3720
Produced: 2026-05-18 12:47:13
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Philosophical Quote Generator
"""

import time
import sys

# ANSI color codes
RESET = '\033[0m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

def typewriter_effect(text, delay=0.03, color=""):
    """Print text with a typewriter effect"""
    full_text = color + text + RESET
    for char in full_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(text, color=CYAN):
    """Print text inside a decorative box"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    top_border = f"{color}╔{'═' * (max_len + 2)}╗{RESET}"
    bottom_border = f"{color}╚{'═' * (max_len + 2)}╝{RESET}"
    
    print(top_border)
    for line in lines:
        print(f"{color}║{RESET} {line.ljust(max_len)} {color}║{RESET}")
    print(bottom_border)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Print header
    print()
    header = f"""{RED}{BOLD}
  ╔═══════════════════════════════════════════════════════╗
  ║                                                       ║
  ║   WOODY ALLEN'S PHILOSOPHICAL QUOTE GENERATOR         ║
  ║              (Existential Edition)                    ║
  ║                                                       ║
  ╚═══════════════════════════════════════════════════════╝
{RESET}"""
    print(header)
    time.sleep(0.5)
    
    # Animated philosophical elements
    print(f"{MAGENTA}  Calculating life's meaning...{RESET}")
    for _ in range(3):
        print(f"{YELLOW}  .{RESET}", end='')
        time.sleep(0.5)
    print()
    time.sleep(0.5)
    
    # The quote with typing effect
    quote = "I'm not afraid of death;\nI'm just terrified that I'll\nbe having a great time and\nit'll interrupt."
    
    print()
    print(f"{BLUE}  Generating your existential crisis...{RESET}")
    time.sleep(1)
    print()
    
    # Print the quote in a box with typing effect
    print_box(quote, YELLOW)
    
    # Add some philosophical pondering
    print()
    pondering = f"""
{GREEN}  ╭──────────────────────────────────────────────╮
  │  Did that help? No.                           │
  │  Did anything help? No.                        │
  │  Is any of this real? Probably not.            │
  ╰──────────────────────────────────────────────╯
{RESET}"""
    typewriter_effect(pondering, 0.02, GREEN)
    
    # Final touch
    print()
    print(f"{RED}{BOLD}  Remember: Life is short. The quote was longer.{RESET}")
    print()

if __name__ == "__main__":
    main()