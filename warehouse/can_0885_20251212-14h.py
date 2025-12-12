"""
Campbell's Soup Can #885
Produced: 2025-12-12 14:32:42
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
COLORS = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m',  # White
]

RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'

def print_typewriter(text, delay=0.05):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_thinking_face():
    """ASCII art of a neurotic thinker"""
    face = """
    """ + BOLD + """
       (•‿•)
      ( • • )
     /| . . |\\
      (  _  )
       \\___/
    """ + RESET
    return face

def animate_worry_bubbles():
    """Create animated worry bubbles"""
    bubbles = ["?", "!", "...", "OMG", "HELP", "WHY"]
    sys.stdout.write("\n    ")
    for i in range(8):
        bubble = random.choice(bubbles)
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{bubble}{RESET}  ")
        sys.stdout.flush()
        time.sleep(0.2)
    print()

def main():
    # Clear screen and set up
    print('\033[2J\033[H', end='')  # Clear screen
    
    # Title with dramatic effect
    print("\n" + "="*60)
    print_typewriter("   WOODY ALLEN'S GUIDE TO MODERN EXISTENTIAL PANIC", 0.03)
    print("="*60 + "\n")
    
    # Draw the thinker
    print(draw_thinking_face())
    
    # Animated worry bubbles
    animate_worry_bubbles()
    
    # The quote with dramatic pauses
    print("\n" + BOLD + "A profound observation:" + RESET)
    print("─" * 50)
    
    quote = (
        "I don't mind dying; I just don't want to be there when it happens. "
        "And frankly, given my track record with dinner parties, "
        "I'm worried the afterlife will be awkward."
    )
    
    # Print with emphasis on key words
    emphasized_words = {
        "dying": COLORS[0],
        "don't": COLORS[1], 
        "there": COLORS[2],
        "track record": COLORS[3],
        "dinner parties": COLORS[4],
        "afterlife": COLORS[5],
        "awkward": COLORS[6]
    }
    
    words = quote.split()
    for i, word in enumerate(words):
        # Clean word for comparison
        clean_word = word.strip('.,;:!?')
        
        if clean_word in emphasized_words:
            color = emphasized_words[clean_word]
            print(f"{color}{BOLD}{word}{RESET}", end=' ')
        else:
            print(word, end=' ')
        
        sys.stdout.flush()
        time.sleep(0.1)
    
    print("\n")
    print("─" * 50)
    
    # Signature with neurotic flourish
    signature = "— Woody Allen (probably on therapy)" 
    print_typewriter(f"\n{ITALIC}{signature}{RESET}", 0.08)
    
    # Final existential mic drop
    print("\n" + random.choice(COLORS) + BOLD + 
          "Remember: 90% of life is just showing up... " +
          RESET + "and I'm chronically late." + RESET)

if __name__ == "__main__":
    main()