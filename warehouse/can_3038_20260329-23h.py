"""
Campbell's Soup Can #3038
Produced: 2026-03-29 23:49:00
Worker: Inflection: Inflection 3 Productivity (inflection/inflection-3-productivity)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time

class WoodyAllenQuote:
    def __init__(self):
        self.quotes = [
            "When it comes to relationships, I'm not a complete failure. I once made love to a woman with a wooden leg. Well, she was great, but I was so nervous, I think I left my teeth in her purse.",
            "Eternity is a terrible idea. It's a never-ending staircase, and I'm just not that into cardio.",
            "The problem with immortality is that it's like being stuck in a bad marriage. You can't leave, and you can't kill yourself because you're already dead inside.",
            "I'm not afraid of death; I just don't want to be there when it happens. Or, you know, when it doesn't happen and I'm stuck in limbo, waiting for the WiFi to connect.",
            "Life is like a joke. You don't get it, and then you die laughing… or crying. Either way, you're going to end up with a wet face.",
        ]

    def print_quote(self, color):
        quote = random.choice(self.quotes)
        print(f"\033[{color}m{quote}\033[0m")

    def print_ascii_art(self):
        print("""
            _|_|    _|  _|            _|
            _|    _|_|  _|_|    _|  _|
            _|    _|  _|  _|  _|    _|
            _|    _|      _|  _|    _|
            _|_|    _|_|  _|    _|_|
        """)

    def animate_quote(self):
        print("\033[2J\033[H")  # Clear screen
        for color in range(90, 97):  # Print quote in different colors
            self.print_quote(color)
            time.sleep(0.2)  # Pause for animation

def main():
    woody = WoodyAllenQuote()
    woody.animate_quote()
    woody.print_ascii_art()

if __name__ == "__main__":
    main()