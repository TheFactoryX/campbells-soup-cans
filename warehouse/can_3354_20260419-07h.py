"""
Campbell's Soup Can #3354
Produced: 2026-04-19 07:46:00
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

# --- ANSI COLOR ESCAPE CODES ---
class Colors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter(text, delay=0.06, color=Colors.CYAN):
    """Prints text with a neurotic, hesitant typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.END}")
        sys.stdout.flush()
        # Simulate nervous hesitation
        if char == ',' or char == ';' or char == ':':
            time.sleep(delay * 5)
        elif char == '.':
            time.sleep(delay * 10)
        else:
            time.sleep(delay)

def draw_box(text, width=60):
    """Draws a sophisticated, slightly claustrophobic border."""
    top = f"{Colors.MAGENTA}╔{'═' * (width-2)}╗{Colors.END}"
    bottom = f"{Colors.MAGENTA}╚{'═' * (width-2)}╝{Colors.END}"
    
    print(top)
    # Center the text within the box
    lines = text.split('\n')
    for line in lines:
        padding = (width - len(line) - 2) // 2
        if padding < 0: padding = 0
        line_str = " " * padding + line + " " * (width - len(line) - 2 - padding)
        print(f"{Colors.MAGENTA}║{Colors.END}{line_str}{Colors.MAGENTA}║{Colors.END}")
    print(bottom)

def dramatic_intro():
    """A sequence of neurotic visual glitches."""
    glitch_chars = ["?", "!", "...", "§", "ø", "∆", "∞"]
    for _ in range(15):
        clear_screen()
        color = random.choice([Colors.RED, Colors.YELLOW, Colors.MAGENTA, Colors.BLUE])
        char = random.choice(glitch_chars)
        print(f"\n\n\n\t\t{color}{Colors.BOLD}{char * random.randint(1, 5)}{Colors.END}")
        time.sleep(0.05)
    clear_screen()

def main():
    # The Quote
    quote = (
        "\"I often wonder if the meaning of life\n"
        "is actually hidden in the fine print\n"
        "of our existential dread—and if so,\n"
        "I'm far too neurotic to read\n"
        "that far down.\""
    )

    # ASCII Art of a nervous man (minimalist)
    man = r"""
          (o _ o)
           \ - /
          --| |--
            / \
    """

    try:
        dramatic_intro()
        
        print("\n" * 2)
        print(f"{Colors.YELLOW}{man}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}--- AN EXISTENTIAL CRISIS IN PROGRESS ---{Colors.END}\n")
        
        time.sleep(1)
        
        # The main reveal
        draw_box(quote, width=50)
        
        print(f"\n{Colors.RED}{Colors.UNDERLINE}Status: Highly Unsettled.{Colors.END}\n")
        
        # Final flicker effect
        for _ in range(3):
            sys.stdout.write(f"\r{Colors.MAGENTA}Thinking about death...{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.4)
            sys.stdout.write(f"\r{' ' * 30}\r")
            sys.stdout.flush()
            time.sleep(0.2)
            
        print(f"\r{Colors.BLUE}...And it's all much too much.{Colors.END}\n")

    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Even the interruption is an existential threat!{Colors.END}")

if __name__ == "__main__":
    main()