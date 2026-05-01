"""
Campbell's Soup Can #3520
Produced: 2026-05-01 15:16:27
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen style quote printer with visual flair.
"""
importtime
import sys

# ANSI color codes
CYAN = '\033[36m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m'

# The quote (original Woody Allen style)
quote = "I'm not concerned about the afterlife; I'm just worried that in heaven they'll serve only steamed vegetables and I'll have to wear a robe."

# Box configuration
total_width = 70          # total width of box including borders
border_char = '*'
inner_width = total_width - 2   # space between left and right borders
left_pad = 2               # spaces between left border and text
max_text_len = inner_width - left_pad  # maximum length of text line

# Wrap text to fit
def wrap_text(text, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

wrapped_lines = wrap_text(quote, max_text_len)

# Padding inside box
pad_top = 1
pad_bottom = 1

# Typing effect function
def type_text(text, color, delay=0.02):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

# Clear screen (optional, comment out if not desired)
print('\033[2J\033[H', end='')

# Print top border
print(CYAN + border_char * total_width + RESET)

# Top padding
for _ in range(pad_top):
    line = ' ' * inner_width
    print(CYAN + border_char + RESET + line + CYAN + border_char + RESET)

# Quote lines with typing
for line in wrapped_lines:
    # Prepare inner string: left padding, line, then fill with spaces
    inner = ' ' * left_pad + line + ' ' * (inner_width - left_pad - len(line))
    # Print left border without newline
    print(CYAN + border_char + RESET, end='')
    # Type the inner text
    type_text(inner, BOLD + YELLOW)
    # Print right border with newline
    print(CYAN + border_char + RESET)

# Bottom padding
for _ in range(pad_bottom):
    line = ' ' * inner_width
    print(CYAN + border_char + RESET + line + CYAN + border_char + RESET)

# Bottom border
print(CYAN + border_char * total_width + RESET)

# Signature
print()
print(" " * 20 + "— Woody Allen (probably)")