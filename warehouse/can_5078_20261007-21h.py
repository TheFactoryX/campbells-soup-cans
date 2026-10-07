"""
Campbell's Soup Can #5078
Produced: 2026-10-07 21:59:03
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

# ANSI color codes
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
M = '\033[95m'
C = '\033[96m'
W = '\033[97m'
BD = '\033[1m'
RD = '\033[0m'

def p(text, color='reset'):
    sys.stdout.write(eval(f"'{color}'") + text + RD if color != 'reset' else text)
    sys.stdout.flush()

def colorize(text, color_code):
    return color_code + text + RD

def type_out(text, color, delay=0.025):
    for ch in text:
        sys.stdout.write(color + ch + RD)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(title, quote_lines, author):
    w = max(len(title) + 4, max(len(l) for l in quote_lines) + 4, len(author) + 8, 34)
    
    print()
    print(colorize('╔' + '═'*(w-2) + '╗', C))
    
    # Title centered
    tl = len(title)
    pl = (w - 2 - tl) // 2
    pr1 = w - 2 - tl - pl
    print(colorize('║', C) + ' '*pl + colorize(BD + Y + title + RD, C) + ' '*pr1 + colorize('║', C))
    
    print(colorize('╠' + '═'*(w-2) + '╣', C))
    
    # Quote lines
    for line in quote_lines:
        padding = w - 4 - len(line)
        print(colorize('║ ', G) + line + ' '*padding + colorize(' ║', G))
    
    print(colorize('╠' + '═'*(w-2) + '╣', C))
    
    # Author
    auth = '-- ' + author
    ap = w - 4 - len(auth)
    print(colorize('║', M) + ' '*ap + colorize(W + auth + RD, M) + ' ' + colorize('║', M))
    
    print(colorize('╚' + '═'*(w-2) + '╝', C))

# === MAIN ===
print()
print()

# Header with rainbow effect
header = "🎬  WOODY ALLEN'S PHILOSOPHICAL QUOTES  🎬"
rainbow_colors = [R, Y, G, C, B, M]
for i, ch in enumerate(header):
    sys.stdout.write(rainbow_colors[i % len(rainbow_colors)] + ch + RD)
    sys.stdout.flush()
    time.sleep(0.02)
print()
print()

# Contemplation spinner
spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
for i in range(18):
    sys.stdout.write(f"\r  {spinner[i%10]}  Analyzing existential dread...  ")
    sys.stdout.flush()
    time.sleep(0.05)
print("\n")

# Main quote
title = " EXISTENTIAL WISDOM "
quote = [
    "I've been in therapy for 20 years and all I've",
    "learned is that I'm not crazy -- I'm just",
    "thoroughly convinced everyone else is delusional.",
]
author = "Woody Allen (probably)"

print_box(title, quote, author)

print()

# Bonus mini-quotes with colors
print(colorize("  💡 ", Y) + colorize("The problem with being neurotic is that nobody", Y))
print(colorize("     believes you when you finally crack -- they just", Y))
print(colorize("     think you're being funny.", Y))
print()
print(colorize("  🎭 ", C) + colorize("Life is too short to take seriously...", C))
print(colorize("     but long enough to worry about it anyway.", C))
print()
print(colorize("  🧠 ", M) + colorize("\"I don't want to achieve immortality through my", M))
print(colorize("     work; I want to achieve it through not dying.\"", M))
print()
print(colorize("  ☕ ", R) + colorize("I'm not afraid of death; I just don't want to", R))
print(colorize("     be there when it happens. Mainly because I", R))
print(colorize("     haven't finished my lunch.", R))
print()

# Fun footer
print(colorize(BD + "  ~ And remember: ~", C))
time.sleep(0.5)
type_out("  \"The talent for being happy is appreciating and", C, 0.02)
type_out("   liking yourself.\" -- Or at least pretending to.", C, 0.02)
print()