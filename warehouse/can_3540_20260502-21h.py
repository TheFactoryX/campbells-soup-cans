"""
Campbell's Soup Can #3540
Produced: 2026-05-02 21:00:00
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import random

# ANSI escape codes for colors/style
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Foreground colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright foreground colors
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"


def typewriter_print(text, delay=0.02, end="\n"):
    """Print text with a typewriter effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(end, end="", flush=True)


def get_terminal_width():
    """Try to get terminal width, default to 80."""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def center(text, width=None):
    """Center text in terminal."""
    if width is None:
        width = get_terminal_width()
    return text.center(width)


def rainbow_color(text):
    """Apply rainbow cycling colors to text character by character."""
    colors = [RED, BRIGHT_RED, YELLOW, BRIGHT_YELLOW, GREEN, BRIGHT_GREEN, CYAN, BRIGHT_CYAN, BLUE, BRIGHT_BLUE, MAGENTA, BRIGHT_MAGENTA]
    result = ""
    color_idx = 0
    for char in text:
        if char == "\n":
            result += char
            continue
        result += colors[color_idx % len(colors)] + char + RESET
        char_width = 1  # simplified
        color_idx += 1
    return result


def scroll_off_screen(lines, delay=0.04):
    """Animate lines scrolling off screen one by one."""
    for i, line in enumerate(lines):
        print(line, flush=True)
        time.sleep(delay)


def build_woody_portrait():
    """Build a stylized Woody Allen type portrait in ASCII."""
    portrait = [
        r"       .---.         .---.",
        r"      ( @ @ )  *.   ( @ @ )",
        r"       \_-_/   | \   \_-_/",
        r"        | |   / | \   | |",
        r"       /   \ | / | | /   \\",
        r"      / /|  \\\_//\ \\\\ | \\\\",
        r"     / / |   || |  \\  \\ \\",
        r"     ||  |   || |  |  ||  |",
        r'     "\\"    "\\"    "\\"  ',
        r'      |______..______..__|',
        r'      \  WORTHLESS OF  /',
        r'       \   NATURE    /',
        r'        \__________/',
    ]
    return portrait


def main():
    width = get_terminal_width()

    # --- Phase 1: ---
    # Dramatic pause, screen wipe feel
    cols = min(width, 72)

    print("\n" * 2)
    time.sleep(0.5)

    # --- Phase 2: The clock ---
    clock_frames = [
        "           _______           ",
        "         .'       '.         ",
        "        /  O     0  \\       ",
        "       |     WHO    |        ",
        "       |   DO I     |        ",
        "       |   ASK?     |        ",
        "        \\  9... 6  /        ",
        "         '. 12__.'.          ",
        "           ''---''           ",
    ]

    for frame in clock_frames:
        line = frame.center(cols)
        time.sleep(0.15)
        print(ITALIC + center(frame) + RESET)

    time.sleep(0.8)
    print()
    typewriter_print(center("The universe is expanding..."), 0.04)
    time.sleep(0.3)
    typewriter_print(center("So is my waistline."), 0.04)
    time.sleep(0.8)
    print()
    print()

    # --- Phase 3: The Deep Quote, letter by letter with drama ---
    quote_lines = [
        "I was recently in a horrifying amusement",
        "",
        "park ride with my shrink, and the car went",
        "",
        "upside down, and my shrink screamed, ''",
        "",
        "HOW OLD ARE YOU?'' and I said, ''AND GOD",
        "",
        "SAID: LET THERE BE IDIOCY'', and he said,",
        "",
        "''NO, I MEAN YOUR AGE'', and I said,",
        "",
        "''IN THE BEGINNING...''",
    ]

    quote_box_top = "+" + "═" * 50 + "+"
    quote_box_bottom = "+" + "═" * 50 + "+"
    quote_box_empty = "║" + " " * 50 + "║"

    # Box drawing colors
    box_color = BRIGHT_YELLOW
    accent_color = BRIGHT_MAGENTA

    time.sleep(0.5)
    print()
    typewriter_print(center(box_color + quote_box_top + RESET), 0.005)
    typewriter_print(center(quote_box_empty), 0.002)
    time.sleep(0.2)

    for i, line in enumerate(quote_lines):
        if line == "":
            # empty spacer
            typewriter_print(center(quote_box_empty), 0.001)
        else:
            # fancy formatting inside box
            if "HOW OLD ARE YOU" in line or "IN THE BEGINNING" in line:
                formatted = f"   {BOLD}{BRIGHT_CYAN}{line}{RESET}"
            elif "NO, I MEAN YOUR AGE" in line:
                formatted = f"   {BOLD}{BRIGHT_GREEN}{line}{RESET}"
            elif "LET THERE BE IDIOCY" in line:
                formatted = f"   {BOLD}{RED}{line}{RESET}"
            elif "shrink" in line:
                formatted = f"   {ITALIC}{WHITE}{line}{RESET}"
            else:
                formatted = f"   {WHITE}{line}{RESET}"

            padded = formatted.ljust(50 + len(RESET) * formatted.count(RESET))
            # It's easier to just print centered
            display_text = f"   {line}"
            padding_needed = 50 - len(line) - 3
            if padding_needed < 0:
                padding_needed = 0

            box_line = f"║{display_text}{' ' * padding_needed}║"

            # slide color through
            if i == 0:
                color_brackets = box_color
            else:
                color_brackets = box_color

            typewriter_print(center(color_brackets + "║" + RESET + "   " + line + " " * max(0, 47 - len(line)) + color_brackets + "║" + RESET), 0.02)
            # Simpler: just line by line
            # The above is too complex, let's simplify

    # Let's restart with a clean approach

    # =====================================================
    # CLEAN RE-DO
    # =====================================================
    # We'll print carefully

    COLS = min(72, width)
    
    # Clear screen
    print("\033[2J\033[H", end="")
    time.sleep(0.3)

    # --- Title Banner ---
    banner = [
        "╔══════════════════════════════════════════════════════════════════════╗",
        "║                                                                      ║",
        "║          🎭  W O O D Y   A L L E N   P H I L O S O P H Y  🎭        ║",
        "║                                                                      ║",
        "╚══════════════════════════════════════════════════════════════════════╝",
    ]

    for line in banner:
        print(BRIGHT_YELLOW + BOLD + center(line, COLS) + RESET)
        time.sleep(0.1)

    print()
    time.sleep(0.5)

    # --- The Quote, built up dramatically ---
    quote_parts = [
        ("I was recently in a horrifying amusement", WHITE),
        ("park ride with my shrink, and the car went", WHITE),
        ("upside down, and my shrink screamed,", WHITE),
        ("", WHITE),
        ("\"HOW OLD ARE YOU?\"", BRIGHT_CYAN + BOLD),
        ("", WHITE),
        ("and I said,", WHITE),
        ("", WHITE),
        ("\"AND GOD SAID: LET THERE BE IDIOCY\"", RED + BOLD),
        ("", WHITE),
        ("and he said,", WHITE),
        ("", WHITE),
        ("\"NO, I MEAN YOUR AGE\"", BRIGHT_GREEN + BOLD),
        ("", WHITE),
        ("and I said,", WHITE),
        ("", WHITE),
        ("\"IN THE BEGINNING...\"", BRIGHT_MAGENTA + BOLD),
    ]

    # Print the quote in a box
    box_width = 56
    print(center(BRIGHT_YELLOW + "┌" + "─" * box_width + "┐" + RESET, COLS))
    print(center(BRIGHT_YELLOW + "│" + " " * box_width + "│" + RESET, COLS))

    for text, color in quote_parts:
        if text == "":
            print(center(BRIGHT_YELLOW + "│" + " " * box_width + "│" + RESET, COLS))
        else:
            padding = box_width - len(text)
            if padding < 0:
                padding = 0
            line = f"{color}{text}{RESET}{' ' * padding}"
            print(center(BRIGHT_YELLOW + "│ " + RESET + line + BRIGHT_YELLOW + " │" + RESET, COLS))
            time.sleep(0.15)

    print(center(BRIGHT_YELLOW + "│" + " " * box_width + "│" + RESET, COLS))
    print(center(BRIGHT_YELLOW + "└" + "─" * box_width + "┘" + RESET, COLS))

    print()
    time.sleep(0.5)

    # --- Attribution ---
    attribution = "— Woody Allen (probably)"
    print(center(DIM + ITALIC + attribution + RESET, COLS))
    print()
    time.sleep(0.8)

    # --- The Portrait ---
    portrait = [
        "              .---.         .---.",
        "             ( @ @ )  *.   ( @ @ )",
        "              \\_-_/   | \\   \\_-__/",
        "               | |   / | \\   | |",
        "              /   \\ | / | | /   \\",
        "             / /|  \\\\ \\_//  \\\\ | \\\\",
        "            / / |   || |  \\  \\ \\",
        "            ||  |   || |  |  ||  |",
        '            "\\"    "\\"    "\\"  ',
        "             |______..______..__|",
        "             \\  WORTHLESS OF  /",
        "              \\   NATURE    /",
        "               \\__________/",
    ]

    portrait_colors = [BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_BLUE, BRIGHT_MAGENTA, WHITE, DIM]

    for i, line in enumerate(portrait):
        color = portrait_colors[i % len(portrait_colors)]
        print(center(color + line + RESET, COLS))
        time.sleep(0.08)

    print()
    time.sleep(0.5)

    # --- Final existential punchline ---
    punchlines = [
        "Life is divided into the horrible and the miserable.",
        "The universe is under no obligation to make sense to you.",
        "I don't want to achieve immortality through my work;",
        "  I want to achieve it through not dying.",
        "Death is a very effective way of cutting down on expenses.",
    ]

    print()
    print(center(DIM + "─" * 40 + RESET, COLS))
    print()

    for punchline in punchlines:
        typewriter_print(center(ITALIC + DIM + punchline + RESET, COLS), 0.03)
        time.sleep(0.4)

    print()
    print(center(DIM + "─" * 40 + RESET, COLS))
    print()

    # --- The spinning existential wheel ---
    print()
    typewriter_print(center(BRIGHT_RED + "SPINNING THE WHEEL OF EXISTENTIAL DREAD..." + RESET, COLS), 0.03)
    print()

    wheel_chars = ["◐", "◓", "◑", "◒"]
    wheel_colors = [BRIGHT_RED, BRIGHT_YELLOW, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_BLUE, BRIGHT_MAGENTA]

    for i in range(24):
        char = wheel_chars[i % len(wheel_chars)]
        color = wheel_colors[i % len(wheel_colors)]
        spaces = " " * (20 + int(10 * (1 if i % 2 == 0 else -1) * (1 if i < 12 else -1)))
        # Simple bounce
        offset = int(15 + 10 * (1 if i % 2 == 0 else 0.5))
        print(center(color + "  " + "·" * (20 - i if i < 12 else i - 12) + char + "·" * (i if i < 12 else 24 - i) + RESET, COLS), end="\r")
        time.sleep(0.1)

    print()
    print()

    # --- Final message ---
    time.sleep(0.3)
    final_messages = [
        (BRIGHT_GREEN + "  ✓  You have been philosophically enriched." + RESET),
        (BRIGHT_RED + "  ✗  Your anxiety has increased by 47%." + RESET),
        (BRIGHT_YELLOW + "  ★  You are now 0.003% closer to understanding nothing." + RESET),
    ]

    for msg in final_messages:
        print(center(msg, COLS))
        time.sleep(0.4)

    print()
    print(center(DIM + "Press Ctrl+C to exit the void." + RESET, COLS))
    print()

    # Keep alive with a gentle pulse
    try:
        pulse_chars = ["·", "•", "●", "•", "·"]
        pulse_idx = 0
        while True:
            char = pulse_chars[pulse_idx % len(pulse_chars)]
            color = pulse_idx % 2 == 0 and DIM or WHITE
            print(center(color + char + " " + char + " " + char + RESET, COLS), end="\r")
            pulse_idx += 1
            time.sleep(0.8)
    except KeyboardInterrupt:
        print()
        print()
        print(center(BRIGHT_YELLOW + "The void thanks you for visiting." + RESET, COLS))
        print(center(DIM + "Goodbye." + RESET, COLS))
        print()


if __name__ == "__main__":
    main()