"""
Campbell's Soup Can #2568
Produced: 2026-03-04 17:57:37
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
from itertools import cycle

def typewriter_effect(text, color_code, delay=0.03, end_char=''):
    for char in text:
        sys.stdout.write(f'\033[{color_code}m{char}\033[0m')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f'\033[0m{end_char}\n')

def print_colored_line(char, width=70, color=33):
    print(f'\033[{color}m{char * width}\033[0m')

def print_colored_sides(char, width=70, color=33, content='', left_padding=1, right_padding=1):
    content_width = len(content)
    padding = ' ' * ((width - content_width - left_padding - right_padding) // 2)
    line = f'\033[{color}m{char}{padding}{content}{padding}{char * (width - content_width - 2 * len(padding) - 2)}\033[0m'
    print(line)

def animated_quote(quote):
    # Split quote into parts for different colors
    parts = [
        ("I've been through analysis, but I still can't figure out why I worry ", 33),  # Yellow
        ("so much about dying. Maybe it's because I've spent so much time worrying ", 36),  # Cyan
        ("about life that I haven't had any time left to actually ", 35),  # Purple
        ("live it properly.", 32),  # Green
    ]
    
    for part, color in parts:
        typewriter_effect(part, color, 0.02)
        time.sleep(0.3)

def main():
    # Clear screen
    print("\033[2J\033[H", end='')
    
    # Animated title
    title = " Woody Allen's Philosophical Musings "
    subtitle = "  A Neurotic Take on Existence  "
    
    # Draw the frame
    print_colored_line('═', 80, 36)
    print_colored_sides('║', 80, 35, title, 0, 0)
    print_colored_sides('║', 80, 36, subtitle, 0, 0)
    print_colored_line('═', 80, 36)
    
    # The quote
    quote = "I've been through analysis, but I still can't figure out why I worry so much about dying. Maybe it's because I've spent so much time worrying about life that I haven't had any time left to actually live it properly."
    
    # Animated quote with different colors
    animated_quote(quote)
    
    # Footer
    footer = " - From the desk of a man who'd rather analyze than live -"
    typewriter_effect(footer, 35, 0.03)  # Purple text
    
    # Bottom decorative line
    print_colored_line('═', 80, 36)
    
    # Add a small ASCII art at the bottom with animation
    woody_faces = [
        [
            "   (o o)   ",
            "  / V \\   ",
            " /( _ )\\  ",
            "  ^^ ^^   ",
        ],
        [
            "   (o o)   ",
            "  / - \\   ",
            " /( _ )\\  ",
            "  ^^ ^^   ",
        ],
        [
            "   (o o)   ",
            "  / ^ \\   ",
            " /( _ )\\  ",
            "  ^^ ^^   ",
        ]
    ]
    
    # Animate the face
    for _ in range(3):
        for face in woody_faces:
            for line in face:
                typewriter_effect(line, 36, 0.01)
            time.sleep(0.5)
            # Move cursor up 4 lines
            sys.stdout.write("\033[4A")
        # Clear the face area
        sys.stdout.write("\033[J")
        time.sleep(0.3)
    
    # Final Woody face
    for line in woody_faces[0]:
        typewriter_effect(line, 36, 0.01)

if __name__ == "__main__":
    main()