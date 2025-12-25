"""
Campbell's Soup Can #1177
Produced: 2025-12-25 20:35:37
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
from itertools import cycle

def color_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write('\n')

def draw_line(char, color, length=50):
    print(color_text(char * length, color))

def main():
    # Title
    draw_line('=', 'yellow')
    print(color_text("        PHILOSOPHY BY WOODY        ", 'cyan'))
    draw_line('=', 'yellow')
    
    # Decorative ASCII art
    print(color_text("""
      .--.
     |o_o |
     |:_/ |
    //   \\ \
   (|     | )
   /'\_   _/`\\
   \\___)=(___/
    """, 'green'))
    
    # Animated quote with different colors
    quote = "I'm not afraid of death; I just don't want to be there when it happens. I figure it's like showing up to a party where you weren't invited, everyone's already drunk, and you have to bring your own snacks. Rude, really."
    
    # Color cycling for extra visual interest
    colors = ['red', 'yellow', 'blue', 'magenta', 'cyan']
    color_cycle = cycle(colors)
    
    # Add some dramatic pauses
    type_text("\n" + color_text("WOODY:", 'white') + " ", 0.05)
    time.sleep(0.5)
    
    # Main quote with color changes
    for word in quote.split():
        color = next(color_cycle)
        type_text(color_text(word + ' ', color), 0.03)
    
    # Decorative ending
    time.sleep(1)
    draw_line('-', 'cyan')
    print(color_text("       Existential blues...       ", 'blue'))
    draw_line('-', 'blue')
    
    # Woody Allen signature
    time.sleep(0.5)
    type_text(color_text("\n   - Woody, probably worrying about something else\n", 'yellow'), 0.05)

if __name__ == "__main__":
    main()