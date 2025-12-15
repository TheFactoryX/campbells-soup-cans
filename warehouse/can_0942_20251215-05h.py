"""
Campbell's Soup Can #942
Produced: 2025-12-15 05:42:39
Worker: Baidu: ERNIE 4.5 21B A3B (baidu/ernie-4.5-21b-a3b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_woody_quote():
    # ANSI escape codes for colors
    RED = "\033[91m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    END = "\033[0m"

    # ASCII art for Woody Allen's signature
    woody_art = r"""
     ______  _      _    _   _   _   _   _   _ 
    |  ____|| |    | |  | \ | | | | | | | | |
    | |__   | |    | |  |  \| | | | | | | | |
    |  __|  | |    | |  | . ` | | | | | | | |
    | |____ | |____| |__| |\  | | |_| |_| |_|
    |______||________|______|_| \_| \___/ \___/
    """

    # Woody Allen quote
    quote = f"""
    {RED}"I'm not afraid of dying; I'm just afraid of waking up and realizing I didn't do anything with my life."{END}
    """

    # Print Woody's art
    print(woody_art)

    # Print the quote with some animation
    for char in quote:
        print(char, end="", flush=True)
        time.sleep(0.05)

    # Final newline
    print()

if __name__ == "__main__":
    print_woody_quote()