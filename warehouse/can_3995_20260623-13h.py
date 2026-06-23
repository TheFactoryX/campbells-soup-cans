"""
Campbell's Soup Can #3995
Produced: 2026-06-23 13:46:16
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ╔══════════════════════════════════════════════════════════════╗
# ║           🎬  W O O D Y   A L L E N   Q U O T E  🎬        ║
# ╚══════════════════════════════════════════════════════════════╝

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
UNDER   = "\033[4m"
BLINK   = "\033[5m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"

def slow_print(text, delay=0.03, color=WHITE):
    """Print text character by character with color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    print()

def sparkle_line(length=50):
    """Generate a random sparkle line."""
    chars = "·✦·✧·★·✩·✪·✫·✬·✭·✮"
    return "".join(random.choice(chars) for _ in range(length))

def draw_box(lines, border_color=CYAN, text_color=YELLOW):
    """Draw a box around text lines."""
    max_len = max(len(line) for line in lines)
    # Account for ANSI codes in length calculation
    visible_max = max_len
    box_width = visible_max + 4

    print(f"{border_color}╔{'═' * box_width}╗{RESET}")
    print(f"{border_color}║{' ' * box_width}║{RESET}")
    for line in lines:
        padding = box_width - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{border_color}║{' ' * left_pad}{text_color}{line}{border_color}{' ' * right_pad}║{RESET}")
    print(f"{border_color}║{' ' * box_width}║{RESET}")
    print(f"{border_color}╚{'═' * box_width}╝{RESET}")

def animate_ellipsis(text, cycles=3, delay=0.4):
    """Animate loading ellipsis."""
    for i in range(cycles):
        for dots in ["", ".", "..", "..."]:
            sys.stdout.write(f"\r  {MAGENTA}{text}{dots} {RESET}   ")
            sys.stdout.flush()
            time.sleep(delay)
    print()

def main():
    # Clear screen
    print("\033[2J\033[H", end="")

    # ─── Title ───
    print()
    print(f"  {DIM}{sparkle_line(55)}{RESET}")
    print()

    title = "✦  T H E   W O O D Y   A L L E N   I N S T I T U T E  ✦"
    print(f"  {BOLD}{YELLOW}{title}{RESET}")

    subtitle = "~ A N I N T E R A C T I V E   P H I L O S O P H Y   E X P E R I E N C E ~"
    print(f"  {DIM}{ITALIC}{subtitle}{RESET}")
    print()

    print(f"  {DIM}{sparkle_line(55)}{RESET}")
    print()

    # ─── "Loading" animation ───
    animate_ellipsis("Consulting the existential void", cycles=2, delay=0.3)
    print()

    # ─── The Quote ───
    quote_lines = [
        "",
        "I finally got my psychiatrist",
        "to admit he's as confused",
        "about the meaning of life",
        "as I am.",
        "",
        "We celebrated by",
        "staring at the wall",
        "together in silence.",
        "",
        "It was the best session",
        "I ever had.",
        "",
    ]

    draw_box(quote_lines, border_color=BLUE, text_color=WHITE)
    print()

    # ─── Attribution ───
    attribution = "— Woody Allen (probably)"
    print(f"  {DIM}{ITALIC}{attribution:>45}{RESET}")
    print()

    # ─── Bonus philosophical footnotes ───
    print(f"  {DIM}{'─' * 55}{RESET}")
    print()

    footnotes = [
        ("📜 Footnote #1:", "The wall was also unavailable for comment."),
        ("📜 Footnote #2:", "The silence was billed at $300/hour."),
        ("📜 Footnote #3:", "Both parties agreed existence is overrated."),
    ]

    for label, text in footnotes:
        print(f"    {GREEN}{label}{RESET} {DIM}{text}{RESET}")
        time.sleep(0.3)

    print()

    # ─── Animated closing ───
    print(f"  {DIM}{sparkle_line(55)}{RESET}")
    print()

    closing_lines = [
        "╔═══════════════════════════════════════════════════════╗",
        "║  \"The universe is not required to be in perfect    ║",
        "║   harmony with human ambition.\" — slightly paraphrased║",
        "╚═══════════════════════════════════════════════════════╝",
    ]
    for line in closing_lines:
        print(f"  {RED}{line}{RESET}")
        time.sleep(0.15)

    print()

    # ─── Final sparkle ───
    for _ in range(3):
        sys.stdout.write(f"\r  {YELLOW}{sparkle_line(55)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)

    print()
    print()
    print(f"  {BOLD}{CYAN}  ✦ Thank you for overthinking. Goodnight. ✦{RESET}")
    print()
    print(f"  {DIM}{sparkle_line(55)}{RESET}")
    print()

if __name__ == "__main__":
    main()