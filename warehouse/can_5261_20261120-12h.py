"""
Campbell's Soup Can #5261
Produced: 2026-11-20 12:54:16
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
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

QUOTE = (
    "I don't want to achieve immortality through my work. "
    "I want to achieve it by simply not dying, "
    "which is turning out to be a full-time job with no vacation days."
)

ATTRIBUTION = "— Woody Allen (probably, and with mild panic)"
WRAP_WIDTH = 54


def wrap(text, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = (current + " " + word).strip()
        if len(candidate) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def typewriter_inline(text, color=MAGENTA, delay=0.05):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        if char in ".!?":
            time.sleep(random.uniform(0.15, 0.45))
        elif char == ",":
            time.sleep(random.uniform(0.05, 0.15))
        else:
            time.sleep(delay)


def main():
    # Clear the terminal
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Neurotic boot sequence
    boot = ">>> booting existential_dread.exe ..."
    for ch in boot:
        sys.stdout.write(CYAN + BOLD + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    time.sleep(0.4)

    lines = wrap(QUOTE, WRAP_WIDTH)
    box_width = WRAP_WIDTH + 4

    # Top of the box
    print(CYAN + "╔" + "═" * box_width + "╗" + RESET)
    print(CYAN + "║" + " " * box_width + "║" + RESET)
    title = "WOODY ALLEN PHILOSOPHY GENERATOR"
    print(CYAN + "║  " + BOLD + YELLOW + title + RESET + " " * (box_width - 2 - len(title)) + "║" + RESET)
    print(CYAN + "║" + " " * box_width + "║" + RESET)
    print(CYAN + "╠" + "═" * box_width + "╣" + RESET)

    # The quote, typed out line by line
    for line in lines:
        sys.stdout.write(CYAN + "║  " + RESET)
        typewriter_inline(line, MAGENTA)
        padding = " " * (WRAP_WIDTH - len(line))
        sys.stdout.write(CYAN + padding + "  ║" + RESET + "\n")
        time.sleep(0.3)

    # Bottom of the box
    print(CYAN + "║" + " " * box_width + "║" + RESET)
    attr_pad_left = (box_width - len(ATTRIBUTION)) // 2
    attr_pad_right = box_width - len(ATTRIBUTION) - attr_pad_left
    print(CYAN + "║" + " " * attr_pad_left + RED + BOLD + ATTRIBUTION + RESET + " " * attr_pad_right + "║" + RESET)
    print(CYAN + "╚" + "═" * box_width + "╝" + RESET)
    print()

    # ASCII art: neurotic glasses
    print(YELLOW + BOLD)
    print("        ___           ___")
    print("       /   \\         /   \\")
    print("      | O O |       | O O |")
    print("       \\ - /         \\ - /")
    print("        | |           | |")
    print("       /   \\         /   \\")
    print(RESET)

    # Final blinking status
    status = "  [ System stable. Panic levels: nominal. ]"
    sys.stdout.write(CYAN + BOLD + status + RESET)
    sys.stdout.flush()
    for _ in range(5):
        time.sleep(0.2)
        sys.stdout.write(CYAN + BOLD + "█" + RESET)
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
    print("\n")


if __name__ == "__main__":
    main()