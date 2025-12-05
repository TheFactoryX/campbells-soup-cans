"""
Campbell's Soup Can #722
Produced: 2025-12-05 03:59:04
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI escape codes for colors and styles
COLORS = {
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "purple": "\033[95m", 
    "red": "\033[91m",
    "reset": "\033[0m",
    "bold": "\033[1m"
}

COSMIC_ART = rf"""
{COLORS['purple']}       *       .       *          .    *         .         *    .    
   .            *        .         .       __/___            *          
         *               (   (           ,-' /|  \ `-.               *  
           .             \ \_| :       _/  _/ |  \  \              .    
       *        .         \/ _/ _\    (`  /__/    \__\                    *
    .       _\/_   *    .-./ /-' /     \    _     _/      *    .   _\/_     
       *   / __  \       |/ '   /       `-._ _ _.-'  .        / __  \   
    .    _/ /  \ \_           *             o O o          * _/ /  \ \_    *
       * \/    \/     .                  .       .       .   \/    \/ {COLORS['reset']}"""

def print_with_effect(text, color="reset", delay=0.05):
    for char in text:
        sys.stdout.write(COLORS[color] + char + COLORS["reset"])
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.02, 0.02))
    print()

def main():
    quote = "I'm convinced there's a cosmic irony department that schedules \npersonal growth right when you've finally mastered self-sabotage."
    author = "- Woody Allen (probably)"

    print(COSMIC_ART)
    print_with_effect("\n「 COSMIC IRONY DEPARTMENT 」", "yellow", 0.08)
    print()
    print_with_effect(quote, "cyan", 0.04)
    print()
    
    # Fading author effect
    for i in range(5):
        fade = max(5 - i, 1)
        print(f"\033[38;5;24{min(8, fade)}m{author}\033[0m", end="\r")
        time.sleep(0.3)
    print()

if __name__ == "__main__":
    main()