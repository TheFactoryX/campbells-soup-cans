"""
Campbell's Soup Can #3303
Produced: 2026-04-15 22:05:09
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

# ANSI Escape Codes for a "Neurotic" aesthetic
class Colors:
    GREY = '\033[90m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def typewriter(text, speed=0.06, color=Colors.WHITE):
    """Simulates a nervous, stuttering typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        # Add a slight random jitter to the speed to mimic anxiety
        time.sleep(speed + random.uniform(0, 0.04))
    print()

def draw_box(content, width=60):
    """Draws a shaky, existential box around the text."""
    print(Colors.GREY + "┌" + "─" * (width - 2) + "┐" + Colors.RESET)
    
    lines = content.split('\n')
    for line in lines:
        padding = width - len(line) - 2
        if padding < 0:
            # If line is too long, wrap it (simplistic)
            print(f"{Colors.GREY}│{Colors.RESET} {line[:width-4]} {Colors.GREY}│{Colors.RESET}")
        else:
            print(f"{Colors.GREY}│{Colors.RESET} {line}{' ' * padding}{Colors.GREY}│{Colors.RESET}")
            
    print(Colors.GREY + "└" + "─" * (width - 2) + "┘" + Colors.RESET)

def neurotic_animation():
    """A brief visual representation of an existential crisis."""
    frames = [
        " (o_o) ",
        " (o.o) ",
        " (O.O) ",
        " (>_<) ",
        " (T_T) ",
        " ( -_-) "
    ]
    print("\n" * 2)
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(f"\r{Colors.RED}{Colors.BOLD} [ INTERNAL MONOLOGUE DETECTED ] {Colors.RESET} {frame}")
            sys.stdout.flush()
            time.sleep(0.15)
    print("\n")

def main():
    # Clear screen (works on most terminals)
    print("\033[H\033[J", end="")

    # The Quote
    quote = (
        "I have a profound, spiritual dread of the infinite,\n"
        "which is really just a fancy way of saying I'm terrified\n"
        "of running out of bagels before I run out of\n"
        "unresolved childhood traumas."
    )

    # Intro sequence
    print(f"{Colors.GREY}--- INITIALIZING EXISTENTIAL DREAD ---{Colors.RESET}\n")
    time.sleep(1)
    
    neurotic_animation()
    
    time.sleep(0.5)
    
    # The Reveal
    draw_box(quote, width=55)
    
    print(f"\n{Colors.CYAN}{Colors.BOLD}--- END OF THOUGHT (UNFORTUNATELY) ---{Colors.RESET}\n")
    
    # Final blinking cursor/anxiety
    try:
        while True:
            sys.stdout.write(f"\r{Colors.YELLOW}Is it over yet? {Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write(f"\r{' ' * 20}")
            sys.stdout.flush()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Finally, some peace.{Colors.RESET}\n")

if __name__ == "__main__":
    main()