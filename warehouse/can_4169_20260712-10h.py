"""
Campbell's Soup Can #4169
Produced: 2026-07-12 10:45:45
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
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

def animate_text(text, delay=0.05, color="\033[96m"):
    """Prints text with a typewriter effect and color."""
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_boxed_quote(quote):
    """Prints a philosophical quote inside a stylized ASCII box."""
    # ANSI Colors
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Preparation
    quote_lines = quote.split('\n')
    width = max(len(line) for line in quote_lines) + 4
    
    # Top border
    print("\n" + CYAN + "╔" + "═" * (width - 2) + "╗" + RESET)
    
    # Content lines
    for line in quote_lines:
        padding = " " * ((width - len(line) - 2) // 2)
        extra_space = " " * (len(padding) + (width - len(line) - 2) % 2)
        print(f"{CYAN}║{MAGENTA}{padding}{line}{extra_space}{CYAN}║{RESET}")
        
    # Bottom border
    print(CYAN + "╚" + "═" * (width - 2) + "╝" + RESET + "\n")

def main():
    """The main execution loop for the neurotic philosopher."""
    # Clear screen (platform dependent, works on most modern terminals)
    print("\033[H\033[J", end="")

    # The "Brain" of the program loading
    load_sequence = [
        ("Initializing existential dread...", "\033[91m"),
        ("Checking for meaning in universe...", "\033[94m"),
        ("Calculating probability of coincidence...", "\033[93m"),
        ("Searching for a good therapist...", "\033[95m"),
        ("Dread successfully loaded.", "\033[92m")
    ]

    for msg, color in load_sequence:
        sys.stdout.write(f"\r{color}▶ {msg}")
        sys.stdout.flush()
        time.sleep(0.8)
        print(" [OK]")

    print("\n" + "\033[90m" + "..." * 30 + "\033[0m\n")
    time.sleep(1)

    # THE QUOTE
    woody_quote = (
        "I asked my therapist if my neuroticism was a sign of "
        "subconscious terror, and he said, 'Don't worry, "
        "everyone is dying, it's just that you're doing it "
        "with significantly more punctuation.'"
    )

    # Animation sequence
    animate_text("--- TRANSMISSION FROM THE NEUROTIC VOID ---", 0.03, "\033[90m")
    print()
    print_boxed_quote(woody_quote)
    print("\033[90m" + "--- END OF EXISTENTIAL CRISIS ---".center(60) + "\033[0m\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[91mEven your attempt to escape the program is a metaphor for the futility of human endeavor.\033[0m")