"""
Campbell's Soup Can #5145
Produced: 2026-10-21 19:20:41
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def main():
    RED = "\033[1;31m"
    YELLOW = "\033[1;33m"
    RESET = "\033[0m"
    width = 75
    top_bottom = f"{RED}+{'─'*(width-2)}+{RESET}"
    middle = f"{RED}|{YELLOW} I'm not afraid of death; I just don't want to be there when it happens. {RESET}{RED}|{RESET}"
    print(top_bottom)
    print(middle)
    print(top_bottom)

if __name__ == "__main__":
    main()