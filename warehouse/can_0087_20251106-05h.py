"""
Campbell's Soup Can #87
Produced: 2025-11-06 05:33:59
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Create ASCII art with color
def print_ascii():
    art = [
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱",
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱",
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱",
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱",
        "╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲",
        "╱╱╲╱╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲",
        "╱╱╱╲╱╱╲╱╲╱╲╱╱╲╱╱╱╲╱╱╲╱╱╲╱╲",
        "╱╱╱╱╲╱╱╲╱╱╱╱╱╲╱╱╱╲╱╱╱╲╱╱╲╲"
    ]
    for line in art:
        print(f"\033[1;34m{line}\033[0m")
        time.sleep(0.05)
    print("\033[1;36m      _____                    \033[0m")
    print("\033[1;36m     |_   _|_   _  ___  ___   \033[0m")
    print("\033[1;36m       | |/ _ \ |/ _ \/ __|  \033[0m")
    print("\033[1;36m       | | (_) | |  __/\__ \  \033[0m")
    print("\033[1;36m       |_|\___/|_|\___||___/  \033[0m")
    time.sleep(0.5)
    print("\033[1;35m     Wooodly Allen Philosophy \033[0m")
    print('\033[1;31m      \/\/\/\/\/\/\/\/\/\/\/  \033[0m')
    print('\033[1;31m      |  \033[1;33m Quote \033[1;31m|                \033[0m')
    print('\033[1;33m      ---------                   \033[0m')
    print('\033[1;32m      |\033[1;35m What if? \033[1;32m| = ...         \033[0m')
    time.sleep(0.5)

# Typing effect with color
def print_typing(text, color='\033[0m'):
    for char in text:
        if char == '\n':
            sys.stdout.write('\n' + color)
            continue
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\033[0m\n')

# Main execution
if __name__ == "__main__":
    print_banner = [
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱",
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱",
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱",
        "╱╱╱╱╱╱╱╱╱╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲",
        "╱╱╱╱╱╱╱╱╱╱╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲",
        "╱╱╱╱╱╱╱╱╱╱╱╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲",
        "╱╱╱╱╱╱╱╱╱╱╱╱╲╲╲╲╲╲╲╲╲╲╲╲╲╲",
        "╱╱╱╱╱╱╱╱╱╱╱╱╱╲╲╲╲╲╲╲╲╲╲╲╲╲"
    ]
    
    for line in print_banner:
        sys.stdout.write(line + '\033[1;35m⫶\033[0m ')
        sys.stdout.flush()
        time.sleep(0.05)
    print()

    print_ascii()
    
    # Typing effect for "THE" and "ANSWER" in quote
    print('\033[1;36mI\033[0m')
    time.sleep(1)
    print('\033[1;36mI'm\033[0m', end='\r')
    time.sleep(1)
    print('\033[1;36mI'm\033[0m', end='\r')
    time.sleep(0.5)
    print('\033[1;36mI'm a\033[0m', end='\r')
    time.sleep(0.5)
    print('\033[1;36mI'm a \033[0m', end='\r')
    time.sleep(0.5)
    print('\033[1;36mI'm a neurotic philosopher\033[0m', end='\r')
    time.sleep(1)
    print('\033[1;33mwho lives with ghosts\033[0m')
    time.sleep(1)
    print('\033[1;31m----------------------------------\033[0m')
    
    # Type the full quote with final color
    print('\033[1;32mI\033[0m')
    time.sleep(1)
    print('\033[1;32mI'm\033[0m', end='\r')
    time.sleep(1)
    print('\033[1;32mI'm a\033[0m', end='\r')
    time.sleep(0.5)
    print('\033[1;32mI'm a \033[0m', end='\r')
    time.sleep(0.5)
    
    print('\033[1;32mI'm not afraid of death;\033[0m')
    time.sleep(0.5)
    print('\033[1;32mI'm not afraid of death;\033[0m \033[1;33mi\033[0m')
    time.sleep(0.5)
    print('\033[1;32mI'm not afraid of death;\033[0m \033[1;33mint0n\033[0m')
    time.sleep(0.5)
    print('\033[1;32mI'm not afraid of death;\033[0m \033[1;33mint0r\033[0m')
    time.sleep(0.5)
    print('\033[1;32mI'm not afraid of death;\033[0m \033[1;33mint0r 8\033[0m')
    time.sleep(0.5)
    print('\033[1;32mI'm not afraid of death;\033[0m \033[1;33mint0r 8nth\033[0m')
    time.sleep(0.5)
    print('\033[1;32mI'm not afraid of death;\033[0m \033[1;33mint0r 8nth 1\033[0m')
    time.sleep(0.5)
    print('\033[1;32mI'm not afraid of death;\033[0m \033[1;33mint0r 8nth 1g\033[0m')
    time.sleep(0.5)
    print('\033[1;33mJust don't want to be there when it happens.\033[0m')
    time.sleep(0.5)
    
    print('\033[1;31m----------------------------------\033[0m')
    print('\033[1;33mTranslated: "I\033[0m \033[1;31mingrained concern')
    print('\033[1;33min the ear-\033[0m \033[1;31menoirist')
    print('\033[1;33mas chimpanzee"\033[0m')
    
    time.sleep(1)
    print('\n\033[1;31mPress Ctrl+C to throw spaghetti at the wall\033[0m')
    while True:
        time.sleep(1)