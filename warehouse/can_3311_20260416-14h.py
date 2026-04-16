"""
Campbell's Soup Can #3311
Produced: 2026-04-16 14:14:08
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def woody_allen_quote():
    # ANSI color codes
    colors = {
        'red': '91',
        'yellow': '93',
        'blue': '94',
        'green': '92',
        'magenta': '95',
        'cyan': '96',
        'white': '97'
    }
    
    # Woody Allen style quote
    quote = "I tried to find the meaning of life, but I kept getting distracted by existential dread and the fact that I forgot to buy milk."
    
    # Animation cycle
    color_sequence = ['red', 'yellow', 'blue', 'green', 'magenta', 'cyan']
    
    for i in range(15):  # Animate 15 times
        clear_screen()
        
        # Apply current color
        current_color = colors[color_sequence[i % len(color_sequence)]]
        
        # Create a pulsing effect by varying the border
        pulse = abs(i % 6 - 3)  # Creates a 0-3-2-1-0-1-2 pattern
        border_char = "═" * (76 + pulse)
        
        # Print the framed quote with animation
        print(colored_text("╔" + border_char + "╗", current_color))
        print(colored_text("║", current_color))
        
        # Split quote into lines for better formatting
        words = quote.split()
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            if len(' '.join(current_line)) > 60:
                lines.append(' '.join(current_line))
                current_line = []
        if current_line:
            lines.append(' '.join(current_line))
            
        # Print quote lines with color variation
        for j, line in enumerate(lines):
            # Create a pulsing effect
            line_color = colors[color_sequence[(i + j + pulse) % len(color_sequence)]]
            padding = " " * (76 + pulse - len(line) - 2)
            print(colored_text(f"║ {line}{padding} ║", line_color))
            
        print(colored_text("║", current_color))
        print(colored_text("╚" + border_char + "╝", current_color))
        
        # Add a subtitle with color variation
        subtitle = " - Woody Allen, probably procrastinating"
        subtitle_color = colors[color_sequence[(i + 3) % len(color_sequence)]]
        print(colored_text(f"\n{subtitle.center(76 + pulse)}", subtitle_color))
        
        # Add a "thinking" animation
        thought_bubbles = ["○", "◔", "◑", "◕", "●"]
        thought_text = f"{thought_bubbles[i % len(thought_bubbles)]} Contemplating existence..."
        thought_color = colors[color_sequence[(i + 5) % len(color_sequence)]]
        print(colored_text(thought_text.center(76 + pulse), thought_color))
        
        time.sleep(0.3)  # Pause between color changes

if __name__ == "__main__":
    woody_allen_quote()