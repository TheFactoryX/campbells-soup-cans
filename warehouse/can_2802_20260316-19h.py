"""
Campbell's Soup Can #2802
Produced: 2026-03-16 19:20:16
Worker: Hunter Alpha (openrouter/hunter-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def print_colored(text, color):
    """Print text with ANSI color codes"""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'reset': '\033[0m'
    }
    print(f"{colors.get(color, '')}{text}{colors['reset']}")

def animate_text(text, delay=0.03):
    """Print text with typing animation"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(text, padding=3):
    """Print text in a decorative ASCII box"""
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    width = max_length + padding * 2 + 2
    
    # Top border
    print_colored("╔" + "═" * (width - 2) + "╗", 'yellow')
    
    # Empty line
    print_colored("║" + " " * (width - 2) + "║", 'yellow')
    
    # Text lines
    for line in lines:
        padding_left = (width - len(line) - 2) // 2
        padding_right = width - len(line) - 2 - padding_left
        print_colored("║" + " " * padding_left + line + " " * padding_right + "║", 'yellow')
    
    # Empty line
    print_colored("║" + " " * (width - 2) + "║", 'yellow')
    
    # Bottom border
    print_colored("╚" + "═" * (width - 2) + "╝", 'yellow')

def print_man_emoji():
    """Print a simple man emoji using ASCII art"""
    print_colored("""
       .-""""""-.
     .'          '.
    /   O      O   \\
   :                 :
   :                 :
   :                 :
    '.             .'
      '-.........-'
     /|         |\\
    / |         | \\
   /  |         |  \\
      (         )
       \\_______/
    """, 'cyan')

def main():
    # The Woody Allen-style philosophical quote
    quote = """I've been thinking about mortality a lot lately.
Not in a morbid way, more like... in a "should I buy
the extended warranty for my toaster" kind of way.
My therapist says I'm confusing existential dread
with kitchen appliance anxiety. But really, what's
the difference? Both are about things that could
end suddenly and leave you with crumbs."""
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Print header
    print_colored("=" * 50, 'purple')
    print_colored("       PHILOSOPHICAL MUSINGS", 'bold')
    print_colored("          (Woody Allen Style)", 'purple')
    print_colored("=" * 50, 'purple')
    print()
    
    # Print man emoji
    print_man_emoji()
    print()
    
    # Print animated intro
    intro_text = "Ah, existence... the only subscription you can't cancel."
    animate_text(intro_text, 0.05)
    print()
    
    # Print the quote in a box
    print_box(quote)
    print()
    
    # Print philosophical punchline
    punchlines = [
        "At least with a broken toaster, you can get a new one.",
        "My toaster has better survival instincts than I do.",
        "Maybe the real enlightenment was the appliances we feared along the way.",
        "I'd rather face my mortality than face a morning without toast."
    ]
    
    punchline = random.choice(punchlines)
    animate_text(f"So I say: {punchline}", 0.04)
    
    # Print decorative footer
    print()
    print_colored("~" * 50, 'green')
    print_colored("  (Remember: We're all just toasters, waiting to pop)", 'green')
    print_colored("~" * 50, 'green')

if __name__ == "__main__":
    main()