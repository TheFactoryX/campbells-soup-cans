"""
Campbell's Soup Can #1075
Produced: 2025-12-21 06:46:33
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

def colorful_print(text, delay=0.03):
    colors = ['\033[36m', '\033[33m', '\033[35m']
    for i, char in enumerate(text):
        sys.stdout.write(random.choice(colors) + char)
        sys.stdout.flush()
        time.sleep(delay * (0.5 + random.random()))
    sys.stdout.write('\033[0m')

def blinking_cursor(duration=3, blink_speed=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write('\033[31m_\033[0m')
        sys.stdout.flush()
        time.sleep(blink_speed)
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(blink_speed)

quote = [
    "  I'm convinced the universe is fundamentally indifferent,",
    "  which is ironic because it took me three weeks to work up",
    "  the courage to tell it how I feel. Now it's just 'seen-zoned'",
    "  by eternity itself. Typical."
]

box_width = max(len(line) for line in quote) + 4

sys.stdout.write('\033[33m╔' + '═' * (box_width) + '╗\033[0m\n')
for line in quote:
    sys.stdout.write('\033[33m║ \033[0m')
    colorful_print(line.center(box_width - 2))
    sys.stdout.write('\033[33m ║\033[0m\n')
sys.stdout.write('\033[33m╚' + '═' * (box_width) + '╝\033[0m\n')

sys.stdout.write("\n  ")
blinking_cursor()
sys.stdout.write("\b\033[K\n")  # Clear cursor and line
colorful_print("\033[3m...this program will self-destruct in existential dread\033[0m\n", 0.05)