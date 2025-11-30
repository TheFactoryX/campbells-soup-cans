"""
Campbell's Soup Can #613
Produced: 2025-11-30 04:04:37
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
    """Prints a funny, philosophical quote in Woody Allen's style with visual flair."""

    quotes = [
        "I'm not sure if I believe in an afterlife, but I am bringing a change of underwear.",
        "My brain is my second favorite organ.",
        "Eternity is a very long time, especially towards the end.",
        "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
        "Life is a sexually transmitted disease.",
        "Death is not the end. There remains the litigation over the estate.",
        "I am two with nature... on the verge of divorce.",
        "Basically my wife was immature. I'd be at home in the bath and she'd come in and sink my boats."
    ]

    quote = random.choice(quotes)
    quote_length = len(quote)

    # ANSI color codes
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    reset_color = "\033[0m"

    # ASCII art
    thinking_man = """
     _,-._
    / \_/ \
    >-(_)-<
    \_/ \_/
      `-'
    """
    print(f"{random.choice(colors)}{thinking_man}{reset_color}")
    time.sleep(0.5)
    
    border_color = random.choice(colors)
    print(f"{border_color}" + "  " + "_" * (quote_length + 4) + f" {reset_color}")
    print(f"{border_color}" + " /" + " " * (quote_length + 5) + f"\\ {reset_color}")

    words = quote.split()
    line = ""
    for word in words:
      if len(line + word) + 1 < quote_length:
        line += word + " "
      else:
          print(f"{border_color}| {line:<{quote_length + 3}} |{reset_color}")
          line = word + " "
    print(f"{border_color}| {line:<{quote_length + 3}} |{reset_color}")


    print(f"{border_color}" + " \\" + "_" * (quote_length + 5) + f"/ {reset_color}")
    print(f"{border_color}" + "    " + "-" * (quote_length + 4) + f" {reset_color}")
    time.sleep(0.5)

    print(f"{random.choice(colors)}   - Woody Allen{reset_color}")


if __name__ == "__main__":
    print_quote()