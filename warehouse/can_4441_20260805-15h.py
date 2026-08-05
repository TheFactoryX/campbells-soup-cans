"""
Campbell's Soup Can #4441
Produced: 2026-08-05 15:27:07
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
import math

def clear_screen():
    print("\033[H\033[J", end="")

def color_text(text, color_code):
    return f"\033[1;{color_code}m{text}\033[0m"

def animate_text(text, delay=0.05):
    """Prints text with a typewriter effect and subtle color shift."""
    colors = ["31", "33", "34", "35", "36"]
    for i, char in enumerate(text):
        sys.stdout.write(color_text(char, colors[i % len(colors)]))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width, height, quote):
    """Renders a neurotic, existential ASCII frame around the quote."""
    border_char = "░"
    corner_char = "╒"
    mid_char = "─"
    side_char = "│"
    bottom_char = "bottom"

    # Prepare the quote into lines
    lines = quote.split('\n')
    quote_width = max(len(line) for line in lines)
    
    # Add padding to quote width
    padding = 4
    content_width = quote_width + (padding * 2)
    
    # Frame dimensions
    frame_width = content_width + 2
    frame_height = len(lines) + 2

    # Top border
    print(color_text(corner_char + mid_char * (frame_width - 2) + corner_char, "37"))

    for i, line in enumerate(lines):
        # Left border
        sys.stdout.write(color_text(side_char, "37"))
        
        # Content line
        line_str = line.center(content_width)
        # Typewriter effect for the line
        for char in line_str:
            sys.stdout.write(color_text(char, "37"))
        
        # Right border
        sys.stdout.write(color_text(side_char, "37") + "\n")

    # Bottom border
    print(color_text(corner_char + mid_char * (frame_width - 2) + corner_char, "37"))

def neurotic_oscillation():
    """Simulates a nervous, vibrating text effect."""
    phrase = "I'm not afraid of the void; I'm just afraid the void will find me unprepared for its lack of conversational depth."
    
    print("\n" * 3)
    print(color_text("LOADING EXISTENTIAL DREAD...", "35"))
    time.sleep(1)
    
    for _ in range(3):
        sys.stdout.write("\r" + color_text("...", "33"))
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

def main():
    # The Woody Allen style quote
    woody_quote = (
        "I'm not afraid of the void; "
        "I'm just afraid the void will find me "
        "unprepared for its total lack of "
        "conversational depth."
    )

    clear_screen()
    neurotic_oscillation()
    
    # Draw the art
    draw_frame(80, 10, woody_quote)
    
    # Post-quote existential crisis
    print("\n")
    final_thoughts = [
        "(And besides, the void doesn't even have a good waiter.)",
        "(Is it too late to join a monastery? No, too much walking.)"
    ]
    
    for thought in final_thoughts:
        time.sleep(1.5)
        animate_text(thought, 0.03)

    print("\n" + color_text("--- END OF PROGRAM (UNLIKE LIFE) ---", "31"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[31mEven your exit is dreadfully predictable.\033[0m")