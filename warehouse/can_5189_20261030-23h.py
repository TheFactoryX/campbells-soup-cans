"""
Campbell's Soup Can #5189
Produced: 2026-10-30 23:47:33
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def main():
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    reset = '\033[0m'
    underline = '\033[4m'

    quote = [
        "I'm terrified of dying, but also terrified of living,",
        "so I exist in this excruciating limbo,",
        "where every breath feels like a poorly timed punchline"
    ]

    # Typing the quote with color transitions
    colors = [red, green, blue]
    print(f"\n{red}{'='*40}{reset}")
    print(f"{red}Philosophy (Woody Allen Style){reset}")
    print(f"{red}{'='*40}{reset}\n")

    print(f"{blue}+{'-'*38}+{reset}\n")
    for idx, line in enumerate(quote):
        color = colors[idx % 3]
        print(f"\t{color}| ", end="")
        for c in line:
            print(c, end="", flush=True)
            time.sleep(0.04)
            if idx < len(quote)-1 and c == ',':
                time.sleep(0.2)
        print(f"{' '*(38 - len(line))}|{reset}  \n")
        time.sleep(0.5)

    print(f"{blue}+{'-'*38}+{reset}")
    time.sleep(2)

if __name__ == "__main__":
    main()