"""
Campbell's Soup Can #1650
Produced: 2026-01-16 17:39:45
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
from os import name as os_name, system

def clear_screen():
    if os_name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def typewriter_effect(text, delay=0.05, color_code='\033[0m'):
    for char in text:
        sys.stdout.write(char + color_code)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woodey(animation_frame=0):
    # Slight head movement animation
    head_offset = " " * (animation_frame % 2)
    
    # Simple Woody Allen ASCII art (glasses and neurotic posture)
    print("\033[38;5;95m" + head_offset + "    .-.")
    print("\033[38;5;95m" + head_offset + "   ( oo )")
    print("\033[38;5;95m" + head_offset + "   /|\\|\\")
    print("\033[38;5;95m" + head_offset + "  / \\ ~ \\")
    print("\033[38;5;95m" + head_offset + " |   X   |")
    print("\033[38;5;95m" + head_offset + " |   |   |")
    print("\033[38;5;95m" + head_offset + " |   |   |")
    print("\033[38;5;95m" + head_offset + " /   |   \\")
    print("\033[38;5;95m" + head_offset + "/_________\\")
    print("\033[38;5;95m" + head_offset + "    | |")

def draw_thought_bubble():
    print("\033[38;5;15m      .-.")
    print("\033[38;5;15m     (   )")
    print("\033[38;5;15m      '-'")
    print("\033[38;5;15m       |")
    print("\033[38;5;15m       |")
    print("\033[38;5;15m       |")
    print("\033[38;5;15m      / \\")
    print("\033[38;5;15m     /   \\")
    print("\033[38;5;15m    /     \\")
    print("\033[38;5;15m   /       \\")
    print("\033[38;5;15m  /         \\")

def print_quote():
    # Title with animation
    title = "\033[1;38;5;208mTHE WOODY ALLEN GUIDE TO EXISTENTIAL CRISES\033[0m"
    
    # Animation sequence
    for i in range(3):
        clear_screen()
        print("\n" * 2)
        typewriter_effect(title.center(80), 0.03, "\033[1;38;5;208m")
        draw_woodey(i)
        time.sleep(0.5)
    
    # Final screen
    clear_screen()
    print("\n" * 2)
    typewriter_effect(title.center(80), 0.03, "\033[1;38;5;208m")
    
    # Decorative line
    print("\033[38;5;208m" + "=" * 80 + "\033[0m")
    
    # Woody ASCII art with thought bubble
    draw_thought_bubble()
    draw_woodey(0)  # Initial Woody without animation
    
    # The quote with typewriter effect
    quote_text = "I tried to be a philosopher once, but I couldn't make ends meet. Now I just stare at my navel and worry about the meaninglessness of it all while eating a pastrami sandwich on rye."
    
    # Create a box for the quote
    box_width = 70
    padding = (80 - box_width) // 2
    
    print("\n\033[38;5;15m" + " " * padding + "+" + "-" * box_width + "+\033[0m")
    
    # Split the quote into lines that fit in the box
    words = quote_text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + ' ' + word) <= box_width - 4:
            current_line += (' ' if current_line else '') + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Print each line with typewriter effect and alternating colors
    colors = ["\033[3;38;5;15m", "\033[3;38;5;225m"]
    for i, line in enumerate(lines):
        color_code = colors[i % len(colors)]
        typewriter_effect(" " * padding + "| " + line + " " * (box_width - 4 - len(line)) + "|", 0.01, color_code)
    
    print("\033[38;5;15m" + " " * padding + "+" + "-" * box_width + "+\033[0m")
    
    # Decorative line
    print("\033[38;5;208m" + "=" * 80 + "\033[0m")
    
    # Footer
    footer = "\033[3;38;5;95m- Woody Allen, probably worrying about something else now -\033[0m"
    typewriter_effect(footer.center(80), 0.03, "\033[3;38;5;95m")
    
    # Simple pause at the end
    print("\n\033[3;38;5;208m(Press Enter to exit)\033[0m")
    input()

if __name__ == "__main__":
    clear_screen()
    print_quote()