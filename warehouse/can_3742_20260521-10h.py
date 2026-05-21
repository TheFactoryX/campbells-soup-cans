"""
Campbell's Soup Can #3742
Produced: 2026-05-21 10:03:03
Worker: Baidu Qianfan: CoBuddy (free) (baidu/cobuddy:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI color codes
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    GRAY = "\033[90m"

def typewriter(text, delay=0.03, color=""):
    for char in text:
        sys.stdout.write(color + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_border(width=60):
    print(Color.CYAN + Color.BOLD + "╔" + "═" * (width - 2) + "╗" + Color.RESET)
    print(Color.CYAN + Color.BOLD + "║" + Color.RESET + " " * (width - 2) + Color.CYAN + Color.BOLD + "║" + Color.RESET)

def ascii_woody():
    woody = f"""
{Color.YELLOW}    .-""""-.
   /          \\\\
  |   O    O   |
  |     __     |
   \\\\   '--'   /
    '-......-'
   {Color.RESET}{Color.ITALIC}  o o o o o o{Color.RESET}"""
    print(woody)

def shimmer_text(text):
    """Make text shimmer between colors"""
    shimmer_colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.MAGENTA, Color.BLUE]
    color_index = 0
    colored = ""
    for char in text:
        colored += shimmer_colors[color_index % len(shimmer_colors)] + char + Color.RESET
        color_index += 1
    return colored

def existential_spiral():
    frames = [
        "    .-""""-.\n   /        \\\n  |  O    O  |\n  |    __    |\n   \\  '--'  /\n    '-....-'",
        "    .-""\"\"\"\"-.\n   /       /|\n  | O      | |\n  |   __   | |\n   \\ '--'  |\n    '-....-",
        "    .-''''-.\n   /    ||   \\\n  |  O  ||  O|\n  |   __||    |\n   \\ '--'  /|\n    '-....-||",
    ]
    for frame in frames:
        sys.stdout.write(f"\r{Color.YELLOW}{frame}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

def main():
    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Title
    print(Color.RED + Color.BOLD + """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║   W O O D Y   A L L E N   P H I L O S O P H Y       ║
    ║              (or: "One More Therapist's Appointment")║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """ + Color.RESET)

    time.sleep(0.5)

    # ASCII Woody
    ascii_woody()
    time.sleep(0.3)

    # Animated existential spiral
    existential_spiral()

    # The quote itself
    print(Color.GREEN + Color.BOLD + "  ┌─────────────────────────────────────────────┐" + Color.RESET)
    time.sleep(0.1)

    quote = shimmer_text(
        "I've always known that existence is meaningless, "
        "but I still get nervous when someone says, "
        "'Your appointment is at 9.'"
    )

    typewriter(f"  │  \"{quote}\"", delay=0.02, color=Color.GREEN + Color.BOLD)
    print(Color.GREEN + Color.BOLD + "  └─────────────────────────────────────────────┘" + Color.RESET)

    time.sleep(0.5)

    # Subtitle
    print()
    print(Color.ITALIC + Color.GRAY + "       — existential dread, delivered with comedic timing —")
    print(Color.RESET)

    # Bonus philosophical musing
    print()
    print(Color.YELLOW + Color.BOLD + "  Also:" + Color.RESET)
    time.sleep(0.3)
    typewriter(
        "Death is the same as being late for a party you never wanted to go to.",
        delay=0.04,
        color=Color.MAGENTA + Color.ITALIC
    )

    print()
    print(Color.CYAN + "     ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀")
    print(Color.CYAN + "     ⚠  tip: if you're reading this, you're already procrastinating  ⚠")
    print(Color.CYAN + "     ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀")

    print(Color.RESET)

if __name__ == "__main__":
    main()