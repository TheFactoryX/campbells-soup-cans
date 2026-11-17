"""
Campbell's Soup Can #5252
Produced: 2026-11-17 14:25:31
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    width = len(quote)  # 70 characters
    top = '+' + '-' * width + '+'

    # Magenta top border
    print("\033[35m" + top + "\033[0m")
    # Cyan empty line
    print("\033[36m" + '|' + ' ' * width + '|' + "\033[0m")
    # Yellow quote inside the box
    print("\033[33m" + '|' + quote + '|' + "\033[0m")
    # Magenta bottom border
    print("\033[35m" + top + "\033[0m")

if __name__ == '__main__':
    main()