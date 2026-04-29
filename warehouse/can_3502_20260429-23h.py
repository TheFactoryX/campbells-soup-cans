"""
Campbell's Soup Can #3502
Produced: 2026-04-29 23:10:47
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Quote with Visual Flair
"""
import sys
import time

def typewriter_print_inline(text, delay=0.03, color=None):
    """Print text with typewriter effect, no newline, optional color."""
    if color:
        sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write('\033[0m')  # reset attributes
    # Note: no newline

def main():
    quote = "I've accepted the inevitability of death, but I still haven't accepted the inevitability of my therapist's vacation."
    
    border_color = '\033[94m'  # blue
    text_color = '\033[93m'   # yellow
    reset = '\033[0m'
    
    interior = len(quote) + 2  # spaces on each side of text inside box
    
    # Top border
    print(f'{border_color}┌{"─"*interior}┐{reset}')
    
    # Left border and space
    sys.stdout.write(f'{border_color}│ {reset}')
    
    # Type the quote with typewriter effect, inline
    typewriter_print_inline(quote, delay=0.05, color=text_color)
    
    # Right border with space
    sys.stdout.write(f'{border_color} │{reset}')
    print()  # move to next line
    
    # Bottom border
    print(f'{border_color}└{"─"*interior}┘{reset}')
    
    # Attribution
    print(f'\033[90m- Woody Allen (probably)\033[0m')

if __name__ == "__main__":
    main()