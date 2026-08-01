"""
Campbell's Soup Can #4401
Produced: 2026-08-01 18:13:11
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
import math

def clear():
    print("\033[H\033[J", end="")

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def animate_typewriter(text, delay=0.05, color="\033[37m"):
    """Prints text with a neurotic, stuttering typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        # Simulate neurotic hesitation
        if char == "," or char == ";" or char == ":":
            time.sleep(delay * 5)
        else:
            time.sleep(delay)
    print()

def draw_frame(text_lines, width=70):
    """Draws a neurotic-looking box around the text."""
    top_bottom = color_text("┌" + "─" * (width - 2) + "┐", "\033[90m")
    bottom = color_text("└" + "─" * (width - 2) + "┘", "\033[90m")
    
    print(top_bottom)
    for line in text_lines:
        # Center text within the frame
        padding = (width - len(line) - 2) // 2
        if padding > 0:
            print(f"{color_text('│', '\033[90m')}{' ' padding}{line}{' ' (width - len(line) - padding - 2)}{color_text('│', '\033[90m')}")
        else:
            print(f"{color_text('│', '\033[90m'){line.ljust(width-2)}{color_text('│', '\033[90m')}")
    print(bottom)

def neurosis_effect():
    """Creates a flickering, jittery background effect."""
    colors = ["\033[31m", "\033[33m", "\033[35m", "\033[36m"]
    for _ in range(15):
        time.sleep(0.1)
        sys.stdout.write("\033[H") # Reset cursor to top
        print(color_text("   ..Existential Dread Loading...", "\033[90m"))
        print(f"   {colors[_ % 4]}*jitter*")
        time.sleep(0.05)

def main():
    # The Woody Allen Style Quote
    quote = (
        "I once had a profound realization about the universe, "
        "but then I remembered that I have a massive sinus infection "
        "and my perception of reality is likely just nasal congestion."
    )
    
    quote_parts = [
        "\"I once had a profound realization about the universe,",
        "but then I remembered that I have a massive sinus",
        "infection and my perception of reality is likely",
        "just nasal congestion.\""
    ]

    clear()
    
    # 1. The intro animation
    neurosis_effect()
    time.sleep(0.5)
    clear()

    # 2. The Big Reveal
    print("\n" * 2)
    
    # Creating a "shaky" frame effect via a loop
    for _ in range(3):
        # Visual flicker/jitter effect
        clear()
        print("\n" * 3)
        print(color_text("   [ INTERNAL MONOLOGUE DETECTED ]", "\033[94m"))
        print("\n")
        
        # Animation of the text being typed into a frame
        animate_typewriter(quote_parts[0], 0.06, "\033[93m")
        animate_typewriter(quote_parts[1], 0.06, "\033[93m")
        animate_typewriter(quote_parts[2], 0.06, "\033[93m")
        animate_typewriter(quote_parts[3], 0.06, "\033[95m")
        
        time.sleep(1)
        clear()
        
        # Final polished presentation
        print("\n" * 4)
        # Draw stylized frame around the final text
        final_lines = [
            "\"I once had a profound realization about",
            "the universe, but then I remembered that",
            "I have a massive sinus infection and my",
            "perception of reality is likely just",
            "nasal congestion.\""
        ]
        draw_frame(final_lines, 55)
        print("\n" + color_text("   — Woody Python (Existential Edition)", "\033[90m"))
        break

    # Final pause for dramatic/neurotic effect
    time.sleep(3)
    print("\n" + color_text("   [ End of stream. Go take an aspirin. ]", "\033[90m"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEven the user is fleeing from the absurdity of existence.")