"""
Campbell's Soup Can #706
Produced: 2025-12-04 09:38:45
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

# Woody Allen's Philosophical Quote Dispenser 1.0
# Because existence is painful, but at least it's funny?

import time

# ANSI Escape Codes for colors and styles
COLORS = {
    'reset': '\033[0m',
    'cyan': '\033[36m',
    'magenta': '\033[35m',
    'yellow': '\033[33m',
    'bold': '\033[1m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'bg_white': '\033[47m',
    'bg_cyan': '\033[46m'
}

def centered_text(text, width=60):
    return text.center(width)

def draw_thought_bubble():
    bubble = [
        "  .-.",
        " /   \\",
        "|  .  |",
        " \___/",
        "  /   \\",
        " /     \\",
        "|       |",
        " \'_____\’"
    ]
    for line in bubble:
        print(COLORS['magenta'] + line + COLORS['reset'])

def main():
    quote = "Analyzing my neuroses is like trying to catch smoke with a butterfly net—pointless and slightly absurd."
    signature = "- Woody Allen (probably)"
    
    width = 60
    border_char = '─'
    top_border = f"┌{border_char * width}┐"
    mid_border = f"│{border_char * width}│"
    bottom_border = f"└{border_char * width}┘"
    
    # Animate the appearance
    print(COLORS['yellow'] + "\n" + centered_text("A PHILOSOPHICAL MOMENT WITH WOODY ALLEN" + COLORS['reset'])
    time.sleep(0.8)
    
    print(COLORS['cyan'] + "\n" + centered_text(top_border) + COLORS['reset'])
    time.sleep(0.5)
    
    print(COLORS['bold'] + COLORS['bg_cyan'] + centered_text(quote) + COLORS['reset'])
    time.sleep(1.5)
    
    print(COLORS['cyan'] + centered_text(mid_border) + COLORS['reset'])
    time.sleep(0.5)
    print(COLORS['cyan'] + centered_text(bottom_border) + COLORS['reset'])
    
    draw_thought_bubble()
    
    print(COLORS['italic'] + "\n" + centered_text(signature) + COLORS['reset'])

if __name__ == "__main__":
    main()