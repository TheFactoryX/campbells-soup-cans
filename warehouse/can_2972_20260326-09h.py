"""
Campbell's Soup Can #2972
Produced: 2026-03-26 09:13:41
Worker: Qwen: Qwen3 VL 235B A22B Instruct (qwen/qwen3-vl-235b-a22b-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    print("\033[2J\033[H", end='')

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# ANSI color codes
RED = "31"
GREEN = "32"
YELLOW = "33"
BLUE = "34"
MAGENTA = "35"
CYAN = "36"
WHITE = "37"
BOLD = "1"
RESET = "0"

# Woody Allen style quote (original creation)
woody_quote = (
    "I've been to therapy for 30 years. "
    "My therapist says I'm making progress. "
    "I told him, 'If I'm making progress, why am I still here?' "
    "He said, 'Because you're paying for it.' "
    "I said, 'That's not progress, that's a Ponzi scheme.'"
)

# ASCII art of Woody Allen's iconic glasses and neurotic expression
woody_art = [
    "     .-\"\"\"-.     ",
    "    /       \\    ",
    "   |  o   o  |   ",
    "   |    ∆    |   ",
    "    \\  ---  /    ",
    "     '-...-'     ",
    "      /   \\      ",
    "     /     \\     ",
    "    /       \\    ",
    "   /         \\   ",
    "  /           \\  ",
    " /             \\ ",
    "|  I'm not late, |
    "|  I'm fashionably|
    "|  existentially |
    "|  delayed...    |",
    " \\             / ",
    "  \\           /  ",
    "   \\         /   ",
    "    \\       /    ",
    "     \\     /     ",
    "      \\   /      ",
    "       \\ /       ",
    "        V        "
]

def animate_quote():
    clear_screen()
    print(color_text("   WOODY ALLEN'S EXISTENTIAL WISDOM   ", "33;1"))
    print(color_text("=" * 40, "33"))
    print()
    
    # Print Woody art with animation
    for i, line in enumerate(woody_art):
        if i == 5:  # Make the glasses blink
            print(color_text(line, "36"))
        elif i == 10:  # Make the text in the speech bubble appear
            print(color_text(line, "35"))
        else:
            print(color_text(line, "34"))
        time.sleep(0.05)
    
    print()
    print(color_text("  " + "=" * 36 + "  ", "33"))
    print()
    
    # Type out the quote with dramatic pauses
    words = woody_quote.split()
    for i, word in enumerate(words):
        if i % 5 == 0 and i > 0:
            print()
            time.sleep(0.3)
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])
        print(color_text(word, color), end=' ')
        sys.stdout.flush()
        time.sleep(0.15)
    print()
    print()
    
    # Add a dramatic flourish
    print(color_text("   ...and then I went to get a bagel.   ", "32;1"))
    print(color_text("   Because existential dread pairs well with sesame seeds.   ", "32"))
    print()
    print(color_text("   - Woody Allen (probably, if he had time between appointments)   ", "35;1"))
    print()

def main():
    # Clear screen and show intro
    clear_screen()
    print(color_text("  ***  WOODY ALLEN'S PHILOSOPHICAL ADVICE  ***  ", "35;1"))
    print(color_text("  (Warning: May cause neurosis, laughter, or sudden cravings for pastrami)  ", "33"))
    print()
    
    # Wait a moment
    time.sleep(1.5)
    
    # Animate the quote
    animate_quote()
    
    # Add a final flourish
    print(color_text("  Press Ctrl+C to escape reality... or just go to therapy.  ", "31;1"))
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(color_text("  You've escaped... for now. But the universe is still waiting.  ", "31;1"))
        print(color_text("  (And your therapist has your next appointment scheduled.)  ", "33"))
        print()