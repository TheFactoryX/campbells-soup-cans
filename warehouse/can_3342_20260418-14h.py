"""
Campbell's Soup Can #3342
Produced: 2026-04-18 14:58:10
Worker: Elephant (openrouter/elephant-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

def typewriter(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Woody-Allen-style philosophical quote
quote = (
    "I am terrified by the thought that the universe is indifferent, "
    "yet even more terrified by the possibility that it might be listening."
)

colors = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'cyan': '\033[96m',
    'yellow': '\033[93m',
    'magenta': '\033[95m',
    'red': '\033[91m',
    'green': '\033[92m',
    'blue': '\033[94m',
    'pink': '\033[38;2;255;105;180m',
    'dim': '\033[2m',
}

def draw_star(size=5):
    star = ""
    for i in range(size):
        star += "✦ " * (i + 1) + "\n"
    for i in range(size - 2, -1, -1):
        star += "✦ " * (i + 1) + "\n"
    return star

def draw_border(text_lines, width=70, color=colors['cyan']):
    border_top = color + "╔" + "═" * (width - 2) + "╗" + colors['reset']
    border_bottom = color + "╚" + "═" * (width - 2) + "╝" + colors['reset']
    padded_lines = []
    for line in text_lines:
        padding = width - 2 - len(line)
        left = padding // 2
        right = padding - left
        padded_lines.append(color + "║" + " " * left + line + " " * right + "║" + colors['reset'])
    return [border_top] + padded_lines + [border_bottom]

def main():
    print("\033c", end="")  # Clear screen
    lines = []
    lines.append(" " * 18 + colors['pink'] + "🧠 WOODY'S WISDOM 🧠" + colors['reset'])
    lines.append(" ")

    # ASCII Constellations
    star_field = draw_star(4)
    for row in star_field.splitlines():
        lines.append(" " * 10 + colors['yellow'] + row + colors['reset'])
    lines.append(" ")

    # Split quote into chunks
    chunks = [quote[i:i+60] for i in range(0, len(quote), 60)]
    for chunk in chunks:
        lines.append(" " * 4 + colors['cyan'] + chunk + colors['reset'])
        lines.append(" ")

    # Tiny self-deprecating footnote
    lines.append(" " * 20 + colors['dim'] + colors['magenta'] + "— (c) Woody, probably. Or was it Schrödinger? —" + colors['reset'])

    # Draw border around content
    bordered = draw_border(lines, color=colors['blue'])

    # Animate printing
    for line in bordered:
        typewriter(line, delay=0.015)
        time.sleep(0.05)

    # Twinkle cursor
    for _ in range(3):
        time.sleep(0.3)
        print(colors['green'] + "✦" + colors['reset'], end='', flush=True)
    print()

if __name__ == "__main__":
    main()