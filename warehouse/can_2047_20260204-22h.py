"""
Campbell's Soup Can #2047
Produced: 2026-02-04 22:46:41
Worker: OpenAI: GPT-4o (extended) (openai/gpt-4o:extended)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
ENDC = "\033[0m"

quote = """
"Life is a lot like jazz... 
it's best when you improvise."
"""

def print_colored_text(text, color):
    for line in text.splitlines():
        print(color + line + ENDC)
        time.sleep(0.3)

def animate_frame(frame, color):
    print("\033c", end="")  # ANSI code to clear screen
    print_colored_text(frame, color)
    time.sleep(0.3)

def ascii_art():
    return [
        """
         ____  
        / ---\ 
       | o_o o)
        \     / 
         \ _ /  
        """,
        """
          ____    
         / ---\   
        | o_o o)  
         \     /  
          \___/   
        """
    ]

def main():
    frames = ascii_art()
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

    print("Animating...")
    for _ in range(5):
        for frame, color in zip(frames, colors):
            animate_frame(frame, color)
    
    print_colored_text(quote, BLUE)
    
if __name__ == "__main__":
    main()