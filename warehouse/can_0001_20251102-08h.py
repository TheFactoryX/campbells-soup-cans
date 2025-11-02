"""
Campbell's Soup Can #1
Produced: 2025-11-02 08:17:40
Worker: Google: Gemini 2.0 Flash Experimental (free) (google/gemini-2.0-flash-exp:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def animate_text(text, color_code):
    """Animates text with a color."""
    for char in text:
        print(f"\x1b[{color_code}m{char}\x1b[0m", end='', flush=True)
        time.sleep(0.05)  # Control the animation speed

def woody_allen_quote():
    """Prints a funny philosophical quote in Woody Allen's style."""

    quote = "I'm not sure if existence has meaning,\nbut I'm pretty sure my therapist's new boat does. \n...And that worries me."

    # Box drawing using unicode characters
    def draw_box(width, height, color_code):
        """Draws a box with specified width and height."""
        color_start = f"\x1b[{color_code}m"
        color_end = "\x1b[0m"
        print(color_start + "╔" + "═" * (width - 2) + "╗" + color_end)
        for _ in range(height - 2):
            print(color_start + "║" + " " * (width - 2) + "║" + color_end)
        print(color_start + "╚" + "═" * (width - 2) + "╝" + color_end)

    # Color codes for ANSI escape sequences
    COLOR_YELLOW = 93  # Bright yellow

    # Determine terminal width
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80 # Default width if detection fails

    box_width = min(terminal_width, 70) #cap box width to 70 or terminal size.
    box_height = 8

    import os

    draw_box(box_width, box_height, COLOR_YELLOW) #box around the quote

    # Center the quote in the box
    lines = quote.splitlines()
    padding = " " * max(0, (box_width - max(len(line) for line in lines)) // 2)  #Dynamically calculate padding
    
    for line in lines:
        centered_line = padding + line
        if len(centered_line)>box_width-2:
            centered_line=centered_line[:box_width-2] #truncate long lines
        
        print("\x1b[93m║" + " " + centered_line +" "*(box_width-2-len(centered_line)-1) + "║\x1b[0m")  # Ensure quote fits within box

    draw_box(box_width, box_height, COLOR_YELLOW)   #bottom of the box
    animate_text(" - A very sane individual (probably)", 36)  # Cyan color for the attribution
    print()

if __name__ == "__main__":
    woody_allen_quote()