"""
Campbell's Soup Can #3807
Produced: 2026-05-28 22:08:09
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

def clear_screen():
    print("\033[H\033[J", end="")

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter(text, delay=0.05, color="\033[37m"):
    """Prints text with a typewriter effect."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def draw_frame(content, width=60):
    """Draws a decorative ASCII box around content."""
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    print(color_text(top, "36"))
    
    lines = content.split('\n')
    for line in lines:
        padding = width - len(line) - 2
        if padding > 0:
            print(f"║ {line}{' ' * padding} ║")
        else:
            print(f"║ {line[:width-4]} ║")
            
    print(color_text(bottom, "36"))

def main():
    # Colors
    CYAN = "36"
    MAGENTA = "35"
    YELLOW = "33"
    RED = "31"
    WHITE = "37"
    
    # The Quote
    quote = (
        "\"I often wonder if the meaning of life is simply to avoid "
        "being perceived by a God who is clearly having a mid-life crisis.\""
    )
    
    # The Setup
    clear_screen()
    
    # 1. Intro Animation: Existential Dread Loading...
    print(color_text("\n\n", WHITE))
    print(color_text("   [ SYSTEM STATUS: NEUROTIC ]\n", RED))
    
    loading_steps = ["Analyzing void...", "Checking ego...", "Searching for purpose...", "Finding nothing..."]
    for step in loading_steps:
        sys.stdout.write(f"\r{color_text(step, YELLOW)}")
        sys.stdout.flush()
        time.sleep(0.8)
    print("\n")
    time.sleep(0.5)
    
    clear_screen()

    # 2. ASCII Art: A tiny, nervous thinker
    thinking_man = [
        "      .---.",
        "     /     \\",
        "    | () () |",
        "     \\  ^  /",
        "      ||||| ",
        "     /|___|\\",
        "    / |   | \\",
        "      |   |  ",
        "      |   |  "
    ]
    
    print("\n")
    for line in thinking_man:
        print(color_text(line.center(60), CYAN))
    print("\n")

    # 3. The Reveal
    # We split the quote into two lines for the box
    quote_lines = [
        quote[:len(quote)//2],
        quote[len(quote)//2:]
    ]
    
    # Create a slight flicker effect before the reveal
    for _ in range(3):
        sys.stdout.write("\033[H\033[J")
        print(color_text("...   ...", YELLOW))
        time.sleep(0.1)
        sys.stdout.write("\033[H\033[J")
        time.sleep(0.1)

    clear_screen()
    
    # Redraw thinker
    for line in thinking_man:
        print(color_text(line.center(60), CYAN))
    print("\n")

    # Print the box with the quote
    draw_frame("\n".join(quote_lines), width=65)
    
    print("\n")
    typewriter("— A voice from the void (probably)", 0.08, "\033[32m")
    
    # 4. Outro
    print("\n")
    time.sleep(1)
    print(color_text("Press Ctrl+C to succumb to the inevitable.", "90"))
    
    try:
        while True:
            # Subtle pulsing effect for the footer
            sys.stdout.write("\r" + color_text("... pondering ...", MAGENTA))
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\r" + " " * 20 + "\r")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\n\n{color_text('Even your exit is unplanned and slightly awkward.', RED)}")
        sys.exit()

if __name__ == "__main__":
    main()