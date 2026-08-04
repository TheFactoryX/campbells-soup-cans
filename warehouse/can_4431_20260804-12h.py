"""
Campbell's Soup Can #4431
Produced: 2026-08-04 12:18:42
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def main():
    quote = "I tried to find the meaning of life, but all I got was this lousy t-shirt and a lingering sense of dread."
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset = '\033[0m'
    border = '*' * (len(quote) + 4)
    sys.stdout.write('\033[96m' + border + reset + '\n')
    sys.stdout.write('\033[96m* ' + reset)
    for ch in quote:
        color = random.choice(colors)
        sys.stdout.write(color + ch + reset)
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write(' *' + reset + '\n')
    sys.stdout.write('\033[96m' + border + reset + '\n')

if __name__ == "__main__":
    main()