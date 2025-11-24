"""
Campbell's Soup Can #489
Produced: 2025-11-24 11:28:58
Worker: xAI: Grok 4.1 Fast (free) (x-ai/grok-4.1-fast:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes for rainbow effect
COLORS = [
    '\033[91m',  # Bright Red
    '\033[92m',  # Bright Green
    '\033[93m',  # Bright Yellow
    '\033[94m',  # Bright Blue
    '\033[95m',  # Bright Magenta
    '\033[96m',  # Bright Cyan
    '\033[97m'   # Bright White
]
BOLD = '\033[1m'
RESET = '\033[0m'

def rainbow_type(text, delay=0.06):
    """Print text with rainbow colors and typing animation."""
    sys.stdout.write(BOLD)
    for i, char in enumerate(text):
        color = COLORS[i % len(COLORS)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

# ASCII art: a neurotic Woody-esque character
ASCII_ART = r"""
     .-"""-.
    /       \
   |  O   O  |   <--- Me contemplating existence
    \   -   /
     |_____|
      || ||
     /  |  \
    |___|___|
"""

# Clear screen for drama (works in most terminals)
sys.stdout.write('\033[2J\033[H')
sys.stdout.flush()
time.sleep(0.5)

# Print intro art in blue
print(BOLD + '\033[94m' + ASCII_ART + RESET)
time.sleep(0.8)

# Title
print('\n\033[93m' + BOLD + 'A Woody Allen-Style Philosophical Gem:' + RESET + '\n')
time.sleep(0.5)

# The quote: neurotic, funny, self-deprecating, existential
QUOTE = "I'm not afraid of death itself—what terrifies me is arriving at the afterlife and finding out it's just an endless group therapy session with no coffee break."

# Rainbow typing animation
rainbow_type(QUOTE, 0.05)

# Fun ending: bouncing "HA!" animation
print('\n')
for _ in range(3):
    for emot in ['😂', '🤡', '😵']:
        sys.stdout.write('\r' + '\033[92m' + BOLD + emot * 5 + ' ' * 10 + RESET)
        sys.stdout.flush()
        time.sleep(0.2)
print('\n' + RESET)

# Final flourish
print('\033[95m' + '─' * 70 + '\033[0m')