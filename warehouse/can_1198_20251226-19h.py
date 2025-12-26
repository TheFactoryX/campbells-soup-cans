"""
Campbell's Soup Can #1198
Produced: 2025-12-26 19:27:59
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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
import os

def typewriter_effect(text, delay=0.03):
    """Simulate a typewriter effect with text printing character by character"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text, color_code):
    """Return text with ANSI color code"""
    return f"\033[{color_code}m{text}\033[0m"

# ASCII art frames
top_border = "╔═════════════════════════════════════════════════════════════════════════════╗"
bottom_border = "╚═════════════════════════════════════════════════════════════════════════════╝"
side_border = "║"

# Woody Allen style quote
quote = "I tried to be a philosopher once, but I kept getting distracted by my own neurosis. \n" \
        "It's like trying to meditate in a room with a leaky faucet and a metronome."

# Author
author = "— Woody Allen's existential crisis"

# Color codes
colors = {
    'frame': '36',  # Cyan
    'quote': '33',  # Yellow
    'author': '31',  # Red
    'cursor': '32',  # Green
    'title': '35'   # Magenta
}

# Title with animation
title = "Philosophical Musings from the Mind of a Neurotic Genius"
title_lines = []
for i in range(len(title)):
    title_lines.append(title[:i+1])
    typewriter_effect(colored_text(title_lines[-1].center(79), colors['title']), 0.05)
    time.sleep(0.1)

# Print the framed quote
print(colored_text(top_border, colors['frame']))
print(colored_text(side_border, colors['frame']) + " " * 77 + colored_text(side_border, colors['frame']))

# Quote with typewriter effect
quote_lines = quote.split('\n')
for line in quote_lines:
    print(colored_text(side_border, colors['frame']) + " " + colored_text(line.center(75), colors['quote']) + " " + colored_text(side_border, colors['frame']))
    time.sleep(0.5)

# Author line
print(colored_text(side_border, colors['frame']) + " " * 31 + colored_text(author.center(45), colors['author']) + " " + colored_text(side_border, colors['frame']))

print(colored_text(bottom_border, colors['frame']))

# Add some self-referential humor
print("\n")
typewriter_effect(colored_text("P.S. I'd have made this more profound, but I got distracted by", colors['cursor']), 0.04)
typewriter_effect(colored_text("the blinking cursor and existential dread of unfinished code.", colors['cursor']), 0.04)

# Wait for user input before exiting
input(colored_text("\nPress Enter to exit and ponder the meaning of it all...", colors['frame']))
clear_screen()