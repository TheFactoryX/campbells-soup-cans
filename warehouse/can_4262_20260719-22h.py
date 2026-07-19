"""
Campbell's Soup Can #4262
Produced: 2026-07-19 22:08:57
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
A neurotic masterpiece: Woody Allen meets ANSI art.
Because existence is meaningless, but at least the colors are pretty.
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    RST  = '\033[0m'
    BLD  = '\033[1m'
    DIM  = '\033[2m'
    ITL  = '\033[3m'
    UL   = '\033[4m'
    BLK  = '\033[30m'
    RED  = '\033[31m'
    GRN  = '\033[32m'
    YEL  = '\033[33m'
    BLU  = '\033[34m'
    MAG  = '\033[35m'
    CYN  = '\033[36m'
    WHT  = '\033[37m'
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ─── The Quote (original, Woody-style) ───
QUOTE = (
    "I told my therapist I'm having an existential crisis. "
    "She said, 'That's $300.' I said, 'Can I pay in installments? "
    "I'm not sure I'll be alive for the next one.'"
)

# ─── Woody ASCII Portrait ───
WOODY = r"""
        \   /     
         \ /      
      .--.--.    
     /  o  o \   
    |   __    |   "I don't want to achieve
    |  |  |   |    immortality through my work;
     \  \/  /     I want to achieve it through
      '----'      not dying... preferably
       |  |       before Tuesday."
      _|  |_     
     (______)    
"""

# ─── Typing animation ───
def typewriter(text: str, delay: float = 0.015, color: str = C.WHT):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ─── Sparkle animation ───
def sparkle_line(width: int = 60, cycles: int = 3):
    chars = "✦✧★☆⋆✦✧★☆⋆"
    for _ in range(cycles):
        line = ''.join(random.choice(chars) for _ in range(width))
        sys.stdout.write(f"\r{C.MAG}{line}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.15)
    print()

# ─── Pulsing box ───
def draw_box(content_lines, border_color=C.CYN, bg_color=C.BG_BLK, padding=2):
    max_len = max(len(line) for line in content_lines)
    inner_w = max_len + padding * 2
    top = f"{border_color}┌{'─' * inner_w}┐{C.RST}"
    bot = f"{border_color}└{'─' * inner_w}┘{C.RST}"
    print(top)
    for line in content_lines:
        padded = line.center(max_len)
        print(f"{border_color}│{C.RST}{bg_color}{' ' * padding}{C.RST}{padded}{bg_color}{' ' * padding}{C.RST}{border_color}│{C.RST}")
    print(bot)

# ─── Main spectacle ───
def main():
    # Clear screen dramatically
    print("\033[2J\033[H", end="")
    
    # Opening sparkle
    sparkle_line(70, 2)
    
    # Woody portrait with color
    print(f"{C.YEL}{WOODY}{C.RST}")
    
    # Pause for effect
    time.sleep(0.5)
    
    # The quote in a fancy box
    quote_lines = [
        f"{C.BLD}{C.WHT}WOODY ALLEN'S THERAPY SESSION{C.RST}",
        "",
        f"{C.ITL}{C.CYN}\"I told my therapist I'm having an existential crisis.\"{C.RST}",
        f"{C.ITL}{C.CYN}\"She said, 'That's $300.'\"{C.RST}",
        f"{C.ITL}{C.CYN}\"I said, 'Can I pay in installments?\"{C.RST}",
        f"{C.ITL}{C.CYN}\"I'm not sure I'll be alive for the next one.'\"{C.RST}",
        "",
        f"{C.DIM}{C.MAG}— The neurotic's guide to financial planning —{C.RST}",
    ]
    
    draw_box(quote_lines, border_color=C.MAG, bg_color=C.BG_BLK)
    
    # Closing sparkle
    time.sleep(0.3)
    sparkle_line(70, 2)
    
    # Final philosophical footnote
    print()
    footnotes = [
        f"{C.DIM}Philosophical footnote: {C.RST}{C.ITL}Existence precedes essence, but anxiety precedes both.{C.RST}",
        f"{C.DIM}Therapist's note: {C.RST}{C.ITL}Patient shows signs of... being alive. Tragic.{C.RST}",
        f"{C.DIM}Insurance status: {C.RST}{C.RED}{C.BLD}DENIED{C.RST}{C.DIM} (pre-existing condition: mortality){C.RST}",
    ]
    for fn in footnotes:
        typewriter(fn, 0.008)
        time.sleep(0.15)
    
    # Final sign-off
    print()
    typewriter(f"{C.YEL}{C.BLD}◉ {C.RST}{C.ITL}This program has been brought to you by existential dread and caffeine.{C.RST}{C.YEL}{C.BLD} ◉{C.RST}", 0.01)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}Interrupted. Even the code has abandonment issues.{C.RST}")
        sys.exit(130)