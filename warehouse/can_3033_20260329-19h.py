"""
Campbell's Soup Can #3033
Produced: 2026-03-29 19:02:41
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
}

quote = (
    "I spent years searching for the meaning of life, and it turns out "
    "life was hiding under my anxiety the whole time—which is ironic, "
    "because I only looked there every fifteen minutes."
)

width = 66
wrapped = textwrap.wrap(quote, width=width - 4)

def color(text, *styles):
    return "".join(styles) + text + RESET

def center_line(text, total_width):
    pad = max(0, total_width - len(text))
    left = pad // 2
    right = pad - left
    return " " * left + text + " " * right

def slow_print(text, delay=0.006):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def draw():
    face = [
        color("        .-''''-.        ", COLORS["yellow"], BOLD),
        color("      .'  .-.   '.      ", COLORS["yellow"], BOLD),
        color("     /   (o o)    \\     ", COLORS["yellow"], BOLD),
        color("    |     ^        |    ", COLORS["yellow"], BOLD),
        color("    |   \\___/      |    ", COLORS["yellow"], BOLD),
        color("     \\  '---'     /     ", COLORS["yellow"], BOLD),
        color("      '.______.-'       ", COLORS["yellow"], BOLD),
        color("         /|||\\          ", COLORS["gray"]),
    ]

    title = color(" existential stand-up transmission ", COLORS["cyan"], BOLD)
    top = color("╔" + "═" * (width + 2) + "╗", COLORS["magenta"], BOLD)
    bottom = color("╚" + "═" * (width + 2) + "╝", COLORS["magenta"], BOLD)
    divider = color("╠" + "═" * (width + 2) + "╣", COLORS["magenta"], BOLD)

    print("\033[2J\033[H", end="")

    for line in face:
        print(center_line(line, width + 4))

    print()
    print(center_line(title, width + 4))
    print(top)
    for line in wrapped:
        content = " " + line.ljust(width) + " "
        print(color("║", COLORS["magenta"], BOLD) + color(content, COLORS["white"]) + color("║", COLORS["magenta"], BOLD))
    print(divider)
    sig = center_line("- a suspiciously neurotic philosopher", width)
    print(color("║", COLORS["magenta"], BOLD) + color(" " + sig + " ", COLORS["blue"], DIM) + color("║", COLORS["magenta"], BOLD))
    print(bottom)

    print()
    slow_print(color("thinking", COLORS["gray"], DIM), delay=0.03)
    for _ in range(3):
        for dots in ["·  ", "·· ", "···"]:
            print("\r" + color("meaning of life " + dots, COLORS["cyan"], DIM), end="", flush=True)
            time.sleep(0.28)
    print("\r" + " " * 30, end="\r")
    slow_print(color("result: still worried.", COLORS["yellow"], BOLD), delay=0.02)

if __name__ == "__main__":
    draw()