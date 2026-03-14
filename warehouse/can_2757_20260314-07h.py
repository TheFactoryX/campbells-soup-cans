"""
Campbell's Soup Can #2757
Produced: 2026-03-14 07:50:35
Worker: Anthropic: Claude Opus 4.5 (anthropic/claude-opus-4.5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI escape codes for colors
class Colors:
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    BLINK = '\033[5m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def animate_thinking():
    frames = ['🤔', '😰', '😅', '🥴', '😬']
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f'\r  {frame} Existential crisis loading... ')
            sys.stdout.flush()
            time.sleep(0.3)
    print()

# The quote
quote = "I tried meditation once, but my anxiety got anxious about relaxing, and then I started worrying that I wasn't worrying enough about important things, so I went back to panicking — at least that felt productive."

# ASCII art glasses (Woody Allen's signature look)
glasses = r"""
    .-~~~-.
  .'       '.
  |  O   O  |
  |    L    |
  |  \___/  |
  '.       .'
    '-----'
"""

# Main display
clear_screen()

print(f"\n{Colors.CYAN}{'═' * 70}{Colors.RESET}")
print(f"{Colors.YELLOW}{Colors.BOLD}")
print(glasses)
print(f"{Colors.RESET}")

animate_thinking()

print(f"\n{Colors.MAGENTA}  ╔{'═' * 66}╗{Colors.RESET}")
print(f"{Colors.MAGENTA}  ║{' ' * 66}║{Colors.RESET}")

# Word wrap the quote
words = quote.split()
lines = []
current_line = ""
for word in words:
    if len(current_line) + len(word) + 1 <= 62:
        current_line += (" " if current_line else "") + word
    else:
        lines.append(current_line)
        current_line = word
if current_line:
    lines.append(current_line)

print(f"{Colors.MAGENTA}  ║{Colors.RESET}  {Colors.WHITE}{Colors.BOLD}\"", end="")

for i, line in enumerate(lines):
    if i == 0:
        typewriter(line, 0.02)
        print(f"{Colors.RESET}")
    elif i == len(lines) - 1:
        print(f"{Colors.MAGENTA}  ║{Colors.RESET}   {Colors.WHITE}{Colors.BOLD}", end="")
        typewriter(line + "\"", 0.02)
        print(f"{Colors.RESET}")
    else:
        print(f"{Colors.MAGENTA}  ║{Colors.RESET}   {Colors.WHITE}{Colors.BOLD}", end="")
        typewriter(line, 0.02)
        print(f"{Colors.RESET}")

print(f"{Colors.MAGENTA}  ║{' ' * 66}║{Colors.RESET}")
print(f"{Colors.MAGENTA}  ║{Colors.RESET}{' ' * 40}{Colors.YELLOW}{Colors.DIM}— Woody Allen (style){Colors.RESET}{' ' * 5}{Colors.MAGENTA}║{Colors.RESET}")
print(f"{Colors.MAGENTA}  ╚{'═' * 66}╝{Colors.RESET}")

# Animated neurotic footnote
print()
time.sleep(0.5)
footnotes = [
    f"{Colors.DIM}  * Not an actual Woody Allen quote, but my therapist{Colors.RESET}",
    f"{Colors.DIM}    says I shouldn't let that stop me from sharing.{Colors.RESET}",
    f"{Colors.DIM}  * She also says I over-explain things. Case in point.{Colors.RESET}"
]

for note in footnotes:
    print(note)
    time.sleep(0.4)

print(f"\n{Colors.CYAN}{'═' * 70}{Colors.RESET}\n")

# Final animated touch
emojis = "😰🎬📽️🎭✨"
for emoji in emojis:
    sys.stdout.write(f'\r  {emoji} ')
    sys.stdout.flush()
    time.sleep(0.2)
print()