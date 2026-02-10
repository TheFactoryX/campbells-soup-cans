"""
Campbell's Soup Can #2151
Produced: 2026-02-10 12:00:25
Worker: Pony Alpha (openrouter/pony-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'dim': '\033[2m',
    'bold': '\033[1m',
    'italic': '\033[3m',
    'reset': '\033[0m',
    'bg_black': '\033[40m',
}

def typewriter(text, delay=0.02):
    """Print text with typewriter effect"""
    for char in text:
        # Random color for each character for neurotic effect
        color = random.choice(['yellow', 'cyan', 'magenta', 'white'])
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay if char not in '.!?' else delay * 8)
    print()

def draw_frame():
    """Draw a neurotic wobbly frame"""
    top = f"{COLORS['dim']}╔" + "═" * 58 + "╗"
    bottom = f"\n╚" + "═" * 58 + "╝{COLORS['reset']}"
    print(top)
    return bottom

def nervous_cursor():
    """Animate a nervous cursor"""
    chars = ['▌', '█', '▌', ' ', '▌', '█']
    for _ in range(3):
        for c in chars:
            sys.stdout.write(f"\r{COLORS['yellow']}{c}{COLORS['reset']}")
            sys.stdout.flush()
            time.sleep(0.05)

def main():
    # Clear screen and add some spacing
    print("\n" * 2)
    
    # Neurotic header
    header = f"{COLORS['bold']}{COLORS['red']}⚠ WOODY'S EXISTENTIAL CRISIS ⚠{COLORS['reset']}"
    print(f"{' ' * 18}{header}\n")
    
    # Draw frame
    bottom = draw_frame()
    
    # The quote - with nervous anticipation
    print(f"{COLORS['dim']}║{COLORS['reset']}", end=" ")
    
    nervous_cursor()
    print("\r    ", end="")  # Clear cursor
    
    # The actual quote
    quote = "I've spent so much time worrying about the meaning of life that I completely forgot to live it. On the bright side, my anxiety has excellent pacing."
    
    typewriter(f"{COLORS['italic']}{quote}{COLORS['reset']}", 0.025)
    
    # Close frame
    print(f"{COLORS['dim']}║{' ' * 58}║")
    print(f"║{COLORS['reset']}", end="")
    print(f"{COLORS['cyan']}    — Someone who needs therapy{COLORS['reset']}", end="")
    print(f"{COLORS['dim']}{' ' * 22}║")
    print(bottom)
    
    # Neurotic footer animation
    print()
    footer = "∗sweats nervously in philosophical∗"
    for i, char in enumerate(footer):
        color = 'dim' if i % 2 else 'yellow'
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")

if __name__ == "__main__":
    main()