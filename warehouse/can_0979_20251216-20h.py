"""
Campbell's Soup Can #979
Produced: 2025-12-16 20:37:29
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Clear and reset screen function
CLEAR = '\033[H\033[2J'
RESET = '\033[0m'

# Colorful ASCII border
BORDER = [
    "\033[33m",  # Yellow
    "\033[36m",  # Cyan
    "\033[35m",  # Magenta
    "\033[31m",  # Bright red
]

# Woody's existential crisis
quote = "I'm afraid of death, but I'm really more afraid of how bad my haircut will look in the afterlife."

def typewriter(text, color_cycle=True, speed=0.03):
    if color_cycle:
        colors = COLORS * len(text)
    else:
        colors = []
    
    for i, char in enumerate(text):
        color = colors[i] if colors else RESET
        print(color + char + RESET, end='', flush=True)
        time.sleep(speed)
    print()

# Main execution
print(CLEAR)
print("\033[31m +-------------------------+ \033[0m")
print("\033[31m | Note to Self:             | \033[0m")
print("\033[31m |    - Always doubt your   | \033[0m")
print("\033[31m |    decisions, they'll    | \033[0m")
print("\033[31m |    make better ones.     | \033[0m")
print("\033[31m +-------------------------+ \033[0m")

time.sleep(2)

# Print quote with animated color cycling
typewriter(quote, color_cycle=True, speed=0.05)

# Final existential shrug with ASCII art
print("\033[36m       --------\033[0m")
print("\033[35m      /          \\\033[0m")
print("\033[34m     /            \\\033[0m")
print("\033[33m     \\             \\ \033[0m")