"""
Campbell's Soup Can #469
Produced: 2025-11-23 13:32:36
Worker: Auto Router (openrouter/auto)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_box(quote, author):
    lines = quote.split('\n')
    max_length = max(len(line) for line in lines)
    width = max_length + 4
    
    # Top border
    print_colored("┌" + "─" * (width - 2) + "┐", "93")
    
    # Quote lines
    for line in lines:
        padding = " " * (max_length - len(line))
        print_colored("│ ", "93", end="")
        print_colored(line + padding, "96", end="")
        print_colored(" │", "93")
    
    # Author line
    author_line = f"- {author}"
    author_padding = " " * (max_length - len(author_line))
    print_colored("│ ", "93", end="")
    print_colored(author_line + author_padding, "95", end="")
    print_colored(" │", "93")
    
    # Bottom border
    print_colored("└" + "─" * (width - 2) + "┘", "93")

def animated_intro():
    print_colored("🎭 WOODY ALLEN'S NEUROTIC WISDOM 🎭", "91")
    print()
    time.sleep(1)
    
    # Animated thinking dots
    print_colored("Contemplating existence", "92", end="")
    for _ in range(3):
        for dot in ["", ".", "..", "..."]:
            print(f"\r\033[92mContemplating existence{dot}   \033[0m", end="", flush=True)
            time.sleep(0.3)
    print("\n")

def print_colored(text, color_code, end="\n"):
    print(f"\033[{color_code}m{text}\033[0m", end=end)

# Main execution
if __name__ == "__main__":
    # Clear screen and show animated intro
    print("\033[2J\033[H")
    animated_intro()
    
    # The quote
    quote = """I told my therapist I had a fear of commitment,
so he made me sign a contract stating I would
continue therapy indefinitely. Now I'm afraid
of my therapist AND commitment. It's like getting
two anxieties for the price of one - which is
great because I also have a fear of bad deals."""
    
    # Create the visual presentation
    create_box(quote, "Woody Allen (probably)")
    
    print()
    print_colored("💭 Remember: Anxiety is just your brain's way of overthinking survival! 💭", "94")
    
    # Blinking exit message
    for _ in range(3):
        print_colored("\n✨ *adjusts glasses nervously* ✨", "93")
        time.sleep(0.5)
        print("\033[A\033[K", end="")  # Move up and clear line
        time.sleep(0.5)
    
    print_colored("\n✨ *adjusts glasses nervously* ✨", "93")