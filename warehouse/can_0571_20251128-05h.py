"""
Campbell's Soup Can #571
Produced: 2025-11-28 05:34:56
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
import random

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BLACK_BG = '\033[40m'

# Woody Allen style quote (original, neurotic & self-deprecating)
quote = "I'm not afraid of death; I just don't want to be there when it happens—probably fumbling for my glasses in the dark."

# Clear screen for dramatic effect
sys.stdout.write('\033[2J\033[H')
sys.stdout.flush()
time.sleep(0.5)

# Animated sparkling intro
sparkles = ['*', '+', '✦', '★', '✧']
for _ in range(20):
    sparkle = random.choice(sparkles)
    color = random.choice([CYAN, YELLOW, PURPLE])
    sys.stdout.write(f'\r{color}{sparkle * 40}{RESET}')
    sys.stdout.flush()
    time.sleep(0.08)
print()  # New line

# ASCII Art Header
header = f"""
{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════╗{RESET}
{BOLD}{CYAN}║{RESET}                    {BOLD}{WHITE}WOODY ALLEN'S NEUROTIC WISDOM{RESET}                    {BOLD}{CYAN}║{RESET}
{BOLD}{CYAN}╠══════════════════════════════════════════════════════════════╣{RESET}
"""
print(header)

# Typewriter animation for the quote with color-cycling letters
colors = [YELLOW, PURPLE, GREEN, BLUE, CYAN, WHITE]
sys.stdout.write('║  ')
sys.stdout.flush()
color_idx = 0
for i, char in enumerate(quote):
    if char == ' ':
        sys.stdout.write(char)
    else:
        color = colors[color_idx % len(colors)]
        sys.stdout.write(f'{BOLD}{color}{char}{RESET}')
        color_idx += 1
    sys.stdout.flush()
    time.sleep(random.uniform(0.03, 0.08))  # Variable speed for organic feel
print(f'{RESET}  {BOLD}{CYAN}║{RESET}')
print(f'{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════╝{RESET}\n')

# Funny existential footer animation (fading existential dread)
footer_phrases = [
    f'{RED}Neurotic applause...{RESET}',
    f'{PURPLE}(But is it real, or just my imagination?){RESET}',
    f'{GREEN}The end... or is it?{RESET}',
]
for phrase in footer_phrases:
    sys.stdout.write(f'\r{phrase:50}')
    sys.stdout.flush()
    time.sleep(1.2)

print('\n' + RESET)  # Final reset