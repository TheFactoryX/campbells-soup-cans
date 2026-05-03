"""
Campbell's Soup Can #3552
Produced: 2026-05-03 17:08:12
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def fade_in(text, delay=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def colorize(text, code):
    return f"\033[{code}m{text}\033[0m"

def brain_wave():
    waves = ["~", "∿", "≈", "∼", "∽", "≈"]
    return "".join(random.choice(waves) for _ in range(30))

def neuron_spark():
    sparks = ["✨", "⚡", "💡", "🌟", "🧠", "💭"]
    return random.choice(sparks)

# ANSI codes
BOLD = "1"
ITALIC = "3"
CYAN = "96"
MAGENTA = "95"
YELLOW = "93"
DIM = "2"
RED = "91"

print("\033[2J\033[H")  # Clear screen

# Header ASCII art
header = [
    "   ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀",
    "   ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀",
    "   ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀",
    "   ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀",
    "   ⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀",
    "   ⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀",
    "   ⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀",
    "   ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇",
    "   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
    "   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
]

for line in header:
    fade_in(colorize(line, CYAN), 0.008)
    time.sleep(0.02)

print()

# Title
title = "  🥶  WOODY'S EXISTENTIAL CRISIS GENERATOR v.0.42 (BETA)  🥶"
print(colorize(title.center(70), f"{BOLD};{YELLOW}"))
print(colorize("═" * 70, DIM))
print()

# Quote box
quote = (
    "I've been having such vivid nightmares about my own mortality "
    "that I woke up the other night screaming—only to realize I was "
    "still asleep, which meant my subconscious had double-killed me "
    "before I even got to the real thing. The universe is clearly "
    "passive-aggressive, and frankly, my therapist's been no help—"
    "she keeps asking me to 'embrace the void,' but the void keeps "
    "asking why I'm wearing socks that don't match. So now I'm "
    "pretty sure existence is just God's way of procrastinating, "
    "and we're all the sticky notes on His fridge reminding Him "
    "to do something meaningful, but He's too busy rewatching "
    "the same Tuesday over and over because He's afraid of what "
    "Wednesday might bring. The only thing I know for certain is "
    "that if I die before I finish this sentence, at least I'll "
    "never have to decide what to wear to my own funeral—"
    "because I'll be dead. And honestly? Liberation."
)

# Decorated quote box
width = 70
lines = []
words = quote.split()
current_line = ""
for word in words:
    if len(current_line) + len(word) + 1 <= width - 4:
        current_line += (" " if current_line else "") + word
    else:
        lines.append(current_line)
        current_line = word
if current_line:
    lines.append(current_line)

border = colorize("╭" + "─" * (width - 2) + "╮", MAGENTA)
print(border)

for i, line in enumerate(lines):
    padded = f"│ {line.ljust(width - 4)} │"
    if i == len(lines) // 2:
        # Sprinkle a brain spark in the middle
        padded = f"│ {line} {neuron_spark()}".ljust(width - 1) + "│"
    print(colorize(padded, f"{ITALIC};{YELLOW}" if i % 2 == 0 else YELLOW))
    time.sleep(0.08)

footer = colorize("╰" + "─" * (width - 2) + "╯", MAGENTA)
print(footer)
print()

# Signature
sig_line = brain_wave()
print(colorize(sig_line.center(70), DIM))
print(colorize("         — Woody (the anxious one) 💭".rjust(45), f"{ITALIC};{CYAN}"))
print(colorize("           circa last Tuesday, probably".rjust(48), DIM))
print()

# Epilogue animation
epilogue = [
    "   The void winks back. It's wearing a monocle.",
    "   You check your email. Nothing. Not even spam.",
    "   A lone sock rolls under the refrigerator.",
    "   You wonder if you locked the front door in 1997.",
    "   The refrigerator hums. It knows something.",
]

for line in epilogue:
    fade_in(colorize(line.center(70), f"{DIM};{CYAN}"), 0.02)
    time.sleep(0.3)

print()
print(colorize("   [ Press Ctrl+C to wake up (or don't) ]".center(70), DIM))

# Gentle pulse
try:
    while True:
        for c in [CYAN, MAGENTA, YELLOW]:
            sys.stdout.write(f"\r{colorize('   ♥'.center(70), f'{DIM};{c}')}")
            sys.stdout.flush()
            time.sleep(0.4)
except KeyboardInterrupt:
    print(f"\n{colorize('   ...and darkness. (refresh to try again)', DIM)}")