"""
Campbell's Soup Can #3443
Produced: 2026-04-25 11:54:23
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def main():
    # ANSI color codes
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'
    
    # Woody Allen style philosophical quote (shortened for visual fit)
    quote = "The meaning of life? I don't know. But I'm here."
    inner_width = 40
    centered_quote = quote.center(inner_width)
    total_width = inner_width + 2  # Total width including borders
    
    # Create the box lines
    top_border = CYAN + '*' * total_width + RESET    side_border = CYAN + '*' + ' ' * inner_width + '*' + RESET
    quote_line = CYAN + '*' + YELLOW + centered_quote + CYAN + '*' + RESET
    
    # Print the visually interesting box
    print(top_border)
    print(side_border)
    print(quote_line)
    print(side_border)
    print(top_border)

if __name__ == "__main__":
    main()