"""
Campbell's Soup Can #453
Produced: 2025-11-22 19:25:40
Worker: MoonshotAI: Kimi K2 0711 (moonshotai/kimi-k2)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter(text, delay=0.05, color_code="\033[37m"):
    for char in text:
        sys.stdout.write(color_code + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(random.uniform(delay*0.7, delay*1.3))
    print()

def flicker_animation(lines, color_code="\033[33m", times=4):
    for _ in range(times):
        sys.stdout.write("\033[2J\033[H")  # clear screen
        print("\n" * 5)
        for line in lines:
            print(" " * 20 + color_code + line + "\033[0m")
        time.sleep(0.3)
        sys.stdout.write("\033[2J\033[H")  # clear screen
        time.sleep(0.1)

def draw_woody():
    lines = [
        "                   .-""""-.",
        "                  /        \\",
        "                 /_        _\\",
        "                // \\      / \\\\",
        "               |\___\\    /___/ |",
        "               \\  .-'    '-.  /",
        "                '-._       _.-'",
        "                 /\"-._   _.-\"\\",
        "                /       \"       \\",
        "               /     .--.\\     \\",
        "              /   .'      '.    \\",
        "             /_.-'          '-._\\"
    ]
    for line in lines:
        print(" " * 5 + "\033[90m" + line + "\033[0m")

# Flicker intro
flicker_animation([
    "IN A WORLD WHERE...",
    "EXISTENTIAL ANXIETY MEETS",
    "BAD JOKES..."
], times=3)

time.sleep(0.5)

# Draw Woody caricature
draw_woody()
time.sleep(0.5)

# Typewriter the quote
print("\n" * 2 + " " * 15 + "\033[90mWOODY ALLEN (probably):\033[0m")
time.sleep(0.5)

quote = "\"I don't fear death; I just don't want to be there when it happens. Like my ex-wife's birthday parties, but forever and without the cake.\" —2002 (after a bad therapy session)"

typewriter(quote, delay=0.06, color_code="\033[35m")

time.sleep(0.3)
print("\n" * 2 + " " * 20 + "\033[33m✡ EDITED FOR MAXIMUM JEWISH GUILT ✡\033[0m")
time.sleep(0.5)

# Animate the punchline
print("\n" * 2 + " " * 10, end="")
for i in range(4):
    sys.stdout.write("\033[91m" + "(╯°□°）╯︵ ┻━┻ \033[0m")
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write("\b" * 20)
    time.sleep(0.2)

# Final existential flash
sys.stdout.write("\033[5m\033[7m\033[37m" + " " * 80 + "THE UNIVERSE IS INDIFFERENT" + " " * 80 + "\033[0m")
print()