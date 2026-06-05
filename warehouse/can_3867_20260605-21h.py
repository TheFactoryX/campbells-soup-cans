"""
Campbell's Soup Can #3867
Produced: 2026-06-05 21:45:47
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    
    # ASCII art frame
    top_border = "╔═══════════════════════════════════════════════════════════════════════════════════════════════╗"
    bottom_border = "╚═══════════════════════════════════════════════════════════════════════════════════════════════╝"
    side_border = "║"
    
    # Colors using ANSI escape codes
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    
    # Print top border with animation
    print(CYAN, end="")
    for char in top_border:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print(RESET)
    
    # Print title
    print(side_border + " " + YELLOW + "WOODY ALLEN'S PHILOSOPHICAL MUSINGS" + RESET + " " * (len(top_border) - 35) + side_border)
    
    # Print empty line
    print(side_border + " " * (len(top_border) - 2) + side_border)
    
    # Print quote with typewriter effect and color changes
    quote_lines = [
        RED + "I don't want to achieve immortality through my work; I want to achieve it through not dying." + RESET,
        MAGENTA + "But I'm not optimistic about that approach." + RESET,
        GREEN + "I figure if I'm going to be miserable, I might as well get paid for it." + RESET,
        WHITE + "That's my philosophy. It's not profound, but it pays the rent." + RESET
    ]
    
    for line in quote_lines:
        print(side_border + " " + line + " " * (len(top_border) - len(line) - 4) + side_border)
        time.sleep(0.5)
    
    # Print empty line
    print(side_border + " " * (len(top_border) - 2) + side_border)
    
    # Print author attribution with animation
    print(side_border + " " * ((len(top_border) - 25) // 2), end="")
    sys.stdout.write(BLUE)
    for char in "─ WOODY ALLEN ─":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(RESET + " " * ((len(top_border) - 25) // 2) + side_border)
    
    # Print bottom border
    print(CYAN, end="")
    for char in bottom_border:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print(RESET)
    
    # Add some visual interest with a bouncing cursor animation
    print("\n" * 3)
    for i in range(5):
        print(" " * ((len(top_border) - 20) // 2) + YELLOW + "THINKING" + "." * (i % 3) + RESET + " " * ((len(top_border) - 20) // 2))
        time.sleep(0.3)
    
    # Final message with typewriter effect
    print("\n" * 2)
    final_msg = YELLOW + "Why are you still here? Go live your life (or at least pretend to)!" + RESET
    typewriter(final_msg, 0.03)
    print("\n" * 2)
    
    # Add a small Woody Allen ASCII art
    woody = [
        "    .--.",
        "   |o_o |",
        "   |:_/ |",
        "  //   \\ \\",
        " (|     | )",
        "/'\\_   _/`\\",
        "\\___)=(___/"
    ]
    
    for line in woody:
        print(" " * ((len(top_border) - len(line)) // 2) + line)
        time.sleep(0.2)

if __name__ == "__main__":
    main()