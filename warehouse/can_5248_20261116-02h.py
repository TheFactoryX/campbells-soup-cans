"""
Campbell's Soup Can #5248
Produced: 2026-11-16 02:44:05
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    # Define ANSI color codes
    GREEN = "\033[92m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    
    # Woody Allen style quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying. And even then, I'm not sure I'd make the cut."
    
    # Box dimensions
    BOX_WIDTH = 50
    INNER_WIDTH = BOX_WIDTH - 2  # 48
    
    # Create box borders
    top_border = GREEN + "+" + "-" * BOX_WIDTH + "+" + RESET
    bottom_border = GREEN + "+" + "-" * BOX_WIDTH + "+" + RESET
    
    # Wrap quote to INNER_WIDTH
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= INNER_WIDTH:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    if current_line:
        lines.append(current_line)
    
    # Pad lines to INNER_WIDTH
    padded_lines = [line.ljust(INNER_WIDTH) for line in lines]
    
    # Print the box
    print(top_border)
    for line in padded_lines:
        full_line = "| " + line + " |"
        print(WHITE + full_line + RESET)
    print(bottom_border)

if __name__ == "__main__":
    main()