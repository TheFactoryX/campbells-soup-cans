"""
Campbell's Soup Can #672
Produced: 2025-12-02 19:30:47
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BACKGROUND_CYAN = "\033[46m"
BACKGROUND_RED = "\033[41m"
BACKGROUND_YELLOW = "\033[43m"

# Woody Allen style quote
QUOTE = "The trouble with psychotherapy is that it helps you understand yourself... " \
        "but ten minutes later, you’re still neurotic and your analyst is still analysting you. " \
        "If only anxiety came with a user manual!"

def spin_cursor(duration=2):
    """Display a playful spinning cursor animation"""
    spinner = ["◈", "♣", "♠", "♥"]
    start_time = time.time()
    while time.time() - start_time < duration:
        for symbol in spinner:
            sys.stdout.write(f"\r{ITALIC}{CYAN}Woody is deep-thinking {symbol} {RESET}")
            sys.stdout.flush()
            time.sleep(0.1)

def draw_boxed_quote(text, width=60):
    """Draw a fancy bordered box with colored background and text"""
    # Ensure text fits in the box
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    max_len = max(len(line) for line in lines)
    box_width = max(width, max_len + 4)
    
    # Build box lines
    top_bottom = f"{BACKGROUND_CYAN}{BOLD}┌{'─' * (box_width - 2)}┐{RESET}"
    padding = " " * 2
    
    print(top_bottom)
    for line in lines:
        padded_line = f"{padding}{line.ljust(box_width - 4)}{padding}"
        print(f"{BACKGROUND_CYAN}{BOLD}│{RESET}{WHITE}{BOLD}{padded_line}{RESET}{BACKGROUND_CYAN}{BOLD}│{RESET}")
    print(top_bottom)

def main():
    # Clear screen with ANSI code (works on most terminals)
    print("\033[H\033[J")
    
    # Show spinning animation
    spin_cursor(1.5)
    
    # Print philosophical quote in styled box
    print(f"\n{CYAN}{BOLD}Woody Allen's Existential Musings:{RESET}\n")
    draw_boxed_quote(QUOTE)
    
    # Add playful footer
    print(f"\n{YELLOW}{ITALIC}Remember: If life gives you neuroses, make lemonade... or just avoid the glass entirely.{RESET}\n")

if __name__ == "__main__":
    main()