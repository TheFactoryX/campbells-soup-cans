"""
Campbell's Soup Can #463
Produced: 2025-11-23 07:28:47
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

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

c = Colors()

quote = "I'm not afraid of the void; it's afraid of my therapy bills piling up eternally."
quote_len = len(quote)
border_width = 78
inner_width = border_width - 4
total_padding = inner_width - quote_len
left_pad = total_padding // 2
right_pad = total_padding - left_pad

# Hide cursor
sys.stdout.write('\033[?25l')
sys.stdout.flush()

print(c.BOLD + c.PURPLE + "  🎭  WOODY ALLEN'S NEUROTIC WISDOM  🎭  " + c.RESET)
print()

# Loading spinner
spinners = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏⠋'
for i in range(60):
    sys.stdout.write(f'\r{c.CYAN}Pondering the absurdity of existence... {spinners[i % len(spinners)]} {c.RESET}')
    sys.stdout.flush()
    time.sleep(0.08)
print('\r' + ' ' * 70 + '\r\n')

# Box borders
top = c.BOLD + c.GREEN + '╔' + '═' * (border_width - 2) + '╗' + c.RESET
bottom = c.BOLD + c.GREEN + '╚' + '═' * (border_width - 2) + '╝' + c.RESET
left_side = c.BOLD + c.GREEN + '║' + c.RESET
right_side = c.GREEN + c.BOLD + '║' + c.RESET
empty_inner = ' ' * inner_width

empty_line = left_side + empty_inner + right_side + '\n'

print(top)
print(empty_line)
print(empty_line)

# Start quote line, centered typewriter effect
sys.stdout.write(left_side)
sys.stdout.write(' ' * left_pad)
sys.stdout.flush()

colors = [c.RED, c.YELLOW, c.GREEN, c.BLUE, c.PURPLE, c.CYAN]
pause_map = {'.': 0.6, ';': 0.4, "'": 0.1, ',': 0.2}
base_delay = 0.035

for i, char in enumerate(quote):
    color = colors[i % len(colors)]
    sys.stdout.write(color + char + c.RESET)
    sys.stdout.flush()
    extra_pause = pause_map.get(char, 0)
    time.sleep(base_delay + extra_pause)

sys.stdout.write(' ' * right_pad + right_side + '\n')
sys.stdout.flush()

print(empty_line)
print(empty_line)
print(bottom)
print()

print(c.WHITE + c.BOLD + "Ah, the human condition... what a neurotic mess." + c.RESET)
print()

# Show cursor
sys.stdout.write('\033[?25h')
sys.stdout.flush()