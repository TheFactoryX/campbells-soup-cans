"""
Campbell's Soup Can #828
Produced: 2025-12-09 23:30:25
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
import sys

# ANSI color codes
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Woody Woody's neurotic quote
quote = (
    "I'd rather have a small anxiety attack now\n"
    "than a big one later in traffic on Sunday."
)

def colored_box(text, border_color=GREEN, text_color=YELLOW, width=60):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max(width, max_len + 4)
    
    horizontal = f'{border_color}╔{'═' * box_width}╗{RESET}'
    separator = f'{border_color}╠{'═' * box_width}╣{RESET}'
    footer = f'{border_color}╚{'═' * box_width}╝{RESET}'
    
    result = [horizontal]
    for line in lines:
        padded = line.center(box_width)
        result.append(f'{border_color}║{text_color} {padded} {border_color}║{RESET}')
    result.append(footer)
    return '\n'.join(result)

def spinning_cursor(duration=2.0):
    symbols = '⸻⸹⸻⸹'
    for i in range(int(duration * 4)):
        sys.stdout.write(f'\r{CYAN}{BOLD}{symbols[i % len(symbols)]} Loading existential crisis...{RESET}')
        sys.stdout.flush()
        time.sleep(0.25)

def main():
    # Animated loading
    spinning_cursor(1.5)
    
    # Print the philosophical box
    print('\n')
    print(colored_box(quote, GREEN, YELLOW))
    
    # Add a funny existential footer
    print(f'\n{CYAN}“Remember: Nothing is certain except death, taxes, and overthinking.” — Woody Allen{RESET}')

if __name__ == "__main__":
    main()