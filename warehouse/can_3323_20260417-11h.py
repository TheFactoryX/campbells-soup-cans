"""
Campbell's Soup Can #3323
Produced: 2026-04-17 11:13:01
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

# ANSI Escape Codes for that "New York Intellectual" vibe
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[33m"
    GREY = "\033[90m"
    RED = "\033[31m"

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter_effect(text, delay=0.05, color=Style.RESET):
    """Prints text character by character for dramatic neurotic effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Style.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(text):
    """Draws a neurotic-looking box around the existential dread."""
    width = len(text) + 4
    border = Style.MAGENTA + "╔" + "═" * (width - 2) + "╗" + Style.RESET
    footer = Style.MAGENTA + "╚" + "═" * (width - 2) + "╝" + Style.RESET
    
    print(f"\n{border}")
    print(f"{Style.CYAN}║ {Style.BOLD}{text}{Style.RESET}{Style.CYAN} ║")
    print(f"{footer}\n")

def main():
    clear_screen()
    
    # The "Brain" animation - simulating an overthinking mind
    thoughts = ["*anxiety*", "*existential dread*", "*is there a God?*", "*did I leave the stove on?*", "*meaninglessness*"]
    
    print(f"{Style.GREY}Initializing Neurotic Subroutines...{Style.RESET}\n")
    time.sleep(1)

    for _ in range(3):
        thought = random.choice(thoughts)
        sys.stdout.write(f"\r{Style.RED}{Style.ITALIC}{thought}{Style.RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")
    time.sleep(1)

    # The Big Reveal
    quote = "I find it incredibly difficult to believe in a benevolent Creator, " \
            "mostly because if He exists, He clearly has a very dark sense of humor " \
            "and a complete lack of respect for my digestive system."

    # Dramatic buildup
    print(f"{Style.YELLOW}--- AN EXISTENTIAL MOMENT DETECTED ---{Style.RESET}")
    time.sleep(1.5)
    
    clear_screen()
    
    # Visual Layout
    print("\n" * 3)
    print(f"{Style.GREY}{'=' * 60}{Style.RESET}")
    print(f"{Style.GREY}{'MANHATTAN PHILOSOPHY SERIES #42':^60}{Style.RESET}")
    print(f"{Style.GREY}{'=' * 60}{Style.RESET}\n")
    
    typewriter_effect(quote, delay=0.04, color=Style.WHITE_BOLD if hasattr(Style, 'WHITE_BOLD') else Style.BOLD)
    
    print("\n")
    draw_frame(Style.ITALIC + "— Woody-ish Pseudo-Intellectual" + Style.RESET)
    
    print(f"\n{Style.GREY}{'=' * 60}{Style.RESET}")
    print(f"{Style.RED}{'Press Ctrl+C to succumb to the void.':^60}{Style.RESET}\n")

if __name__ == "__main__":
    # Making sure we don't crash if user hits Ctrl+C
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Style.RED}Even your exit is a cry for help. Goodbye.{Style.RESET}")
        sys.exit()

# Helper for Bold White if needed
Style.WHITE_BOLD = "\033[1;37m"