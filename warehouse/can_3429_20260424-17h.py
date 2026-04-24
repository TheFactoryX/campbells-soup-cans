"""
Campbell's Soup Can #3429
Produced: 2026-04-24 17:12:41
Worker: inclusionAI: Ling-2.6-flash (free) (inclusionai/ling-2.6-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def print_woody_quote():
    # ANSI color codes
    purple = "\033[35m"
    cyan = "\033[36m"
    yellow = "\033[33m"
    red = "\033[31m"
    green = "\033[32m"
    reset = "\033[0m"
    bold = "\033[1m"
    dim = "\033[2m"
    
    # Woody Allen style quote
    quote_parts = [
        "I'm not afraid of death; I just don't want",
        "to be there when it happens.",
        "",
        dim + "— Woody Allen, probably while",
        "overanalyzing his life choices." + reset
    ]
    
    # ASCII art - a neurotic brain
    brain_art = [
        "      ░▒▓██████▓▒░      ",
        "   ░▒▓██▓▓▓▓▓▓██▓▒░   ",
        "  ███▓▓▓▓▓▓▓▓▓▓▓▓███  ",
        "  ███▓▓▓▓▓▓▓▓▓▓▓▓███  ",
        "    ███▓▓▓▓▓▓▓▓███    ",
        "       ███▓▓▓██       ",
        "       ███▓▓▓██       ",
        "        █████         ",
        "       ▄█████▄        ",
        "     ▄██████████      ",
        "    █████████████     ",
        "   ███████████████    ",
        "   ███████████████    ",
        "    ░▒▓██████▓▒░     ",
        "       ░░░░░░         "
    ]
    
    # Animation effect
    for i in range(5):
        sys.stdout.write('\033c')  # Clear screen
        
        # Print title with animation
        title = f"{purple}{bold}WOODY ALLEN{reset}"
        subtitle = f"{cyan}Existential Crisis Club {red}[{yellow}Member Since 1945{red}]{cyan}  {reset}"
        
        print(title.center(60))
        print(subtitle.center(60))
        print()
        
        # Print brain with pulsing effect
        pulse = "█" * (i + 1) if i < 3 else "█" * (6 - i)
        print(f"{dim}{' '.join(line.center(50) for line in brain_art)}{reset}")
        print()
        
        # Print quote with typing effect
        for line in quote_parts:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.02)
            print()
        
        time.sleep(1)
    
    # Final static display
    sys.stdout.write('\033c')
    print(title.center(60))
    print(subtitle.center(60))
    print()
    print(brain_art[7])  # Just the brain
    print()
    for line in quote_parts:
        print(line)
    print()
    print(f"{yellow}🎭{reset} The universe is an accident. {cyan}Probably.{reset}")

if __name__ == "__main__":
    print_woody_quote()