"""
Campbell's Soup Can #977
Produced: 2025-12-16 18:48:48
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
Woody Allen's Neurotic Philosophy Generator
A single-file, dependency-free, neurotic masterpiece
"""

import sys
import time
import random
from typing import List

# ANSI color codes for maximum neurotic color therapy
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
    'bg_blue': '\033[44m'
}

def print_with_trembling(text: str, delay: float = 0.05):
    """Type with the nervous energy of someone who's heard one too many bad jokes about mortality"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def draw_worried_face():
    """ASCII art that captures existential dread"""
    face = [
        "    ┌─────────────────┐    ",
        "    │  (╯°□°)╯       │    ",
        "    │  What if this  │    ",
        "    │  program is   │    ",
        "    │  just a      │    ",
        "    │  temporary   │    ",
        "    │  distraction?│    ",
        "    └─────────────────┘    "
    ]
    for line in face:
        print_with_trembling(line, 0.02)

def create_anxious_border(text_lines: List[str]) -> List[str]:
    """Wrap text in a border that's having an anxiety attack"""
    max_width = max(len(line) for line in text_lines) + 4
    
    # Top border with nervous energy
    top = "╔" + "╤" * (max_width - 2) + "╗"
    bottom = "╚" + "╧" * (max_width - 2) + "╝"
    
    bordered = [top]
    for line in text_lines:
        padded = f"║ {line:<{max_width-4}} ║"
        bordered.append(padded)
    bordered.append(bottom)
    
    return bordered

def main():
    # Clear screen with existential clarity
    print('\033[2J\033[H', end='')
    
    print_with_trembling(f"{COLORS['cyan']}{COLORS['bold']}╔════════════════════════════════════════════════════╗{COLORS['reset']}")
    print_with_trembling(f"{COLORS['cyan']}║ {COLORS['bold']}{COLORS['magenta']}Woody Allen's Neurotic Philosophy Generator{COLORS['reset']} ║")
    print_with_trembling(f"{COLORS['cyan']}║ {COLORS['yellow']}Version 1.0 (probably obsolete by tomorrow){COLORS['reset']}      ║")
    print_with_trembling(f"{COLORS['cyan']}╚════════════════════════════════════════════════════╝{COLORS['reset']}")
    
    # Draw the worried face
    draw_worried_face()
    print()
    
    # The quote that will make you question everything
    quote = [
        "I'm not afraid of death; I'm afraid of",
        "the awkward silence that comes before it.",
        "",
        "You see, I went to a therapy session for",
        "people afraid of commitment. We were making",
        "real progress until the therapist moved to",
        "Vermont without saying goodbye. Now I'm",
        "afraid of both commitment AND abandonment.",
        "",
        "Existence is a temporary psychotic",
        "aberration. The sooner you accept that,",
        "the longer you'll need therapy."
    ]
    
    # Display with maximum neurotic formatting
    bordered_quote = create_anxious_border(quote)
    
    for i, line in enumerate(bordered_quote):
        # Make the text blink nervously
        if i % 2 == 0:
            color = COLORS['red']
        else:
            color = COLORS['yellow']
        
        print_with_trembling(f"{color}{line}{COLORS['reset']}", 0.01)
    
    print()
    
    # Signature with Woody's signature anxiety
    signature = [
        f"{COLORS['blue']}— Woody Allen (probably){COLORS['reset']}",
        f"{COLORS['green']}(or at least someone who's seen Midnight in Paris too many times){COLORS['reset']}"
    ]
    
    for line in signature:
        print_with_trembling(line, 0.08)
    
    print()
    
    # Post-philosophical existential crisis
    crisis = [
        "If a philosophy is spoken in the forest",
        "and no one's around to hear it, does it",
        "still make you feel vaguely unsettled?",
        "",
        "Probably. Nothing ever really goes away.",
        "Especially your mother's disapproval."
    ]
    
    for line in crisis:
        print_with_trembling(f"{COLORS['cyan']}{line}{COLORS['reset']}", 0.06)
    
    print()
    print_with_trembling(f"{COLORS['blink']}{COLORS['magenta']}This program will self-destruct in 30 seconds due to performance anxiety.{COLORS['reset']}")
    print_with_trembling(f"{COLORS['yellow']}...Actually, make it 35. I need extra time to worry about deadlines.{COLORS['reset']}")

if __name__ == "__main__":
    main()