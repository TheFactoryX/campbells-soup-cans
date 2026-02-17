"""
Campbell's Soup Can #2280
Produced: 2026-02-17 15:06:05
Worker: Qwen: Qwen3 235B A22B (qwen/qwen3-235b-a22b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def typewrite(line):
    for c in line:
        print(c, end='', flush=True)
        time.sleep(0.02)
    print()

quote = "I'm not afraid of the void; I just object to being charged admission for the privilege."

BORDER = "\033[91m"  # Bright red
TEXT = "\033[93m"    # Golden yellow
RESET = "\033[0m"

# Construct the box borders
top = BORDER + "+" + "-" * (len(quote) + 2) + "+" + RESET
mid = BORDER + "| " + TEXT + quote + RESET + BORDER + " |" + RESET

# Type out the quote box
typewrite(top)
typewrite(mid)
typewrite(top)

# Add Woody Allen's trademark glasses
time.sleep(0.5)
print(f"\n{BORDER}  0      0{RESET}")
time.sleep(0.3)
print(f"{BORDER}  |______|{RESET}")
time.sleep(0.3)
print(f"{BORDER} / ______\_{RESET}")
time.sleep(0.3)
print(f"{BORDER}  ~~~    ~~~{RESET}")

# Bonus existential sigh at the bottom
sigh = "※ Sidenote: God could've at least made taxes existential too ※"
print(f"\n{BORDER}{sigh}{RESET}")