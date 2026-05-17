"""
Campbell's Soup Can #3706
Produced: 2026-05-17 07:44:13
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI Escape Sequences for Colors and Styling
class Colors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CLEAR = '\033[H\033[J'

def typewriter_print(text, delay=0.05, color=Colors.CYAN):
    """Simulates a neurotic, hesitant typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.END}")
        sys.stdout.flush()
        # Random slight pauses to simulate neurotic hesitation
        time.sleep(delay + random.uniform(0, 0.1))
    print()

def draw_frame(quote):
    """Creates a stylish, slightly chaotic border for the quote."""
    width = len(quote) + 8
    top_border = f"{Colors.MAGENTA}╔{'═' * (width-2)}╗{Colors.END}"
    bottom_border = f"{Colors.MAGENTA}╚{'═' * (width-2)}╝{Colors.END}"
    
    print(top_border)
    print(f"{Colors.MAGENTA}║  {Colors.END}{quote}{Colors.MAGENTA}  ║{Colors.END}")
    print(bottom_border)

def brain_animation():
    """A little visual 'existential dread' animation."""
    frames = [
        "  (  )  ",
        " ( @ @ ) ",
        "(  ---  )",
        " ( @ @ ) ",
        "  (  )  "
    ]
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(f"\r{Colors.YELLOW}{Colors.BOLD}Neurotic Thought Process: {frame}{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.15)
    print("\n")

def main():
    # The Woody Allen-esque Quote
    quote = '"I find the concept of eternal life deeply troubling; primarily because I have no idea how I'll manage my social anxiety for that long."'

    # 1. Clear Screen
    sys.stdout.write(Colors.CLEAR)
    
    # 2. Intro sequence
    print(f"\n{Colors.BLUE}{Colors.BOLD}--- THE EXISTENTIAL CRISIS ENGINE v1.0 ---{Colors.END}\n")
    time.sleep(0.5)
    
    # 3. The 'Thinking' animation
    brain_animation()
    
    # 4. The Reveal
    print(f"{Colors.RED}{Colors.BOLD}CRITICAL THOUGHT DETECTED:{Colors.END}\n")
    time.sleep(1)
    
    draw_frame(quote)
    
    # 5. The Post-Thought Panic
    print(f"\n{Colors.GREEN}Status: Slightly more anxious than before.{Colors.END}")
    print(f"{Colors.BLUE}Press Enter to contemplate the void (or just exit)...{Colors.END}")
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Even your exit is neurotic.{Colors.END}")