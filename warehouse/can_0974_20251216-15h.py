"""
Campbell's Soup Can #974
Produced: 2025-12-16 15:36:27
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
from itertools import cycle

class WoodyAllenQuote:
    def __init__(self):
        # ANSI color codes
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'reset': '\033[0m'
        }
        
        # Woody Allen style quote
        self.quote = """I tried to find meaning in life, but then I realized it's like trying to find a parking spot in Manhattan—everyone's looking for the same thing, and by the time you find it, you're too exhausted to enjoy it."""
        
        # ASCII art border elements
        self.border = {
            'top': '╔' + '═' * 70 + '╗',
            'side': '║',
            'bottom': '╚' + '═' * 70 + '╝',
            'corner': ['╔', '╗', '╚', '╝']
        }
        
        # Animation states
        self.states = ['neurotic', 'anxious', 'existential', 'funny']
        self.state_cycle = cycle(self.states)
        self.current_state = next(self.state_cycle)
    
    def color_text(self, text, color):
        """Apply color to text using ANSI escape codes"""
        return f"{self.colors[color]}{text}{self.colors['reset']}"
    
    def print_frame(self, color):
        """Print a colored frame around the quote"""
        # Top border
        print(self.color_text(self.border['top'], color))
        # Quote line
        formatted_quote = f"{self.border['side']} {self.color_text(self.quote.center(68), color)} {self.border['side']}"
        print(formatted_quote)
        # Bottom border
        print(self.color_text(self.border['bottom'], color))
    
    def typewriter_effect(self, text, color, delay=0.02):
        """Print text character by character with a delay"""
        for char in text:
            sys.stdout.write(self.color_text(char, color))
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def display_state(self, state):
        """Display current mental state with ASCII art"""
        state_art = {
            'neurotic': r"""
   (°_o)
  /|o o|\
 / | ˉ | \
    ||||
    ||||
""",
            'anxious': r"""
    ~~~~
  ( o.o )
   > ^ <
   -----
""",
            'existential': r"""
    ?_?
   /|o|\
  / | | \
 /  | |  \
    ||||
""",
            'funny': r"""
    \o/
    (o.o)
   >  v  <
    ---
"""
        }
        
        print("\n" + self.color_text(state_art[state], 'yellow'))
        print(self.color_text(f"Woody Allen's {state} state:", 'cyan'))
    
    def run(self):
        """Main function to run the quote display"""
        # Clear screen
        print("\033[H\033[J", end="")
        
        # Title
        title = "WOODY ALLEN'S PHILOSOPHICAL MUSINGS"
        self.typewriter_effect(title.center(80), 'magenta', delay=0.03)
        
        # Display current state
        self.display_state(self.current_state)
        
        # Print the quote frame
        self.print_frame('cyan')
        
        # Subtitle with Woody Allen's name
        print("\n")
        self.typewriter_effect("                — Woody Allen", 'green')
        
        # Wait a bit before cycling to next state
        time.sleep(3)
        self.current_state = next(self.state_cycle)
        
        # Create a blinking effect for the exit message
        print("\n" * 3)
        for i in range(3):
            print("\r" + self.color_text("Press Ctrl+C to exit Woody Allen's mind...", 'red'), end="")
            time.sleep(0.5)
            print("\r" + " " * 50, end="")
            time.sleep(0.5)
        print("\n" + self.color_text("      (I'm not going anywhere, I'm just making you anxious)", 'yellow'))

if __name__ == "__main__":
    woody = WoodyAllenQuote()
    try:
        woody.run()
    except KeyboardInterrupt:
        print("\n" + woody.color_text("\nI was going to say something profound, but now I've forgotten...", 'magenta'))
        woody.typewriter_effect("                                 — Woody Allen, probably", 'green')