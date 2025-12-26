"""
Campbell's Soup Can #1186
Produced: 2025-12-26 07:33:33
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not neurotic—I just have a sensitive nervous system."

# Spinner animation
spinner_chars = ['|', '/', '-', '\\']
for c in spinner_chars:
    print(f'\r{c}', end='', flush=True)
    time.sleep(0.1)
print('\r', end='', flush=True)
print()  # Move to next line after spinner

# ANSI color codes
border_color = '\033[93m'  # Yellow
text_color = '\033[92m'   # Green
reset = '\033[0m'

border = '+' + '-' * 58 + '+'
print(f"{border_color}{border}{reset}")
print(f"{text_color}| {quote} |{reset}")
print(f"{border_color}{border}{reset}")