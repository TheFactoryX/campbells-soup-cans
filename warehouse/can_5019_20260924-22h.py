"""
Campbell's Soup Can #5019
Produced: 2026-09-24 22:24:58
Worker: inclusionAI: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLACK = "\033[40m"

# Woody Allen quote
QUOTE = (
    "\"I spent years trying to find the meaning of life, "
    "and all I found was that I couldn't figure out "
    "how to assemble my IKEA furniture. "
    "But at least the existential dread was flat-pack.\""
)

AUTHOR = "— Woody Allen (paraphrased by someone who also can't assemble furniture)"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, delay=0.03, color=None, bold=False):
    """Animate text appearing letter by letter."""
    prefix = BOLD if bold else ""
    suffix = BOLD if bold else ""
    for char in text:
        if color:
            sys.stdout.write(f"{color}{prefix}{char}{suffix}{RESET}")
        else:
            sys.stdout.write(f"{prefix}{char}{suffix}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(top_char, mid_char, bottom_char, color):
    """Draw a decorative ASCII frame."""
    width = 80
    print(f"\n{color}")
    # Top border
    print("  " + top_char * (width - 4))
    # Decorative lines
    print(f"  {top_char}  {' ' * (width - 6)}  {top_char}")
    print(f"  {top_char}  {'░' * (width - 6)}  {top_char}")
    # Middle
    print(f"  {mid_char}  {'★' * (width - 6)}  {mid_char}")
    # Continue frame
    print(f"  {top_char}  {'░' * (width - 6)}  {top_char}")
    print(f"  {top_char}  {' ' * (width - 6)}  {top_char}")
    print("  " + bottom_char * (width - 4))
    print(RESET)

def blink(text, times=3):
    """Make text blink."""
    for _ in range(times):
        sys.stdout.write(f"\r{BOLD}{YELLOW}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r{DIM}{BLUE}{text}{RESET}")森林
        sys.stdout.flush()
        time.sleep(0.4)
    print()

def main():
    clear_screen()

    # Print top decorative frame
    draw_frame("═", "║", "═", MAGENTA)

    time.sleep(0.5)

    # Title with color
    typewrite("🎬", 0.01, MAGENTA)
    time.sleep(0.3)
    typewrite("  ", 0.01)
    typewrite("    ", 0.01)
    timewrite = lambda t, d=0.03, c=None, b=False: typewrite(t, d, c, b)

    typewrite("  W O O D Y   A L L E N   L O G I C", 0.04, CYAN, True)
    time.sleep(0.5)
    typewrite("  ───────────────────────────────────", 0.02, DIM)
    time.sleep(0.5)

    # The quote with animation
    print(f"\n  {GREEN}{BOLD}{'▓' * 5}{RESET}  EXISTENTIAL CRISIS INCOMING  {GREEN}{BOLD}{'▓' * 5}{RESET}")
    time.sleep(0.5)
    print()
    typewrite("  ", 0.01, YELLOW)
    typewrite("╭", 0.01, RED)
    typewrite("─" * 70, 0.005, RED)
    typewrite("╰", 0.01, RED)
    time.sleep(0.3)

    # Type the actual quote in white
    typewrite("  " + QUOTE, 0.05, WHITE)
    time.sleep(0.5)

    # Author attribution
    typewrite("  ", 0.01)
    typewrite(AUTHOR, 0.03, YELLOW, True)
    time.sleep(0.5)

    # Bottom decorative frame
    print()
    draw_frame("─", "│", "─", BLUE)

    # Blink the punchline
    time.sleep(0.5)
    typewrite("\n  💡 ", 0.01, MAGENTA)
    blink("  Still thinking about it...", 2)

    time.sleep(0.5)

    # Final ASCII art
    print(f"\n  {RED}")
    print("         .--._")
    print("        /      \\")
    print("       | Woody  |")
    print("       | Allen  |")
    print("        \\  ☕  /")
    print("         '----'")
    print("      ( existential dread )")
    print(f"  {RESET}")
    time.sleep(1)
    typewrite("  The universe is a cruel, indifferent place... but at least the pizza is hot.", 0.04, CYAN, True)
    print(f"\n  {DIM}  [Press Enter to exit]{RESET}")
    input()

if __name__ == "__main__":
    main()