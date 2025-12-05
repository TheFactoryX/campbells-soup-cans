"""
Campbell's Soup Can #741
Produced: 2025-12-05 23:30:12
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import textwrap

# ANSI escape codes for colors
GRAY = "\033[90m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

def typewriter(text, color=RESET, delay=0.03):
    """Print text with typewriter effect and specified color"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Woody Allen-style quote
    quote = "I'm plagued by existential dread, but what really keeps me up at night is whether I remembered to unplug the iron."
    attribution = "— Woody Allen"

    # ASCII art brain with thought bubble
    brain_art = rf"""
    {GRAY}           ____
         _[] /]{RESET}{BOLD}{BLUE}O{O}{RESET}{GRAY}
        |____| 
         /()\ 
        _\__/_{RESET}
    """

    # Build the thought bubble
    wrapped_text = textwrap.wrap(quote, width=40)
    max_width = max(len(line) for line in wrapped_text)
    bubble_top = " " + "_" * (max_width + 6)
    bubble_bottom = " " + "-" * (max_width + 6)

    # Clear screen and position cursor
    print("\033[H\033[J", end="")

    # Display ASCII art
    typewriter(brain_art, GRAY, 0.001)

    # Display thought bubble
    typewriter(bubble_top, BLUE, 0.005)
    for line in wrapped_text:
        padded_line = f"|  {line.center(max_width)}  |"
        typewriter(padded_line, BLUE, 0.02)
    typewriter(bubble_bottom, BLUE, 0.005)
    print()

    # Display attribution with fade-in effect
    att_lines = attribution.split("\n")
    for line in att_lines:
        for i in range(len(line)):
            sys.stdout.write(YELLOW + line[:i+1] + RESET)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(0.5)

if __name__ == "__main__":
    main()