"""
Campbell's Soup Can #4049
Produced: 2026-06-29 21:45:33
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

# ─── Color Palette ───
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
GRAY    = "\033[90m"

def slow_print(text, delay=0.03, color=WHITE):
    """Print text character by character with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sparkle_line(length=50):
    """Generate a decorative sparkle line."""
    chars = "· ✦ · ✧ · ★ · ✧ · ✦ ·"
    line = ""
    while len(line) < length:
        line += chars
    return line[:length]

def rainbow_text(text):
    """Return text with rainbow colors cycling through characters."""
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    result = ""
    for i, char in enumerate(text):
        result += f"{colors[i % len(colors)]}{char}"
    return result + RESET

def animate_ellipsis(duration=2, interval=0.4):
    """Animate loading ellipsis."""
    for _ in range(int(duration / interval)):
        for dots in [".", "..", "..."]:
            sys.stdout.write(f"\r  {GRAY}contemplating the void{dots} {RESET}")
            sys.stdout.flush()
            time.sleep(interval)
    print()

def clear_screen():
    print("\033[2J\033[H", end="")

def main():
    clear_screen()

    # ─── Title Banner ───
    print()
    print(f"{CYAN}{'═' * 60}{RESET}")
    print(f"{YELLOW}        🎬  THE WOODY ALLEN PHILOSOPHICAL GENERATOR  🎬{RESET}")
    print(f"{CYAN}{'═' * 60}{RESET}")
    print()

    # ─── Dramatic Pause ───
    time.sleep(0.5)
    slow_print("  📽️  A deep thought is being extracted from the cosmos...", 0.02, GRAY)
    print()
    time.sleep(0.5)
    animate_ellipsis(3, 0.5)
    print()

    # ─── The Quote ───
    quote = "I finally made peace with my insecurities — they're the only ones who truly understand me."

    # Box drawing
    border_color = MAGENTA
    accent = YELLOW

    # Calculate box width
    box_width = 56

    print(f"  {border_color}╔{'═' * box_width}╗{RESET}")
    print(f"  {border_color}║{' ' * box_width}║{RESET}")

    # Word-wrap the quote to fit inside the box
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= box_width - 4:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    for line in lines:
        padding = box_width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        colored_line = rainbow_text(line)
        # We need to pad manually since ANSI codes mess up len()
        print(f"  {border_color}║{RESET} {' ' * left_pad}{colored_line}{' ' * right_pad} {border_color}║{RESET}")

    print(f"  {border_color}║{' ' * box_width}║{RESET}")

    # Attribution
    attribution = "— Woody Allen (probably)"
    attr_pad = box_width - 4 - len(attribution)
    print(f"  {border_color}║{' ' * (attr_pad + 2)}{DIM}{ITALIC}{attribution}{RESET}  {border_color}║{RESET}")

    print(f"  {border_color}╚{'═' * box_width}╝{RESET}")
    print()

    # ─── Decorative Footer ───
    print(f"  {GRAY}{sparkle_line(55)}{RESET}")
    print()

    # ─── Bonus "Existential Footnote" ───
    time.sleep(0.8)
    slow_print(f"  {DIM}※ This thought will expire when the universe reaches heat death.{RESET}", 0.015, GRAY)
    time.sleep(0.3)
    slow_print(f"  {DIM}※ Side effects may include: anxiety, overthinking, and an{RESET}", 0.015, GRAY)
    slow_print(f"  {DIM}  inexplicable urge to live in Manhattan.{RESET}", 0.015, GRAY)
    print()

    # ─── Animated "The End" ───
    time.sleep(0.5)
    the_end = "✦  FIN  ✦"
    for i in range(3):
        colors_cycle = [YELLOW, MAGENTA, CYAN]
        sys.stdout.write(f"\r    {colors_cycle[i]}{BOLD}{the_end}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    print()
    print()
    print(f"  {GRAY}{'─' * 55}{RESET}")
    print(f"  {DIM}Thank you for laughing at the absurdity of existence.{RESET}")
    print(f"  {GRAY}{'─' * 55}{RESET}")
    print()

if __name__ == "__main__":
    main()