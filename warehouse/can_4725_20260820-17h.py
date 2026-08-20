"""
Campbell's Soup Can #4725
Produced: 2026-08-20 17:45:17
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

# ANSI colour codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

quote = (
    f"{RED}╔{'─'*44}╗{RESET}\n"
    f"{RED}║{CYAN}  \"I am not afraid of death; I just don't want to be there when it happens.\"{RED} ║{RESET}\n"
    f"{RED}║{CYAN}  {YELLOW} — {RESET}{GREEN}Woody Allen{RED}{CYAN}{RESET}\n"
    f"{RED}╚{'─'*44}╝{RESET}"
)

print(quote, end="")