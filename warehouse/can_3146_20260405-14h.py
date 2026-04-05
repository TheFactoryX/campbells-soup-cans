"""
Campbell's Soup Can #3146
Produced: 2026-04-05 14:54:20
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_centered(text, width=70):
    padding = (width - len(text)) // 2
    return " " * padding + text

def print_typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def quote_box():
    # ASCII art frames with colors
    top_border = color_text("╔" + "═" * 68 + "╗", "36")
    bottom_border = color_text("╚" + "═" * 68 + "╝", "36")
    side_border = color_text("║", "36")
    
    # Woody Allen styled quote
    quote = color_text("I'm not afraid of death, I'm just afraid that my", "33")
    quote2 = color_text("afterlife will be spent in a small apartment", "33")
    quote3 = color_text("with bad acoustics and an eternal critic", "33")
    quote4 = color_text("who keeps asking me 'what's your point?'", "33")
    
    # Signature
    signature = color_text("- Woody Allen", "35")
    
    # Title
    title = color_text("WOODY ON LIFE", "31;1")
    
    # Animation sequence
    frames = [
        [top_border],
        [side_border + color_text("  ".center(68), "36") + side_border],
        [side_border + color_text("  ".center(68), "32") + side_border],
        [side_border + color_text("  ".center(68), "36") + side_border],
        [side_border + color_text("  ".center(68), "32") + side_border],
        [side_border + color_text("  ".center(68), "36") + side_border],
        [side_border + print_centered(title, 68) + side_border],
        [side_border + color_text("  ".center(68), "36") + side_border],
        [side_border + print_centered(quote, 68) + side_border],
        [side_border + print_centered(quote2, 68) + side_border],
        [side_border + print_centered(quote3, 68) + side_border],
        [side_border + print_centered(quote4, 68) + side_border],
        [side_border + color_text("  ".center(68), "36") + side_border],
        [side_border + print_centered(signature, 68) + side_border],
        [side_border + color_text("  ".center(68), "36") + side_border],
        [bottom_border]
    ]
    
    # Print animated frames
    for frame in frames:
        for line in frame:
            print(line)
        time.sleep(0.1)
    
    # Add a subtle pulsing effect
    for i in range(5):
        sys.stdout.write("\033[?25l")  # Hide cursor
        sys.stdout.write("\033[H")    # Move cursor to top
        for frame in frames:
            for line in frame:
                print(line)
        time.sleep(0.5)
        
        # Dim the text
        dimmed_top_border = color_text("╔" + "═" * 68 + "╗", "36;2")
        dimmed_bottom_border = color_text("╚" + "═" * 68 + "╝", "36;2")
        dimmed_side_border = color_text("║", "36;2")
        dimmed_quote = color_text("I'm not afraid of death, I'm just afraid that my", "33;2")
        dimmed_quote2 = color_text("afterlife will be spent in a small apartment", "33;2")
        dimmed_quote3 = color_text("with bad acoustics and an eternal critic", "33;2")
        dimmed_quote4 = color_text("who keeps asking me 'what's your point?'", "33;2")
        dimmed_signature = color_text("- Woody Allen", "35;2")
        dimmed_title = color_text("WOODY ON LIFE", "31;1;2")
        
        dimmed_frames = [
            [dimmed_top_border],
            [dimmed_side_border + color_text("  ".center(68), "36;2") + dimmed_side_border],
            [dimmed_side_border + print_centered(dimmed_title, 68) + dimmed_side_border],
            [dimmed_side_border + print_centered(dimmed_quote, 68) + dimmed_side_border],
            [dimmed_side_border + print_centered(dimmed_quote2, 68) + dimmed_side_border],
            [dimmed_side_border + print_centered(dimmed_quote3, 68) + dimmed_side_border],
            [dimmed_side_border + print_centered(dimmed_quote4, 68) + dimmed_side_border],
            [dimmed_side_border + print_centered(dimmed_signature, 68) + dimmed_side_border],
            [dimmed_bottom_border]
        ]
        
        for frame in dimmed_frames:
            for line in frame:
                print(line)
        time.sleep(0.5)
    
    sys.stdout.write("\033[?25h")  # Show cursor

if __name__ == "__main__":
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Print the quote box animation
    quote_box()
    
    # Final thought
    print("\n")
    print_centered(color_text("Perhaps that's why he makes so many movies...", "37;2"))
    print_centered(color_text("He's trying to find the point before the critic does.", "37;2"))