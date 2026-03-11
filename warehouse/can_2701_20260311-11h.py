"""
Campbell's Soup Can #2701
Produced: 2026-03-11 11:47:45
Worker: EssentialAI: Rnj 1 Instruct (essentialai/rnj-1-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import colorama

colorama.init(autoreset=True)
# Define some ANSI escape codes
CYAN = "\033[96m"
RESET = "\033[0m"

def animation():
    woody_head = [
        "        \033[93m === \033[0m       ",
        "       \033[93m \033[0m  \033[93m \033[0m      ",
        "      \033[93m \033[0m    \033[93m \033[0m     ",
        "       \033[93m \033[0m  \033[93m \033[0m      ",
    ]
    for line in woody_head:
        print(line, end="\r")
        time.sleep(0.05)
    time.sleep(1)

def woody_style_quote():
    print(f"{CYAN}Woody Allen's Philosophical Nonsense")
    print("===============================")
    # Animate the head
    animation()
    # The quote
    print(f"{CYAN}\"Guilt is such a great motivator, \033[1mbut I can't seem to remember what I did wrong.\033[0m\"")
    print("No, I haven't seen it, but I've seen the right people!")
    # Add some ASCII art
    print("  ____")
    print(" /    \\")
    print("/ /\\ / \\")
    print("\\ \\ \\\\ /")
    print(" \\ \\|| / ")
    print("  || ||\n")

if __name__ == "__main__":
    woody_style_quote()
    # Keep the console open
    input(f"{RESET}Press Enter to exit...")
