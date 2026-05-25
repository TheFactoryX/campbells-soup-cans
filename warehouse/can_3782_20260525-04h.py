"""
Campbell's Soup Can #3782
Produced: 2026-05-25 04:55:22
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, self‑contained program that prints a single Woody‑Allen‑style
philosophical quip with a splash of colour and a little “typewriter”
animation.  No external libraries required – just pure ANSI escape codes.
"""

import sys
import time

# ----------------------------------------------------------------------
# ANSI colour / style helpers
# ----------------------------------------------------------------------
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

FG_RED    = "\033[31m"
FG_GREEN  = "\033[32m"
FG_YELLOW = "\033[33m"
FG_BLUE   = "\033[34m"
FG_MAGENTA= "\033[35m"
FG_CYAN   = "\033[36m"
FG_WHITE  = "\033[37m"

BG_BLACK  = "\033[40m"

# Choose a palette that works on most terminals
PALETTE = [FG_CYAN, FG_MAGENTA, FG_YELLOW, FG_GREEN, FG_BLUE]

# ----------------------------------------------------------------------
# The quote (feel free to tweak the wording)
# ----------------------------------------------------------------------
quote = (
    "I think the meaning of life is like a bad joke:\n"
    " you keep waiting for the punchline, but the joke is\n"
    " that there isn’t one – and the audience is yourself."
)

# ----------------------------------------------------------------------
# Helper: print text one character at a time (typewriter effect)
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.03, colour: str = FG_WHITE) -> None:
    for ch in text:
        # Cycle colours for a subtle rainbow effect
        if ch != "\n":
            colour = PALETTE[(int(time.time()*10) + ord(ch)) % len(PALETTE)]
        else:
            colour = RESET
        sys.stdout.write(f"{colour}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ----------------------------------------------------------------------
# Helper: draw a simple ASCII box around the quote
# ----------------------------------------------------------------------
def boxed(text: str) -> str:
    lines = text.splitlines()
    max_len = max(len(line) for line in lines)
    top    = f"{FG_WHITE}{BOLD}+{'-' * (max_len + 2)}+{RESET}"
    bottom = f"{FG_WHITE}{BOLD}+{'-' * (max_len + 2)}+{RESET}"
    boxed_lines = [top]
    for line in lines:
        padded = line + " " * (max_len - len(line))
        boxed_lines.append(f"{FG_WHITE}{BOLD}|{RESET} {padded} {FG_WHITE}{BOLD}|{RESET}")
    boxed_lines.append(bottom)
    return "\n".join(boxed_lines)

# ----------------------------------------------------------------------
# Main animation
# ----------------------------------------------------------------------
def main() -> None:
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    frame = """
{c1}      .-""""-.
{c2}    / -   -  \\
{c3}   |  .-. .- |
{c4}   |  \\ o| o/
{c5}    \\   \\_/ /
{c6}     '-.__.-'   {reset}
""".strip("\n")

    # Print a quick “thinking” animation with the little stick‑figure
    for i in range(6):
        sys.stdout.write("\033[H")  # move cursor to top‑left after clear
        sys.stdout.write(frame.format(
            c1=FG_RED, c2=FG_GREEN, c3=FG_YELLOW,
            c4=FG_BLUE, c5=FG_MAGENTA, c6=FG_CYAN,
            reset=RESET))
        sys.stdout.flush()
        time.sleep(0.15)

    # Show the quote inside a box with a typewriter effect
    sys.stdout.write("\033[H")  # top‑left again
    boxed_text = boxed(quote)
    typewriter(boxed_text, delay=0.02)

    # Final flourish
    sys.stdout.write("\n" + FG_WHITE + BOLD + "— Woody Allen, probably\n" + RESET)
    sys.stdout.flush()


if __name__ == "__main__":
    main()