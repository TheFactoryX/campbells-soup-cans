"""
Campbell's Soup Can #3836
Produced: 2026-05-31 23:31:08
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ─── ANSI Colors ───────────────────────────────────────
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
W = "\033[97m"
D = "\033[90m"
X = "\033[0m"
BD = "\033[1m"

# ─── Woody Allen Quote ───────────────────────────────
quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
author = "Woody Allen"

# ─── ASCII Art Theater Mask ───────────────────────────
mask = f"""
{D}        .-""""""-.
       /          \\
      |   {R}O      O{D}  |
      |     {R}\\___/{D}    |
       \\          /
        '-......-'{X}"""

# ─── Animated Build ─────────────────────────────────
import time

# Clear screen
print("\033[2J\033[H", end="")

# Fade in the theater
frames = [
    f"\n{D}    🎭{X}",
    f"\n{D}   🎭 {X}",
    f"\n{D}  🎭  {X}",
    f"\n{D} 🎭   {X}",
    f"\n{D}🎭    {X}",
]

for frame in frames:
    sys.stdout.write("\033[2J\033[H")
    print(frame)
    time.sleep(0.15)

# Final display
sys.stdout.write("\033[2J\033[H")

# ─── The Big Reveal ───────────────────────────────
print(f"""
{C}╔{'═'*60}╗
║{' '*60}║
║{BD}{Y}  🎭  WOODY ALLEN ON EXISTENTIAL DESPAIR  🎭{X}{C}  ║
║{' '*60}║
╚{'═'*60}╝{X}

{D}        .-""""""-.
       /   {R}O      O{D}  \\
      |     {R}\\___/{D}    |
       \\          /
        '-......-'{X}

{C}  ┌{'─'*58}┐
  │{X}                                                          {C}│{X}""")

# Type out the quote word by word
words = quote.split()
line = "  "
for i, word in enumerate(words):
    test_line = line + (" " if line.strip() else "") + word
    if len(test_line) > 56:
        padding = 58 - len(line.strip())
        print(f"{C}│{X} {line}{' '*padding}{C}│{X}")
        line = "  " + word
    else:
        line = test_line
padding = 58 - len(line.strip())
print(f"{C}│{X} {line}{' '*padding}{C}│{X}")

print(f"""{C}  │                                                          │
  │{' '*58}│
  │{X}                    {M}~ {author}{X}{' '*(56-len(author)-2)}{C}│
  └{'─'*58}┘{X}

{G}  💡 Life is full of misery, loneliness, and suffering
     — and it's all over much too soon.{X}

{D}  ════════════════════════════════════════════════════════════
     Press Ctrl+C to escape the void.{X}
""")