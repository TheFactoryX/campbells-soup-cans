"""
Campbell's Soup Can #3988
Produced: 2026-06-22 12:25:54
Worker: Mistral: Ministral 3 8B 2512 (mistralai/ministral-8b-2512)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
from itertools import cycle

# ANSI color codes for fun
COLORS = cycle([
    '\033[91m',  # Red
    '\033[93m',  # Yellow
    '\033[96m',  # Cyan
    '\033[94m',  # Blue
    '\033[92m',  # Green
    '\033[95m',  # Magenta
    '\033[0m'    # Reset
])

# ASCII art for Woody Allen's face (simplified)
WOODY_ASCII = r"""
   _______
  /       \
 |   O   O |
 |    ∆    |
 |  (   )  |
  \_______/
   |   |   |
   |___|___|
"""

# Neurotic typing animation
def neurotic_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.8, 1.2))
    print()

# Boxed quote with color
def woody_box(quote):
    color = next(COLORS)
    reset = '\033[0m'

    # Top border
    print(color + '┌' + '─' * (len(quote) + 4) + '┐' + reset)

    # Quote with padding
    print(color + '│ ' + ' ' * 2 + quote + ' ' * 2 + ' │' + reset)

    # Bottom border
    print(color + '└' + '─' * (len(quote) + 4) + '┘' + reset)

# Woody Allen's existential rant
def woody_rant():
    rants = [
        "I don't want to achieve immortality through my work; I want to achieve it through not dying. But I'm not sure that's possible anymore.",
        "I'm not afraid of death; I just don't want to be there when it happens. And I don't want to be here when it happens either.",
        "Life is like a movie, but the plot is terrible and the acting is even worse. And I'm in it, which is the worst part.",
        "I used to be indecisive, but now I'm just confused. It's a bit like being lost in a maze, but the maze is also lost.",
        "I don't know what I think about anything, but I think about it a lot. And that's probably why I'm so unhappy.",
        "I'm not paranoid, I'm just looking at the world through a lens that's been slightly scratched by existential dread.",
        "I don't want to be remembered as a genius, just as someone who tried really hard to be normal. And failed.",
        "I'm not saying I'm depressed, I'm just saying I'm in a phase where I'm questioning everything, including my own sanity.",
        "I don't know if I believe in God, but I sure as hell believe in therapy. And coffee. And therapy with coffee.",
        "I'm not afraid of the dark, I'm afraid of the light because it reveals all the things I don't want to see."
    ]

    # Pick a random rant
    rant = random.choice(rants)

    # Print Woody's face with a little animation
    for _ in range(3):
        print(next(COLORS) + WOODY_ASCII + next(COLORS))
        time.sleep(0.3)

    # Print the rant with neurotic typing
    print("\n" + next(COLORS) + "=" * 50 + next(COLORS))
    neurotic_print("A WOODY ALLEN THOUGHT EXPERIMENT:")
    print("\n" + next(COLORS) + "=" * 50 + next(COLORS) + "\n")

    # Print the boxed quote
    woody_box(rant)

    # Add a little existential afterthought
    print("\n" + next(COLORS) + "P.S." + next(COLORS) + " I just realized I might be overthinking this quote too.")
    print(next(COLORS) + "But then again, what's the alternative?" + next(COLORS))

# Main program
if __name__ == "__main__":
    woody_rant()