"""
Campbell's Soup Can #5096
Produced: 2026-10-12 00:33:00
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
CYAN = '\033[36m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
RED = '\033[31m'
BLUE = '\033[34m'
BOLD = '\033[1m'
RESET = '\033[0m'

def slow_type(text, delay=0.03, color=YELLOW):
    """Type out text character by character with a delay"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    sys.stdout.flush()

def print_ascii_art():
    """Print a Woody Allen-style ASCII art"""
    art = f"""
{CYAN}    _____ _    _ _____    _    _____           _    _____ _  _{RESET}
{CYAN}   / ____| |  | |  __ \\  / \\  |  __ \\         / \\  |  __ \\| || |{RESET}
{CYAN}  | (___ | |  | | |__) |/  \\ | |  | |       /  \\ | |  | | || |{RESET}
{CYAN}   \\___ \\| |  | |  _  / / \\ \\| |  | |      / /\\ \\| |  | | || |{RESET}
{CYAN}   ____) | |__| | | \\ \\/  _ \\ |  | |_____/ ____ \\ | |__| | || |{RESET}
{CYAN}  |_____/ \\____/|_|  \\_\\/_/ \\_|_|_________/_    \\_\\_____/|_||_|{RESET}
{CYAN}                                                         {RESET}
{MAGENTA}    A neurotic existential crisis in box form{RESET}
    """
    print(art)

def main():
    # Clear screen (works on most systems)
    print("\033[2J\033[H", end="")
    
    # Print title
    print(f"{BOLD}{BLUE}=== WOODY ALLEN STYLE PHILOSOPHICAL QUOTE ==={RESET}\n")
    
    # Print ASCII art
    print_ascii_art()
    print()
    
    # The quote
    quote = "I don't want to achieve immortality through my work. I want to achieve it through not dying. But since that's not working, I'll settle for understanding why I'm afraid of the dark when I know the light will eventually come back."
    
    # Print quote with typing effect
    print(f"{BOLD}{YELLOW}\"{RESET}", end="")
    slow_type(quote, delay=0.04)
    print(f"{BOLD}{YELLOW}\"{RESET}")
    print()
    
    # Print author
    print(f"{CYAN}— A nervous existentialist who's probably overthinking this entire quote{RESET}")
    print()
    
    # Print some extra philosophical musings
    extras = [
        "P.S. I called my therapist about my fear of commitment. She said, 'Just think of it as a long-term relationship with yourself.'",
        "P.P.S. Then I thought, 'What if I'm in a long-term relationship with myself and I don't even like myself?'",
        "P.P.P.S. This is why I prefer movies. At least the characters have plot armor."
    ]
    
    for extra in extras:
        print(f"{MAGENTA}{extra}{RESET}")
        time.sleep(0.5)
    
    # Final existential dread
    print(f"\n{RED}...and that's why I carry a spare existential crisis in my pocket.{RESET}")

if __name__ == "__main__":
    main()