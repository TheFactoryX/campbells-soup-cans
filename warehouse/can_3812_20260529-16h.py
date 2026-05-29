"""
Campbell's Soup Can #3812
Produced: 2026-05-29 16:53:24
Worker: OpenAI: GPT-5.4 (openai/gpt-5.4)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import shutil
import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

COLORS = {
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "white": "\033[97m",
    "gray": "\033[90m",
    "red": "\033[91m",
}


def color(text, *styles):
    return "".join(styles) + text + RESET


def center_text(text, width):
    return text.center(width)


def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def type_line(text, delay=0.012):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def boxed_lines(lines, width, border_color, text_color):
    inner = width - 4
    top = color("╔" + "═" * (width - 2) + "╗", border_color, BOLD)
    bottom = color("╚" + "═" * (width - 2) + "╝", border_color, BOLD)
    body = []
    for line in lines:
        padded = line.ljust(inner)
        body.append(color("║ ", border_color, BOLD) + color(padded, text_color) + color(" ║", border_color, BOLD))
    return [top] + body + [bottom]


def main():
    width = max(60, min(88, shutil.get_terminal_size((80, 24)).columns))

    brain = [
        color("        .-''''-.", COLORS["magenta"], BOLD),
        color("      .'  .-.   '.", COLORS["magenta"], BOLD),
        color("     /   /   \\    \\", COLORS["magenta"], BOLD),
        color("    ;   |  o  |    ;", COLORS["magenta"], BOLD),
        color("    |   \\  ^  /    |", COLORS["magenta"], BOLD),
        color("    ;    '---'     ;", COLORS["magenta"], BOLD),
        color("     \\  .-'''-.   /", COLORS["magenta"], BOLD),
        color("      '._panic_.'", COLORS["yellow"], BOLD),
    ]

    title = color("ANXIETY, BUT MAKE IT PHILOSOPHICAL", COLORS["cyan"], BOLD)
    subtitle = color("a tiny existential cabaret", COLORS["gray"], DIM)

    quote = (
        "I tried to find the meaning of life, but it got nervous, "
        "started apologizing, and asked if we could just be friends."
    )

    wrapped = textwrap.wrap(quote, width=width - 10)
    box = boxed_lines(wrapped, min(width - 6, max(len(max(wrapped, key=len)) + 4, 40)), COLORS["blue"], COLORS["white"])

    clear()

    for line in brain:
        print(center_text(line, width))
        time.sleep(0.05)

    print()
    print(center_text(title, width))
    print(center_text(subtitle, width))
    print()
    time.sleep(0.35)

    for line in box:
        print(center_text(line, width))
        time.sleep(0.08)

    print()
    blink = [
        color("   existence.exe", COLORS["yellow"], BOLD) + color(" ... loading", COLORS["gray"]),
        color("   existence.exe", COLORS["yellow"], BOLD) + color(" ... crashing", COLORS["red"], BOLD),
        color("   existence.exe", COLORS["yellow"], BOLD) + color(" ... overthinking", COLORS["magenta"], BOLD),
    ]
    for line in blink:
        print(center_text(line, width))
        time.sleep(0.28)

    print(RESET)


if __name__ == "__main__":
    main()