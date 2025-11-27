"""
Campbell's Soup Can #547
Produced: 2025-11-27 03:29:41
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI escape codes for colors
GREEN = '\033[32m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# ASCII art of Woody Allen character
woody_art = f"""
{CYAN}                  ,-.   .-,
                  (  `-^'  )
                   '-O-O-'
                     | | |
                     | | |
                    / / \\ \\
                   / /   \\ \\
                  | |      | |
                  | |      | |
                   \ \    / /
                    '-.__.-'
{RESET}
"""

# Animated quote with delay
quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
center = "=" * ((os.get_terminal_size().columns - len(quote)) // 2)
print(f"{center} WoOdy's Neurotic Thought {center}\n")

for char in quote:
    sys.stdout.write(f"{GREEN}{char}{RESET}")
    sys.stdout.flush()
    time.sleep(0.05)
print("\n")

# Fancy border
border_width = max(40, os.get_terminal_size().columns)
border_top = f"{CYAN}╔{'═' * (border_width - 2)}╗{RESET}"
border_bottom = f"{CYAN}╚{'═' * (border_width - 2)}╗{RESET}"

print(border_top)
print(f"{CYAN}║{RESET} {YELLOW}{quote.center(border_width - 4)}{RESET} {CYAN}║{RESET}")
print(border_bottom)

# Print the ASCII art centered
term_width = os.get_terminal_size().columns
for line in woody_art.split('\n'):
    padding = ' ' * ((term_width - len(line.strip())) // 2)
    print(f"{padding}{line}")

# Ending with Woody's signature
print(f"\n{CYAN}{'─' * term_width}")
print(f"{YELLOW}NEUROTIC WISDOM PITFALLING INTO COMPLEXITY: {RESET} self-deprecation as lifestyle choice")
print(f"{CYAN}{'─' * term_width}{RESET}")