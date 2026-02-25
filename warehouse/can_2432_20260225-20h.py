"""
Campbell's Soup Can #2432
Produced: 2026-02-25 20:54:55
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def type_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_border(width, height):
    border_color = color_text("", "36")
    horizontal_line = color_text("╔" + "═" * (width - 2) + "╗", "36")
    vertical_line = color_text("║" + " " * (width - 2) + "║", "36")
    bottom_line = color_text("╚" + "═" * (width - 2) + "╝", "36")
    
    print(horizontal_line)
    for _ in range(height):
        print(vertical_line)
    print(bottom_line)

def main():
    clear_screen()
    
    # Woody Allen style quote
    quote = "You know, I'm not afraid of death. I just don't want to be there when it happens. " \
            "It's like waiting for a bus that never comes - except this bus takes you to " \
            "nowhere and the fare is your entire life savings. And they don't even give " \
            "you change back!"
    
    # Split quote into lines for better formatting
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        if len(' '.join(current_line)) > 60:
            lines.append(' '.join(current_line[:-1]))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # Set up the display
    width = 70
    height = 10
    
    # Title
    title = color_text("WOODY ALLEN ON LIFE AND DEATH", "35;1")
    title = title.center(width)
    
    # Animation sequence
    type_effect(title, 0.02)
    time.sleep(0.5)
    
    # Draw border
    draw_border(width, height)
    
    # Print quote with color effects
    y_offset = 1
    for i, line in enumerate(lines):
        # Alternate colors for visual interest
        if i % 2 == 0:
            colored_line = color_text(line, "33;1")  # Yellow
        else:
            colored_line = color_text(line, "34")  # Blue
        
        # Center the line in the box
        centered_line = colored_line.center(width - 4)
        # Position the line in the box
        print("\033[36m║\033[0m " + centered_line + f" \033[36m║\033[0m")
    
    # Bottom border
    bottom_line = color_text("╚" + "═" * (width - 2) + "╝", "36")
    print(bottom_line)
    
    # Add a funny attribution
    time.sleep(1)
    attribution = color_text("   - Woody Allen (probably)", "32")
    type_effect(attribution, 0.05)
    
    # Add a final animated thought
    time.sleep(1)
    final_thought = color_text("...or maybe he just forgot to say it.", "37;3")
    type_effect(final_thought, 0.05)
    
    # Blinking cursor effect
    for i in range(3):
        sys.stdout.write("\r" + color_text("Press ENTER to continue... ", "32;5"))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r" + " " * 30 + "\r")
        sys.stdout.flush()
        time.sleep(0.5)
    
    input()

if __name__ == "__main__":
    main()