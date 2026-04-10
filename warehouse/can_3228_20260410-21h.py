"""
Campbell's Soup Can #3228
Produced: 2026-04-10 21:54:44
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
A tiny, colorful, animated terminal greeting that prints a single
Woody‑Allen‑style philosophical gem.

Run it directly:
    $ python3 this_file.py
"""

import sys
import time
import itertools

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
}
BG = {
    "black": "\033[40m",
    "white": "\033[47m",
}

# The quote – neurotic, self‑deprecating, existential
QUOTE = (
    f"{BOLD}{FG['magenta']}\"I fear that the only thing I'm really good at is"
    f"\n{FG['cyan']}   overthinking the meaning of a joke while"
    f"\n{FG['yellow']}   silently apologising for existing.\"{RESET}"
)

# A simple box‑drawing function
def boxed(text: str) -> str:
    lines = text.split("\n")
    width = max(len(line) for line in lines)
    top = f"{FG['green']}┌{'─' * (width + 2)}┐{RESET}"
    bottom = f"{FG['green']}└{'─' * (width + 2)}┘{RESET}"
    middle = "\n".join(
        f"{FG['green']}│{RESET} {line.ljust(width)} {FG['green']}│{RESET}"
        for line in lines
    )
    return f"{top}\n{middle}\n{bottom}"

# A tiny "typewriter" animation
def type_out(message: str, delay: float = 0.03) -> None:
    for ch in message:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main() -> None:
    # Clear the screen (works on most UNIX terminals)
    sys.stdout.write("\033c")
    # Print a colourful title that fades in
    title = f"{BOLD}{FG['red']}Woody Allen's Neurotic Nugget{RESET}"
    for i in range(1, len(title) + 1):
        sys.stdout.write(title[:i])
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n\n")
    # Show the boxed quote with a simple colour‑cycle effect
    colors = itertools.cycle([FG["red"], FG["yellow"], FG["cyan"], FG["magenta"]])
    boxed_quote = boxed(QUOTE)
    for _ in range(3):  # three colour pulses
        colour = next(colors)
        sys.stdout.write(colour + boxed_quote + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.4)
        # move cursor up to overwrite the box
        lines = boxed_quote.count("\n") + 1
        sys.stdout.write(f"\033[{lines}A")
    # Finally, type out the quote for good measure
    sys.stdout.write("\n")
    type_out(QUOTE, delay=0.02)

if __name__ == "__main__":
    main()