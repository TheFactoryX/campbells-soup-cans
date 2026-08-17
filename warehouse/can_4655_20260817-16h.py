"""
Campbell's Soup Can #4655
Produced: 2026-08-17 16:45:19
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

def clear_screen():
    """Clears the terminal console."""
    print("\033[H\033[J", end="")

def colorize(text, color_code):
    """Wraps text in ANSI color codes."""
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.05, color="\033[37m"):
    """Prints text with a typewriter animation effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def draw_box(text, width=60, padding=2):
    """Draws a fancy ASCII box around the quote."""
    border = "╔" + "═" * (width - 2) + "╗"
    footer = "╚" + "═" * (width - 2) + "╝"
    
    print(color("╔" + "═" * (width - 2) + "╗", "\033[36m"))
    
    # Center text within the box
    lines = text.split('\n')
    for line in lines:
        # Handle line wrapping if necessary (simplified)
        if len(line) > width - (padding * 2):
            line = line[:width - (padding * 2)]
        
        left_pad = " " * padding
        right_pad = " " * (width - len(line) - padding * 2)
        print(f"{color('║', '\033[36m')}{left_pad}{line}{right_pad}{color('║', '\033[36m')}")
        
    print(color(footer, "\033[36m"))

def main():
    # ANSI Color palette
    CYAN = "36"
    YELLOW = "33"
    MAGENTA = "35"
    RED = "31"
    WHITE = "37"
    GREEN = "32"

    clear_screen()

    # 1. Intro Animation: The "Existential Dread" Loading Bar
    print(color("\n\n", WHITE))
    print(colorize(" [ LOADING EXISTENTIAL CRISIS... ] ", YELLOW))
    print("")
    
    bar_width = 30
    for i in range(bar_width + 1):
        percent = int((i / bar_width) * 100)
        bar = "█" * i + "░" * (bar_width - i)
        sys.stdout.write(f"\r{color(bar, GREEN)} {percent}%")
        sys.stdout.flush()
        time.sleep(0.05)
    
    print("\n\n")
    time.sleep(0.5)
    clear_screen()

    # 2. The "Neurotic" Header
    print(color("*" * 50, CYAN))
    print(colorize("   A MOMENT OF INTROSPECTION FOR THE NERVOUS   ", MAGENTA))
    print(color("*" * 50, CYAN))
    print("\n")

    # 3. The Quote
    # A custom Woody Allen style quote: neurotic, existential, and slightly panicked.
    woody_quote = (
        "My therapist says I have a profound fear of the unknown, "
        "but personally, I think I'm just suspicious of the known. "
        "I mean, if I can't predict the meaning of life, "
        "how am I supposed to plan my weekend?"
    )

    # 4. Final Visual Presentation
    # Add some "stuttering" text effect to mimic nervousness
    nervous_quote = ""
    for char in woody_quote:
        nervous_quote += char
        if random.random() > 0.95: # Occasional hesitation
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.1)
    
    draw_box(nervous_quote, width=65)

    print("\n")
    print(colorize("--- End of thought (and sanity) ---", RED))
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[31m[ Even the user couldn't handle this much philosophy. ]\033[0m")