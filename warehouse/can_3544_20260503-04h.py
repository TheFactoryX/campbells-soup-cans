"""
Campbell's Soup Can #3544
Produced: 2026-05-03 04:11:28
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, colorful, animated Woody‑Allen‑style philosophical quote printer.
Run the script directly – no external libraries required.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour codes
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# A handful of pleasant foreground colours
FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}

# ----------------------------------------------------------------------
# The quote – think neurotic, self‑deprecating, existential…
# ----------------------------------------------------------------------
quote = (
    "I’m terrified of the meaning of life, "
    "but even more terrified of the day I finally understand it."
)

# ----------------------------------------------------------------------
# Helper: type‑writer effect with colour cycling
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04) -> None:
    """
    Print *text* character‑by‑character, cycling foreground colours.
    """
    colours = itertools.cycle([FG["cyan"], FG["magenta"], FG["yellow"]])
    for ch in text:
        sys.stdout.write(next(colours) + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Helper: draw a decorative box around the quote
# ----------------------------------------------------------------------
def boxed(text: str, padding: int = 2) -> str:
    """
    Return *text* surrounded by a colourful ASCII art box.
    """
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    horiz = "─" * (max_len + padding * 2)
    top    = f"{FG['green']}┌{horiz}┐{RESET}"
    bottom = f"{FG['green']}└{horiz}┘{RESET}"
    middle = []
    for line in lines:
        space = " " * (max_len - len(line))
        middle.append(
            f"{FG['green']}│{RESET}"
            f"{' ' * padding}{line}{space}{' ' * padding}"
            f"{FG['green']}│{RESET}"
        )
    return "\n".join([top] + middle + [bottom])

# ----------------------------------------------------------------------
# Main animation
# ----------------------------------------------------------------------
def main() -> None:
    # Clear the terminal (works on most Unix terminals & Windows 10+)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Display a brief intro with a slow fade‑in
    intro = f"{BOLD}{FG['red']}~*~ Woody‑Allen’s Existential Corner ~*~{RESET}"
    for i in range(1, len(intro) + 1):
        sys.stdout.write(intro[:i] + "\r")
        sys.stdout.flush()
        time.sleep(0.03)
    time.sleep(0.6)

    # Print the boxed quote, then type‑write the quote inside
    box = boxed("")
    print(box)               # empty box as a placeholder
    time.sleep(0.3)

    # Overwrite the empty box with the real content
    box_lines = box.split("\n")
    # Compute where the interior lines start (the second line)
    for idx, line in enumerate(box_lines):
        if "│" in line:
            # replace the inside of the box with the quote line by line
            content = quote if idx == 1 else ""
            padded = f"{FG['green']}│{RESET}{' ' * 2}{content}{' ' * (len(line)-len(content)-4)}{FG['green']}│{RESET}"
            sys.stdout.write("\033[{}A".format(len(box_lines)-idx))  # move cursor up
            sys.stdout.write("\r" + padded + "\n")
            sys.stdout.flush()
            time.sleep(0.4)

    # Finally, animate the quote with a type‑writer effect
    sys.stdout.write("\n")
    typewriter(quote, delay=0.05)

    # A little outro
    smiley = f"{FG['yellow']}{BOLD}:){RESET}"
    sys.stdout.write(f"\n{smiley}  {FG['blue']}Thanks for pondering the absurdity with me!{RESET}\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()