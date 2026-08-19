"""
Campbell's Soup Can #4705
Produced: 2026-08-19 20:45:15
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Woody Allen style quote
quote = "I'm not afraid of commitment. I'm afraid of the morning after commitment. And the night before that. And the afternoon naps in between."

# Colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def print_animated_quote():
    # Print the quote character by character with color cycling
    colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
    
    # Print the box border first
    print(Colors.BOLD + Colors.WHITE + "┌" + "─" * (len(quote) + 2) + "┐")
    
    # Print the quote line by line
    sys.stdout.write(Colors.BOLD + Colors.WHITE + "│ " + Colors.RESET)
    for i, char in enumerate(quote):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        time.sleep(0.03)  # Typing animation
        sys.stdout.flush()
    
    print(Colors.WHITE + "  " + Colors.BOLD + Colors.WHITE + "│")
    
    # Print the bottom border
    print(Colors.BOLD + Colors.WHITE + "└" + "─" * (len(quote) + 2) + "┘")
    
    # Print attribution with fade effect
    print()
    attribution = "— Woody Allen (probably)"
    for i in range(len(attribution), 0, -1):
        print(Colors.MAGENTA + "  " + " " * i + attribution[i:] + Colors.RESET)
        time.sleep(0.1)
    
    # Print the depression warning
    print()
    print(Colors.RED + "⚠️  Warning: May cause existential dread and excessive couch time  ⚠️" + Colors.RESET)

def main():
    # Header with ASCII art
    print(Colors.CYAN + """
  ____  ____ ____    _____ ____    ____  ____   ___  ____  
 / ___|/ ___|  _ \  / ____|  _ \  / ___||  _ \ / _ \|  _ \ 
 \___ \___ | | | || | (___ | | | || |  __ | |_) | | | | |_) |
  ___) |___ || |_| |  \___ \| |_| || |___ ||  _ <||_| |  _ < 
 |____/_____|____/    |____/|____/  \____||_| \_\\___/|_| \_\
                                                            
""" + Colors.RESET)
    print()
    print_animated_quote()

if __name__ == "__main__":
    main()