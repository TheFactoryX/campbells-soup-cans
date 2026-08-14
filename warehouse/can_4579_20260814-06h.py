"""
Campbell's Soup Can #4579
Produced: 2026-08-14 06:42:10
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def main():
    quote_lines = [
        ("Do I exist when no one is watching?", 31),
        ("Probably. But is that any better than existing when everyone is?", 33),
        ("At least when no one is watching, I don't have to pretend to be awake.", 36)
    ]
    max_length = max(len(line[0]) for line in quote_lines)
    border_length = max_length + 4

    top = "╔" + "═" * border_length + "╗"
    bottom = "╚" + "═" * border_length + "╝"

    print(f"\033[31m{top}\033[0m")
    for line, color in quote_lines:
        padded_line = line.ljust(max_length)
        content = f"║ {padded_line} ║"
        print(f"\033[{color}m{content}\033[0m")
    print(f"\033[31m{bottom}\033[0m")

if __name__ == "__main__":
    main()