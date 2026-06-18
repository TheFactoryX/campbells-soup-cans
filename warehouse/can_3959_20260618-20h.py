"""
Campbell's Soup Can #3959
Produced: 2026-06-18 20:38:40
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

# Woody Allen style philosophical quote with colorful ASCII framing

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    border = "+----------------------------------------+"
    RED = "\033[31m"
    BG_BLACK = "\033[40m"
    RESET = "\033[0m"
    print(f"{RED}{BG_BLACK}{border}{RESET}")
    print(f"{RED}{BG_BLACK}| {quote} |{RESET}")
    print(f"{RED}{BG_BLACK}{border}{RESET}")

if __name__ == "__main__":
    main()