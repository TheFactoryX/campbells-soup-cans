"""
Campbell's Soup Can #2386
Produced: 2026-02-23 03:19:25
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

BORDER_COLOR = '\033[93m'
TEXT_COLOR = '\033[96m'
RESET = '\033[0m'
INNER_WIDTH = 40
QUOTE_LINES = [
    "I'm so neurotic I worry about the",
    "expiration date on my existential dread."
]
SHAKE_OFFSETS = [0, 1, 0, -1, 0, 1, 0, -1, 0]

for frame, dx in enumerate(SHAKE_OFFSETS):
    shifted_lines = []
    for line in QUOTE_LINES:
        padded = line.ljust(INNER_WIDTH)
        if dx >= 0:
            shifted = ' ' * dx + padded[:INNER_WIDTH - dx]
        else:
            shifted = padded[-dx:] + ' ' * (-dx)
        shifted_lines.append(shifted)
    
    frame_content = []
    frame_content.append(BORDER_COLOR + '╔' + '═' * INNER_WIDTH + '╗' + RESET)
    frame_content.append(BORDER_COLOR + '║' + RESET + TEXT_COLOR + ' ' * INNER_WIDTH + RESET + BORDER_COLOR + '║' + RESET)
    for line in shifted_lines:
        frame_content.append(BORDER_COLOR + '║' + RESET + TEXT_COLOR + line + RESET + BORDER_COLOR + '║' + RESET)
    frame_content.append(BORDER_COLOR + '║' + RESET + TEXT_COLOR + ' ' * INNER_WIDTH + RESET + BORDER_COLOR + '║' + RESET)
    frame_content.append(BORDER_COLOR + '╚' + '═' * INNER_WIDTH + '╝' + RESET)
    
    if frame > 0:
        print('\033[F' * 5, end='', flush=True)
    print('\n'.join(frame_content), flush=True)
    
    time.sleep(0.12)