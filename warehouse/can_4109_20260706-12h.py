"""
Campbell's Soup Can #4109
Produced: 2026-07-06 12:58:32
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
    "I tried to find the meaning of life, but it kept getting nervous and "
    "changing the subject—so now I just panic politely and call it philosophy."
)

wrapped = textwrap.wrap(quote, width=58)
inner_width = max(len(line) for line in wrapped) + 2

def c(text, *styles):
    return "".join(styles) + text + RESET

def slow_print(text, delay=0.004):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def center_line(text, width):
    return text.center(width)

def box_lines(lines):
    top = c("╭" + "─" * inner_width + "╮", COLORS["magenta"], BOLD)
    bottom = c("╰" + "─" * inner_width + "╯", COLORS["magenta"], BOLD)
    body = [
        c("│", COLORS["magenta"], BOLD)
        + " "
        + c(line.ljust(inner_width - 2), COLORS["yellow"])
        + " "
        + c("│", COLORS["magenta"], BOLD)
        for line in lines
    ]
    return [top] + body + [bottom]

art = [
    c("        .-''''-.", COLORS["cyan"], BOLD),
    c("      .'  .-.   '.", COLORS["cyan"], BOLD),
    c("     /   (   )    \\", COLORS["cyan"], BOLD),
    c("    |  .-`-'-.    |", COLORS["cyan"], BOLD),
    c("    | /  o o  \\   |", COLORS["cyan"], BOLD),
    c("    | |   ^    |  |", COLORS["cyan"], BOLD),
    c("    | |  '-'   |  |", COLORS["cyan"], BOLD),
    c("    |  \\ '---' /   |", COLORS["cyan"], BOLD),
    c("     \\  '.___.'   /", COLORS["cyan"], BOLD),
    c("      '._     _.'", COLORS["cyan"], BOLD),
    c("         '---'", COLORS["cyan"], BOLD),
]

title = c(center_line("ANXIOUS COSMIC WISDOM", 64), COLORS["white"], BOLD)
subtitle = c(center_line("a quote that needs therapy", 64), COLORS["gray"], DIM)

print("\033[2J\033[H", end="")
print()
slow_print(title, 0.0015)
slow_print(subtitle, 0.0015)
print()

for line in art:
    slow_print(center_line(line, 64), 0.0007)

print()
for line in box_lines(wrapped):
    slow_print(center_line(line, 64), 0.0012)

print()
print(c(center_line("— probably muttered while overthinking mortality", 64), COLORS["blue"], DIM))