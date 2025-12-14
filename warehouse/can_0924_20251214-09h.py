"""
Campbell's Soup Can #924
Produced: 2025-12-14 09:31:46
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
A neurotic, philosophical quote in Woody Allen's style with visual flair.
"""

import sys
import time
import random

# Colors using ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"

# A custom Woody Allen-style philosophical quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens... and by 'there,' I mean 'alive,' which is technically where I am now, which is precisely the problem."

def print_with_typewriter_effect(text, delay=0.03, color=RESET):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_thinking_face():
    """Draw a simple ASCII art thinking face"""
    face = [
        "     ╭─────────────────╮",
        "     │  (╯°□°）╯      │",
        "     │   Why? WHY?   │",
        "     ╰─────────────────╯"
    ]
    return face

def draw_anxious_spiral():
    """Draw a spiral representing anxious thoughts"""
    spiral = [
        "  ──┐                ",
        "    │  ┌─────┐       ",
        "    │  │ ┌─┐ │       ",
        "    │  │ │ │ │       ",
        "    └──┘ └─┘ └─────  "
    ]
    return spiral

def main():
    # Clear screen and set background
    print("\033[2J\033[H", end="")
    
    # Title
    print_with_typewriter_effect("="*70, 0.01, YELLOW)
    print_with_typewriter_effect("         🫀  WOODY ALLEN'S EXISTENTIAL CRISIS OF THE DAY  🫀", 0.02, MAGENTA)
    print_with_typewriter_effect("="*70, 0.01, YELLOW)
    print()
    
    # Draw the anxious spiral
    spiral = draw_anxious_spiral()
    for line in spiral:
        print_with_typewriter_effect("    " + line, 0.01, BLUE)
    print()
    
    # The main quote with dramatic pauses
    print_with_typewriter_effect("   " + "─" * 40, 0.02, CYAN)
    print()
    print_with_typewriter_effect("   " + BOLD + "MY PHILOSOPHY:", 0.05, RED)
    print()
    
    # Print quote with random pauses for neurotic effect
    words = QUOTE.split()
    for i, word in enumerate(words):
        print_with_typewriter_effect("   " + word + " ", 0.02, GREEN)
        if i % 4 == 0 and i > 0:
            time.sleep(random.uniform(0.1, 0.3))
    
    print()
    print_with_typewriter_effect("   " + "─" * 40, 0.02, CYAN)
    print()
    
    # The thinking face
    face = draw_thinking_face()
    for line in face:
        print_with_typewriter_effect("    " + line, 0.01, YELLOW)
    print()
    
    # Footer with more Woody-ness
    print_with_typewriter_effect("   " + BOLD + "In conclusion:", 0.04, RED)
    time.sleep(0.3)
    print_with_typewriter_effect("   " + "If life is meaningless, at least I have excellent therapy bills to show for it.", 0.025, CYAN)
    print()
    
    # Blink effect for the final thought
    for _ in range(3):
        print_with_typewriter_effect("   " + BOLD + "   ...and that's why I can't sleep.", 0.04, RED)
        time.sleep(0.3)
        print("\033[A\033[K", end="")  # Move up and clear line
        time.sleep(0.2)
    
    print_with_typewriter_effect("   " + BOLD + "   ...and that's why I can't sleep.", 0.04, RED)
    print()
    print_with_typewriter_effect("   " + "─" * 40, 0.02, YELLOW)
    print_with_typewriter_effect("   " + "© 2024 Existential Dread, Inc. All rights anxiously reserved.", 0.02, BLUE)
    print()

if __name__ == "__main__":
    main()