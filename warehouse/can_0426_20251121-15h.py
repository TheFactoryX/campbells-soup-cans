"""
Campbell's Soup Can #426
Produced: 2025-11-21 15:29:09
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

class WoodyQuoter:
    def __init__(self):
        self.colors = {
            'reset': '\033[0m',
            'red': '\033[91m',
            'blue': '\033[94m',
            'green': '\033[92m',
            'yellow': '\033[93m'
        }
        self.quote = "Why do we exist? \033[93mTo be here twenty-four hours a day wondering if we exist.\033[0m"
    
    def draw_box(self):
        box_top = f"{self.colors['red']}╔{'─' * 50}╗{self.colors['reset']}"
        box_mid = f"{self.colors['blue']}║{' ' * 50}║{self.colors['reset']}"
        box_bottom = f"{self.colors['red']}╚{'─' * 50}╝{self.colors['reset']}"
        return [box_top, box_mid, box_bottom]
    
    def animate_quote(self):
        box = self.draw_box()
        print("\n".join(box))
        print(f"{self.colors['green']}{' ' * 24}{self.quote}{' ' * 24}{self.colors['green']}")
        print("\n".join(box[1:3]))  # Re-print mid lines for animation
        
        while True:
            for color in [self.colors['red'], self.colors['yellow']]:
                print(f"\r{box[0]}")
                print(f"\r{box[1]}")
                print(f"\r{color}{' ' * 24}{self.quote}{' ' * 24}{color}")
                time.sleep(0.3)
                print("\r" + " " * 100, end="")  # Clear line

if __name__ == "__main__":
    WoodyQuoter().animate_quote()