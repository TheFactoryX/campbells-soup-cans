"""
Campbell's Soup Can #2257
Produced: 2026-02-16 11:08:25
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

quote = "I’m not afraid of death; I just don’t want to be there when it happens."
art = r"""
   _____
  /_____\ 
 (  o o  )
  \  ^  /
   \___/ 
   /|\  
  / | \ 
"""

# ANSI color codes (rainbow cycle)
colors = [
    '\033[31m',  # red
    '\033[33m',  # yellow
    '\033[32m',  # green
    '\033[34m',  # blue
    '\033[35m',  # magenta
    '\033[36m',  # cyan
]
reset = '\033[0m'

# Print ASCII art line by line with cycling colors
for i, line in enumerate(art.splitlines()):
    sys.stdout.write(colors[i % len(colors)] + line + reset + '\n')
    sys.stdout.flush()
    time.sleep(0.15)  # slight pause for a playful effect

# Print the Woody Allen–style quote in bright white
sys.stdout.write('\033[97m' + quote + reset + '\n')
sys.stdout.flush()