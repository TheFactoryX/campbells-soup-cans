"""
Campbell's Soup Can #2125
Produced: 2026-02-08 20:44:23
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen inspired existential quote printer.
Prints a single humorous quote using ANSI colors, borders, and a scrolling marquee.
"""

import sys
import time
import random

# Bright foreground colors (256‑color palette)
FG_COLORS = [90, 91, 92, 93, 94, 95, 96, 97]

def draw_border(text):
    """Prints a simple framed box around the given text."""
    WIDTH = 80
    border_top = "╔" + "=" * WIDTH + "╗"
    border_mid = "║" + " " * WIDTH + "║"
    border_bottom = "╚" + "=" * WIDTH + "╝"
    print(f"\033[38;5;95m{border_top}\n{border_mid}\n{border_bottom}\033[0m")
    print(text)
    print(f"\033[38;5;95m{border_mid}\n{border_bottom}\033[0m")

def scrolling_quote(quote):
    """Animates the quote by scrolling it from right to left."""
    quote_len = len(quote)
    travel_distance = quote_len + 150
    speed = 0.017   # ~58 FPS
    for offset in range(travel_distance + 1):
        spaces = travel_distance - offset
        fg = random.choice(FG_COLORS)
        color_code = f"\033[38;5;{fg}m"
        sys.stdout.write(f"\r{color_code}{' ' * spaces}{quote}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\r\033[0m")

def main():
    # Intro ascii art
    print("\n\033[38;5;226m", end="")
    intro_art = """
╔════════════════════════════════════════════════════════════════════════╗
║                     * * * * * * * * * * * * * * * * * * * * *       ║
╚════════════════════════════════════════════════════════════════════════╝
"""
    print(intro_art)
    print("\033[0m")
    
    # Woody Allen quote (single line)
    woody_quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Scroll the quote for a few seconds
    scrolling_quote(woody_quote)
    
    # Stable version inside a fancy box
    draw_border(woody_quote)
    
    # Outro
    print("\n\033[38;5;95mThanks for pondering the absurdities of existence.\033[0m\n\033[38;5;97m── Upstage AI ──\033[0m")

if __name__ == "__main__":
    main()