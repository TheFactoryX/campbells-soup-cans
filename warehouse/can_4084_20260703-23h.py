"""
Campbell's Soup Can #4084
Produced: 2026-07-03 23:18:14
Worker: Anthropic: Claude Fable 5 (anthropic/claude-fable-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
 ~ THE EXISTENTIAL FORTUNE COOKIE ~
 A neurotic quote generator (serves one)
"""

import sys
import time
import random

# ---------- ANSI helpers ----------
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"

def fg(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

CREAM   = fg(255, 244, 214)
GOLD    = fg(255, 200,  87)
ROSE    = fg(255, 130, 150)
MINT    = fg(140, 235, 190)
SKY     = fg(130, 190, 255)
LAV     = fg(200, 160, 255)
GRAY    = fg(150, 150, 150)

PALETTE = [GOLD, ROSE, MINT, SKY, LAV]

QUOTE = ("The universe is expanding, my anxiety is expanding, "
         "and yet my apartment somehow keeps getting smaller. "
         "I asked God for a sign — He sent me a parking ticket.")

ATTRIB = "— definitely not Woody Allen, probably my therapist"


def slow_print(text, delay=0.02, color=CREAM, end="\n"):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def rainbow_line(text):
    out = ""
    for i, ch in enumerate(text):
        out += PALETTE[i % len(PALETTE)] + ch
    return out + RESET


def wrap(text, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        if len(line) + len(w) + 1 > width:
            lines.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        lines.append(line)
    return lines


def marquee_glasses():
    # Woody's iconic glasses, blinking into existence
    frames = [
        "   .-.   .-.  ",
        "  ( o )-( o ) ",
        "  ( - )-( - ) ",
        "  ( o )-( o ) ",
    ]
    art = [
        GOLD + "        _______" + RESET,
        GOLD + "       /       \\" + RESET,
    ]
    for line in art:
        print(line)
    for _ in range(3):
        for f in frames[1:3]:
            sys.stdout.write("\r" + GOLD + "      " + f + RESET)
            sys.stdout.flush()
            time.sleep(0.25)
    sys.stdout.write("\r" + GOLD + "      " + frames[1] + RESET + "\n")
    print(GOLD + "         `-'  " + DIM + " *nervous adjusting of glasses*" + RESET)
    print()


def thinking_dots():
    msg = "contemplating the void (and my rent)"
    sys.stdout.write(DIM + ITALIC + "  " + msg + RESET)
    sys.stdout.flush()
    for _ in range(6):
        sys.stdout.write(DIM + "." + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")


def boxed_quote(text, attrib, width=54):
    lines = wrap(text, width)
    top    = "  ╭" + "─" * (width + 4) + "╮"
    bottom = "  ╰" + "─" * (width + 4) + "╯"

    print(SKY + top + RESET)
    print(SKY + "  │" + " " * (width + 4) + "│" + RESET)
    for ln in lines:
        pad = width - len(ln)
        sys.stdout.write(SKY + "  │  " + RESET)
        slow_print(ln, delay=0.035, color=BOLD + CREAM, end="")
        sys.stdout.write(" " * pad + SKY + "  │" + RESET + "\n")
    print(SKY + "  │" + " " * (width + 4) + "│" + RESET)

    apad = width - len(attrib)
    print(SKY + "  │  " + RESET + " " * apad + ITALIC + GRAY + attrib + RESET + SKY + "  │" + RESET)
    print(SKY + bottom + RESET)


def sparkle_footer():
    stars = "  " + " ".join(random.choice("✦✧·*") for _ in range(24))
    print()
    print(rainbow_line(stars))
    print(DIM + ITALIC + "   (existential dread sold separately)" + RESET)
    print()


def main():
    print()
    print(rainbow_line("  ═══════ THE NEUROTIC ORACLE SPEAKS ═══════"))
    print()
    marquee_glasses()
    thinking_dots()
    boxed_quote(f"\u201c{QUOTE}\u201d", ATTRIB)
    sparkle_footer()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + DIM + "  Fine. Even my program gets abandoned." + RESET)