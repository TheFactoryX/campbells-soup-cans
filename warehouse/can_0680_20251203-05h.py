"""
Campbell's Soup Can #680
Produced: 2025-12-03 05:35:01
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time

# ANSI escape codes for colors and styles
RESET = '\033[0m'
BOLD = '\033[1m'
MAGENTA_BG = '\033[45m'
WHITE_FG = '\033[37m'
YELLOW_FG = '\033[33m'

# A philosophical gem in true Woody Allen style
QUOTE = (
    "The true terror of existence isn't death, darling—\n"
    "it's realizing you'll spend eternity wondering\n"
    "if anyone ever really preferred you for you,\n"
    "or merely as a convenient excuse to avoid\n"
    "making interesting conversation at parties."
)

def box-decoration(text_lines, width_padding=4):
    """Create a fancy boxed layout for the quote"""
    max_len = max(len(line) for line in text_lines)
    box_width = max_len + width_padding
    
    # Border characters
    top = f'╔{"═" * box_width}╗'
    bottom = f'╚{"═" * box_width}╝'
    
    # Build boxed lines
    boxed_lines = [top]
    for line in text_lines:
        padding = (box_width - len(line)) // 2
        boxed_lines.append(f'║{" " * padding}{line}{" " * (box_width - padding - len(line))}║')
    boxed_lines.append(bottom)
    
    return boxed_lines

def pulse_color(text, foreground, background, duration=0.5):
    """Create a subtle pulsing color effect"""
    print(f"{background}{foreground}{text}{RESET}")

def main():
    # Split quote into lines
    quote_lines = QUOTE.split('\n')
    
    # Create decorated box
    boxed_quote = box-decoration(quote_lines)
    
    # Colorful introduction
    print(f"{MAGENTA_BG}{WHITE_FG}")
    print("\n" * 2)
    print(" ┌────────────────────────────────────┐")
    print(" │   A Neurotic's Guide to Being     │")
    print(" │         Alive & Confused          │")
    print(" └────────────────────────────────────┘")
    print("\n" * 2)
    
    # Animate the quote box
    for line in boxed_quote:
        pulse_color(line, WHITE_FG, MAGENTA_BG)
        time.sleep(0.1)
    
    # Witty signature
    print("\n" * 2)
    pulse_color(f"{YELLOW_FG}   - Said while avoiding commitment and existential dread {RESET}", YELLOW_FG, MAGENTA_BG)
    print(f"{MAGENTA_BG}{WHITE_FG}")
    print(" ╭───────────────────────────────╮")
    print(" │  'I take existential crises      │")
    print(" │   one nervous breakdown at a time'│")
    print(" ╰───────────────────────────────╯")
    print(RESET)

if __name__ == "__main__":
    main()