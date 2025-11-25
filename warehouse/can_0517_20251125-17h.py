"""
Campbell's Soup Can #517
Produced: 2025-11-25 17:34:41
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

def print_typewriter(text, delay=0.05):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_ellipse():
    """Draw a simple ASCII ellipse"""
    ellipse = [
        "                    , - ~ ~ ~ - ,",
        "                , '                 ' ,",
        "            , '                       ' ,",
        "          , '                           ' ,",
        "         ,                                   ,",
        "        ,                                     ,",
        "        ,                                     ,",
        "        ,                                     ,",
        "         ,                                   ,",
        "          , '                           ' ,",
        "            , '                       ' ,",
        "                , '                 ' ,",
        "                    , - ~ ~ ~ - ,"
    ]
    return ellipse

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Draw the ellipse frame
    ellipse_lines = draw_ellipse()
    
    # Quote in Woody Allen's style
    quote = "I'm not afraid of death; I'm just afraid it will disrupt my therapy schedule."
    attribution = "-- Woody Allen (probably during a panic attack)"
    
    # Calculate centering
    max_width = max(len(line) for line in ellipse_lines)
    quote_width = max(len(quote), len(attribution))
    padding = max(0, (max_width - quote_width) // 2)
    
    # Print the ellipse with quote inside
    for i, line in enumerate(ellipse_lines):
        if i == len(ellipse_lines) // 2 - 1:
            # Print quote line
            colored_quote = COLORS['cyan'] + COLORS['bold'] + quote + COLORS['reset']
            spaces = ' ' * (padding - 2)
            print(line[:2] + spaces + colored_quote + ' ' * (len(line) - len(line[:2]) - len(spaces) - len(colored_quote)) + line[-2:])
        elif i == len(ellipse_lines) // 2:
            # Print attribution line
            colored_attribution = COLORS['magenta'] + attribution + COLORS['reset']
            spaces = ' ' * (padding - 2)
            print(line[:2] + spaces + colored_attribution + ' ' * (len(line) - len(line[:2]) - len(spaces) - len(colored_attribution)) + line[-2:])
        elif i == len(ellipse_lines) // 2 + 1:
            # Print some neurotic asterisks
            asterisk_line = COLORS['yellow'] + "      *sigh* " + COLORS['red'] + "Why do I even bother?" + COLORS['reset']
            spaces = ' ' * (padding - 2)
            print(line[:2] + spaces + asterisk_line + ' ' * (len(line) - len(line[:2]) - len(spaces) - len(asterisk_line)) + line[-2:])
        else:
            # Animate the ellipse with random colors
            colored_line = ""
            for char in line:
                if char in ",'-~":
                    color = random.choice([COLORS['red'], COLORS['blue'], COLORS['green'], COLORS['yellow']])
                    colored_line += color + char + COLORS['reset']
                else:
                    colored_line += char
            print(colored_line)
        
        time.sleep(0.1)
    
    print()
    
    # Add some neurotic afterthoughts with typewriter effect
    afterthoughts = [
        "Also, what if the afterlife has bad lighting?",
        "And don't even get me started on reincarnation...",
        "What if I come back as a soy candle? Talk about existential dread!"
    ]
    
    for thought in afterthoughts:
        time.sleep(0.8)
        color = random.choice([COLORS['red'], COLORS['magenta'], COLORS['cyan']])
        print_typewriter(f"  {color}•{COLORS['reset']} {thought}", 0.03)
    
    # Final dramatic exit
    time.sleep(1)
    print()
    print_typewriter("  " + COLORS['blue'] + "Life: It's not the end that scares me..." + COLORS['reset'], 0.08)
    time.sleep(0.5)
    print_typewriter("  " + COLORS['red'] + "           it's the insurance premiums." + COLORS['reset'], 0.08)

if __name__ == "__main__":
    main()