"""
Campbell's Soup Can #3686
Produced: 2026-05-15 20:34:31
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_allen_quote():
    # ANSI color codes
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    RESET = "\033[0m"
    
    # Clear screen
    clear_screen()
    
    # Title with border
    title = "WOODY ALLEN'S PHILOSOPHICAL MUSINGS"
    print("\n" + WHITE + "=" * 70 + RESET)
    print(CYAN + BOLD + title.center(70) + RESET)
    print(WHITE + "=" * 70 + RESET + "\n")
    
    # Quote
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon. "
        "I tried to find the meaning of life, but then I remembered I had to return this library book, "
        "and suddenly the existential questions seemed much less urgent. "
        "I've often wondered if my life has any purpose, and then I thought about it, "
        "and decided that maybe my purpose is to wonder about my purpose. "
        "It's a nice little recursive loop I've got going. "
        "Like a dog chasing its tail, except I'm neurotic and I worry about whether I locked the door."
    )
    
    # Create a decorative box
    box_width = 68
    box_border = WHITE + "|" + RESET
    
    print(box_border + " " * box_width + box_border)
    
    # Print the quote with animation
    words = quote.split()
    current_line_length = 0
    
    for i, word in enumerate(words):
        # Cycle through colors
        colors = [YELLOW, GREEN, BLUE, MAGENTA, CYAN]
        color = colors[i % len(colors)]
        
        # Style variations
        if i % 5 == 0:
            style = BOLD
        else:
            style = ""
        
        # Check if we need a new line
        if current_line_length + len(word) + 1 > box_width - 2:
            print("\n" + box_border + " ", end="")
            current_line_length = 1
        
        # Print the word
        print(f"{style}{color}{word} {RESET}", end="")
        current_line_length += len(word) + 1
        
        # Add a small delay for animation effect
        time.sleep(0.03)
        sys.stdout.flush()
    
    # Close the box
    print("\n" + box_border + " " * box_width + box_border)
    print(WHITE + "=" * 70 + RESET + "\n")
    
    # Woody Allen ASCII art
    woody = [
        WHITE + "      .--." + RESET,
        WHITE + "     |o_o |" + RESET,
        WHITE + "     |:_/ |" + RESET,
        WHITE + "    //   \\ \\" + RESET,
        WHITE + "   (|     | )" + RESET,
        WHITE + "  /' \\   / \\\\" + RESET,
        WHITE + "  ||   |   ||" + RESET,
        WHITE + "  =='  ==  ==" + RESET
    ]
    
    for line in woody:
        print(line.center(70))
    
    # Signature
    print("\n" + RED + ITALIC + "                - Woody Allen (probably not)" + RESET)
    print("\n")
    
    # Wait a moment before ending
    time.sleep(3)
    clear_screen()

if __name__ == "__main__":
    woody_allen_quote()