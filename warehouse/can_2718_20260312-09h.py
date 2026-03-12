"""
Campbell's Soup Can #2718
Produced: 2026-03-12 09:02:25
Worker: Hunter Alpha (openrouter/hunter-alpha)
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

# ANSI color codes
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def type_text(text, color=Colors.WHITE, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_woody_quote():
    """Print a funny philosophical quote in Woody Allen's style"""
    
    # The quote parts
    quote_parts = [
        ("You know,", Colors.YELLOW),
        ("I've been thinking about mortality a lot lately.", Colors.CYAN),
        ("", Colors.WHITE),
        ("Not in a", Colors.YELLOW),
        ("'I should write my will'", Colors.RED),
        ("kind of way,", Colors.YELLOW),
        ("but more in a", Colors.YELLOW),
        ("'why do I keep buying green bananas'", Colors.GREEN),
        ("kind of way.", Colors.YELLOW),
        ("", Colors.WHITE),
        ("Existence is like a bad movie you can't walk out of—", Colors.MAGENTA),
        ("except the popcorn is overpriced,", Colors.CYAN),
        ("the person behind you keeps kicking your seat,", Colors.RED),
        ("and you're pretty sure the plot stopped making sense", Colors.BLUE),
        ("around the second act.", Colors.BLUE),
        ("", Colors.WHITE),
        ("The only philosophical question that truly haunts me is:", Colors.BOLD + Colors.YELLOW),
        ("If I'm not here tomorrow,", Colors.WHITE),
        ("will someone finally water my plants?", Colors.GREEN),
        ("", Colors.WHITE),
        ("I mean,", Colors.YELLOW),
        ("even Camus never had to deal with that level of absurdity.", Colors.MAGENTA)
    ]
    
    # ASCII art header
    print(Colors.BOLD + Colors.RED + """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║  "I'm not afraid of death;                         ║
    ║   I just don't want to be there when it happens."  ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """ + Colors.RESET)
    
    # Add some "nervous" decorative elements
    for _ in range(3):
        print(Colors.YELLOW + "~" * 60 + Colors.RESET)
        time.sleep(0.1)
    
    print()
    
    # Print the quote with typewriter effect
    for text, color in quote_parts:
        if text == "":
            print()
            time.sleep(0.2)
        else:
            type_text(text, color, delay=0.04)
            time.sleep(0.1)
    
    print()
    
    # Add some existential decoration
    print(Colors.MAGENTA + "*" * 60 + Colors.RESET)
    
    # Final flourish
    type_text("— Woody Allen (probably, while looking nervously at his watch)", 
              Colors.BOLD + Colors.CYAN, delay=0.05)
    
    # Add a "neurotic" PS
    time.sleep(0.5)
    print()
    type_text("P.S. This quote is 100% accurate, give or take 90%.", 
              Colors.YELLOW, delay=0.02)
    
    # Final decorative element
    print(Colors.GREEN + """
    ╭─────────────────────────────────────────╮
    │  Remember: We're all just stardust      │
    │  with anxiety disorders.               │
    ╰─────────────────────────────────────────╯
    """ + Colors.RESET)

def main():
    """Main function to run the program"""
    try:
        print_woody_quote()
    except KeyboardInterrupt:
        print(Colors.RED + "\n\nEven quitting this program feels existential..." + Colors.RESET)

if __name__ == "__main__":
    main()