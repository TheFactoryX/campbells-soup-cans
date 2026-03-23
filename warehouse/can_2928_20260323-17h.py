"""
Campbell's Soup Can #2928
Produced: 2026-03-23 17:10:15
Worker: OpenAI: GPT-5 Codex (openai/gpt-5-codex)
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
ITALIC = "\033[3m"
PALETTE = [
    "\033[38;5;219m",
    "\033[38;5;117m",
    "\033[38;5;191m",
    "\033[38;5;213m",
    "\033[38;5;159m",
]
EDGE_COLOR = "\033[38;5;207m"
GLOW = "\033[38;5;225m"
CYAN = "\033[96m"

def typewriter_line(text, palette, delay=0.035):
    color_index = 0
    active_color = palette[0]
    for char in text:
        if char.isalpha():
            active_color = palette[color_index % len(palette)]
            color_index += 1
        elif char.strip():
            active_color = palette[color_index % len(palette)]
        sys.stdout.write(active_color + char + RESET)
        sys.stdout.flush()
        if char in ",;:":
            time.sleep(delay * 1.6)
        elif char in ".!?":
            time.sleep(delay * 2.3)
        elif char.strip():
            time.sleep(delay)
        else:
            time.sleep(delay / 2)

def centered_lines(lines, width):
    return [line.center(width) for line in lines]

def show_spinner(message, cycles=20, delay=0.07):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(cycles):
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r{DIM}{CYAN}{message} {frame}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r" + " " * (len(message) + 6) + "\r")
    sys.stdout.flush()

def print_ascii_art():
    art = [
        "            ___",
        "         .-\"   \"-.",
        "        /  .---.  \\",
        "       /  /     \\  \\",
        "       |  |  .-. |  |",
        "       |  | ( o )|  |",
        "       |  |  `-' |  |",
        "       |  |\\___/|  |",
        "       |  |\\___/|  |",
        "       \\  \\     /  /",
        "        `-.`---'.-'",
        "           `\"\"\"`",
        "        neurotic bifocals",
    ]
    width = shutil.get_terminal_size((80, 20)).columns
    padded = centered_lines(art, width)
    for idx, line in enumerate(padded):
        color = PALETTE[idx % len(PALETTE)]
        print(color + line + RESET)
        time.sleep(0.05)

def display_quote_box(quote):
    width = shutil.get_terminal_size((80, 20)).columns
    wrapped = textwrap.wrap(quote, width=min(68, max(40, width - 12)))
    inner_width = max(len(line) for line in wrapped)
    top = EDGE_COLOR + "╭" + "─" * (inner_width + 2) + "╮" + RESET
    bottom = EDGE_COLOR + "╰" + "─" * (inner_width + 2) + "╯" + RESET
    print()
    print(top)
    for line in wrapped:
        padded_line = line.ljust(inner_width)
        sys.stdout.write(EDGE_COLOR + "┃ " + RESET)
        typewriter_line(padded_line, PALETTE, delay=0.038)
        sys.stdout.write(EDGE_COLOR + " ┃" + RESET + "\n")
        sys.stdout.flush()
    print(bottom)

def main():
    print("\033c", end="")
    show_spinner("calibrating existential dread")
    print_ascii_art()
    time.sleep(0.5)
    quote = (
        "I scheduled a debate with the universe about meaning; it countered by double-booking "
        "me with my own mortality. We're negotiating refreshments, but only my anxiety "
        "remembered to bring napkins."
    )
    display_quote_box(quote)
    print()
    print(f"{DIM}{ITALIC}{GLOW}— whispered in a dimly lit Brooklyn cafe, probably by me{RESET}")

if __name__ == "__main__":
    main()