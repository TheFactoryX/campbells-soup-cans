"""
Campbell's Soup Can #593
Produced: 2025-11-29 05:33:38
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
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

def print_with_typewriter(text, delay=0.05):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_worried_face():
    """Animate a worried Woody Allen-style face"""
    faces = [
        "    🙁    ",
        "    😟    ",
        "    😰    ",
        "    😱    ",
        "    😥    ",
        "    😦    "
    ]
    
    for _ in range(3):
        for face in faces:
            sys.stdout.write(f"\r{COLORS['yellow']}{face}{COLORS['reset']}")
            sys.stdout.flush()
            time.sleep(0.2)

def print_woody_quote():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Print header with animation
    print_with_typewriter(f"{COLORS['magenta']}{COLORS['bold']}" + "╔" + "═" * 58 + "╗" + f"{COLORS['reset']}")
    
    header_text = "   WOODY ALLEN'S GUIDE TO HAPPINESS (OR LACK THEREOF)   "
    print_with_typewriter(f"{COLORS['magenta']}║{COLORS['reset']}{COLORS['cyan']}{header_text}{COLORS['magenta']}║{COLORS['reset']}")
    
    print_with_typewriter(f"{COLORS['magenta']}" + "╚" + "═" * 58 + "╝" + f"{COLORS['reset']}")
    
    # Animate worried face
    animate_worried_face()
    print()
    
    # The quote with dramatic pauses
    quote = "I'm not afraid of death; I just don't want to be there when it happens... "
    continuation = "Then again, I'm probably overthinking this. I always overthink everything. "
    final = "Existence is basically one long therapy bill with occasional pizza breaks."
    
    print()
    print_with_typewriter(f'{COLORS["blue"]}{COLORS["bold"]}💭  WOODY SAYS:{COLORS["reset"]}')
    print()
    time.sleep(0.5)
    
    print_with_typewriter(f'{COLORS["white"]}"{quote}"{COLORS["reset"]}', 0.08)
    time.sleep(1.2)
    
    print_with_typewriter(f'{COLORS["white"]}"{continuation}"{COLORS["reset"]}', 0.07)
    time.sleep(1.0)
    
    print_with_typewriter(f'{COLORS["white"]}"{final}"{COLORS["reset"]}', 0.06)
    
    print()
    time.sleep(0.5)
    
    # Add some neurotic footnotes
    footnotes = [
        f"{COLORS['red']}⓵{COLORS['reset']} I scheduled this existential crisis for Tuesday, but I got anxious and moved it to today.",
        f"{COLORS['red']}⓶{COLORS['reset']} My therapist says I have commitment issues. I think she's just afraid of intimacy.",
        f"{COLORS['red']}⓷{COLORS['reset']} I tried meditation, but I kept worrying about whether I was doing it wrong."
    ]
    
    print(f"{COLORS['magenta']}{COLORS['bold']}Neurotic Footnotes:{COLORS['reset']}")
    for note in footnotes:
        time.sleep(0.7)
        print(f"  {note}")
    
    # ASCII therapy couch
    print()
    print(f"{COLORS['green']}")
    print("Therapy Couch (for when the quote hits too close to home):")
    print("  ________________________________________________")
    print(" /| _____  || || || || || || || || || || || || || ||")
    print("(_)|_____|_||_||_||_||_||_||_||_||_||_||_||_||_||_||")
    print(f"{COLORS['reset']}")
    
    # Blinking cursor of existential doubt
    print(f"\n{COLORS['cyan']}💭 Processing existential dread", end='')
    for _ in range(6):
        print(".", end='', flush=True)
        time.sleep(0.3)
        print("\b ", end='', flush=True)
        time.sleep(0.3)
        print("\b.", end='', flush=True)
    print(f"{COLORS['reset']}")

if __name__ == "__main__":
    try:
        print_woody_quote()
        print(f"\n{COLORS['yellow']}Remember: 80% of success is showing up... and 80% of life is realizing you're in the wrong movie.{COLORS['reset']}")
    except KeyboardInterrupt:
        print(f"\n{COLORS['red']}...And that's when I decided to end things on a cliffhanger. Classic me.{COLORS['reset']}")