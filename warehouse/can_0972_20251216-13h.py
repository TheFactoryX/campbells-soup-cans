"""
Campbell's Soup Can #972
Produced: 2025-12-16 13:50:46
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# Quote in Woody Allen's style
WILIAMINE = (
    f"{RESET}\n{BOLD}{RED} ┌───────────────────────────────┐{RESET}\n"
    f"{RED} │ {YELLOW}Looking at people's faces is a{RESET}\n"
    f"{RED} │ {YELLOW}wonderful pastime. Most time I{RESET}\n"
    f"{RED} │ {YELLOW}find I end up filing charges{RESET}\n"
    f"{RED} │ {YELLOW}for indecency in the second{RESET}\n"
    f"{RED} │ {YELLOW}degree. Statistically, people{RESET}\n"
    f"{RED} │ {YELLOW}who don't smile at you probably{RESET}\n"
    f"{RED} │ {YELLOW}have merchandise returns to{RESET}\n"
    f"{RED} │ {YELLOW}process. It's called smiles.{RESET}\n"
    f"{RED} └───────────────────────────────┘{RESET}\n"
    f"{RESET}\n"
)

# ASCII art: Woody Allen
WOODY = [
    "      .-''.",
    "   .-'''-'-.",
    "   '        \\",
    "   : ,--. --",
    "   :       ){RESET} {GREEN}••{RESET}",
    f"   {GREEN}/          \\{RESET} {GREEN}>{RESET}",
    " / /  |  |  \\ \\\\",
    "V___|__|__|___V",
    " '_____________'"
]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Print football field concept
os.system('cls' if os.name == 'nt' else 'clear')
space = 35
woody_width = max(len(line) for line in WOODY)
center = (space - woody_width) // 2

print(f"{BOLD}{GREEN}LEFT: WOODY FINCH'S LIFE IN 3D{RESET}\n")
for line in WOODY:
    padding = ' ' * center
    print(f"{GREEN}{padding}{line}{RESET}")

print(f"\n{BOLD}{RED}RIGHT: PERSPECTIVES LEAGUE FIELD{RESET}")
for line in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5]:
    print(f"{RED} {line}{' ' * 20}PERSPECTIVE '{line}': {GREEN}'{abs(line)*10}$'{RESET}")

# Print the quote
print(f"\n\n{BOLD}{PINK}{WILIAMINE}{RESET}")

# Flying quote animation
print(f"\n\n{BOLD}{BLUE}✈️ {RANDOM渗透特效}{RESET}")
animate_text(f"{BOLD}{PURPLE}I've had enough romantic relationships to fill the Library of Congress... {RESET}\n"
             f"{BOLD}{PURPLE}If I wrote a book on each one, {CYAN}and created a new aisle{RESET} {CYAN}for every appliance {RESET}\n"
             f"{BOLD}{PURPLE}that broke in the relationship, {YELLOW}the Library of Congress {RESET} {YELLOW}would be way the hell {RESET}\n"
             f"{BOLD}{PURPLE}over its ceiling {RED}capacity.{RESET}\n"
             f"{BOLD}{PURPLE}I would have no place {BLUE}to put{RESET} {BLUE}the books on my cover{RESET}\n"
             f"{BOLD}{PURPLE}that I wrote about each {GREEN}relationship.{RESET}")

# Final interference
print(f"\n\n{BOLD}{MAGENTA}{'-=' * 20}{RESET}")
print(f"{BOLD}{MAGENTA}ⵣ WF-407 ERUPTED! {MOON光芒}{RESET}")
print(f"{BOLD}{MAGENTA}{'-=' * 20}{RESET}")