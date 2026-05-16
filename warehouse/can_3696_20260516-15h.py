"""
Campbell's Soup Can #3696
Produced: 2026-05-16 15:16:05
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

# ANSI Escape Codes for the Neurotic Aesthetic
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    GREY = "\033[90m"
    WHITE = "\033[37m"

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter(text, delay=0.06, color=Colors.WHITE):
    """Prints text with a nervous, stuttering typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        # Add a slight randomness to the delay to simulate neurosis
        time.sleep(delay + random.uniform(0, 0.04))
    print()

def draw_glasses():
    """ASCII Art of those iconic thick glasses."""
    glasses = [
        f"{Colors.WHITE}      .-------.       .-------.      {Colors.RESET}",
        f"{Colors.WHITE}     /   {Colors.YELLOW}O{Colors.WHITE}   \\     /   {Colors.YELLOW}O{Colors.WHITE}   \\     {Colors.RESET}",
        f"{Colors.WHITE}    |    {Colors.YELLOW}---{Colors.WHITE}    |-----|    {Colors.YELLOW}---{Colors.WHITE}    |    {Colors.RESET}",
        f"{Colors.WHITE}     \\_______/       \\_______/     {Colors.RESET}"
    ]
    for line in glasses:
        print(line)
        time.sleep(0.1)

def render_existential_crisis():
    clear_screen()
    
    # Phase 1: The Anxiety Build-up
    print(f"\n{Colors.GREY}[ System: Checking pulse... ]{Colors.RESET}")
    time.sleep(0.5)
    print(f"{Colors.GREY}[ System: Analyzing cosmic insignificance... ]{Colors.RESET}")
    time.sleep(0.8)
    print(f"{Colors.GREY}[ System: Locating misplaced sense of purpose... ]{Colors.RESET}")
    time.sleep(1.2)
    print(f"{Colors.RED}[ ERROR: PURPOSE NOT FOUND. ]{Colors.RESET}\n")
    time.sleep(1.0)

    clear_screen()
    
    # Phase 2: The Visual Presentation
    draw_glasses()
    print(f"\n{Colors.CYAN}{Colors.BOLD}--- A MOMENT OF PROFOUND UNCERTAINTY ---{Colors.RESET}\n")
    
    quote = (
        "\"I asked my therapist if there's a meaning to life, "
        "and he told me that's a very expensive question. "
        "Now I'm sitting here, terrified of the infinite void, "
        "and I can't even decide if I should have the bagel with "
        "cream cheese or just succumb to the void entirely.\""
    )

    # The Reveal
    typewriter(quote, delay=0.05, color=Colors.WHITE)
    
    print(f"\n{Colors.MAGENTA}--- END OF EXISTENCE (OR JUST THE PROGRAM) ---{Colors.RESET}\n")
    
    # Phase 3: The Fading Out
    time.sleep(1)
    print(f"{Colors.GREY}Press Ctrl+C to flee from your responsibilities.{Colors.RESET}")

if __name__ == "__main__":
    try:
        render_existential_crisis()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Running away? Typical.{Colors.RESET}")
        sys.exit()