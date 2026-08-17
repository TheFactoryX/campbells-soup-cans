"""
Campbell's Soup Can #4649
Produced: 2026-08-17 10:48:09
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def ansi(color_code):
    return f'\033[{color_code}m'

CYAN = ansi(36)
MAGENTA = ansi('0;35m')
GREEN = ansi(32)
YELLOW = ansi('0;33m')
BLUE = ansi(34)
RESET = ansi(0)

def create_woody_box(lines, border_color, text_color):
    max_len = max(len(line) for line in lines)
    border = f"{border_color}{'+' + '-' * (max_len + 2) + '+'}{RESET}"
    content = []
    for line in lines:
        padded = line.ljust(max_len)
        content.append(f"{text_color}*| {padded} |*{RESET}")
    return '\n'.join([border] + content + [border])

def animated_print(text, delay=0.15):
    for line in text.split('\n'):
        print(line)
        time.sleep(delay)

# Woody Allen Style Quote
woody_quote = [
    "Suffering is the price we pay for experience,",
    "and I've paid enough to buy a small country.",
    "I'm not afraid of death—I just don't want to be there"
    "when it happens, which reminds me why I never leave"
    "the house without a detailed exit strategy."
]

# Create the box with color scheme
box = create_woody_box(woody_quote, CYAN, YELLOW)

# Print with typing effect
animated_print(box)

# Reset all colors at the end
print(RESET)