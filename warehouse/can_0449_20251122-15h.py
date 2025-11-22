"""
Campbell's Soup Can #449
Produced: 2025-11-22 15:29:04
Worker: xAI: Grok 4.1 Fast (x-ai/grok-4.1-fast)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
colors = ['\033[91m', '\033[93m', '\033[92m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']

quote = "I don't fear the abyss; the abyss fears my ability to overthink it into a full-blown anxiety attack."

def rainbow_typewriter(text, delay=0.03):
    words = text.split()
    for i, word in enumerate(words):
        col = colors[i % len(colors)]
        sys.stdout.write(BOLD + col + word + RESET + ' ')
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Animated spinner
sys.stdout.write(BOLD + '\033[96mGenerating neurosis')
sys.stdout.flush()
spinner = '⠏⠇⠧⠦⠴⠼⠸⠹⠙⠋'
for _ in range(40):
    for j, char in enumerate(spinner):
        sys.stdout.write('\r' + BOLD + '\033[96m' + char + ' Generating neurosis' + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
print('\r' + ' ' * 30 + '\r')

print('\n')
print(BOLD + '\033[95m' + '╔══════════════════════════════════════════════════════════════════════════════════════╗' + RESET)
print(BOLD + '\033[93m' + '║' + ' ' * 78 + 'WOODY ALLEN' + ' ' * 33 + '║' + RESET)
print(BOLD + '\033[95m' + '╠══════════════════════════════════════════════════════════════════════════════════════╣' + RESET)
print('\033[97m' + '║  ' + RESET, end='')
rainbow_typewriter(quote)
line2_len = 78 - 4  # adjust for padding
print('\033[95m' + '║' + RESET + ' ' * (line2_len - len(quote)) + '\033[95m' + '║')
print(BOLD + '\033[95m' + '╚══════════════════════════════════════════════════════════════════════════════════════╝' + RESET)
print(DIM + '\033[90m' + ' (Neurotic wisdom dispensed. Therapy not included.)' + RESET + '\n')