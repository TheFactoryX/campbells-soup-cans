"""
Campbell's Soup Can #595
Produced: 2025-11-29 07:29:22
Worker: xAI: Grok 4.1 Fast (free) (x-ai/grok-4.1-fast:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

colors_list = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

quote = "The universe is indifferent, which is fine—my self-loathing is personal enough for both of us."
inner_width = 92
quote_len = len(quote)
left_pad = (inner_width - quote_len) // 2
right_pad = inner_width - quote_len - left_pad

clear_screen()
time.sleep(0.5)

# Title
title = "Woody Allen's Neurotic Wisdom"
title_centered = title.center(inner_width)
print(BOLD + MAGENTA + title_centered + RESET)
time.sleep(0.8)

# Box top
print('╔' + '═' * inner_width + '╗')
time.sleep(0.3)

# Content line with rainbow typing effect
sys.stdout.write('║')
sys.stdout.flush()
for _ in range(left_pad):
    sys.stdout.write(' ')
    sys.stdout.flush()
time.sleep(0.1)

for i, char in enumerate(quote):
    color = colors_list[i % len(colors_list)]
    sys.stdout.write(color + char + RESET)
    sys.stdout.flush()
    time.sleep(0.035)

for _ in range(right_pad):
    sys.stdout.write(' ')
sys.stdout.write('║\n')
sys.stdout.flush()
time.sleep(0.5)

# Box bottom
print('╚' + '═' * inner_width + '╝')

# Signature
signature = "— A Neurotic's Take (Inspired by Woody Allen)"
sig_pad = (inner_width - len(signature)) // 2
print(YELLOW + ' ' * sig_pad + signature + RESET)

time.sleep(2)
print("\n" + CYAN + "(Existential sigh...)" + RESET)