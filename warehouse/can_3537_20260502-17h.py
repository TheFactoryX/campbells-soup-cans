"""
Campbell's Soup Can #3537
Produced: 2026-05-02 17:06:49
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import random
import os

# ANSI color codes
RESET  = "\033[0m"
BOLD   = "\033[1m"
BLUE   = "\033[34m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
MAGENTA= "\033[35m"

# Quote in Woody Allen style
QUOTE = (
    f"{BOLD}{YELLOW}I keep telling myself I could achieve immortality by writing famous words, "
    f"but the only thing my brain has mastered is writing a million apologies for misplacing "
    f"my keys.{RESET}"
)

# Frame template with placeholders for width and height
FRAME_TPL = (
    "╔{top_left}═{horizontal:^{width}}═{top_right}╗\n"
    "║{inner:^{width}}║\n"
    "╚{bottom_left}═{horizontal:^{width}}═{bottom_right}╝"
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_quote():
    words = QUOTE.split()
    for i in range(1, len(words) + 1):
        clear_screen()
        line = ' '.join(words[:i])
        box = FRAME_TPL.format(
            top_left="◤", top_right="◥", bottom_left="◣", bottom_right="◤",
            horizontal="─", inner=line, width=len(line) + 4
        )
        # Random color for each frame
        color = random.choice([BLUE, CYAN, MAGENTA, YELLOW])
        print(f"{color}{box}{RESET}")
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        animate_quote()
    except KeyboardInterrupt:
        sys.exit()