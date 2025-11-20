"""
Campbell's Soup Can #412
Produced: 2025-11-20 23:29:22
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
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

woody_quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "I've decided to take an active part in my continuing nonexistence.",
    "Never love anyone who treats you like he's the prince and you're the princess.",
    "I used to think I was indecisive, but now I'm not so sure.",
    "I'm having an affair with the French language; it's just enchanting.",
    "I'm not saying I'm stupid, but I have a very aggressive stroke."
]

color_codes = [
    '\033[1;91m',  # bright red
    '\033[1;34m',  # blue
    '\033[1;92m',  # bright green
    '\033[1;35m',  # magenta
    '\033[1;33m'   # yellow
]

colors = color_codes * 2  # Double the array to loop through colors multiple times
current_color_idx = 0

def print_wizard_quote():
    clear_screen()
    width = 50
    quote = woody_quotes[0]
    
    # ASCII art of Woody Allen
    ascii_art = [
        "   ___.",
        "  (0.0)",
        "  ( > )",
        "   ^ ^ ",
        "/////////////",
        " Woozy the wizard",
        "/////////////"
    ]
    
    # Drop shadow effect
    for i in range(10):
        clear_screen()
        shadow_indent = 4
        sys.stdout.write(" " * shadow_indent + " \n" * i)
        for line in ascii_art:
            sys.stdout.write(" " * (shadow_indent + i) + line + "\n")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Wizard with quote animation
    for i in range(60):
        clear_screen()
        sys.stdout.write("   ___.\n")
        sys.stdout.write("  (O.O)\n")
        sys.stdout.write("  ( > )\n")
        sys.stdout.write("   ^ ^ \n")
        
        angled = 1 + int(abs(5 - i))
        chars_to_move = wide_quote = " " * angled + quote + " " * (width - angled - len(quote))
        sys.stdout.write("/////////////" + " " * angled + "\n")
        sys.stdout.write(colors[current_color_idx] + "| " + chars_to_move + " |\033[0m\n")
        sys.stdout.write("/////////////" + " " * angled + "\n")
        
        sys.stdout.write("\n" + " " * angled + "  The rhinoceros flies!\n")
        sys.stdout.write(" " * (angled - 2) + "(They're watching and recording this)\n")
        current_color_idx = (current_color_idx + 1) % len(colors)
        sys.stdout.flush()
        time.sleep(0.2 if i < 50 else 0.05)

 print_wizard_quote()