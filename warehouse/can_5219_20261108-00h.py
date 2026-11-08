"""
Campbell's Soup Can #5219
Produced: 2026-11-08 00:36:40
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

# ANSI escape codes
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

QUOTE = (
    "I'm not afraid of death. I just don't want to be there when it happens—"
    "especially if there's a cover charge, a two-drink minimum, and I'm not on the list."
)


def wrap(text, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 > width:
            lines.append(current)
            current = word
        else:
            current = (current + " " + word).strip()
    if current:
        lines.append(current)
    return lines


def slow_type(text, delay=0.025, color=WHITE, end="\n"):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def draw_box_edge(left, fill, right, color, width):
    print(color + left + fill * width + right + RESET)


def main():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    width = 68
    print()
    draw_box_edge("╔", "═", "╗", CYAN, width)
    print(BOLD + MAGENTA + f"{'WOODY ALLEN: PHILOSOPHY FOR THE NEUROTIC':^{width}}" + RESET)
    draw_box_edge("╚", "═", "╝", CYAN, width)
    print()

    time.sleep(0.4)
    slow_type(f"{YELLOW}🎭 Today's existential crisis:{RESET}\n", delay=0.03, color=YELLOW)
    time.sleep(0.3)

    wrapped = wrap(QUOTE, width - 6)
    inner_w = max(len(line) for line in wrapped) + 2

    print(BLUE + "┌" + "─" * inner_w + "┐" + RESET)
    for line in wrapped:
        sys.stdout.write(BLUE + "│ " + RESET)
        slow_type(line, delay=0.02, color=WHITE, end="")
        padding = inner_w - len(line) - 1
        print(" " * padding + BLUE + " │" + RESET)
    print(BLUE + "└" + "─" * inner_w + "┘" + RESET)
    print()

    time.sleep(0.3)
    slow_type(f"{DIM}– A very nervous person, probably{RESET}", delay=0.02, color=GREEN)
    print()
    time.sleep(0.2)
    slow_type(
        f"{RED}(If you laughed, you're in denial. If you didn't laugh, you're in deeper denial.){RESET}",
        delay=0.02,
        color=RED,
    )
    print()
    draw_box_edge("╔", "═", "╗", CYAN, width)
    draw_box_edge("╚", "═", "╝", CYAN, width)
    print()


if __name__ == "__main__":
    main()