"""
Campbell's Soup Can #4706
Produced: 2026-08-19 21:41:07
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
Woody Allen Philosophical Quote Generator
A neurotic exploration of existence, one ANSI escape code at a time.
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    RST  = '\033[0m'
    BOLD = '\033[1m'
    DIM  = '\033[2m'
    ITAL = '\033[3m'
    UL   = '\033[4m'
    BLINK = '\033[5m'
    
    # Foreground
    BLK  = '\033[30m'
    RED  = '\033[31m'
    GRN  = '\033[32m'
    YEL  = '\033[33m'
    BLU  = '\033[34m'
    MAG  = '\033[35m'
    CYN  = '\033[36m'
    WHT  = '\033[37m'
    GRY  = '\033[90m'
    LR   = '\033[91m'
    LG   = '\033[92m'
    LY   = '\033[93m'
    LB   = '\033[94m'
    LM   = '\033[95m'
    LC   = '\033[96m'
    LW   = '\033[97m'
    
    # Background
    BBG  = '\033[40m'
    RBG  = '\033[41m'
    GBG  = '\033[42m'
    YBG  = '\033[43m'
    BBG2 = '\033[44m'
    MBG  = '\033[45m'
    CBG  = '\033[46m'
    WBG  = '\033[47m'

# ─── Woody's Face (ASCII) ───
WOODY = f"""
{C.GRY}         .--.            {C.RST}
{C.GRY}        / {C.WHT}..{C.GRY} \\           {C.RST}
{C.GRY}       | {C.YEL}@@{C.GRY} |           {C.RST}   {C.ITAL}"I'm not afraid of death.{C.RST}
{C.GRY}       | {C.CYN}\\/{C.GRY} |           {C.RST}   {C.ITAL}I just don't want to be{C.RST}
{C.GRY}        \\__/            {C.RST}   {C.ITAL}there when it happens."{C.RST}
{C.GRY}       _||||_           {C.RST}
{C.DIM}     .' |||| '.         {C.RST}
{C.DIM}    /  ||||  \\        {C.RST}
{C.DIM}   |   ||||   |       {C.RST}
{C.DIM}    \\  ||||  /        {C.RST}
{C.DIM}     '.____.'         {C.RST}
"""

# ─── The Quote (Original Woody-style) ───
QUOTE_LINES = [
    ("I've developed a new philosophy:", C.CYN, False),
    ("I only dread the future on Tuesdays.", C.LY, True),
    ("", None, False),
    ("Monday's too early for existential dread,", C.GRY, False),
    ("Wednesday I have my analyst,", C.GRY, False),
    ("Thursday's reserved for hypochondria,", C.GRY, False),
    ("Friday I'm too tired to care,", C.GRY, False),
    ("And weekends? Weekends are for", C.GRY, False),
    ("regretting Monday's optimism.", C.LR, True),
    ("", None, False),
    ("The universe is indifferent.", C.LB, False),
    ("My therapist is indifferent.", C.LB, False),
    ("My cholesterol is indifferent.", C.LB, False),
    ("But my indigestion?", C.LM, True),
    ("My indigestion has OPINIONS.", C.LM | C.BOLD, True),
    ("", None, False),
    ("I asked God for a sign.", C.WHT, False),
    ("He sent me a parking ticket.", C.RED, True),
    ("", None, False),
    ("Life is a tragedy", C.MAG, False),
    ("for those who feel,", C.MAG, False),
    ("a comedy for those who think,", C.YEL, False),
    ("and a billing error", C.RED, True),
    ("for those who read the fine print.", C.LG, True),
]

# ─── Decorative Elements ───
DIVIDER = f"{C.GRY}{'═' * 62}{C.RST}"
STARS   = f"{C.YEL} ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ {C.RST}"

def typewriter(text: str, color: str = "", delay: float = 0.015, newline: bool = True):
    """Print with typewriter effect."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C.RST)
    if newline:
        print()
    else:
        sys.stdout.flush()

def fade_in(text: str, color: str = "", steps: int = 12, delay: float = 0.04):
    """Fade in text by gradually increasing brightness."""
    for i in range(steps + 1):
        intensity = int(232 + (i * 23 / steps))  # 232-255 grayscale
        # Simulate with alternating dim/bold
        style = C.DIM if i < steps // 2 else (C.BOLD if i == steps else "")
        sys.stdout.write(f"\r{style}{color}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def blink_text(text: str, color: str = C.RED, times: int = 3, delay: float = 0.3):
    """Make text blink."""
    for _ in range(times):
        sys.stdout.write(f"\r{color}{C.BLINK}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(f"\r{' ' * len(text)}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"\r{color}{text}{C.RST}")
    sys.stdout.flush()

def clear_screen():
    """Clear terminal."""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

# ─── Main Animation Sequence ───
def main():
    hide_cursor()
    try:
        clear_screen()
        
        # 1. Title card with Woody's face
        print(f"\n{C.BOLD}{C.CYN}{'╔' + '═' * 58 + '╗'}{C.RST}")
        print(f"{C.BOLD}{C.CYN}║{C.RST}  {C.LY}WOODY ALLEN'S GUIDE TO EXISTENTIAL DREAD{C.RST}  {C.BOLD}{C.CYN}║{C.RST}")
        print(f"{C.BOLD}{C.CYN}{'╚' + '═' * 58 + '╝'}{C.RST}\n")
        
        print(WOODY)
        time.sleep(0.8)
        
        # 2. Stars divider
        print(STARS)
        time.sleep(0.3)
        
        # 3. Typewriter the quote line by line
        for line, color, emphasis in QUOTE_LINES:
            if not line:
                print()
                time.sleep(0.15)
                continue
            
            if color is None:
                print()
                continue
            
            style = C.BOLD if emphasis else ""
            delay = 0.008 if not emphasis else 0.025
            
            # Special effects for key lines
            if "OPINIONS" in line:
                typewriter("  " + line, color | style, delay)
                blink_text("  " + line, color | style, times=2, delay=0.25)
                print()
            elif "parking ticket" in line:
                typewriter("  " + line, color | style, delay)
                # Flash red background
                for _ in range(2):
                    sys.stdout.write(f"\r  {C.WBG}{C.BLK}{C.BOLD}{line}{C.RST}")
                    sys.stdout.flush()
                    time.sleep(0.2)
                    sys.stdout.write(f"\r  {color}{style}{line}{C.RST}")
                    sys.stdout.flush()
                    time.sleep(0.2)
                print()
            elif "billing error" in line:
                typewriter("  " + line, color | style, delay)
                # Cash register sound visual
                sys.stdout.write(f" {C.YEL}$$$ {C.RST}")
                sys.stdout.flush()
                time.sleep(0.3)
                print()
            else:
                typewriter("  " + line, color | style, delay)
            
            time.sleep(0.12 if emphasis else 0.05)
        
        # 4. Final divider
        print()
        print(STARS)
        time.sleep(0.3)
        
        # 5. Closing thought - fade in
        closing_lines = [
            (f"{C.ITAL}{C.GRY}— As told to my analyst, who fell asleep.{C.RST}", False),
            (f"{C.DIM}Session fee: $300. Nap fee: priceless.{C.RST}", False),
        ]
        
        for line, _ in closing_lines:
            fade_in("  " + line, delay=0.03)
            time.sleep(0.15)
        
        # 6. Final Woody sign-off
        print()
        signoff = f"{C.CYN}{C.BOLD}  ♫  *whistles anxiously while checking pulse*  ♫{C.RST}"
        for ch in signoff:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.02)
        print("\n")
        
        # 7. Credits
        print(f"{C.GRY}  Generated by a neurotic algorithm with separation anxiety.{C.RST}")
        print(f"{C.GRY}  No philosophers were harmed in the making of this quote.{C.RST}")
        print(f"{C.DIM}  (Except Nietzsche. He's used to it.){C.RST}\n")
        
    finally:
        show_cursor()

if __name__ == "__main__":
    # Check if stdout supports color
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print("I've developed a new philosophy: I only dread the future on Tuesdays.")
        print("Monday's too early for existential dread, Wednesday I have my analyst,")
        print("Thursday's reserved for hypochondria, Friday I'm too tired to care,")
        print("And weekends? Weekends are for regretting Monday's optimism.")
        print("The universe is indifferent. My therapist is indifferent.")
        print("My cholesterol is indifferent. But my indigestion?")
        print("My indigestion has OPINIONS.")
        print("I asked God for a sign. He sent me a parking ticket.")
        print("Life is a tragedy for those who feel, a comedy for those who think,")
        print("and a billing error for those who read the fine print.")
        print("\n— As told to my analyst, who fell asleep.")
        print("Session fee: $300. Nap fee: priceless.")
        sys.exit(0)
    
    main()