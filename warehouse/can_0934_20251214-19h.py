"""
Campbell's Soup Can #934
Produced: 2025-12-14 19:26:49
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
    """Prints a funny, neurotic philosophical quote in Woody Allen's style with visual flair."""

    quote = "🦋 I'm dating a nymphomaniac. The upside: great sex. The downside: she's seeing four other shrinks. 🤔 Is there even OBJECTIVE reality? Or just REALLY well-lit anxiety? 💀"
    colors = ["\033[31m", "\033[33m", "\033[32m", "\033[34m", "\033[35m", "\033[36m", "\033[91m", "\033[93m", "\033[92m", "\033[94m", "\033[95m", "\033[96m"]
    reset = "\033[0m"

    box_width = max(len(line) for line in quote.splitlines()) + 4 # +4 for padding

    top_border = "╔" + "═" * (box_width - 2) + "╗"
    bottom_border = "╚" + "═" * (box_width - 2) + "╝"

    print(random.choice(colors) + top_border + reset)
    for line in quote.splitlines():
        padding = " " * ((box_width - len(line) - 2) // 2)
        colored_line = random.choice(colors) + "║ " + padding + line + padding + " ║" + reset
        #Adjust padding for lines where the difference results in one extra space
        if (box_width - len(line) - 2) % 2 != 0: 
            colored_line = colored_line.replace(" ║", "  ║")
        print(colored_line)
    print(random.choice(colors) + bottom_border + reset)

if __name__ == "__main__":
    print_quote()