"""
Campbell's Soup Can #4987
Produced: 2026-09-19 05:53:44
Worker: DeepSeek: DeepSeek V4 Flash 0731 (free) (deepseek/deepseek-v4-flash-0731:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
DIM = "\033[2m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def spinner(duration=1.2):
    chars = "|/-\\"
    end = time.time() + duration
    i = 0
    msg = "Contemplating the void"
    while time.time() < end:
        sys.stdout.write(f"\r{msg}... {chars[i % len(chars)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    # Clear the line
    sys.stdout.write("\r" + " " * (len(msg) + 20) + "\r")
    sys.stdout.flush()


def type_out(text, color=YELLOW, delay=0.02):
    """Type text out character by character."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    sys.stdout.flush()


def center_text(text, width=60):
    return text.center(width)


def print_interior_line(line, is_attribution=False):
    """Print one line inside the decorative box."""
    sys.stdout.write(GREEN + "| " + RESET)

    if line == "":
        sys.stdout.write(" " * 56)
    elif is_attribution:
        spaces = 56 - len(line)
        if spaces > 0:
            sys.stdout.write(" " * spaces)
        type_out(line, color=BOLD + MAGENTA, delay=0.03)
    else:
        type_out(line, color=BOLD + YELLOW, delay=0.018)
        spaces = 56 - len(line)
        if spaces > 0:
            sys.stdout.write(" " * spaces)

    sys.stdout.write(GREEN + " |" + RESET + "\n")
    sys.stdout.flush()


def main():
    clear_screen()

    # Title
    print()
    print(BOLD + BLUE + center_text("WOODY ALLEN PRESENTS") + RESET)
    print(CYAN + center_text("~ A PHILOSOPHICAL MOMENT ~") + RESET)
    print()

    # Animated thinking spinner
    spinner()
    print()

    # Quote and attribution
    quote = (
        "Death is a great way to lose weight \u2014 and I should know, "
        "I've been dieting since 1965. When my time comes, I plan to negotiate. "
        "I'll say, 'Can we make it a near-death experience instead? "
        "I have a matinee to catch.'"
    )
    attribution = "\u2014 Woody Allen"

    # Wrap the quote to fit inside the box
    content_width = 56
    wrapper = textwrap.TextWrapper(
        width=content_width,
        break_long_words=False,
        break_on_hyphens=False
    )
    quote_lines = wrapper.wrap(quote)

    # Build the interior lines for the box
    lines = [""]  # top padding
    lines.extend(quote_lines)
    lines.append("")  # blank line before attribution
    lines.append(attribution)
    lines.append("")  # bottom padding

    # Draw the box with the quote
    print(GREEN + "+" + "-" * 58 + "+" + RESET)
    for line in lines:
        if line == "":
            print_interior_line("")
        elif line == attribution:
            print_interior_line(line, is_attribution=True)
        else:
            print_interior_line(line)
    print(GREEN + "+" + "-" * 58 + "+" + RESET)

    # A cheeky closer
    time.sleep(0.4)
    print()
    type_out(
        "(Or maybe I should just stop overthinking and get the pasta.)",
        color=CYAN + ITALIC + DIM,
        delay=0.015,
    )
    print("\n")


if __name__ == "__main__":
    main()