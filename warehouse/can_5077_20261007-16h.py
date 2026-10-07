"""
Campbell's Soup Can #5077
Produced: 2026-10-07 16:29:19
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
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
import os

# ANSI escape codes
class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    CY = '\033[96m'
    W = '\033[97m'
    BLD = '\033[1m'
    DIM = '\033[2m'
    ITAL = '\033[3m'
    RESET = '\033[0m'
    BG = '\033[44m'

def s_print(text, color=C.W, delay=0.025):
    for ch in text:
        sys.stdout.write(color + ch + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_frame(text, color=C.Y):
    lines = text.split('\n')
    w = max(len(l) for l in lines) + 4
    top = color + '╔' + '═' * w + '╗' + C.RESET
    bot = color + '╚' + '═' * w + '╝' + C.RESET
    print(top)
    for l in lines:
        print(color + '║ ' + l.ljust(w) + ' ║' + C.RESET)
    print(bot)

# Quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "To you, I'm an atheist; to God, I'm the Loyal Opposition.",
    "I would not want to belong to any club that would have me as a member.",
    "I'm not crazy, I've just been in a very bad mood for 40 years.",
    "The brain is my second favorite organ.",
    "I find it very draining to go somewhere I've never been before; it always makes me tired.",
    "My brain is my second favorite organ.",
    "I don't want to live on in the hearts of my countrymen; I want to live on in my apartment.",
    "If you want to make God laugh, tell him your plans.",
    "I chose to be absent-when did that become a crime?"
]

quote = random.choice(quotes)

# ASCII art - Woody style neurotic face
face = f"""{C.CY}
         .---.
        /     \\
       | O   O |
       |   >   |
        \\ '-' /
         |   |
        /     \\
       '-------'
{CYAN}      ~ ~ ~ ~ ~ ~ ~
{CYAN}   existential crisis mode: ON
{CYAN}   anxiety level: 9000
{CYAN}   therapist: cancelled appointment
{CYAN}   sandwich: needed urgently
{C.RESET}"""

# Main animation
clear()
print()

# Stage 1: Dots
s_print(C.CY + "." * 20 + C.RESET, C.CY, 0.08)
time.sleep(0.3)

# Stage 2: Thinking
s_print(C.M + "Hmm..." + C.RESET, C.M, 0.12)
time.sleep(0.4)
s_print(C.M + "Well..." + C.RESET, C.M, 0.12)
time.sleep(0.4)

# Stage 3: Face reveal
print(face)
time.sleep(0.6)

# Stage 4: Quote in frame
print()
s_print(C.Y + "═══ WOODY'S WISDOM ═══" + C.RESET, C.Y, 0.04)
print()
draw_frame(quote, C.Y)
print()

# Stage 5: Neurotic commentary
comment = random.choice([
    C.R + "     ...but seriously, though." + C.RESET,
    C.G + "     I need a sandwich." + C.RESET,
    C.B + "     My therapist says I overthink." + C.RESET,
    C.M + "     The universe is indifferent." + C.RESET,
    C.CY + "     I'd like to teach the world to chill." + C.RESET,
])
s_print(comment, C.W, 0.03)
print()
s_print(C.DIM + "     (existential dread delivered fresh)" + C.RESET, C.DIM, 0.02)
print()