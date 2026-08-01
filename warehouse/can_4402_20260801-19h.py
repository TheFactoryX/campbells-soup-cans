"""
Campbell's Soup Can #4402
Produced: 2026-08-01 19:35:49
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
Woody Allen-style Philosophical Quote Generator
A neurotic, existential, and oddly comforting musing on the absurdity of existence.
"""

import sys
import time
import os

# ANSI Color Codes
class Colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"

# Quote in Woody Allen's neurotic style
WOODY_QUOTE = (
    "I've been contemplating my own mortality this morning—\n"
    "which is ridiculous, because I can't even finish a bagel\n"
    "without worrying it'll be the last thing I ever eat. Life\n"
    "is like a fatal comedy: you're the star, the audience, and\n"
    "the guy who forgot his lines. And the theater is on fire.\n"
    "But hey, at least I'm consistent—consistently anxious about\n"
    "being inconsistent in my anxiety. Existential crisis? That's\n"
    "just my love language, really."
)

def typewriter(text, delay=0.03):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def animate_text(text, colors_cycle=None):
    """Animate text with cycling colors."""
    if colors_cycle is None:
        colors_cycle = [
            Colors.CYAN, Colors.YELLOW, Colors.MAGENTA,
            Colors.GREEN, Colors.BLUE, Colors.RED
        ]
    
    for i, char in enumerate(text):
        color = colors_cycle[i % len(colors_cycle)]
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.015)

def print_box(text_lines, width=70, border_color=Colors.CYAN):
    """Print text inside a fancy ASCII box."""
    print(f"{border_color}╔{'═' * width}╗")
    for line in text_lines:
        # Center the text
        padding = width - len(line)
        left = padding // 2
        right = padding - left
        print(f"║{' ' * left}{line}{' ' * right}║")
    print(f"╚{'═' * width}╝{Colors.RESET}")

def print_wavy_border(text, top=True):
    """Print a wavy decorative border."""
    symbols = "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
    if top:
        print(f"{Colors.MAGENTA}    {symbols}{Colors.RESET}")
    else:
        print(f"{Colors.MAGENTA}{symbols}    {Colors.RESET}")

def print_ascii_art():
    """Print some abstract, existential ASCII art."""
    art_lines = [
        f"{Colors.DIM}      .-'''-.        .-'''-.{Colors.RESET}",
        f"{Colors.DIM}     /  _   /\\    /\\   _  \\{Colors.RESET}",
        f"{Colors.DIM}    |  (_)  \\ \\  / /  (_)  |{Colors.RESET}",
        f"{Colors.DIM}     \\      /  \\/  \\      /{Colors.RESET}",
        f"{Colors.DIM}      '----'    '--'----'`{Colors.RESET}",
    ]
    for line in art_lines:
        print(line)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        # Clear screen for clean presentation
        clear_screen()

        # Print title with color
        title = "WOODY ALLEN-STYLE PHILOSOPHICAL QUOTE GENERATOR"
        print(f"\n{Colors.BOLD}{Colors.YELLOW}{'=' * 60}")
        print(f"{' ' * 5}{title}")
        print(f"{'=' * 60}{Colors.RESET}")

        # Wavy border
        print_wavy_border("", top=True)

        # Print ASCII art
        print_wavy_border("", top=False)

        # Dramatic pause
        time.sleep(0.8)

        # Print the quote with typewriter effect and animated colors
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}    ✦ YOUR DAILY DOSE OF EXISTENTIAL ANXIETY ✦{Colors.RESET}\n")
        time.sleep(0.3)

        animate_text(WOODY_QUOTE)
        
        print(f"\n\n{Colors.ITALIC}{Colors.DIM}— A profoundly neurotic AI, after much worry about whether it should print this at all{Colors.RESET}")
        
        time.sleep(1)

        # Print a colorful footer
        footer_lines = ["Thank you for contemplating nothingness with us!", 
                        "Please tip your existentialist waiter."]
        print_box(footer_lines, width=60, border_color=Colors.GREEN)

    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Even the quote is afraid to finish itself. Goodbye!{Colors.RESET}")

if __name__ == "__main__":
    main()