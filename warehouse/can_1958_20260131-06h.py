"""
Campbell's Soup Can #1958
Produced: 2026-01-31 06:58:08
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI escape codes for colors and formatting
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# Woody Allen style quote
quote = [
    "I don't want to achieve immortality through my work;",
    "I want to achieve it through not dying.",
    "- Woody Allen"
]

# ASCII art frame
frame_top = f"{GREEN}┌{'─' * 50}┐{RESET}"
frame_bottom = f"{GREEN}└{'─' * 50}┘{RESET}"

def print_quote():
    # Print frame top
    print(frame_top)
    
    # Print quote with animation
    for line in quote:
        # Add some delay for dramatic effect
        time.sleep(0.5)
        
        # Alternate colors for each line
        if line == quote[0]:
            color = RED
        elif line == quote[1]:
            color = YELLOW
        else:
            color = BLUE
        
        # Print line with color and indentation
        print(f"{color}│    {line:<44}│{RESET}")
    
    # Print frame bottom
    print(frame_bottom)

# Print the quote
print_quote()