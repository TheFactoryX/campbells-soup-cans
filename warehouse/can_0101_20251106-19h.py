"""
Campbell's Soup Can #101
Produced: 2025-11-06 19:26:59
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03, color=WHITE):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + '\n')
    sys.stdout.flush()

def draw_line(char='-', length=60, color=WHITE):
    sys.stdout.write(color + char * length + RESET + '\n')
    sys.stdout.flush()

def main():
    clear_screen()
    
    # Title
    draw_line('=', 70, MAGENTA)
    type_text("            WOODY ALLEN ON PHILOSOPHY AND LIFE", 0.02, YELLOW)
    draw_line('=', 70, MAGENTA)
    
    # Add some dramatic pause
    time.sleep(1)
    
    # ASCII art Woody silhouette
    woody_art = """
        {}
           .--.
           |o_o |
           |:_/ |
          //   \\ \
         (|     | )
        /'\_   _/`\\
        \\___)=(___/
    """.format(CYAN)
    type_text(woody_art, 0.01)
    
    time.sleep(1)
    
    # The quote with color emphasis
    type_text("\n", 0.05)
    draw_line('-', 70, BLUE)
    type_text("\n", 0.05)
    
    # Quote with emphasis on key words
    quote = "I tried to be a philosopher once, but I couldn't make a living from it, "
    emphasized_quote = ""
    for i, word in enumerate(quote.split()):
        if word in ["philosopher", "couldn't", "living"]:
            emphasized_quote += f"{BOLD}{RED}{word}{RESET} "
        else:
            emphasized_quote += f"{word} "
    
    type_text(emphasized_quote, 0.03)
    
    punchline = f"{BOLD}{GREEN}so I went back to neurosis—it pays better and has better dental.{RESET}"
    type_text(punchline, 0.05)
    
    type_text("\n", 0.05)
    draw_line('-', 70, BLUE)
    
    # Final thought
    time.sleep(2)
    type_text("\n", 0.05)
    type_text("(After a thoughtful pause while adjusting his glasses...)", 0.02, YELLOW)
    time.sleep(1.5)
    type_text("\n", 0.05)
    type_text("You know, the only thing I'm certain of is that I'm probably wrong about this.", 0.03, WHITE)
    
    # Exit gracefully
    time.sleep(3)
    clear_screen()

if __name__ == "__main__":
    main()