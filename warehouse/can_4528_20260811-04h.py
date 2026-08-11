"""
Campbell's Soup Can #4528
Produced: 2026-08-11 04:39:33
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    quote = "I'm not afraid of death; I check my email."
    RED   = "\033[31m"
    GREEN = "\033[32m"
    YELLOW= "\033[33m"
    RESET = "\033[0m"
    
    border = f"{RED}+{'-'*48}{RESET}"
    inner  = f"{GREEN}|{YELLOW}{quote}{RESET}{' '*6}{RESET}|"
    
    print("\n" + border)
    print(inner)
    print(border + "\n")

if __name__ == "__main__":
    main()