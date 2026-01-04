"""
Campbell's Soup Can #1382
Produced: 2026-01-04 08:43:05
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

quote = "I'm not afraid of death; I just don't want to be there when it happens."

def animate():
    typewriter("Woody Allen once said:\n")
    time.sleep(1)
    sys.stdout.write("\033[1;31m") # red color
    typewriter("I'm not afraid of death;\n") 
    sys.stdout.write("\033[0;0m") # reset color
    sys.stdout.write("\033[1;32m") # green color
    typewriter("I just don't want to be there when it happens.\n")
    sys.stdout.write("\033[0;0m") # reset color

animate()