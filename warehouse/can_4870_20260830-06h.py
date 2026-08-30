"""
Campbell's Soup Can #4870
Produced: 2026-08-30 06:40:27
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
Woody Allen Quote Generator - A neurotic masterpiece in ANSI
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

# ─── Woody's Iconic Glasses ASCII ───
GLASSES = [
    f"{C.CYN}       ▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄{C.RST}",
    f"{C.CYN}    ▄█████████▄   ▄█████████▄{C.RST}",
    f"{C.CYN}   █████████████ █████████████{C.RST}",
    f"{C.CYN}   █████████████ █████████████{C.RST}",
    f"{C.CYN}    ▀█████████▀   ▀█████████▀{C.RST}",
    f"{C.CYN}       ▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀{C.RST}",
    f"{C.CYN}           ▄▄▄▄▄▄▄{C.RST}",
    f"{C.CYN}      ▄█████████████▄{C.RST}",
    f"{C.CYN}     █████████████████{C.RST}",
    f"{C.CYN}     █████████████████{C.RST}",
    f"{C.CYN}      ▀█████████████▀{C.RST}",
    f"{C.CYN}         ▀▀▀▀▀▀▀{C.RST}",
]

# ─── The Quote (Original Woody-style) ───
QUOTE_LINES = [
    ("I told my analyst I have a", C.WHT),
    ("fear of commitment. He said,", C.WHT),
    ("'That'll be $300.' I said,", C.WHT),
    ("'Can I pay in installments?'", C.YEL + C.BLD),
    ("", C.RST),
    ("He said, 'We don't do", C.WHT),
    ("installments. But we do", C.WHT),
    ("accept existential dread", C.MAG + C.ITL),
    ("as currency.'", C.MAG + C.ITL),
    ("", C.RST),
    ("So I gave him three", C.WHT),
    ("sleepless nights and", C.WHT),
    ("a recurring dream about", C.CYN + C.ITL),
    ("my mother.", C.CYN + C.ITL),
]

# ─── Decorative Elements ───
STARS = "✦ ✧ ★ ☆ ✦ ✧ ★ ☆ ✦ ✧ ★ ☆ ✦"
DIVIDER = f"{C.DIM}{'─' * 52}{C.RST}"

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=C.WHT, delay=0.02, newline=True):
    """Print text with typewriter effect."""
    for char in text:
        print(f"{color}{char}{C.RST}", end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def fade_in_text(text, color=C.WHT, steps=10):
    """Fade in text by gradually increasing brightness."""
    for i in range(steps + 1):
        brightness = i / steps
        # Simulate brightness with color intensity
        if brightness < 0.3:
            c = C.DIM + color
        elif brightness < 0.7:
            c = color
        else:
            c = C.BLD + color
        print(f'\r{c}{text}{C.RST}', end='', flush=True)
        time.sleep(0.03)
    print()

def draw_glasses_animation():
    """Draw glasses with a fun build-up animation."""
    for i, line in enumerate(GLASSES):
        print(f'\033[{i+3};1H{line}')
        time.sleep(0.05)
    time.sleep(0.3)

def draw_boxed_quote():
    """Draw the quote in a nice animated box."""
    box_width = 56
    top = f"{C.CYN}┌{'─' * box_width}┐{C.RST}"
    bottom = f"{C.CYN}└{'─' * box_width}┘{C.RST}"
    
    print(f"\n{top}")
    
    for line_text, line_color in QUOTE_LINES:
        padding = box_width - len(line_text)
        left_pad = padding // 2
        right_pad = padding - left_pad
        line = f"{C.CYN}│{C.RST}{' ' * left_pad}{line_color}{line_text}{C.RST}{' ' * right_pad}{C.CYN}│{C.RST}"
        print(line)
        time.sleep(0.15)
    
    print(bottom)

def sparkle_animation(duration=2.0):
    """Create a sparkle effect around the quote."""
    start = time.time()
    sparkles = ['✦', '✧', '★', '☆', '✨', '⋆', '✦', '✧']
    while time.time() - start < duration:
        for i in range(3):
            line = ''.join(random.choice(sparkles) + ' ' for _ in range(20))
            print(f'\r{C.YEL}{line}{C.RST}', end='', flush=True)
            time.sleep(0.1)
        print('\r' + ' ' * 40 + '\r', end='')

def neurotic_typing():
    """Type the quote with Woody-esque hesitations."""
    hesitations = ["...", " um ", " uh ", " wait ", " no, ", " actually "]
    
    print(f"\n{C.DIM}Internal monologue:{C.RST}\n")
    
    for line_text, line_color in QUOTE_LINES:
        if not line_text.strip():
            print()
            time.sleep(0.3)
            continue
            
        # Add random hesitation
        if random.random() < 0.3:
            h = random.choice(hesitations)
            typewriter(h, C.RED + C.ITL, 0.05, False)
        
        typewriter(line_text, line_color, 0.015)
        time.sleep(0.1)

def main():
    # Setup
    clear_screen()
    hide_cursor()
    
    try:
        # Title card
        print(f"\n{C.BLD}{C.MAG}{'=' * 60}{C.RST}")
        print(f"{C.BLD}{C.MAG}||{C.RST} {C.YEL}WOODY ALLEN QUOTE GENERATOR v1.0{C.RST} {C.MAG}||{C.RST}")
        print(f"{C.BLD}{C.MAG}{'=' * 60}{C.RST}")
        print(f"{C.DIM}    \"Neurosis is just high-altitude thinking...\"{C.RST}\n")
        
        # Draw glasses
        print(f"{C.CYN}    Rendering iconic eyewear...{C.RST}\n")
        draw_glasses_animation()
        
        # Pause for effect
        time.sleep(0.5)
        
        # Method 1: Typewriter with hesitations
        neurotic_typing()
        
        print(f"\n{DIVIDER}")
        
        # Method 2: Boxed version
        print(f"\n{C.CYN}Formatted for your refrigerator:{C.RST}")
        draw_boxed_quote()
        
        print(f"\n{DIVIDER}")
        
        # Final sparkle
        print(f"\n{C.YEL}✦ Quote certified neurotic ✦{C.RST}\n")
        sparkle_animation(1.5)
        
        # Signature
        print(f"\n{C.DIM}— Generated at 3AM during an existential crisis{C.RST}")
        print(f"{C.DIM}  (Analyst not included. Batteries sold separately.){C.RST}\n")
        
    finally:
        show_cursor()

if __name__ == '__main__':
    main()