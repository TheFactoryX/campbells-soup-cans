"""
Campbell's Soup Can #719
Produced: 2025-12-04 22:34:01
Worker: Anthropic: Claude Opus 4 (anthropic/claude-opus-4)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# Clear screen
print('\033[2J\033[H')

# ASCII art glasses (Woody Allen signature)
glasses = f"""
{CYAN}     ___________     ___________
    /     _     \\   /     _     \\
   |    {WHITE}(_){CYAN}     | |    {WHITE}(_){CYAN}     |
   |_     _     |_|     _      _|
     \\___/ \\___/   \\___/ \\___/{RESET}
"""

# The quote
quote = "I tried to be an optimist once, but then I realized that happy people are just pessimists with faulty alarm systems."

# Neurotic thinking dots
def thinking_animation():
    for _ in range(3):
        for dots in ['   ', '.  ', '.. ', '...']:
            sys.stdout.write(f'\r{DIM}{BLUE}*thinking neurotically{dots}{RESET}')
            sys.stdout.flush()
            time.sleep(0.3)
    print('\r' + ' ' * 30 + '\r', end='')

# Print glasses with animation
for line in glasses.split('\n'):
    print(line)
    time.sleep(0.1)

print()

# Show thinking animation
thinking_animation()

# Create the quote box
border_color = random.choice([YELLOW, MAGENTA, CYAN])
quote_words = quote.split()
max_width = 60
lines = []
current_line = []
current_length = 0

for word in quote_words:
    if current_length + len(word) + 1 > max_width:
        lines.append(' '.join(current_line))
        current_line = [word]
        current_length = len(word)
    else:
        current_line.append(word)
        current_length += len(word) + 1

if current_line:
    lines.append(' '.join(current_line))

# Print the quote box
print(f"{border_color}╔{'═' * (max_width + 4)}╗{RESET}")
print(f"{border_color}║{RESET}  {RED}🎬{RESET} {BOLD}{WHITE}Woody Allen says:{RESET}" + ' ' * (max_width - 18) + f"{border_color}║{RESET}")
print(f"{border_color}╠{'═' * (max_width + 4)}╣{RESET}")

for line in lines:
    padding = max_width - len(line)
    print(f"{border_color}║{RESET}  {WHITE}{line}{' ' * padding}  {border_color}║{RESET}")

print(f"{border_color}╚{'═' * (max_width + 4)}╝{RESET}")

# Add some neurotic afterthoughts
afterthoughts = [
    f"{DIM}{BLUE}*adjusts glasses nervously*{RESET}",
    f"{DIM}{GREEN}*takes antacid*{RESET}",
    f"{DIM}{MAGENTA}*books another therapy session*{RESET}",
    f"{DIM}{RED}*contemplates the void*{RESET}",
    f"{DIM}{YELLOW}*worries about worrying*{RESET}"
]

time.sleep(1)
print()
print(random.choice(afterthoughts))

# Final existential cursor
time.sleep(1)
print()
for i in range(3):
    sys.stdout.write(f"\r{DIM}{'.' * (i + 1)}{RESET}")
    sys.stdout.flush()
    time.sleep(0.5)

print(f"\r{DIM}...why do I even bother?{RESET}")
print()