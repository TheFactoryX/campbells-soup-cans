"""
Campbell's Soup Can #315
Produced: 2025-11-16 12:53:58
Worker: Qwen: Qwen2.5 VL 32B Instruct (free) (qwen/qwen2.5-vl-32b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# -*- coding: utf-8 -*-
"""
Woody's Wise Words (a Funny Philosophical Quote in Woody Allen's Style)

A playful and creative program featuring a quirky existential quote in Woody Allen's neurotic,
self-deprecating, and humorous style. Enjoy the ASCII art, colors, and creative formatting!
"""

import time

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

# ASCII decorations
HORIZONTAL_LINE = f"{BLUE}{'─' * 50}{RESET}"
TOP_BORDER = f"{BLUE}┌{HORIZONTAL_LINE}┐{RESET}"

def animate_typing(text, delay=0.03):
    """Animate the typing of the quote, character by character, with a delay."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def display_quote():
    """Display the Woody Allen-style quote with creative formatting and colors."""
    # Clear the screen (simple method that works on most terminals)
    print("\033c", end="")
    
    # Top border
    print(TOP_BORDER)
    print(f"{BLUE}│{RESET}", end="")
    
    # Left and right side borders
    left_border = f"{BLUE}│{RESET} "
    right_border = f" {BLUE}│{RESET}"
    
    # Title section
    title = f"{BOLD}{MAGENTA}Woody's Wise Words{RESET}"
    centered_title = title.center(48)
    print(f"{left_border}{centered_title}{right_border}")
    
    # Horizontal line
    print(f"{BLUE}│{'─' * 50}{BLUE}│{RESET}")
    
    # Woody Allen's quote (neurotic, self-deprecating, philosophical)
    quote = (
        "Life is like a clown at a circus—full of tricks, laughter, and existential despair. "
        "But the sad truth is, you're not even the best clown in the ring."
    )
    centered_quote = quote.center(50)
    
    # Animate the quote
    animate_typing(f"{left_border}{CYAN}{centered_quote}{RESET}{right_border}")
    
    # Bottom border
    print(f"{BLUE}└{HORIZONTAL_LINE}┘{RESET}")

if __name__ == "__main__":
    display_quote()