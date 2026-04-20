"""
Campbell's Soup Can #3377
Produced: 2026-04-20 19:33:41
Worker: Elephant (openrouter/elephant-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# ============ CONFIG ============
BG_COLOR = "\033[48;2;5;5;15m"
TEXT_COLOR = "\033[38;2;220;220;230m"
HIGHLIGHT_COLOR = "\033[38;2;255;215;0m"
ERROR_COLOR = "\033[38;2;220;100;100m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
CLEAR = "\033[2J"
HOME = "\033[H"

QUOTE = (
    "I’m terrified of the inevitable nothingness, "
    "so I distract myself with trivialities, "
    "which is exactly how I end up writing "
    "one-sentence philosophies at 3 a.m."
)

ART_LINES = [
    "          ,#####,           ",
    "        ,#((((#\\          ",
    "       #/*  O  O\\*#         ",
    "       #\\  ---  /#         ",
    "        #\\   _   /#          ",
    "         #\\_(_)//           ",
    "          \\___/'            ",
    "           ||||             ",
    "          ~~~~~            ",
]

def type_writer(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def draw_frame(lines, width=56, padding=2):
    top = "+" + "-" * width + "+"
    blank = "|" + " " * width + "|"
    out = [top, blank]
    for line in lines:
        padding_space = " " * ((width - len(line)) // 2)
        out.append("|" + padding_space + line + padding_space + " " * (width - len(line) - len(padding_space)) + "|")
    out.append(blank)
    out.append(top)
    return "\n".join(out)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(CLEAR + HOME + BG_COLOR + TEXT_COLOR)

    # Title
    title = " WOODY-ISH PHILOSOPHY "
    print("\n" + " " * 18 + HIGHLIGHT_COLOR + BOLD + UNDERLINE + title + RESET)
    time.sleep(0.5)

    # ASCII Art
    print()
    for line in ART_LINES:
        print(" " * 10 + HIGHLIGHT_COLOR + line + RESET)
    time.sleep(0.6)
    print()

    # Frame around quote
    framed = draw_frame(QUOTE.split(), width=56, padding=3)
    print(" " + ERROR_COLOR + framed + RESET)
    time.sleep(0.5)

    # Animated typing of the quote inside the frame
    print("\n" + " " * 26 + ITALIC + HIGHLIGHT_COLOR + "The revelation:\033[0m")
    time.sleep(0.4)
    print(" " * 18 + TEXT_COLOR)
    type_writer(QUOTE, delay=0.04)
    print(TEXT_COLOR)

    # Footer
    time.sleep(0.5)
    footer1 = "Existential dread is just fear with better lighting."
    footer2 = "Stay neurotic — it’s the only authentic way to be inauthentic."
    print(" " * 14 + ERROR_COLOR + footer1 + RESET)
    time.sleep(0.35)
    print(" " * 14 + ERROR_COLOR + footer2 + RESET)

    print("\n" + BG_COLOR + TEXT_COLOR)
    print(" " * 22 + "─┬─ ｡°(° ۶ ۶ °) ｡°─┬─ ")
    print(" " * 20 + "  (  ≧ ﹏ ≦ )   — Woody")
    print(" " * 22 + "─┴─ ｡°(° ︵ ︵) ｡°─┴─ ")
    print(RESET)

if __name__ == "__main__":
    main()