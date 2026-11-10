"""
Campbell's Soup Can #5227
Produced: 2026-11-10 09:51:31
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI color codes
class Colors:
    NEUROTIC_BLUE = '\033[94m'
    ANXIOUS_YELLOW = '\033[93m'
    DEPRESSIVE_CYAN = '\033[96m'
    PARANOID_MAGENTA = '\033[95m'
    EXISTENTIAL_RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'

def slow_print(text, delay=0.03, color=Colors.RESET):
    """Print text slowly with a given color"""
    for char in text:
        print(f"{color}{char}{Colors.RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def create_anxiety_border(width=60):
    """Create a border that looks like nervous ticks"""
    borders = ["-", "_", "~", "."]
    return "".join(random.choice(borders) for _ in range(width))

def print_woody_allen_quote():
    """Print a Woody Allen style quote with visual flair"""
    
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # Title with existential dread
    print(f"{Colors.PARANOID_MAGENTA}{Colors.BOLD}")
    print("    ___                   ___                   ___")
    print("   /__\\                 /__\\                 /__\\")
    print("  /    \\               /    \\               /    \\")
    print(" /      \\             /      \\             /      \\")
    print("/________\\___________/________\\___________/________\\")
    print(f"{Colors.RESET}")
    
    # Subtitle
    print(f"{Colors.ANXIOUS_YELLOW}{Colors.ITALIC}")
    print("    An Existential Musing by Someone Who Probably Overthinks This")
    print(f"{Colors.RESET}\n")
    
    # The quote - original Woody Allen style
    quote = (
        "I always thought I was an existentialist, but then I realized "
        "I was just really, really tired. The universe is a cruel, "
        "indifferent place, and yet here I am, still trying to find "
        "meaning in a world where the only certainty is that my "
        "next therapy session will probably be about my fear of "
        "commitment... to this sentence."
    )
    
    # Print border
    border = create_anxiety_border()
    print(f"{Colors.DEPRESSIVE_CYAN}{border}{Colors.RESET}")
    
    # Print quote with dramatic pauses
    print(f"{Colors.NEUROTIC_BLUE}{Colors.BOLD}")
    slow_print("    \"", 0.1, Colors.NEUROTIC_BLUE)
    
    words = quote.split()
    for i, word in enumerate(words):
        if i % 8 == 0 and i > 0:  # New line every 8 words for dramatic effect
            print()
            slow_print("     ", 0.05, Colors.NEUROTIC_BLUE)
        
        # Randomly emphasize certain words
        if word.lower() in ["existentialist", "cruel", "indifferent", "meaning", "certainty"]:
            color = Colors.EXISTENTIAL_RED
            delay = 0.1
        elif word.lower() in ["really", "tired", "here", "am"]:
            color = Colors.ANXIOUS_YELLOW
            delay = 0.08
        else:
            color = Colors.NEUROTIC_BLUE
            delay = 0.04
            
        slow_print(word + " ", delay, color)
    
    slow_print("\"", 0.1, Colors.NEUROTIC_BLUE)
    print(f"{Colors.RESET}")
    
    # Bottom border
    print(f"{Colors.DEPRESSIVE_CYAN}{border}{Colors.RESET}")
    
    # Neurotic footnote
    print(f"\n{Colors.PARANOID_MAGENTA}{Colors.ITALIC}")
    print("    P.S. - I probably overthought this quote too much.")
    print("    P.P.S. - Is it too late to change my mind about being a philosopher?")
    print("    P.P.P.S. - What if I'm just pretending to be deep?")
    print(f"{Colors.RESET}")
    
    # Animated existential crisis (dots that appear and disappear)
    print(f"\n{Colors.EXISTENTIAL_RED}")
    print("    Thinking", end="")
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(" still thinking...", end="", flush=True)
    time.sleep(1)
    print("\r    Still overthinking it" + " " * 30 + f"{Colors.RESET}")

if __name__ == "__main__":
    print_woody_allen_quote()