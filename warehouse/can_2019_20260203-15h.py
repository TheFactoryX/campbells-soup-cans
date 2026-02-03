"""
Campbell's Soup Can #2019
Produced: 2026-02-03 15:03:36
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_quote.py
import time
import sys

def print_quote():
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying."
    )

    # ANSI escape codes for colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Frame for the quote
    frame_color = MAGENTA
    quote_color = YELLOW
    author_color = CYAN

    frame = (
        f"{frame_color}┌{'─' * 50}┐\n"
        f"│{BOLD}{quote_color} I don't want to achieve immortality through my work; {RESET}{frame_color}│\n"
        f"│{BOLD}{quote_color} I want to achieve it through not dying. {RESET}{frame_color}│\n"
        f"└{'─' * 50}┘{RESET}\n"
    )

    # Print with a typing effect
    for char in frame:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)  # Adjust speed as needed

    # Add a delay before showing the author
    time.sleep(0.5)

    # Print author with a different color
    author = f"{author_color}{BOLD} - Woody Allen{RESET}\n"
    sys.stdout.write(author)
    sys.stdout.flush()

if __name__ == "__main__":
    print_quote()