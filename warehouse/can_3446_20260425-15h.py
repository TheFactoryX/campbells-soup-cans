"""
Campbell's Soup Can #3446
Produced: 2026-04-25 15:56:13
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter(text, delay=0.02, color="\033[93m"):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write("\033[0m")

def sparkle(text, color_code):
    result = ""
    for c in text:
        if c == " ":
            result += " "
        else:
            result += f"\033[{color_code}m{c}\033[0m" if random.random() > 0.3 else f"\033[97;1m{c}\033[0m"
    return result

def main():
    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    
    # ASCII doodle of a neurotic brain
    brain = [
        "        (__)       ",
        "        (oo)____   ",
        "       /  /    \\\\  ",
        "      / |    | \\\\ ",
        "     *  ||----||  *",
        "        ^^  ^^     "
    ]
    
    # Animate brain with colors
    colors = [91, 93, 95, 92, 94, 96]
    for frame in range(3):
        sys.stdout.write("\033[5;10H")
        for i, line in enumerate(brain):
            sys.stdout.write(f"\033[{colors[(i+frame)%len(colors)]}m{line}\\033[0m\\n")
            sys.stdout.write("\\033[1A" if i < len(brain)-1 else "")
        sys.stdout.flush()
        time.sleep(0.4)
    
    # Quote box
    quote = "I finally realized that my entire existence is just God's way of procrastinating on His own mortality."
    
    # Build decorative frame
    width = len(quote) + 6
    top = "╭" + "─" * (width - 2) + "╮"
    bottom = "╰" + "─" * (width - 2) + "╯"
    
    # Center on screen
    sys.stdout.write("\\n\\n")
    
    # Animate reveal
    sys.stdout.write("\\033[48;5;235m\\033[97m  " + " " * (width - 4) + "  \\033[0m\\n")
    
    typewriter("\\033[48;5;235m\\033[97m╭" + "─" * (width - 2) + "╮\\033[0m\\n", 0.01)
    typewriter("\\033[48;5;235m\\033[97m│  \\033[0m", 0.01)
    
    # The quote itself, with sparkling effect
    for c in quote:
        sys.stdout.write(sparkle(c, random.choice([91, 93, 95, 92])))
        sys.stdout.flush()
        time.sleep(0.03)
    
    typewriter("\\033[48;5;235m\\033[97m  │\\033[0m\\n", 0.01)
    typewriter("\\033[48;5;235m\\033[97m╰" + "─" * (width - 2) + "╯\\033[0m\\n", 0.01)
    
    # Signature with twinkling effect
    sys.stdout.write("\\n")
    sig = "   — Woody Allen (probably, while overthinking a bagel)"
    for i, c in enumerate(sig):
        col = 90 if i < 3 else (random.choice([240, 242, 244, 246]) if random.random() > 0.7 else 250)
        sys.stdout.write(f"\\033[38;5;{col}m{c}")
        sys.stdout.flush()
        time.sleep(0.02)
    
    # Twinkling stars footer
    sys.stdout.write("\\n\\n")
    stars = ["✦", "✧", "★", "✩", "✪", "✫"]
    for _ in range(40):
        star = random.choice(stars)
        col = random.choice([196, 202, 208, 214, 220, 226, 46, 51, 81, 159])
        sys.stdout.write(f"\\033[38;5;{col}m{star}\\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    
    sys.stdout.write("\\n\\n\\033[0m")

if __name__ == "__main__":
    main()