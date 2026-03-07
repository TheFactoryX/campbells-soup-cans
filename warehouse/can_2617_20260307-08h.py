"""
Campbell's Soup Can #2617
Produced: 2026-03-07 08:50:31
Worker: Mistral: Mistral Large 3 2512 (mistralai/mistral-large-2512)
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

def woody_print(text, color_code, delay=0.05):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_quote():
    colors = [
        "38;5;208",  # orange
        "38;5;220",  # yellow
        "38;5;118",  # green
        "38;5;141",  # purple
        "38;5;203",  # pink
    ]

    frame1 = r"""
       _____
     o8%8888,
   o88%8888888.
  8'-    -:8888b
 8'         8888
d8.-=. ,==-.:888b
>8 `~` :`~' d8888
88         ,88888
88b. `-~  ':88888
888b ~==~ .:88888
88888o--:':::8888
`88888| :::' 8888b
8888^^'       8888b
d888           ,%888b.
d88%            %%%8--'-.
/88:.__ ,       _%-' ---  -
    '''::===..-'   =  --.
    """

    frame2 = r"""
       _____
     o8%8888,
   o88%8888888.
  8'-    -:8888b
 8'         8888
d8.-=. ,==-.:888b
>8 `~` :`~' d8888
88         ,88888
88b. `-~  ':88888
888b ~==~ .:88888
88888o--:':::8888
`88888| :::' 8888b
8888^^'       8888b
d888           ,%888b.
d88%            %%%8--'~
/88:.__ ,       _%-'~
    '''::===..-'   = ~
    """

    quote = "\"My one regret in life is that I am not someone else... preferably someone who's not me.\""
    attribution = "- Woody Allen (probably)"

    for _ in range(3):
        for frame in [frame1, frame2]:
            print("\033[H\033[J", end="")  # Clear screen
            woody_print(frame, random.choice(colors))
            time.sleep(0.2)

    print("\n")
    woody_print("╔" + "═" * (len(quote) + 2) + "╗", "38;5;220")
    woody_print(f"║ {quote} ║", "38;5;118")
    woody_print("╚" + "═" * (len(quote) + 2) + "╝", "38;5;220")
    print("\n")
    woody_print(" " * (len(quote) // 2 - len(attribution) // 2) + attribution, "38;5;203")

if __name__ == "__main__":
    animate_quote()