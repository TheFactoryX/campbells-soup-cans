"""
Campbell's Soup Can #3746
Produced: 2026-05-21 21:48:17
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def type_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ANSI color codes
PURPLE = '\033[95m'
CYAN = '\033[96m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

# Display title with animation
title = f"{BOLD}{PURPLE}╔════════════════════════════════╗\n║  WOODY ALLEN'S PHILOSOPHICAL   ║\n║       WISDOM BOX ™             ║\n╚════════════════════════════════╝{RESET}"
for line in title.split('\n'):
    type_print(line, 0.02)

# Boxed quote with typing effect
quote = f"{BOLD}{CYAN}┌──────────────────────────────────────────────┐{RESET}\n" \
        f"{BOLD}{YELLOW}|{RESET} I told my therapist about my fear of death.{BOLD}{YELLOW}|{RESET}\n" \
        f"{BOLD}{GREEN}|{RESET} She said I should try not to think about it.{BOLD}{GREEN}|{RESET}\n" \
        f"{BOLD}{BLUE}|{RESET} I replied, “How can I not think about it{BOLD}{BLUE}|{RESET}\n" \
        f"{BOLD}{RED}|{RESET} when I’m terrified of not existing?”{BOLD}{RED}|{RESET}\n" \
        f"{BOLD}{CYAN}└──────────────────────────────────────────────┘{RESET}"

for line in quote.split('\n'):
    type_print(line, 0.03)

# Final touch with fading effect
time.sleep(0.5)
print(f"\n{BOLD}{PURPLE}...and that's why I take naps.{RESET}")