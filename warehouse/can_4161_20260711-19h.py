"""
Campbell's Soup Can #4161
Produced: 2026-07-11 19:31:41
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def woody_allen_quote():
    quote = ("I used to fear death.\n"
             "Now I worry the afterlife has no WiFi.\n"
             "How will I stream my existential dread?\n"
             "What if the customer service is run by my ex?")
    
    colors = [
        "\033[95m",  # Magenta
        "\033[94m",  # Blue
        "\033[96m",  # Cyan
        "\033[92m",  # Green
    ]
    
    # Create animated typing effect
    def animate_text(text, color_index):
        for char in text:
            print(f"{colors[color_index]}{char}\033[0m", end='', flush=True)
            time.sleep(0.03)
        print()
    
    # Print decorative border
    width = 50
    print("\n\033[93m" + "═" * width + "\033[0m")
    print("\033[93m║\033[0m" + " " * (width - 2) + "\033[93m║\033[0m")
    
    # Print animated quote
    for i, line in enumerate(quote.split('\n')):
        color = (i * 2) % len(colors)
        print("\033[93m║\033[0m ", end='')
        animate_text(line.ljust(width - 4), color)
    
    print("\033[93m" + "═" * width + "\033[0m\n")

if __name__ == "__main__":
    woody_allen_quote()