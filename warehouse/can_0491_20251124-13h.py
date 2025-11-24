"""
Campbell's Soup Can #491
Produced: 2025-11-24 13:45:50
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
LIGHT_BLUE = '\033[1;96m'
RESET = '\033[0m'

# Funny Woody Allen style quote
quote = (
    "I used to think I was indecisive, but now I'm not so sure. "
    "Life is like an ice cream - no matter how it's treatin' me, my head stays solid."
)

# Visual components
mustache = [
    "   /\\      /\\",
    "  /  \\    /  \\",
    "       \\/",
    "    /     \\",
    "          /",
    "         /",
    "(._.) 朋友们"
]

box_width = 63
inner_width = box_width - 2  # For visual framing
padding = (inner_width - len(quote)) // 2

# Create the border strings
border_top = LIGHT_BLUE + '╔' + '═' * inner_width + '╗' + RESET
border_bottom = LIGHT_BLUE + '╚' + '═' * inner_width + '╝' + RESET
quote_frame = LIGHT_BLUE + '║' + ' ' * padding + quote + ' ' * padding + '║' + RESET

# Display the mustache and title with animation
def print_with_undulating_text(text, color, delay=0.015):
    """Print text with passing-through effect"""
    num_cols = box_width
    text_len = len(text)
    blank_area = ' ' * (num_cols + text_len)
    for start in range(-text_len, num_cols):
        display = blank_area[start:start+num_cols]
        sys.stdout.write(display + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

print_with_undulating_text("  ◌•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-嵩", BLUE)
print_with_undulating_text(f"  {GREEN}Oo--o Allen's Brain Explosion ⚡{RESET}", RED)

# Print mustache
for line in mustache:
    print(GREEN + line + RESET)
    time.sleep(0.15)

print()

# Frame the quote
print(border_top)
print(quote_frame)

# Typing effect on the quote
print(LIGHT_BLUE + '║' + RESET, end='', flush=True)
for char in quote:
    print(LIGHT_BLUE + char + RESET, end='', flush=True)
    time.sleep(0.03)
print(LIGHT_BLUE + '║' + RESET)

print(border_bottom)

# Display the source with ASCII art
print()
time.sleep(1)
print(RED + " ├────────────────────────────────────────────────┐" + RESET)
time.sleep(0.3)
print(RED + " │              ⊙  MARK NOAH PIE  ⊙            │" + RESET)
time.sleep(0.3)
print(RED + " ├──────────────────────┬──────────────────────┤" + RESET)
time.sleep(0.3)
print(RED + " │  ⊿   ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⊿ │  ⊿  This IS a joke!  ⊿ │" + RESET)
time.sleep(0.3)
print(RED + " └──────────────────────┴──────────────────────┘" + RESET)
time.sleep(0.5)
print()