"""
Campbell's Soup Can #2174
Produced: 2026-02-11 22:49:44
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_allen_quote.py
import time

def print_colored(text, color_code):
    """Prints text in specified color using ANSI escape codes."""
    print(f"\033[{color_code}m{text}\033[0m")

def print_quote(quote, author):
    """Prints the quote with colorful and creative formatting."""
    # Clear the screen
    print("\033[H\033[J", end="")

    # Print title
    print_colored("W O O D Y   A L L E N   Q U O T E", "1;37;44")
    print()

    # Print quote box
    print_colored("╔" + "═" * 60 + "╗", "1;32")
    print_colored("║" + " " * 60 + "║", "1;32")
    for line in quote.split('\n'):
        print_colored(f"║ {line:<58} ║", "1;32")
    print_colored("║" + " " * 60 + "║", "1;32")
    print_colored("╚" + "═" * 60 + "╝", "1;32")

    # Print author
    print()
    print_colored(f" - {author}", "1;33")

def animate_loading():
    """Animates a loading effect before showing the quote."""
    print("Loading Woody Allen's wisdom...")
    for _ in range(3):
        for char in "|/-\\":
            print(f"\r{char}", end="", flush=True)
            time.sleep(0.1)
    print("\r ", end="")

def main():
    # Woody Allen style quote
    quote = (
        "I don't believe in an afterlife, although I am bringing a change of underwear."
    )
    author = "Woody Allen"

    animate_loading()
    print_quote(quote, author)

if __name__ == "__main__":
    main()