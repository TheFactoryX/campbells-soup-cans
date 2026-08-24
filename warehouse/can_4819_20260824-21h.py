"""
Campbell's Soup Can #4819
Produced: 2026-08-24 21:44:00
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic existential crisis, beautifully formatted.
Pure Python. No dependencies. Just anxiety and ANSI codes.
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    RST = '\033[0m'
    BLD = '\033[1m'
    DIM = '\033[2m'
    ITL = '\033[3m'
    UL  = '\033[4m'
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ─── The Quote ───
QUOTE = (
    "I took a speed-reading course and read War and Peace in twenty minutes.\n"
    "It involves Russia."
)

ATTRIBUTION = "— Woody Allen (probably, or maybe just my therapist)"

# ─── ASCII Art: A tiny neurotic stick figure ───
WOODY = r"""
       \  |  /
        \ | /
      __  ^  __
     /  \___/  \
    |  (o) (o)  |   "Why is there something
    |     ^     |    instead of nothing?
    |  \_____/  |    And why is the nothing
     \_________/     so expensive?"
      |     |
     _/ \___/ \_
"""

# ─── Animation Frames for "thinking" dots ───
THINKING_FRAMES = [
    f"{C.DIM}  .{C.RST}",
    f"{C.DIM}  ..{C.RST}",
    f"{C.DIM}  ...{C.RST}",
    f"{C.DIM}   ..{C.RST}",
    f"{C.DIM}    .{C.RST}",
    f"{C.DIM}     {C.RST}",
]

# ─── Helpers ───
def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_up(n=1):
    print(f'\033[{n}A', end='')

def typewriter(text, delay=0.03, color='', end='\n'):
    for ch in text:
        print(f"{color}{ch}{C.RST}", end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def glitch_text(text, iterations=3):
    """Briefly glitch the text for effect."""
    chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"
    for _ in range(iterations):
        glitched = ''.join(random.choice(chars) if random.random() < 0.1 else c for c in text)
        print(f"\r{C.RED}{glitched}{C.RST}", end='', flush=True)
        time.sleep(0.05)
    print(f"\r{text}", end='', flush=True)

# ─── Main Show ───
def main():
    hide_cursor()
    try:
        clear_screen()
        
        # 1. Title card with dramatic pause
        print(f"\n{C.BG_BLK}{C.YEL}{C.BLD}  ═══════════════════════════════════════  {C.RST}")
        print(f"{C.BG_BLK}{C.YEL}{C.BLD}     A WOODY ALLEN MOMENT OF CLARITY      {C.RST}")
        print(f"{C.BG_BLK}{C.YEL}{C.BLD}  ═══════════════════════════════════════  {C.RST}\n")
        time.sleep(0.8)
        
        # 2. The stick figure appears line by line
        for line in WOODY.strip('\n').split('\n'):
            print(f"{C.CYN}{line}{C.RST}")
            time.sleep(0.15)
        time.sleep(0.5)
        
        # 3. Thinking animation
        print(f"\n{C.MAG}{C.ITL}  Contemplating existence{C.RST}", end='', flush=True)
        for _ in range(2):
            for frame in THINKING_FRAMES:
                print(f"\r{C.MAG}{C.ITL}  Contemplating existence{frame}{C.RST}", end='', flush=True)
                time.sleep(0.25)
        print(f"\r{C.MAG}{C.ITL}  Contemplating existence... {C.GRN}✓{C.RST}")
        time.sleep(0.4)
        
        # 4. The quote - typewriter style with color cycling
        print(f"\n{C.BLD}{C.WHT}  ┌{'─' * 58}┐{C.RST}")
        print(f"{C.BLD}{C.WHT}  │{C.RST} {' ' * 58} {C.BLD}{C.WHT}│{C.RST}")
        move_up(1)
        print(f"{C.BLD}{C.WHT}  │{C.RST} ", end='', flush=True)
        
        # Split quote into lines
        quote_lines = QUOTE.split('\n')
        colors = [C.YEL, C.CYN, C.GRN, C.MAG, C.BLU]
        
        for i, line in enumerate(quote_lines):
            color = colors[i % len(colors)]
            typewriter(line, delay=0.02, color=color, end='')
            print(f" {C.BLD}{C.WHT}│{C.RST}")
            if i < len(quote_lines) - 1:
                print(f"{C.BLD}{C.WHT}  │{C.RST} ", end='', flush=True)
        
        print(f"{C.BLD}{C.WHT}  │{C.RST} {' ' * 58} {C.BLD}{C.WHT}│{C.RST}")
        print(f"{C.BLD}{C.WHT}  └{'─' * 58}┘{C.RST}")
        time.sleep(0.6)
        
        # 5. Attribution with a little flair
        print(f"\n{C.DIM}{C.ITL}  {ATTRIBUTION}{C.RST}")
        time.sleep(0.4)
        
        # 6. Final existential footer
        footers = [
            "  My analyst says I have a preoccupation with death. \n  He also says I have a preoccupation with life. \n  I'm seeing a pattern here.",
            "  The universe is indifferent. My landlord is not. \n  Guess which one sends threatening letters?",
            "  I don't believe in an afterlife, \n  but I'm bringing a change of underwear just in case.",
            "  Existential dread: $0. \n  Therapy: $200/hr. \n  Realizing the therapist needs therapy: Priceless.",
        ]
        footer = random.choice(footers)
        print(f"\n{C.BLU}{C.DIM}{footer}{C.RST}\n")
        
        # 7. A final nervous blink
        for _ in range(3):
            print(f"\r{C.RED}{C.BLD}  █ PANIC █{C.RST}", end='', flush=True)
            time.sleep(0.15)
            print(f"\r{' ' * 15}", end='', flush=True)
            time.sleep(0.15)
        print(f"\r{C.GRN}{C.BLD}  ✓ Acceptance (temporary){C.RST}")
        
        print(f"\n{C.DIM}  [Press Enter to resume worrying...]{C.RST}")
        input()
        
    finally:
        show_cursor()
        clear_screen()
        print(f"{C.ITL}The anxiety has been saved to /dev/null. Have a nervous day.{C.RST}\n")

if __name__ == '__main__':
    main()