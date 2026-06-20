"""
Campbell's Soup Can #3972
Produced: 2026-06-20 12:10:53
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter(text, speed=0.03):
    """Prints text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def main():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Header with thinking emoji
    print(f"\n{MAGENTA}{'═'*55}{RESET}")
    print(f"{CYAN}   🧠 WOODY ALLEN'S EXISTENTIAL THERAPY SESSION 🧠{RESET}")
    print(f"{MAGENTA}{'═'*55}{RESET}\n")
    
    # A perfectly Woody Allen quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Decorative box with colors
    print(f"{YELLOW}  ╭─────────────────────────────────────────────────────╮")
    print(f"{YELLOW}  │                                                       │")
    print(f"{WHITE}  │  {quote:<51}{RESET}")
    print(f"{YELLOW}  │                                                       │")
    print(f"{YELLOW}  ╰─────────────────────────────────────────────────────╯")
    
    time.sleep(1.5)
    typewriter(f"\n{GREEN}  [Long pause, followed by nervous laughter]{RESET}")
    time.sleep(0.5)
    typewriter(f"{RED}  [Pulls out phone] [Texts therapist: 'Help'?]{RESET}")
    time.sleep(0.5)
    typewriter(f"{BLUE}  [Stares into middle distance]{RESET}")

if __name__ == "__main__":
    main()