"""
Campbell's Soup Can #2107
Produced: 2026-02-07 22:47:21
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

# ANSI color codes
RED   = "\033[91m"
GREEN = "\033[92m"
YELLOW= "\033[93m"
BLUE  = "\033[94m"
MAGENTA = "\033[95m"
CYAN  = "\033[96m"
RESET = "\033[0m"

quote = "I’m not afraid of death; I just don’t want to be there when it happens."

def colored(txt, col): 
    return f"{col}{txt}{RESET}"

WIDTH  = 66
HEIGHT = 9

border = colored("╔" + "═"*(WIDTH-2) + "╗", CYAN)
bottom = colored("╚" + "═"*(WIDTH-2) + "╝", CYAN)
empty  = colored("║" + " "*(WIDTH-2) + "║", CYAN)

lines = [border]

msg = colored(quote, MAGENTA)
msg_line = "║" + " "*((WIDTH-2)-len(msg))//2 + msg + " "*((WIDTH-2)-len(msg)+1)//2 + "║"
lines.append(msg_line)

for _ in range(HEIGHT-3):
    lines.append(empty)

lines.append(bottom)

# Print the box with a tiny pause for “animation”
for l in lines:
    sys.stdout.write(l + "\n")
    sys.stdout.flush()
    time.sleep(0.05)

# A quick winking wink for extra flair
wink = colored("😉", YELLOW)
for _ in range(2):
    sys.stdout.write(wink)
    sys.stdout.flush()
    time.sleep(0.4)
    sys.stdout.write("\b" * len(wink))
    sys.stdout.flush()
    time.sleep(0.2)

sys.stdout.write("\n")