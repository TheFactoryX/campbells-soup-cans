"""
Campbell's Soup Can #4584
Produced: 2026-08-14 15:07:06
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
A delightfully neurotic philosophical musing...
In the style of Woody Allen (but with better font choices).
"""

import sys
import time
import random

# ANSI color codes because existential dread looks better in Technicolor
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    
    # The existential palette
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Background therapy
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

def typewriter(text, delay=0.03, color=""):
    """Print text like a neurotic philosopher typing furiously"""
    for char in text:
        print(color + char + Colors.RESET, end='', flush=True)
        time.sleep(delay)
    print()

def animated_box(text_lines, border_color=Colors.CYAN, fill_color=Colors.YELLOW, 
                  animation_delay=0.1, glitch_effect=True):
    """Create a beautifully neurotic box with glitchy animations"""
    
    max_len = max(len(line) for line in text_lines)
    width = max_len + 6  # Padding for dramatic effect
    
    # Top border with dramatic flair
    top = border_color + Colors.BOLD + "+" + "-" * width + "+" + Colors.RESET
    bottom = border_color + Colors.BOLD + "+" + "-" * width + "+" + Colors.RESET
    
    # Clear some space for the existential void
    for _ in range(3):
        print()
    
    # Print top border with animation
    print("  " + top)
    
    # Center and print each line with neurotic jitter
    for i, line in enumerate(text_lines):
        if glitch_effect:
            # Occasional existential crisis in the formatting
            jitter = random.choice([0, 0, 0, 1, -1, 0, 0])
            spaces = (width - len(line)) // 2 + jitter
        else:
            spaces = (width - len(line)) // 2
            
        spaces = max(1, spaces)  # Don't let anxiety affect spacing too much
        
        left_pad = " " * spaces
        right_pad = " " * (width - len(line) - spaces)
        
        if i == 0 and glitch_effect:
            # Special neurotic entrance for the first line
            print("  " + border_color + "|" + " " * width + "|" + Colors.RESET)
            time.sleep(animation_delay)
            
        styled_line = f"{border_color}|{Colors.RESET} {fill_color}{line}{Colors.RESET} {left_pad}{right_pad}{border_color}|{Colors.RESET}"
        print("  " + styled_line)
        time.sleep(animation_delay * (0.5 + random.random()))
    
    # Bottom border
    print("  " + bottom)
    
    for _ in range(2):
        print()

def create_woody_allen_quote():
    """Generate a quote so neurotic it makes a therapist nervous"""
    
    # The quote that asks the big questions while worrying about dinner
    quote_lines = [
        "I don't want to achieve immortality",
        "through my work...",
        "I want to achieve it",
        "by not dying.",
        "",
        "See? Perfectly reasonable.",
        "For a man who's terrified of",
        "his own mortgage."
    ]
    
    return quote_lines

def print_ascii_art_header():
    """Print a wonderfully neurotic ASCII art header"""
    
    art = [
        "  ┌─────────────────────────────────────────┐",
        "  │    ╔╗╔╔╗╔╔╦╗╦╔╦╗╦╚╗╔╚╔╦╗                │",
        "  │    ║║║╠╩╗ ║ ║ ║ ║╠╣ ║║╠╩╗ ║               │",
        "  │    ╚╝╩╚═╝ ╩ ╩ ╩ ╩╚═╝╩ ╩ ╩ ╩               │",
        "  │                                         │",
        "  │  A Neurotic Philosophical Musing        │",
        "  └─────────────────────────────────────────┘"
    ]
    
    for line in reversed(range(len(art))):
        print(Colors.MAGENTA + Colors.DIM + "  " + art[line] + Colors.RESET)
        time.sleep(0.1)
    
    print()

def print_credits():
    """Self-deprecating credits because humility is important"""
    
    credits = f"""
{Colors.DIM}
╔════════════════════════════════════════════════════════════╗
║  "A profound statement about the human condition."          ║
║  — Someone who definitely knows what they're doing         ║
║                                                           ║  
║  This program may or may not solve your problems.          ║
║  It probably won't.                                        ║
╚════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
    
    for char in credits:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def main():
    """Where the anxiety begins"""
    
    # Clear screen for maximum dramatic effect
    print("\033[2J\033[H", end='')  # ANSI clear screen
    
    # Header with existential anxiety
    print(Colors.RED + Colors.BOLD + "\n" + "="*50 + Colors.RESET)
    print(Colors.RED + Colors.BOLD + "  AN EXISTENTIAL CRISIS IN D minor".center(50) + Colors.RESET)
    print(Colors.RED + Colors.BOLD + "="*50 + Colors.RESET)
    print()
    
    # Create and display the quote
    quote_lines = create_woody_allen_quote()
    
    # Print it in a beautifully neurotic box
    animated_box(quote_lines, 
                 border_color=Colors.MAGENTA,
                 fill_color=Colors.YELLOW,
                 animation_delay=0.3,
                 glitch_effect=True)
    
    # Some existential commentary
    commentary = [
        ("Which reminds me...", Colors.CYAN),
        ("Did I leave the oven on?", Colors.YELLOW),
        ("Or worse...", Colors.RED),
        ("Did I remember to exist today?", Colors.WHITE),
    ]
    
    for text, color in commentary:
        typewriter("  " + text, delay=0.05, color=color + Colors.ITALIC)
        time.sleep(0.5)
    
    print()
    
    # Final neurotic flourish
    final_message = (
        f"{Colors.BOLD}Anyway...{Colors.RESET} "
        f"{Colors.DIM}(this has been a public service announcement "
        f"from your constantly worried neighbor){Colors.RESET}"
    )
    typewriter("  " + final_message, delay=0.04, color="")
    
    # Print credits with appropriate shame
    print_credits()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Even the existential crisis can be interrupted
        print(f"\n{Colors.YELLOW}Well, that was uncomfortable.{Colors.RESET}")
        sys.exit(0)