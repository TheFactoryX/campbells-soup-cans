"""
Campbell's Soup Can #402
Produced: 2025-11-20 13:41:51
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
import sys

def print_quote():
    quotes = [
        "I'm not sure if the universe is expanding, or if my apartment is just getting smaller. Either way, I need more closet space.",
        "Existential angst is just anxiety with bigger words. And slightly better posture. Maybe.",
        "The meaning of life? Probably something to do with avoiding phone calls and definitely not gluten.",
        "I tried being optimistic once. It was exhausting. I needed a nap and a therapist.",
        "I asked my psychiatrist if I was crazy. He said, 'Not yet, but you're close.' Which I think means he's overcharging me.",
        "Is it better to be loved or feared? I'd prefer to be loved, but $20 million would be nice too."
    ]

    quote = random.choice(quotes)

    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
    ]

    reset_color = "\033[0m"

    # ASCII Art borders
    top_border = "  " + "=" * (len(quote) + 4)
    bottom_border = "  " + "=" * (len(quote) + 4)

    print("\n")  # Add some vertical space
    print(random.choice(colors) + top_border + reset_color)

    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= len(top_border) - 6: # Account for padding
            line += word + " "
        else:
            print(random.choice(colors) + "  || " + line.center(len(top_border) - 6) + " || " + reset_color)
            line = word + " "
        time.sleep(0.05) # Added small delay for scrolling effect

    print(random.choice(colors) + "  || " + line.center(len(top_border) - 6) + " || " + reset_color)


    print(random.choice(colors) + bottom_border + reset_color)
    print("\n")  # Add some vertical space



if __name__ == "__main__":

    def spinning_cursor():
        while True:
          for cursor in '|/-\\':
            yield cursor

    spinner = spinning_cursor()

    print("\033[33mThinking... Philosophizing... Fretting... \033[0m", end="")

    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

    print_quote()