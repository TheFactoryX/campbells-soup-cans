"""
Campbell's Soup Can #1532
Produced: 2026-01-11 06:48:55
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def print_woody():
    quote = (
        "I’m not afraid of death; I just don’t want to be there when it happens… "
        "but also I’m terrified of being forgotten."
    )
    border = "╔════════════════════════╗"
    empty = "║                         ║"
    closing = "╚════════════════════════╝"

    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(RED + border + RESET)
    print(YELLOW + empty + RESET, YELLOW + quote + RESET, YELLOW + empty + RESET)
    print(RED + closing + RESET)


if __name__ == "__main__":
    print_woody()