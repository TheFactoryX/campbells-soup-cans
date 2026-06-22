"""
Campbell's Soup Can #3989
Produced: 2026-06-22 17:50:13
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
from itertools import cycle

QUOTE = [
    "I don't believe in overnight success. I believe in \n\n",
    "/   /\\   \\   \\   \\   \\   \\   \\",
    "\\ /  \\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\",
    " \\ \\   /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ \\ ",
    "  \\ \\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\  \\ ",
    "   \\ \\ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/  \\ \\  \\n\nYour Confidence", 
    "}_`)|",
    "   |  (  `"
]

COLORS = cycle([
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[94m"   # Blue
])

spacing = [0, 4, 0, 2, 6, 4, 2, 0]
fade_speed = 0.15
base_delay = 0.07
scroll_speed = 0.08

print(
    "\033[H\033[J"  # Clear screen
    f"                                         \n"
    "         ___        ___       ___        ___\n"
    "        |   |      |   |     |   |      |   |\n"
    "        |   |      |   |     |   |      |___|\n"
    "...     |   |      |   |     |   |                ...\n"
    "...     \\   |\\\\    |   |     |   |   .../ \\\n"
    "...     |    |  \u222b  |   |     |   |                ...\n"
    "                        |\\\\ / /`\n"
    "                        /  O O \\\n"
    "                       /  (O O)\n"
    "                      /  >(#<)\n"
    "                      \\_/ \u2614 \\\\\n"
    "                     /    -----=------------\n"
    "                   ``/ \u2192 \u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u2192 (\u21a5\n"
    "                     \n"
    "                     \n"
    "                     \n"
)

color_iter = cycle(COLORS)
intervals = [random.uniform(0.03, 0.07) for _ in range(len(QUOTE))]
start_time = time.time()

for i, (line, delay) in enumerate(QUOTE):
    line = line.rstrip()
    color = next(color_iter)
    old_len = 0
    
    while old_len < len(line):
        current_len = min(old_len + int(random.expovariate(1 / spacing[i])) + 1, len(line))
        segment = line[old_len:current_len]
        elapsed = time.time() - start_time
        wait = max(0, delay - elapsed % (1 / fade_speed))
        
        print(f"\033[12G\033[H\033[J{color}{segment}", end="", flush=True)
        animation_chars = ">_<|\\".split()
        anim_char = random.choice(animation_chars)
        print(f" {anim_char}", end="", flush=True)
        time.sleep(0.04)
        print(f"\r", end="")
        
        old_len = current_len
        time.sleep(wait)
    
    print(f"\033[12G\033[H\033[J{color}{line}", end="\r", flush=True)
    time.sleep(base_delay)

print("\033[97m", "\033[H\033[J", end="", flush=True)
print(
    "\n    __          __    ___      ___    ___      ___    ___\n"
    "   /  |        /  \\  |   |    |   |  |   |    |O  \\O    |    |   |\n"
    "  /   |       /    | |   |    |   |  |   |    |   ) |    |    |___|\n"
    " /    |      /      ||   |    |   |  |   |    |_ / |    |               ...\n"
    "/     |     /       ||   |    |   |  |   |    /   \\|    |                        ...\n"
    "/      \\|    /        |   |    |   |  |   |   \u2192 / \\ \\`\n"
    "\\        \\__/ \\         |   |    |   |  |   |   |    | \\\\\n"
    "/         |  \\\\ _^_ \\     |   |    |   |  |   |  / \\_/ \\\\\n"
    "\\         |  |  \\`O ./    |   |    |   |  |   | /    ) \\\\\n"
    "\\        /  \\`------- /   \\__/    |   |  |   | /    ) \\\\\n"
    " \\       |  |  \\` twenty-one\n"
    "\n"
)
time.sleep(1)