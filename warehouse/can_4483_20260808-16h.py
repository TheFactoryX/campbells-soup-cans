"""
Campbell's Soup Can #4483
Produced: 2026-08-08 16:52:01
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

# ANSI Escape Sequences for a neurotic color palette
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
RED = "\033[31m"
GREY = "\033[90m"

def typewriter_effect(text, delay=0.05, color=RESET):
    """Prints text character by character to simulate neurotic pacing."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width, height, color):
    """Draws a shaky, neurotic-looking box."""
    top = f"{color}┌{'─' * (width-2)}┐{RESET}"
    bottom = f"{color}└{'─' * (width-2)}┘{RESET}"
    side = f"{color}│{RESET}"
    
    print(top)
    for _ in range(height):
        print(f"{side}{' ' * (width-2)}{side}")
    print(bottom)

def clear_screen():
    """Clears the terminal."""
    print("\033[H\033[J", end="")

def main():
    # The "Neurotic Philosophical Insight"
    quote = "I have a profound fear of the infinite, primarily because it implies a very long waiting room without any decent bagels."
    author = "— A Neurotic Intellectual"

    clear_screen()

    # Phase 1: The Existential Dread (Intro Animation)
    print(f"\n{GREY}Searching for meaning in a meaningless universe...{RESET}")
    time.sleep(1)
    
    for i in range(3):
        sys.stdout.write(f"\r{RED}Panic Level: {'!' * (i+1)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

    # Phase 2: The Big Reveal
    # We'll create a dynamic "shaking" box effect
    quote_text = f"    \"{quote}\"    "
    author_text = f"    {author}    "
    
    box_width = len(quote_text) + 4
    box_height = 5

    # Animate the appearance of the quote
    for _ in range(2): # Subtle shake effect
        clear_screen()
        offset = " " * random.randint(0, 1)
        
        print(f"\n{offset}{CYAN}┌{'─' * (box_width-2)}┐{RESET}")
        
        # Row 1 (Empty)
        print(f"{offset}{CYAN}│{RESET}{' ' * (box_width-2)}{CYAN}│{RESET}")
        
        # Row 2 (The Quote)
        # We print it with a typing effect inside the frame
        sys.stdout.write(f"{offset}{CYAN}│{RESET}")
        typewriter_effect(quote_text, 0.04, MAGENTA)
        # Note: typewriter_effect adds a newline, so we handle layout carefully
        # Since we can't easily 'typewriter' into a middle line without complex logic, 
        # we'll just print the lines for simplicity in this art style.
        
        # Let's re-do the drawing logic for a cleaner look
        clear_screen()
        print(f"\n\n{offset}{YELLOW}{BOLD}╔══════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{offset}{YELLOW}║{RESET}                                                              {YELLOW}║{RESET}")
        
        # Print the quote split into two lines for better aesthetics
        line1 = quote[:45]
        line2 = quote[45:]
        print(f"{offset}{YELLOW}║{RESET}  {MAGENTA}{line1.ljust(47)}{RESET} {YELLOW}║{RESET}")
        print(f"{offset}{YELLOW}║{RESET}  {MAGENTA}{line2.ljust(47)}{RESET} {YELLOW}║{RESET}")
        
        print(f"{offset}{YELLOW}║{RESET}                                                              {YELLOW}║{RESET}")
        print(f"{offset}{YELLOW}╚══════════════════════════════════════════════════════════════╝{RESET}")
        print(f"{offset}{GREY}{author_text}{RESET}")
        
        time.sleep(0.1)
        if _ == 0: time.sleep(0.1)

    # Phase 3: The Fading Exit
    time.sleep(2)
    print(f"\n{RED}Now, if you'll excuse me, I have to go analyze my childhood.{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Even the exit is existential. Goodbye.{RESET}")