"""
Campbell's Soup Can #2860
Produced: 2026-03-20 07:13:59
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# 🎨 Color palette for Woody's existential chaos
COLORS = ['\033[38;5;202m', '\033[38;5;166m', '\033[38;5;46m', '\033[38;5;255m', '\033[38;5;196m', '\033[0m']
quote = "If life's a comedy, I'm the castigator. If it's tragedy, I'm the one with the wrong act."

# 🧱 Box art with ASCII flair
def art_frame():
    print("\033[47;30m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\033[0m")
    print("\033[38;5;208m█     \\   (-woody-style-sudden-panic)     \\    █\033[0m")
    print("\033[38;5;205m█  .--'  '  '    ' '  .--  \\   \\   \\    █\033[0m")
    print("\033[38;5;203m█ /`-_-` ` ` ` ` `-_` `-.`  \\   \\   \\    █\033[0m")
    print("\033[38;5;201m█|        YOU'RE  ALIVE?  |        █\033[0m")
    print("\033[38;5;198m█ \\       (  BUT  HOW?  ) \\       █\033[0m")
    print("\033[38;5;195m█  \\      (  ANSWER:  MEH )      \\   █\033[0m")
    print("\033[38;5;192m█   '---------------------'   \\   █\033[0m")
    print("\033[47;30m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\033[0m")

# 🎭 The Woody-style quote with animated color show
def woody_quote():
    text = quote.split()
    for i in range(len(text)):
        delay = 0.3 * (i % 4)  # Faster/slower color shifts
        print(f"\033[{COLORS[i % 6]}End of sidewalks, another dead end\033[0m", end='\r')
        time.sleep(delay)

# Run the show
if __name__ == "__main__":
    art_frame()
    print(f"\033[38;5;200m{quote.center(70)}\033[0m")  # Center the core quote
    woody_quote()  # Color chaos animation
    print("\n\033[31m(andof)  \033[0m")  # Woody's signature exit