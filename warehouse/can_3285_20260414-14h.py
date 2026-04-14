"""
Campbell's Soup Can #3285
Produced: 2026-04-14 14:13:09
Worker: Cohere: Command A (cohere/command-a)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors and formatting
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Woody Allen style quote
quote = """
"{0}I was thrown out of college for cheating on the metaphysics exam; I looked into the soul of the boy sitting next to me.{1}"
""".format(BOLD + MAGENTA, RESET)

# ASCII art frame
frame = """
{0}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                  {1}WOODY ALLEN'S PHILOSOPHICAL CORNER{0}                  +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|                                                                   |
|                                                                   |
|                   {2}{} {0}|
|                                                                   |
|                                                                   |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""".format(WHITE, YELLOW, RESET)

# Animation function
def animate_quote(quote, frame):
    lines = quote.strip().split('\n')
    for i in range(3):  # 3 lines of animation
        sys.stdout.write(frame.format('\n'.join([' ' * (i * 20) + line for line in lines])))
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\r' + frame.format(' ' * 80))  # Clear the line
        sys.stdout.flush()
    print(frame.format(quote.strip()))

# Main function
if __name__ == "__main__":
    animate_quote(quote, frame)
    time.sleep(2)  # Pause for effect
    print("\n{0}Press Enter to exit...{1}".format(BOLD + RED, RESET))
    input()