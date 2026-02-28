"""
Campbell's Soup Can #2479
Produced: 2026-02-28 08:45:16
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, sys

def moving_text(text, delay=0.07):
    """Display text one character at a time with carriage return."""
    for i in range(len(text)):
        sys.stdout.write('\r' + text[:i+1])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def colored(text, fg=94, bg=46):
    """Wrap text in ANSI color codes."""
    return f"\033[{bg};{fg}m{text}\033[0m"

def ascii_woody():
    """A tiny ASCII doodle of Woody's silhouette."""
    return """
   __
  / _\   ___
 / /_| | / |
|___   | /|
     __/
"""

def draw_box(colored_text):
    """Print a simple box around the colored quote."""
    width = len(colored_text) + 4
    border = '+'
    line = '-' * width
    print(f"{border}{line}{border}")
    print(f"|{colored_text.center(width)}|")
    print(f"{border}{line}{border}")

def main():
    # Header animation
    moving_text("W O O D Y   A L L E N   Q U O T E")
    
    # ASCII illustration
    sys.stdout.write("\n")
    print(ascii_woody())
    
    # Woody Allen style philosophical quote
    raw_quote = "I'm not afraid of death; I just don't want to be there when it happens."
    colored_quote = colored(raw_quote, fg=94, bg=46)
    draw_box(colored_quote)

    # Keep the window open
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()