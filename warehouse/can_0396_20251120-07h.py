"""
Campbell's Soup Can #396
Produced: 2025-11-20 07:30:42
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

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_allen_quote():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Colors
    frame_color = "\033[1;36m"  # Cyan
    quote_color = "\033[0;33m"  # Yellow
    woody_color = "\033[1;35m"  # Magenta
    anxiety_color = "\033[1;31m" # Red
    neurosis_color = "\033[0;32m" # Green
    reset_color = "\033[0m"
    
    # Top border with neurosis symbols
    print(f"{frame_color}{'+' + '~' * 70 + '+'}{reset_color}")
    print(f"{frame_color}|{reset_color} {anxiety_color}{'⚠ NEUROSIS LEVEL: MAXIMUM ⚠'}{reset_color}")
    print(f"{frame_color}{'+' + '=' * 70 + '+'}{reset_color}")
    
    # Woody Allen ASCII art
    print(f"{frame_color}|{reset_color}", end=" ")
    woody_art = r"""
   .-.
  /   \
 | o o |
  \ ~ /
   ^^
    \_______/
    |     |
    |     |
   /|_____|\
  /         \
 /           \
"""
    print(f"{woody_color}{woody_art}{reset_color}")
    
    # Quote introduction
    print(f"{frame_color}|{reset_color}", end=" ")
    print(f"{frame_color}{' '}{'WOODY ALLEN ON THE ABSURDITY OF BEING NEUROTIC':^70}{reset_color}")
    
    # Quote border with anxiety symbols
    print(f"{frame_color}|{reset_color}", end=" ")
    print(f"{frame_color}{'=' * 70}{reset_color}")
    
    # The quote itself - more neurotic and self-deprecating
    quote = "I'm not afraid of death; I'm just terrified of what happens after I die, but only if there's an afterlife where I have to account for all the times I've second-guessed myself while worrying about my mortality - which is probably why I'm destined for hell, where I'll spend eternity worrying about whether I should have worried more in the first place."
    
    # Print with typewriter effect
    print(f"{frame_color}|{reset_color}  ", end="")
    typewriter(quote, 0.02)
    
    # Quote border
    print(f"{frame_color}|{reset_color}", end=" ")
    print(f"{frame_color}{'=' * 70}{reset_color}")
    
    # Footer with neurotic symbols
    footer = " - Woody Allen, probably while procrastinating on his next screenplay about worrying about whether his writings are neurotic enough"
    print(f"{frame_color}|{reset_color}", end=" ")
    print(f"{quote_color}{footer}{reset_color}")
    
    # Neurosis indicators
    print(f"{frame_color}|{reset_color} {neurosis_color}{'↗' * 70}{reset_color}")
    print(f"{frame_color}{'+' + '~' * 70 + '+'}{reset_color}")
    
    # Reset color
    print(reset_color)

if __name__ == "__main__":
    woody_allen_quote()