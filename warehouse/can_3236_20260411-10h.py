"""
Campbell's Soup Can #3236
Produced: 2026-04-11 10:55:50
Worker: MoonshotAI: Kimi K2 0905 (moonshotai/kimi-k2-0905)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, random, sys, textwrap, os

def colorize(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def neon(r, g, b, text, glow=1):
    base = colorize(r, g, b, text)
    if glow:
        shadow = colorize(r//3, g//3, b//3, text.replace("█", "░").replace("▓", "░"))
        return "\n".join(shadow + "\n" + base)
    return base

def slow_type(text, delay=0.03, jitter=0.02):
    for ch in text:
        if ch == "\n":
            time.sleep(0.2)
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter))
        if ch in ".!?":
            time.sleep(0.15)

def fade_in_quote(lines):
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            ch = lines[row][col]
            # fade character
            for gray in [8, 4, 2, 0]:
                sys.stdout.write(f"\033[{row+3};{col+3}H{colorize(gray,gray,gray*3,ch)}")
                sys.stdout.flush()
                time.sleep(0.005)
            sys.stdout.write(f"\033[{row+3};{col+3}H{ch}")
            sys.stdout.flush()

# clear
print("\033[2J", end="")

# curtain
for i in range(0, 40, 2):
    print(colorize(60, 30, 90, "█" * (i + 1)).center(80))
    time.sleep(0.05)
print("\n\n")

quote = [
    "I don't mind dying,\n",
    "I just don't want to be there\n",
    "when it happens—\n",
    "especially if there's a reception line."
]

# ascii frame
frame = colorize(180, 40, 100, """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

sys.stdout.write("\033[5;0H")  # move cursor
print(frame)

# fade in quote inside frame
fade_in_quote([line.rstrip() for line in quote])

# signature flicker
sig = "  — Woody Allen (probably)  "
sig_color = lambda t: colorize(random.randint(200,255), random.randint(100,180), random.randint(120,200), t)
sys.stdout.write("\033[17;50H")
for _ in range(25):
    sys.stdout.write(sig_color(sig[random.randint(0,len(sig)-1)]))
    sys.stdout.flush()
    time.sleep(0.08)

# final flicker and hold
time.sleep(0.4)
sys.stdout.write("\033[17;50H" + colorize(255,180,200, sig))
sys.stdout.flush()

# existential cursor blink
while True:
    sys.stdout.write(f"\033[?25h" if random.random() > 0.7 else "\033[?25l")
    time.sleep(0.3)