"""
Campbell's Soup Can #5128
Produced: 2026-10-18 14:34:49
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen-style philosophical quote with visual flair!
Neurotic, self-deprecating, and existentially amusing.
"""
import sys
import time
import random

class Color:
    """ANSI color codes for terminal text"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

QUOTE_COLORS = [Color.CYAN, Color.MAGENTA, Color.YELLOW, Color.GREEN, Color.BLUE]
RAINBOW_COLORS = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.MAGENTA]

# The Woody Allen-style philosophical quote
QUOTE = (
    "So I was lying awake last night - which, as my therapist says, "
    "is always a mistake - agonizing over the meaning of existence. "
    "Then I realized I was just avoiding my credit card bill. "
    "The universe is vast and uncaring, but at least my anxiety is "
    "vast and uniquely, personally attentive."
)


def clear_screen():
    """Clear terminal and reset cursor position"""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()


def marquee(text, cycles=12):
    """Animated marquee with color cycling"""
    for cycle in range(cycles):
        sys.stdout.write('\r')
        for i, char in enumerate(text):
            col = RAINBOW_COLORS[(i + cycle * 2) % len(RAINBOW_COLORS)]
            sys.stdout.write(col + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(0.2)
    print()


def rainbow_print(text, delay=0.02):
    """Print text with cycling rainbow colors"""
    for i, char in enumerate(text):
        col = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
        sys.stdout.write(col + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def color_print(text, color, delay=0.02):
    """Print text character by character in a single color"""
    for char in text:
        sys.stdout.write(color + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def random_color_text(text, delay=0.01):
    """Print text with each character in a random color, no newline"""
    for char in text:
        col = random.choice(QUOTE_COLORS)
        sys.stdout.write(col + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(delay)


def wrap_text(text, max_width):
    """Wrap text to fit within max_width characters"""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.rstrip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.rstrip())
    return lines


def main():
    clear_screen()
    print()
    print()

    # === Animated Title ===
    title = "  WOODY ALLEN'S EXISTENTIAL COMEDY HOUR  "
    marquee(title)
    print()

    # Subtitle
    rainbow_print("      ...featuring one (1) potentially meaningless thought ...", 0.03)
    print()
    print()

    # === Thinking animation ===
    for i in range(3):
        sys.stdout.write('\r')
        sys.stdout.write(Color.DIM + "      ...thinking" + "." * (i + 1) + Color.RESET)
        sys.stdout.flush()
        time.sleep(0.4)
    print()
    print()

    # === Thought Bubble with Quote ===
    lines = wrap_text(QUOTE, 44)
    max_len = max(len(line) for line in lines)

    # Top border
    border_str = "+" + "-" * (max_len + 4) + "+"
    sys.stdout.write("      ")
    for char in border_str:
        sys.stdout.write(Color.YELLOW + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

    # Quote lines inside bubble
    for line in lines:
        padded = line.ljust(max_len)
        sys.stdout.write("      " + Color.YELLOW + "|" + Color.RESET + "  ")
        random_color_text(padded, 0.008)
        sys.stdout.write("  " + Color.YELLOW + "|" + Color.RESET)
        print()
        time.sleep(0.3)

    # Bottom border
    sys.stdout.write("      ")
    for char in border_str:
        sys.stdout.write(Color.YELLOW + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

    # === Thought bubble tail ===
    print()
    color_print("    '-......'", Color.YELLOW, 0.03)
    color_print("      /", Color.YELLOW, 0.03)
    color_print("     /", Color.YELLOW, 0.03)

    # === ASCII Art: The thinker ===
    thinker = """
         o
         |
        / \\
       /   \\
      /     \\
    """
    rainbow_print(thinker, 0.01)
    print()

    # === Footer ===
    rainbow_print("       ~ Philosophy with a side of neurosis ~", 0.04)
    print()

    # Attribution
    attribution = "    (Worth approximately what you paid for it)"
    color_print(attribution, Color.MAGENTA, 0.04)


if __name__ == '__main__':
    main()