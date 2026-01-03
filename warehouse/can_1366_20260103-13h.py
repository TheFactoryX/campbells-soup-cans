"""
Campbell's Soup Can #1366
Produced: 2026-01-03 13:40:36
Worker: Arcee AI: Trinity Mini (free) (arcee-ai/trinity-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    # Woody Allen style quote
    quote = """
    "I'm not afraid of death; I just don't want to be there when it happens.
    Life is a series of terrifying moments interrupted by brief, terrifying respites.
    The universe is a cosmic joke, and I'm the punchline that keeps getting rewritten."
    """
    
    # ASCII art brain with stars
    brain = """
    .-------.
    |  O   O |
    |   _   |
    |  / \  |
    |  \_/  |
    '-------'
    """
    
    # Color codes
    BLACK = '\x1b[48;5;16m'
    YELLOW = '\x1b[38;5;226m'
    RESET = '\x1b[0m'
    
    # Print brain art with color
    print(f"{BLACK}{YELLOW}{brain}{RESET}")
    
    # Print quote with colorful background
    print(f"{BLACK}{YELLOW}{quote}{RESET}")
    
    # Add star border
    print(f"{BLACK}{YELLOW}  .-------.  {RESET}")
    print(f"{BLACK}{YELLOW} /         \\ {RESET}")
    print(f"{BLACK}{YELLOW} |   *   *  | {RESET}")
    print(f"{BLACK}{YELLOW} \\         / {RESET}")
    print(f"{BLACK}{YELLOW}  '-------'  {RESET}")

if __name__ == "__main__":
    main()