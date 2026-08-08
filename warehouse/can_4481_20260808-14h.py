"""
Campbell's Soup Can #4481
Produced: 2026-08-08 14:49:37
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI Color Codes
class Color:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter(text, delay=0.05, color=Color.CYAN):
    """Simulates a neurotic, hesitant typing style."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Color.END}")
        sys.stdout.flush()
        # Add slight jitter to simulate neurosis
        time.sleep(delay + random.uniform(0, 0.03))
    print()

def draw_frame(content, width=60):
    """Draws a stylish, slightly unstable frame."""
    border_char = random.choice(['*', '~', '?', '!', '.'])
    top = f"{Color.MAGENTA}{border_char * (width + 2)}{Color.END}"
    bottom = f"{Color.MAGENTA}{border_char * (width + 2)}{Color.END}"
    
    print(top)
    # Center content
    lines = content.split('\n')
    for line in lines:
        padding = (width - len(line)) // 2
        if padding > 0:
            print(f"{Color.MAGENTA}{border_char}{Color.END}{' ' * padding}{line}{' ' * (width - len(line) - padding)}{Color.MAGENTA}{border_char}{Color.END}")
        else:
            print(f"{Color.MAGENTA}{border_char}{Color.END}{line}{Color.MAGENTA}{border_char}{Color.END}")
    print(bottom)

def animate_existential_dread():
    """A small visual distraction to represent anxiety."""
    dots = [".  ", ".. ", "...", " ..", "  ."]
    for _ in range(3):
        for dot in dots:
            sys.stdout.write(f"\r{Color.YELLOW}Searching for meaning in a void of nothingness{Color.END}{dot}")
            sys.stdout.flush()
            time.sleep(0.3)
    print("\n")

def main():
    clear_screen()
    
    # Intro animation
    print(f"\n\n{Color.BOLD}{Color.BLUE}--- NEUROTIC THOUGHT GENERATOR v1.0 ---{Color.END}\n")
    time.sleep(1)
    
    animate_existential_dread()
    
    # The Quote
    quote = (
        "I have a profound fear of the infinite,\n"
        "but I'm even more terrified of a brunch\n"
        "where the mimosas are lukewarm and\n"
        "nobody asks about my neuroses."
    )
    
    # Creative presentation
    draw_frame(quote, width=55)
    
    print(f"\n{Color.ITALIC}{Color.RED}— A very anxious philosopher{Color.END}\n")
    
    # Final flickering effect
    for _ in range(3):
        sys.stdout.write(f"\r{Color.YELLOW}Are you okay?{Color.END}")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\r" + " " * 20 + "\r")
        time.sleep(0.1)
    
    print(f"{Color.BOLD}{Color.CYAN}System shutdown. Go lie down.{Color.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}Even the interruption is existential.{Color.END}")