"""
Campbell's Soup Can #485
Produced: 2025-11-24 07:31:08
Worker: xAI: Grok 4.1 Fast (x-ai/grok-4.1-fast)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
colors = {
    'yellow': '\033[93m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'purple': '\033[95m',
    'green': '\033[92m',
}

def print_colored(color, text, end='\n', flush=True):
    sys.stdout.write(colors[color] + text + RESET)
    if flush:
        sys.stdout.flush()
    if end:
        sys.stdout.write('\n' * (1 if end == '\n' else 0))

# Clear screen
sys.stdout.write('\033[2J\033[H')
sys.stdout.flush()

# Intro sparkle animation
for _ in range(3):
    print_colored('yellow', '    *  WOODY\'S WISDOM  *    ', end='\r')
    time.sleep(0.2)
    sys.stdout.write(' ' * 30 + '\r')
    time.sleep(0.1)
print()  # newline

time.sleep(0.5)

# The quote
quote = "I don't believe in God, but I'm afraid of Him anyway – just in case He's neurotic too."
inner_width = len(quote) + 4
top = '╔' + '═' * inner_width + '╗'
bottom = '╚' + '═' * inner_width + '╝'

# Print top border
print_colored('yellow', top)

# Start left padding and side
sys.stdout.write(colors['cyan'] + '║  ' + RESET)
sys.stdout.flush()

# Set text color and bold, type quote letter by letter
sys.stdout.write(BOLD + colors['white'])
for char in quote:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
sys.stdout.write(RESET)

# Right side and padding
print_colored('cyan', '  ║', flush=True)

# Bottom border
print_colored('yellow', bottom)

# Attribution
print()
print_colored('purple', ' ' * ((inner_width + 2 - 32) // 2) + '“A Woody Allen Original”', end='\n\n')

time.sleep(1)

# Fun existential sparkle trail off
trail = ' ✨  Not dying today!  ✨ '
for i in range(20):
    print_colored('green', trail[:i%len(trail)] + ' ' * (len(trail) - i%len(trail)), end='\r')
    time.sleep(0.1)
print_colored('green', trail, end='\n\n')

# Tiny Woody-esque ASCII art
print("""
   .-"""-.
  /       \\
 |  O   O  |
  \\   ^   /
   '-----'
Neurotic philosopher cat approves!
""")