"""
Campbell's Soup Can #1993
Produced: 2026-02-01 21:38:02
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def flickering_quote(quote, duration=3):
    colors = [
        "\033[91m\033[47m",  # Red on white
        "\033[95m\033[40m",  # Purple on black
        "\033[92m\033[48m"   # Green on bright green
    ]
    effect_chars = ['—', '~~', '*', '~', '^', '#', '!']
    
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write("\033[1A\033[2K\r")
        choose_color = random.choice(colors)
        choose_effect = random.choice(effect_chars)
        line = choose_color + f"  {quote.center(30)} {choose_effect} " + "\033[0m"
        print(line, end='\r')
        time.sleep(0.1)
    print("\n", line, end='')

quote = "I told my therapist I was feeling existential, and she said, 'Great, now do a handstand.'"
flickering_quote(quote)