"""
Campbell's Soup Can #2529
Produced: 2026-03-02 19:06:27
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ANSI color codes
BLUE = '\033[94m'
BOLD_BLUE = '\033[1;94m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
BG_NERVY = '\033[48;5;57m'  # Dark blue background
TEXT_GOLD = '\033[38;5;220m'  # Gold text
RESET = '\033[0m'

clear_screen()

# ASCII Art: Neurotic Coffee Cup (Woody's essential accessory)
coffee_art = [
    "            " + CYAN + "~" + RESET + "              ",
    "           " + CYAN + "~ ~" + RESET + "             ",
    "          " + CYAN + "~   ~" + RESET + "            ",
    "           " + CYAN + "~ ~" + RESET + "             ",
    "            " + CYAN + "~" + RESET + "              ",
    "        " + YELLOW + ".-------." + RESET + "         ",
    "        " + YELLOW + "|  " + MAGENTA + "o" + YELLOW + "  |" + RESET + "         ",
    "        " + YELLOW + "|  " + MAGENTA + "o" + YELLOW + "  |" + RESET + "         ",
    "        " + YELLOW + "`-------´" + RESET + "         ",
    "          " + YELLOW + "_______" + RESET + "           "
]

for line in coffee_art:
    print(line)
print()

# Create a trembling box effect with shaky borders
box_width = 50
top_border = BOLD_BLUE + '┎' + ''.join([['-', '_'][i % 2] for i in range(box_width)]) + '┒' + RESET
bottom_border = BOLD_BLUE + '┖' + ''.join([['-', '_'][i % 2 + 1] for i in range(box_width)]) + '┚' + RESET

# Philosophical quote in Woody Allen style
quote = "I'm not afraid of death; I'm just not sure I want to be there when my therapist finally figures out what's wrong with me."

# Break into lines while preserving words
words = quote.split()
lines = []
current_line = []
for word in words:
    if len(' '.join(current_line + [word])) <= box_width - 4:  # Account for borders
        current_line.append(word)
    else:
        lines.append(' '.join(current_line))
        current_line = [word]
if current_line:
    lines.append(' '.join(current_line))

# Add empty line above quote for spacing
lines.insert(0, "")
lines.append("")

# Print the trembling box with typewriter effect
print(top_border)
for i, line in enumerate(lines):
    # Randomly tremble the side borders
    left_shake = ' ' if i % 3 == 0 else ''
    right_shake = ' ' if i % 3 == 2 else ''
    
    # Center text with pulsing background
    padded = line.center(box_width - 4)
    bg_pulse = BG_NERVY if i % 2 == 0 else '\033[48;5;21m'  # Dark blue vs deep purple
    
    sys.stdout.write(BLUE + '┃' + RESET + left_shake)
    sys.stdout.write(bg_pulse + TEXT_GOLD)
    typewriter(padded, 0.05 if i > 0 and i < len(lines) - 1 else 0.00)  # Faster for empty lines
    sys.stdout.write(RESET + BLUE + right_shake + '┃' + RESET + '\n')
print(bottom_border)

# Final touch: Add neurotic blinking cursor effect after quote
time.sleep(0.3)
for _ in range(3):
    sys.stdout.write(BLUE + "    (I need more coffee...)" + RESET)
    sys.stdout.flush()
    time.sleep(0.4)
    sys.stdout.write('\r' + ' ' * 25 + '\r')
    sys.stdout.flush()
    time.sleep(0.2)
sys.stdout.write(MAGENTA + "    (Why is everything so complicated?)" + RESET)
sys.stdout.flush()