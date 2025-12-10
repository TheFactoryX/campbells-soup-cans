"""
Campbell's Soup Can #840
Produced: 2025-12-10 13:49:52
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def typewriter(text, speed=0.05, color_start=None, color_end=None):
    if color_start and color_end:
        r1, g1, b1 = color_start
        r2, g2, b2 = color_end
        steps = len(text)
        for i, char in enumerate(text):
            r = int(r1 + (r2 - r1) * i / steps)
            g = int(g1 + (g2 - g1) * i / steps)
            b = int(b1 + (b2 - b1) * i / steps)
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}")
            sys.stdout.flush()
            time.sleep(speed if char not in [' ', '\n'] else speed*0.2)
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed if char not in [' ', '\n'] else speed*0.2)

def main():
    quote = (
        "The universe is expanding at an alarming rate,\n"
        "which really makes you wonder - \n"
        "why does my therapist still charge by the hour?\n"
        "I mean, if space itself isn't worth more per cubic foot,\n"
        "why should my existential dread be?\n"
        "\n"
        "                          - Woody Allen probably never said this"
    )

    # Box dimensions
    lines = quote.split('\n')
    max_width = max(len(line) for line in lines)
    box_width = max_width + 8

    # Rainbow box top
    print(f"\033[37m╔{'═' * (box_width - 2)}╗")

    # Motivated/panicked scribbles around text
    scribbles = ['※', '✺', '⁕', '✤', 'ꙮ', '⁂']
    for line in lines:
        colored_scribble = f"\033[38;2;{random.randint(150,255)};{random.randint(0,100)};{random.randint(0,100)}m{random.choice(scribbles)}\033[0m"
        print(f"\033[37m║{colored_scribble}  ", end='')
        typewriter(line.ljust(max_width), 
                   color_start=(255, 223, 0),   # Start with golden yellow
                   color_end=(255, 255, 255))   # End with white
        print(f"  {colored_scribble}\033[37m║")

    # Rainbow box bottom (different color per character)
    print(f"╚{'═' * (box_width - 2)}╝\033[0m\n")
    for char in ' ' * 15 + "Now panic appropriately.":
        sys.stdout.write(f"\033[38;2;{random.randint(50,255)};{random.randint(50,255)};{random.randint(50,255)}m{char}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\033[0m")

if __name__ == "__main__":
    main()