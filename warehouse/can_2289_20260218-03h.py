"""
Campbell's Soup Can #2289
Produced: 2026-02-18 03:17:47
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

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def print_colored(text, color):
    """Print text in the specified color."""
    print(f"{color}{text}{RESET}")

def animate_text(text, color, delay=0.1):
    """Animate text by printing one character at a time."""
    for char in text:
        print(f"{color}{char}{RESET}", end="", flush=True)
        time.sleep(delay)
    print()  # Newline after the text

def print_boxed_text(text, border_color, text_color):
    """Print text inside a box with colored border and text."""
    width = len(text) + 4
    print_colored("┌" + "─" * width + "┐", border_color)
    print_colored(f"│  {text}  │", text_color)
    print_colored("└" + "─" * width + "┘", border_color)

def main():
    quote = (
        "I don't want to achieve immortality through my work;\n"
        "I want to achieve it through not dying."
    )

    print("\n" * 2)  # Add some space at the top

    # Animate the quote with colors
    animate_text("Woody Allen's Philosophy:", CYAN, 0.1)
    time.sleep(0.5)

    print_boxed_text(quote, YELLOW, GREEN)

    print("\n" * 2)  # Add some space at the bottom

if __name__ == "__main__":
    main()