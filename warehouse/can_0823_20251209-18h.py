"""
Campbell's Soup Can #823
Produced: 2025-12-09 18:44:55
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'blink': '\033[5m',
    'reset': '\033[0m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
}

def print_slowly(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_anxiety_meter():
    """Draw a neurotic anxiety meter"""
    print(f"{COLORS['bg_yellow']}{COLORS['blue']}{COLORS['bold']}")
    print(" " * 50)
    print("            ANXIETY LEVEL: 97%")
    print(" " * 50)
    print(f"{COLORS['reset']}")
    
    # Draw the meter bar
    bar_length = 40
    filled = int(bar_length * 0.97)
    print(f"{COLORS['red']}{COLORS['bold']}")
    print(" " * 10 + "█" * filled + f"{COLORS['yellow']}⚡{COLORS['cyan']} PANIC!{COLORS['red']}█" * (bar_length - filled))
    print(f"{COLORS['reset']}")

def draw_couch():
    """ASCII art of a psychoanalyst couch"""
    couch = f"""
{COLORS['cyan']}          /\\
         /  \\
        /    \\
       /      \\
      /        \\
     /          \\
    /            \\
   /              \\
  /                \\
 /                  \\
/                    \\
{COLORS['yellow']}|  {COLORS['bold']}WOODY'S COUCH{COLORS['reset']}{COLORS['yellow']}    |
|  - 50% off today -   |
|  existential dread  |
|  included free     {COLORS['cyan']}|
{COLORS['cyan']} \\                    /
 \\                  /
  \\                /
   \\              /
    \\            /
     \\          /
      \\        /
       \\      /
        \\    /
         \\  /
          \\/
{COLORS['reset']}"""
    return couch

def main():
    # Clear screen and set up
    print("\033[2J\033[H", end="")  # Clear and move cursor to top
    
    # Title with blinking effect (just for fun)
    print(f"\n{COLORS['bg_magenta']}{COLORS['white']}{COLORS['bold']}")
    print(" " * 15 + "WOODY ALLEN PHILOSOPHICAL ADVICE" + " " * 15)
    print(f"{COLORS['reset']}\n")
    
    # Draw the couch
    print(draw_couch())
    
    # Draw anxiety meter
    draw_anxiety_meter()
    
    # The quote with dramatic pause
    print(f"\n{COLORS['magenta']}{COLORS['bold']}")
    print(" " * 20 + "AND NOW, A PROFOUND THOUGHT:")
    print(f"{COLORS['reset']}")
    
    time.sleep(1)
    
    # Typewriter effect for the quote
    quote = "I'm not afraid of death, I just don't want to be there when it happens. Also, I'm pretty sure my therapist is judging me, and frankly, I don't like his couch."
    
    print(f"\n{COLORS['blue']}{COLORS['bold']}")
    print(" " * 10 + "╔" + "═" * 50 + "╗")
    
    # Print quote with typing effect
    print(" " * 10 + "║", end="")
    print_slowly(f" {quote} ", delay=0.02)
    
    print(" " * 10 + "╚" + "═" * 50 + "╝")
    print(f"{COLORS['reset']}")
    
    # Signature with neurotic disclaimer
    time.sleep(0.5)
    print(f"\n{COLORS['yellow']}{COLORS['underline']}")
    print(" " * 25 + "- Woody Allen (probably)")
    print(f"{COLORS['reset']}")
    
    # Add some neurotic asterisks
    print(f"\n{COLORS['red']}")
    print(" " * 15 + "*" * 50)
    print(" " * 15 + "* DISCLAIMER: This quote may increase your       *")
    print(" " * 15 + "* existential dread by 37%. Side effects include *")
    print(" " * 15 + "* mild hypochondria and excessive worrying.      *")
    print(" " * 15 + "*" * 50)
    print(f"{COLORS['reset']}")
    
    # Final touch - some scattered anxiety dots
    print(f"\n{COLORS['cyan']}")
    for i in range(3):
        time.sleep(0.3)
        dots = "." * random.randint(3, 8)
        spaces = " " * random.randint(10, 60)
        print(spaces + dots)
    print(f"{COLORS['reset']}")

if __name__ == "__main__":
    main()