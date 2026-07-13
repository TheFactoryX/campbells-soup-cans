"""
Campbell's Soup Can #4184
Produced: 2026-07-13 17:22:33
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
DIM = "\033[2m"

quote = "I'm not afraid of existential oblivion; I'm just terrified that in the vast, indifferent void, I'll still be able to hear my mother asking why I'm not a lawyer."

def wrap(text, width):
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= width:
            current += w + " "
        else:
            lines.append(current.strip())
            current = w + " "
    lines.append(current.strip())
    return lines

def main():
    box_width = 64
    lines_full = wrap(quote, box_width - 4)
    
    glasses = [
        "      ___________________________      ",
        "     /  _______________________  \\    ",
        "    |  /       |       |      \\  |    ",
        "    | |   O    |   O   |   O  | |    ",
        "    |  \\       |       |      /  |    ",
        "     \\  \\_____|_______|_____/  /     ",
        "      \\_______________________/      ",
    ]
    
    for i in range(len(quote) + 1):
        typed_so_far = quote[:i]
        lines = wrap(typed_so_far, box_width - 4)
        while len(lines) < len(lines_full):
            lines.append("")
        if i < len(quote) and lines:
            lines[-1] = (lines[-1] + "\033[5m█\033[0m")[:box_width-2]
            
        sys.stdout.write("\033[2J\033[H")
        
        for line in glasses:
            print(CYAN + BOLD + line.center(80) + RESET)
        print()
        
        print(YELLOW + "+" + "-" * (box_width - 2) + "+" + RESET)
        for line in lines:
            padded = line.ljust(box_width - 4)
            print(YELLOW + "| " + RESET + MAGENTA + padded + YELLOW + " |" + RESET)
        print(YELLOW + "+" + "-" * (box_width - 2) + "+" + RESET)
        
        time.sleep(0.015)
        
    time.sleep(0.5)
    sys.stdout.write("\033[2J\033[H")
    for line in glasses:
        print(CYAN + BOLD + line.center(80) + RESET)
    print()
    print(YELLOW + "+" + "-" * (box_width - 2) + "+" + RESET)
    for line in lines_full:
        print(YELLOW + "| " + RESET + MAGENTA + line.ljust(box_width - 4) + YELLOW + " |" + RESET)
    print(YELLOW + "+" + "-" * (box_width - 2) + "+" + RESET)
    
    print()
    print(BOLD + " " * 15 + "-- allegedly Woody Allen (via Python)" + RESET)
    
    thoughts = ["\t*checks if meaning of life is in mailbox*",
                "\t*realizes it's not, panics quietly*",
                "\t*muses on mortality and matzo ball soup*"]
    for t in thoughts:
        print(DIM + CYAN + t + RESET)
        time.sleep(1)
        sys.stdout.write("\033[A\033[K")
    print(DIM + CYAN + "\t*existential silence*" + RESET)

if __name__ == "__main__":
    main()