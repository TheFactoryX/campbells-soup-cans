"""
Campbell's Soup Can #1446
Produced: 2026-01-07 07:38:27
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def animate_text(text, delay=0.05, color=RESET):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # ASCII art frame
    print(f"\n{CYAN}           .-""'-.")
    print(f"          /       \\")
    print(f"          \\       /")
    print(f"    {RED}_.-~{CYAN}`-.-'`~-{RED}._{RESET}")
    
    animate_text(f"\n{YELLOW}       (ᵔᴥᵔ) {MAGENTA}THOUGHTS FROM THE SHADOWS{RESET}", 0.02)
    
    quote = f"\n{YELLOW}»»  Life is just a desperate scramble to find\n    meaning in TV shows before the universe\n    changes the channel.{RESET}"
    
    # Quote box with animation
    print(f"\n{RED}╭{''.join('─'*28)}╮")
    for line in quote.split('\n'):
        print(f"{RED}│ {RESET}", end='')
        animate_text(line.ljust(26), 0.03, YELLOW)
    print(f"{RED}╰{''.join('─'*28)}╯{RESET}")
    
    # Flashing attribution
    for _ in range(3):
        print(f"{MAGENTA}\r― Woody Allen's subconscious{RESET}", end='')
        time.sleep(0.3)
        print("\r                      ", end='')
        time.sleep(0.2)
    print(f"{MAGENTA}\r― Woody Allen's subconscious{RESET}\n")

if __name__ == "__main__":
    main()