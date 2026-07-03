"""
Campbell's Soup Can #4076
Produced: 2026-07-03 04:08:55
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes for terminal text styling
COLORS = {
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'yellow': '\033[93m',
    'reset': '\033[0m'
}

# Philosophical quote lines in Woody Allen's neurotic style
quote_lines = [
    "I don't fear death itself—",
    "It's the paperwork after that",
    "Terrifies me. Forms in triplicate,",
    "And I've never been good",
    "With bureaucracy. Either way,",
    "I hope my afterlife has better",
    "Lighting. And maybe a decent",
    "Cafeteria. Also, no more",
    "Therapy sessions."
]

# Determine box width based on longest line
max_line_length = max(len(line) for line in quote_lines)
box_width = max_line_length + 4  # Adding padding

# Print decorative title
print(f"{COLORS['magenta']}╔{'═' * box_width}╗")
print(f"║ {'Woody Allen Wisdom':^{box_width-2}} ║")
print(f"╚{'═' * box_width}╝{COLORS['reset']}")

time.sleep(0.5)  # Dramatic pause before the quote

# Print animated quote box
print(f"{COLORS['cyan']}╔{'─' * (box_width-2)}╗{COLORS['reset']}")

for line in quote_lines:
    # Add delay before each line for dramatic effect
    time.sleep(0.3)
    
    # Center the line within the box
    centered_line = line.center(max_line_length + 2)
    
    # Print left border
    print(f"{COLORS['cyan']}│{COLORS['reset']}", end='')
    
    # Animate text character-by-character
    for char in centered_line:
        print(f"{COLORS['yellow']}{char}{COLORS['reset']}", 
              end='', flush=True)
        time.sleep(0.02)
    
    # Print right border
    print(f"{COLORS['cyan']}│{COLORS['reset']}")

# Print bottom border
print(f"{COLORS['cyan']}╚{'─' * (box_width-2)}╝{COLORS['reset']}")