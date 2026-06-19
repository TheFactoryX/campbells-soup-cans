"""
Campbell's Soup Can #3964
Produced: 2026-06-19 16:14:13
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

# ANSI color codes
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"

def typewriter(text, delay=0.04, color=RESET):
    """Prints text with typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()

# The quote that captures Woody Allen's essence
woody_quote = "I'm having fun... I'm having so much fun... says the guy who's literally hiding in a bathroom."

# Create the visual presentation
print(f"\n{BLUE}{'·' * 60}{RESET}")
print(f"{CYAN}{BOLD}    ╔══════════════════════════════════════════════════╗")
print(f"    ║{YELLOW}   🎬 WOODY ALLEN PHILOSOPHICAL QUOTE CORNER  🎬    ║")
print(f"    ╚══════════════════════════════════════════════════╝{RESET}")
print(f"{BLUE}{'·' * 60}{RESET}\n")

# Display the quote with typewriter effect
typewriter("   ", 0.01, RESET)
typewriter("   ", 0.01, RED)
typewriter("   ██████╗ ███████╗███████╗ █████╗ ██╗      ", 0.005, MAGENTA)
typewriter("   ██╔════╝ ██╔════╝██╔════╝██╔══██╗██║     ", 0.005, MAGENTA)
typewriter("   ██║  ███╗█████╗  ███████╗███████║██║     ", 0.005, MAGENTA)
typewriter("   ██║   ██║██╔══╝  ╚════██║██╔══██║██║     ", 0.005, MAGENTA)
typewriter("   ╚██████╔╝███████╗███████║██║  ██║███████╗", 0.005, MAGENTA)
typewriter("    ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝", 0.005, MAGENTA)
typewriter("   ", 0.01, RESET)

print(f"\n{GREEN}{'─' * 60}{RESET}\n")

# Print the actual quote in a creative way
print(f"{YELLOW}   ┌─────────────────────────────────────────────────────────┐")
print(f"   │                                                         │")
print(f"{RED}{BOLD}   │  {woody_quote}  │{RESET}")
print(f"   │                                                         │")
print(f"{YELLOW}   └─────────────────────────────────────────────────────────┘{RESET}")

print(f"\n{GREEN}{'─' * 60}{RESET}")

# Attribution with flair
print(f"\n{CYAN}                                     {WHITE}— A worried man, probably{RESET}")
print(f"{BLUE}{'·' * 60}{RESET}\n")

# Self-deprecating footer
time.sleep(0.5)
typewriter("   (Yes, I'm having an existential crisis while writing this)", 0.03, CYAN)
typewriter("   (It's called 'art')", 0.03, CYAN)
print(f"\n{BLUE}{'·' * 60}{RESET}\n")