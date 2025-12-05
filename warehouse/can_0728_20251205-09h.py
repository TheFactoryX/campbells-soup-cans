"""
Campbell's Soup Can #728
Produced: 2025-12-05 09:34:44
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic, Woody Allen-style philosophical quote generator.
Because nothing says "existential dread" like ANSI escape codes.
"""

import sys
import time
import random

# Colors that scream "I'm in therapy and it's not helping"
COLORS = {
    'nervous': '\033[93m',  # Yellow - the color of anxiety
    'doom': '\033[91m',      # Red - impending disaster
    'therapy': '\033[94m',   # Blue - the couch is judging me
    'existential': '\033[95m', # Magenta - deep philosophical crisis
    'coffee': '\033[96m',    # Cyan - my only sustenance
    'neurotic': '\033[92m',  # Green - envy and indigestion
    'reset': '\033[0m'       # Reset - back to reality (sigh)
}

def print_ellipse(text, color='nervous', delay=0.05):
    """Type like you're having a panic attack, but make it stylish."""
    sys.stdout.write(COLORS[color])
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(COLORS['reset'])
    print()

def draw_anxious_spiral(size=12):
    """Draw a spiral because my thoughts won't stop spiraling."""
    print(COLORS['doom'] + " " * 10 + "∞" + COLORS['reset'])
    print(COLORS['existential'] + " " * 8 + "It's all meaningless!" + COLORS['reset'])
    
def draw_coffee_stain():
    """A coffee stain because I'm running on caffeine and existential dread."""
    stain = [
        "      @@@@      ",
        "    @@@@@@@@    ",
        "   @@@@@@@@@@   ",
        "  @@@@@@@@@@@@  ",
        " @@@@@@@@@@@@@@ ",
        "@@@@@@@@@@@@@@@@",
        "@@@@@@    @@@@@@",
        " @@@@@    @@@@@ ",
        "  @@@@    @@@@  ",
        "   @@      @@   ",
        "    @      @    "
    ]
    for line in stain:
        print(COLORS['coffee'] + line + COLORS['reset'])

def main():
    # Clear screen because sometimes I wish I could clear my mind
    print('\033[2J\033[H', end='')
    
    # Draw some visual anxiety
    draw_anxious_spiral()
    print()
    
    # Coffee stain for authenticity
    draw_coffee_stain()
    print()
    
    # Frame the quote like it's hanging in a museum of neuroses
    print(COLORS['neurotic'] + "=" * 70 + COLORS['reset'])
    print(COLORS['neurotic'] + "|" + " " * 68 + "|" + COLORS['reset'])
    
    # The quote that captures the human condition (in 12 words or less)
    quote = "I don't suffer from existential dread; I enjoy it—it gives my anxiety something to do."
    
    # Center it because even my neuroses deserve to be centered
    padding = (68 - len(quote)) // 2
    print(COLORS['neurotic'] + "|" + " " * padding + COLORS['reset'], end='')
    print_ellipse(quote, 'existential', 0.08)
    print(COLORS['neurotic'] + "|" + " " * padding + " " * (68 - len(quote) - padding) + "|" + COLORS['reset'])
    print(COLORS['neurotic'] + "|" + " " * 68 + "|" + COLORS['reset'])
    print(COLORS['neurotic'] + "=" * 70 + COLORS['reset'])
    
    # The byline
    byline = "— Woody Allen (probably said this during therapy)"
    print("\n" + COLORS['therapy'] + " " * (35 - len(byline)//2) + byline + COLORS['reset'])
    
    # A post-it note of self-doubt
    print("\n" + COLORS['nervous'] + "P.S. Was that quote funny? Probably not. Nothing ever is." + COLORS['reset'])
    
    # Blinking cursor because the anxiety never stops
    for _ in range(3):
        print(COLORS['doom'] + " " * 40 + "█" + COLORS['reset'], end='\r')
        time.sleep(0.5)
        print(" " * 41, end='\r')
        time.sleep(0.5)

if __name__ == "__main__":
    main()