"""
Campbell's Soup Can #3213
Produced: 2026-04-09 23:53:29
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

# ANSI Escape Codes for the neurotic atmosphere
class Style:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_GREY = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RED = '\033[91m'
    END = '\033[0m'

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter(text, delay=0.06, color=Style.BOLD):
    """Simulates a nervous, stuttering neurotic speech pattern."""
    full_text = ""
    for char in text:
        sys.stdout.write(color + char + Style.END)
        sys.stdout.flush()
        # Add random pauses to mimic anxiety
        if char == ',' or char == ';' or char == ':':
            time.sleep(delay * 10)
        elif char == ' ':
            time.sleep(delay * 2)
        else:
            time.sleep(delay)
        sys.stdout.write('\n' * 0 if char != '\n' else '') # Ensure line breaks work
    print()

def draw_frame(quote):
    """Draws a fancy, slightly crumbling border."""
    width = len(quote) + 6
    border_char = "░"
    
    print(Style.DARK_GREY + "╔" + "═" * (width - 2) + "╗" + Style.END)
    print(Style.DARK_GREY + "║" + Style.END, end="")
    print(Style.CYAN + "  " + quote + "  " + Style.END, end="")
    print(Style.DARK_GREY + "║" + Style.END)
    print(Style.DARK_GREY + "╚" + "═" * (width - 2) + "╝" + Style.END)

def neurosis_animation():
    """A quick visual pulse of existential dread."""
    colors = [Style.RED, Style.PURPLE, Style.CYAN, Style.DARK_GREY]
    for _ in range(3):
        for c in colors:
            clear_screen()
            print("\n\n\n")
            print(Style.BOLD + c + "   [ SEARCHING FOR MEANING... ]" + Style.END)
            time.sleep(0.1)

def main():
    # The Woody Allen Quote
    quote = "I try to find meaning in the universe, but I usually just find a profound sense of gastrointestinal discomfort and the terrifying realization that I forgot to turn off the stove."

    try:
        # Stage 1: The Nervous Build-up
        clear_screen()
        print("\n\n")
        print(Style.DARK_GREY + "   (Deep, anxious sighing sounds in the background...)" + Style.END)
        time.sleep(1.5)
        
        neurosis_animation()

        # Stage 2: The Delivery
        clear_screen()
        print("\n\n")
        print(Style.ITALIC + Style.DARK_GREY + "--- A Sudden Epiphany ---" + Style.END + "\n")
        time.sleep(1)
        
        typewriter(quote, delay=0.05, color=Style.BOLD + Style.PURPLE)
        
        # Stage 3: The Visual Finale
        print("\n")
        draw_frame("EXISTENTIAL CRISIS DETECTED")
        
        print(f"\n{Style.RED}{Style.ITALIC}[ End of Transmission. Please contact your therapist. ]{Style.END}\n")

    except KeyboardInterrupt:
        print(f"\n{Style.RED}Even your exit is neurotic.{Style.END}")

if __name__ == "__main__":
    main()