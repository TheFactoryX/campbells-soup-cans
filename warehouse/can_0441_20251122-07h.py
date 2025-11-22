"""
Campbell's Soup Can #441
Produced: 2025-11-22 07:27:52
Worker: Google: Gemini 2.0 Flash Experimental (free) (google/gemini-2.0-flash-exp:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def print_quote():
    quotes = [
        "I'm dating a schizophrenic. We go everywhere together. He doesn't.",
        "Eternal nothingness is fine, if you are dressed for it.",
        "Life is divided into the horrible and the miserable.",
        "Basically my wife was immature. I'd be at home in the bath and she'd come in and sink my boats.",
        "Eternity is very long, especially towards the end.",
        "If God exists, why is he so unhelpful?",
        "I'm not afraid of heights, have you seen my standards?",
        "My brain? It's my second favorite organ.",
        "I took a speed reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
        "What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet."
        ]

    quote = random.choice(quotes)

    colors = [
        "\033[31m",  # red
        "\033[32m",  # green
        "\033[33m",  # yellow
        "\033[34m",  # blue
        "\033[35m",  # magenta
        "\033[36m",  # cyan
        "\033[91m",  # Bright Red
        "\033[92m",  # Bright Green
        "\033[93m",  # Bright Yellow
        "\033[94m",  # Bright Blue
        "\033[95m",  # Bright Magenta
        "\033[96m"   # Bright Cyan
    ]
    reset_color = "\033[0m"

    border_color = random.choice(colors)
    text_color = random.choice(colors)
    while text_color == border_color:
          text_color = random.choice(colors)

    width = max(len(quote) + 6,40) # Minimum frame width

    print(border_color + "┏" + "━" * (width - 2) + "┓" + reset_color)
    print(border_color + "┃" + " " * (width - 2) + "┃" + reset_color)


    padding = (width - len(quote)-2) // 2
    quote_line = border_color +"┃"+ " " * padding + text_color + quote + reset_color + border_color+ " " * (width - len(quote) - 2 - padding) + "┃"+ reset_color
    print(quote_line)


    print(border_color + "┃" + " " * (width - 2) + "┃" + reset_color)
    print(border_color + "┗" + "━" * (width - 2) + "┛" + reset_color)

if __name__ == "__main__":
    print_quote()