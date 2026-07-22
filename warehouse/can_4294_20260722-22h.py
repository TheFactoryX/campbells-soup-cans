"""
Campbell's Soup Can #4294
Produced: 2026-07-22 22:15:44
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os

# Color definitions
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
NC = "\033[0m"

def clear():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()

    # Decorative ASCII frame
    print(YELLOW + "╔════════════════════════════════════════════════════════════════╗" + NC)
    print(CYAN + "║ " + WHITE + "Woody’s Existential Coffee Bar " + " " * 30 + CYAN + "║" + NC)
    print(YELLOW + "╚════════════════════════════════════════════════════════════════╝" + NC)
    print()

    # Simple coffee cup ASCII art
    cup = f"""{GREEN}
           ( )
          (O o)
          / ^ \\
    {NC}"""
    print(cup)
    print()

    # The philosophical quote in Woody Allen's style
    quote = (
        RED +
        "“I'm not afraid of the universe; I'm just embarrassed by how badly it's organized—think of it as a cosmic soufflé with too much flour and too little charm.”"
        + NC
    )

    # Print the quote inside a nice box
    width = 78
    border = YELLOW + "+" + "-" * width + "+" + NC
    print(border)
    print(CYAN + "|" + " " + quote + " " + CYAN + "|" + NC)
    print(border)

if __name__ == "__main__":
    main()