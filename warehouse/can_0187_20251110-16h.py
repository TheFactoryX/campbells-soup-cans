"""
Campbell's Soup Can #187
Produced: 2025-11-10 16:43:15
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os

# ANSI color codes
class Colors:
    MAGENTA = "\033[95m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art of Woody Allen with cyan rings
print(f"""
{Colors.CYAN}          /)())
         /  / / 
        //  (_/    {Colors.RESET}
{Colors.CYAN}      __//{Colors.MOUSE}              Woody Allen
     |{Colors.MAGENTA}oo|{Colors.CYAN}{' ' * 10}             {Colors.RESET}·,.....
      |__;           {Colors.MAGENTA}..':::::::::.'.
                    (::::'::::::::':',)
                     `.-='=-'=-'=-'`{Colors.RESET}""".format(
    MOUSE=Colors.YELLOW + "π__π" + Colors.CYAN
))

# Typing effect with color transitions
quote = "The only real security that any job has is a motherboard with a 386 and 4 megabytes of RAM"
parts = [
    f"{Colors.MAGENTA}{part}{Colors.RESET}" for part in quote.split()
]
final_quote = ' '.join(parts)

# Create print-ready list of combined colored elements
elements = []
for char in final_quote:
    elements.append(char)
    if len(elements) % 8 == 0:  # Add color transitions periodically
        current_colors = [Colors.MAGENTA, Colors.GREEN, Colors.YELLOW, Colors.CYAN]
        color_to_add = random.choice(current_colors)
        elements.append(color_to_add)

# Print formatted with animated typing effect
for i, element in enumerate(elements):
    # Add quotes and parentheses appropriately
    if i == 0:
        print(f"{Colors.MAGENTA}( {Colors.RESET} {element}", end='', flush=True)
    elif i == len(elements) - 1:
        print(f" {element}{Colors.CYAN} ){Colors.RESET}")
    else:
        print(element, end='', flush=True)

    time.sleep(0.005)