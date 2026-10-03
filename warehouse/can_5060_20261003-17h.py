"""
Campbell's Soup Can #5060
Produced: 2026-10-03 17:57:17
Worker: Space Bunny Alpha (stealth/space-bunny-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import textwrap
import time

quote = "The meaning of life, I've decided, is to keep busy postponing the question of what it is."

def main():
    width = 72
    inner_width = width - 4
    lines = textwrap.wrap(quote, width=inner_width)
    colors = [
        "\033[95m",
        "\033[96m",
        "\033[93m",
        "\033[92m",
        "\033[94m",
    ]
    reset = "\033[0m"
    bold = "\033[1m"

    print(f"{bold}\033[96m}+{'-' * width}+\033[0m")

    character_index = 0
    for line in lines:
        sys.stdout.write(f"{bold}\033[96m}| \033[0m")
        for character in line:
            color = colors[character_index % len(colors)]
            sys.stdout.write(f"{color}{character}{reset}")
            sys.stdout.flush()
            time.sleep(0.012)
            character_index += 1

        padding = inner_width - len(line)
        sys.stdout.write(" " * padding)
        sys.stdout.write(f"{bold}\033[96m} |\033[0m\n")

    print(f"{bold}\033[96m}+{'-' * width}+\033[0m")

if __name__ == "__main__":
    main()