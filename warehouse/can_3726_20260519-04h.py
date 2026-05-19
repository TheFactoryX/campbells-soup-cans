"""
Campbell's Soup Can #3726
Produced: 2026-05-19 04:33:28
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sysdef main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    half1 = quote[:len(quote)//2]
    half2 = quote[len(quote)//2:].strip()
    width = 42  # total width including borders
    border = "+" + "-" * (width-2) + "+"
    side = "|" + " " * (width-2) + "|"
    line1 = "|  " + half1.ljust(width-6) + "  |"
    line2 = "|  " + half2.ljust(width-6) + "  |"
    lines = [border, side, line1, line2, side, border]
    cyan_bg = "\033[46m"
    magenta_fg = "\033[35m"
    reset = "\033[0m"
    for line in lines:
        if line.startswith("|") and line.endswith("|"):
            inner = line[1:-1]
            print(cyan_bg + magenta_fg + inner + reset)
        else:
            print(line)

if __name__ == "__main__":
    main()