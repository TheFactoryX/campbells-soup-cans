"""
Campbell's Soup Can #510
Produced: 2025-11-25 10:42:21
Worker: Qwen: Qwen3 Next 80B A3B Thinking (qwen/qwen3-next-80b-a3b-thinking)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote_lines = [
    "I'm not afraid of dying; I just don't want to be present when it occurs.",
    "After all, someone has to be there to pay the bills."
]

max_line_length = max(len(line) for line in quote_lines)
max_width = max_line_length + 4

top_line = '*' * max_width
box_lines = [top_line]
for l in quote_lines:
    centered_l = l.center(max_width - 4)
    line_str = '*' + ' ' + centered_l + ' ' + '*'
    box_lines.append(line_str)
box_lines.append(top_line)

for i, line in enumerate(box_lines):
    for j, char in enumerate(line):
        if i == 0 or i == len(box_lines) - 1:
            color = "\033[92m"
        else:
            if j == 0 or j == 1 or j == len(line) - 2 or j == len(line) - 1:
                color = "\033[92m"
            else:
                color = "\033[93m"
        print(color + char + "\033[0m", end='', flush=True)
        time.sleep(0.02)
    print()
print("\033[91m" + "Slightly existential, slightly rich, slightly absurd." + "\033[0m")