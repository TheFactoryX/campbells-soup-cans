"""
Campbell's Soup Can #676
Produced: 2025-12-02 23:30:26
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter(text, color_code, delay=0.03):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote = [
        "  Life is absurd, but my absurdity somehow always",
        "  ends up being late to the cosmic joke. I once",
        "  missed eternity because subway directions were",
        "  unclear in the afterlife brochure."
    ]
    author = "  – Woody Allen's Neurotic Cousin"

    # ANSI color codes
    box_color = "1;31"  # bold red
    text_color = "1;33"  # bold yellow
    art_color = "1;36"  # bold cyan
    
    # Top box border
    print(f"\033[{box_color}m╭{'─' * 49}╮\033[0m")
    
    # Quote lines
    for line in quote:
        print(f"\033[{box_color}m│\033[0m", end="")
        typewriter(line, text_color)
        print(f"\033[{box_color}m│\033[0m", end=" ")
        print()
    
    # Author line
    print(f"\033[{box_color}m│\033[0m", end="")
    typewriter(author.rjust(49), "1;35")  # magenta
    print(f"\033[{box_color}m│\033[0m", end=" ")
    
    # Bottom box border
    print(f"\033[{box_color}m╰{'─' * 49}╯\033[0m")
    print()
    
    # ASCII art animation
    faces = [
        r"   o   ",
        r"  /|\  ",
        r"  / \  ",
        r"  ˰   ˰ ",
        r"  ‿   ‿ "
    ]
    
    for i in range(3):
        for frame in (0, 1):
            print("\033[F" * len(faces), end="")  # Move cursor up
            for line in faces:
                eye = "ಠ" if frame else "ó"
                face_line = line.replace("o", f" {eye} ", 1)
                print(f"\033[{art_color}m{face_line.center(50)}\033[0m")
            time.sleep(0.3)

if __name__ == "__main__":
    main()