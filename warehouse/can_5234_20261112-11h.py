"""
Campbell's Soup Can #5234
Produced: 2026-11-12 11:12:37
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI escape codes
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
CLEAR_LINE = "\033[K"

BOX_WIDTH = 66

# The single Woody Allen-style philosophical quote
QUOTE_LINES = [
    "   I'm not afraid of death; I just don't want to be there",
    "   when it happens. Also, I'm pretty sure I left the stove on,",
    "   which feels like a more pressing existential crisis.",
]


def neurotic_type(text, color=YELLOW, delay=0.05):
    """Type out text with anxious typos and frantic backspace corrections."""
    i = 0
    while i < len(text):
        char = text[i]

        # Occasional neurotic typo on alphabetic characters
        if char.isalpha() and random.random() < 0.15:
            typo = random.choice("qwertyuiopasdfghjklzxcvbnm")
            sys.stdout.write(RED + typo + RESET)
            sys.stdout.flush()
            time.sleep(delay * 3)
            sys.stdout.write("\b \b")  # backspace, space, backspace
            sys.stdout.flush()
            time.sleep(delay)

        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        i += 1
        time.sleep(delay)


def box_border(left, fill, right, color=CYAN):
    return color + left + fill * (BOX_WIDTH - 2) + right + RESET


def main():
    # Opening nervous loading animation
    for i in range(14):
        dots = "." * (i % 4)
        sys.stdout.write(
            f"\r{MAGENTA}{BOLD}Summoning Woody Allen existential dread{dots}{RESET}{CLEAR_LINE}"
        )
        sys.stdout.flush()
        time.sleep(0.09)
    sys.stdout.write("\n\n")

    # Top border
    print(box_border("╔", "═", "╗"))

    # Title centered
    title_visible = "WOODY ALLEN: PHILOSOPHY & ANXIETY"
    title_colored = f"{BOLD}{title_visible}{RESET}"
    inner = BOX_WIDTH - 2
    pad_left = (inner - len(title_visible)) // 2
    pad_right = inner - pad_left - len(title_visible)
    print(CYAN + "║" + " " * pad_left + title_colored + " " * pad_right + CYAN + "║" + RESET)

    print(box_border("╠", "═", "╣"))
    print(CYAN + "║" + " " * inner + "║" + RESET)

    # Type the quote inside the box
    available = BOX_WIDTH - 4  # room for ║ space ... space ║
    for line in QUOTE_LINES:
        sys.stdout.write(CYAN + "║ " + RESET)
        display = line[:available]
        neurotic_type(display, color=YELLOW, delay=0.05)
        remaining = available - len(display)
        sys.stdout.write(" " * remaining)
        sys.stdout.write(CYAN + " ║" + RESET)
        sys.stdout.write("\n")
        time.sleep(0.25)

    print(CYAN + "║" + " " * inner + "║" + RESET)
    print(box_border("╚", "═", "╝"))

    # ASCII neurotic couch / existential dread figure
    print()
    print(GREEN + BOLD + "          ____" + RESET)
    print(GREEN + BOLD + "         /    \     <-- my therapist's couch" + RESET)
    print(GREEN + BOLD + "        /      \    <-- also where I contemplate mortality" + RESET)
    print(GREEN + BOLD + "       |  o  o  |" + RESET)
    print(GREEN + BOLD + "       |   ^   |" + RESET)
    print(GREEN + BOLD + "        \  --- /" + RESET)
    print(GREEN + BOLD + "         \___/   <-- me, existing" + RESET)
    print()

    # Footer
    footer = f"{MAGENTA}Existential dread successfully installed.{RESET}"
    print(footer.center(BOX_WIDTH + 10))


if __name__ == "__main__":
    main()