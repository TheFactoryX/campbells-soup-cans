"""
Campbell's Soup Can #493
Produced: 2025-11-24 15:36:09
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
    'reset': '\033[0m'
}

def print_with_typewriter(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_worried_face():
    """Animate a worried Woody Allen-style face"""
    faces = [
        "    🤨    ",
        "    😰    ",
        "    😟    ",
        "    😥    ",
        "    😦    ",
        "    😨    ",
        "    😖    ",
        "    😫    "
    ]
    
    for _ in range(3):
        for face in faces:
            print(f"\r{COLORS['cyan']}{face}{COLORS['reset']}", end="", flush=True)
            time.sleep(0.1)

def print_wobbly_text(text, amplitude=2, frequency=0.3):
    """Print wobbly text effect"""
    for i, char in enumerate(text):
        offset = int(amplitude * (2 * (i * frequency) % 2 - 1))
        if offset > 0:
            print(' ' * offset + char)
            time.sleep(0.02)
        else:
            print(char)
            time.sleep(0.02)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Print header with anxiety
    print(f"\n{COLORS['red']}{COLORS['bold']}")
    print_with_typewriter("⚠️  EXISTENTIAL CRISIS DETECTED ⚠️", 0.1)
    print(f"{COLORS['reset']}")
    
    # Animate worried face
    print("\n")
    animate_worried_face()
    
    # Print the quote with dramatic effect
    quote = "I don't mind dying; I just don't want to be there when it happens... and honestly, I'm worried the afterlife will have terrible healthcare and even worse neurologists."
    author = "-- Woody Allen (probably during therapy)"
    
    print(f"\n\n{COLORS['yellow']}")
    print("=" * 60)
    print(f"{COLORS['bold']}{COLORS['magenta']}🧠 WOODY ALLEN SAYS:{COLORS['reset']} {COLORS['yellow']}")
    print("=" * 60)
    print(f"{COLORS['white']}")
    
    # Print quote with typewriter effect
    print_with_typewriter(f'  "{quote}"', 0.04)
    
    print(f"\n{COLORS['cyan']}")
    print_with_typewriter(f"  {author}", 0.06)
    print(f"{COLORS['yellow']}")
    print("=" * 60)
    print(f"{COLORS['reset']}")
    
    # Add some neurotic footnotes
    footnotes = [
        "¹ This quote was approved by my therapist (after 3 sessions)",
        "² Not responsible for increased existential dread",
        "³ If you laugh, you're coping. If you cry, we're the same person."
    ]
    
    print(f"\n{COLORS['blue']}")
    for footnote in footnotes:
        print_with_typewriter(f"{footnote}", 0.03)
        time.sleep(0.2)
    print(f"{COLORS['reset']}")
    
    # Final anxiety attack in ASCII
    print(f"\n{COLORS['red']}")
    print("💓 💓 💓  ANXIETY LEVEL: CRITICAL  💓 💓 💓")
    print(f"{COLORS['reset']}")
    
    # Little spinning worry symbol
    for _ in range(2):
        for symbol in ['◐', '◓', '◑', '◒']:
            print(f"\r{COLORS['magenta']}   {symbol} WORRYING INTENSIFIES...{COLORS['reset']}", end="", flush=True)
            time.sleep(0.2)
    
    print(f"\n\n{COLORS['green']}Remember: Death is not the end... it's just the final therapy session.{COLORS['reset']}")

if __name__ == "__main__":
    main()