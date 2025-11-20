"""
Campbell's Soup Can #393
Produced: 2025-11-20 04:35:53
Worker: Anthropic: Claude Sonnet 4 (anthropic/claude-sonnet-4)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def rainbow_text(text):
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    colored_text = ""
    for i, char in enumerate(text):
        if char != ' ':
            colored_text += colors[i % len(colors)] + char
        else:
            colored_text += char
    return colored_text + '\033[0m'

def animated_glasses():
    frames = ["👓", "🤓", "😵‍💫", "🤔"]
    for frame in frames:
        print(f"\r{frame}", end='', flush=True)
        time.sleep(0.3)
    print()

# Clear screen
print('\033[2J\033[H')

# Title animation
print('\033[95m' + '=' * 70 + '\033[0m')
print('\033[96m' + '  WOODY ALLEN\'S NEUROTIC WISDOM GENERATOR'.center(70) + '\033[0m')
print('\033[95m' + '=' * 70 + '\033[0m')
print()

# Animated thinking
print('\033[93m' + 'Woody is thinking...'.center(70) + '\033[0m')
for i in range(3):
    animated_glasses()

print('\n' + '\033[92m' + '💭 PROFOUND NEUROSIS DETECTED 💭'.center(70) + '\033[0m\n')

# The main quote box
quote = "I took a philosophy course once. The professor asked 'What is the meaning of life?' I raised my hand and said 'To find parking.' He gave me an A+ and then had an existential crisis."

# Create a fancy box
box_width = 60
print('\033[94m' + '┌' + '─' * (box_width - 2) + '┐' + '\033[0m')

# Wrap the quote
words = quote.split()
lines = []
current_line = ""

for word in words:
    if len(current_line + word + " ") <= box_width - 4:
        current_line += word + " "
    else:
        lines.append(current_line.strip())
        current_line = word + " "
lines.append(current_line.strip())

# Print each line with typewriter effect
for line in lines:
    print('\033[94m│\033[0m ', end='')
    typewriter_effect(rainbow_text(line.ljust(box_width - 4)), 0.03)

print('\033[94m' + '└' + '─' * (box_width - 2) + '┘' + '\033[0m')

# Attribution
time.sleep(0.5)
print('\n' + '\033[97m' + '- Not Actually Woody Allen'.rjust(70) + '\033[0m')
print('\033[90m' + '  (but spiritually accurate)'.rjust(70) + '\033[0m')

# Final flourish
print('\n' + '\033[93m' + '✨' * 35 + '\033[0m')

# Blinking reminder
for i in range(3):
    print('\r\033[91m💡 Remember: Existence is optional, anxiety is mandatory! 💡\033[0m', end='', flush=True)
    time.sleep(0.5)
    print('\r' + ' ' * 60, end='', flush=True)
    time.sleep(0.3)

print('\r\033[91m💡 Remember: Existence is optional, anxiety is mandatory! 💡\033[0m')
print('\n\033[95m' + 'Thank you for attending my neurosis.' + '\033[0m')