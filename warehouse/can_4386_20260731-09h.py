"""
Campbell's Soup Can #4386
Produced: 2026-07-31 09:59:44
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

# ANSI Color Codes for that neurotic, cinematic aesthetic
class Colors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    GRAY = '\033[90m'

def clear_screen():
    print("\033[CLS\033[H", end="")

def typewriter_effect(text, color=Colors.RESET, speed=0.04):
    """Simulates a nervous, stuttering typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        # Occasional nervous pause
        if char == ',' or char == '.' or char == ';':
            time.sleep(speed * 4)
        else:
            time.sleep(speed)

def draw_frame():
    """Draws a cinematic-style border."""
    width = 60
    print(Colors.GRAY + "┌" + "─" * (width - 2) + "┐")
    print("│" + " " * (width - 2) + "│")
    print(Colors.GRAY + "└" + "─" * (width - 2) + "┘" + Colors.RESET)

def animate_neurotic_dots():
    """Visualizes the feeling of existential dread/waiting."""
    dots = ["", ".", "..", "...", "...."]
    for _ in range(3):
        for dot in dots:
            sys.stdout.write(f"\r{Colors.MAGENTA}Checking the meaning of existence {dot}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.4)
    print("\n")

def main():
    clear_screen()
    
    # The Woody Allen Style Quote
    quote = "I finally decided to stop worrying about whether I'm happy, " \
            "and instead focus on whether my neuroses are at least " \
            "technically interesting to a psychoanalyst."

    author = "— A Neurotic Existentialist"

    # --- PHASE 1: THE INTRO ---
    print("\n" * 2)
    print(f"{Colors.GRAY}Loading existential dread...{Colors.RESET}")
    animate_neurotic_dots()

    # --- PHASE 2: THE FRAME ---
    draw_frame()
    
    # --- PHASE 3: THE REVEAL ---
    # We'll split the quote to fit inside the box
    lines = [
        "I finally decided to stop worrying about",
        "whether I'm happy, and instead focus on",
        "whether my neuroses are at least",
        "technically interesting to a",
        "psychoanalyst."
    ]

    for line in lines:
        # Typewriter effect inside the frame
        sys.stdout.write("│ ")
        typewriter_effect(line.ljust(57), color=Colors.YELLOW, speed=0.03)
        sys.stdout.write(" │\n")

    # --- PHASE 4: THE SIGNATURE ---
    print("│ " + " " * 57 + "│")
    typewriter_effect(" " * 57 + author, color=Colors.CYAN, speed=0.02)
    print("│ " + " " * 57 + "│")
    
    draw_frame()
    print("\n" + f"{Colors.RED}{Colors.BOLD} [END OF SESSION ]{Colors.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Even the program has an existential crisis and quits.{Colors.RESET}")