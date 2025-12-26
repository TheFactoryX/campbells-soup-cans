"""
Campbell's Soup Can #1202
Produced: 2025-12-26 23:31:24
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
RED = "\033[31m"

def typewriter(text, speed=0.04, color=""):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(speed, speed * 1.4))
    sys.stdout.write("\n")
    sys.stdout.flush()

def draw_box(text_lines, border_color=GREEN, text_color=YELLOW):
    """Draw a decorative box around the given lines of text."""
    width = max(len(line) for line in text_lines) + 4
    top = f"{border_color}┌{'─' * width}┐{RESET}"
    bottom = f"{border_color}└{'─' * width}┘{RESET}"
    sys.stdout.write(top + "\n")
    for line in text_lines:
        padding = width - len(line) - 2
        sys.stdout.write(f"{border_color}│{RESET} {text_color}{line}{RESET} {' ' * padding}{border_color}│{RESET}\n")
    sys.stdout.write(bottom + "\n")
    sys.stdout.flush()

def main():
    quote = (
        "I keep my existential crisis in a drawer right next to my copy of "
        "‘The Stranger in a Rainstorm.’  I’ve never been afraid of the "
        "unknown, as long as I can keep a coffee maker within arm’s reach."
    )
    author = "- Woody (not the director, the philosopher)"

    # Build the ASCII art background
    banner = [
        f"{BOLD}{CYAN}               _   _  ____ ___",
        f"{CYAN}              | \\ | |/ ___|_ _|",
        f"{CYAN}   _ __  _ __  |  \\| | |    | | ",
        f"{GREEN}  | '_ \\| '__| | |\\  | |    | | ",
        f"{GREEN}  | | | | |    | | \\ | |___ | | ",
        f"{RED}  |_| |_|_|    |_|  \\_|____|___|{RESET}"
    ]

    # Clear screen and print banner
    sys.stdout.write("\033[2J\033[H")  # ANSI to clear screen and move cursor to home
    for line in banner:
        sys.stdout.write(line + "\n")
    sys.stdout.flush()

    time.sleep(1)

    # Show the quote inside a colored box with typewriter effect
    boxed_lines = [quote, author]
    for line in boxed_lines:
        # type each line with a short delay inside the box
        write_line = f"{BOLD}{YELLOW}{line}{RESET}"
        typewriter(write_line, speed=0.03)  # faster typing
    # Re-draw the box after typing
    draw_box([f"{BOLD}{YELLOW}{quote}{RESET}", f"{BOLD}{YELLOW}{author}{RESET}"], border_color=MTAG)

    # Final flourish
    sys.stdout.write(f"{MAGENTA}\nPress Ctrl+C to exit or wait for the world to end…{RESET}\n")
    # Keep the program alive until interrupted
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        sys.stdout.write("\nGoodbye, mad philosophers!{RESET}\n")
        sys.exit(0)

# Define the magic word for the color (used above but not defined)
MTAG = RED

if __name__ == "__main__":
    main()
