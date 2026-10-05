"""
Campbell's Soup Can #5070
Produced: 2026-10-05 22:37:53
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
A neurotic little program that whispers Woody Allen wisdom into the void.
No external dependencies. Just pure, unadulterated existential dread with colors.
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    
    # Foreground
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    GRY = '\033[90m'
    LRG = '\033[91m'
    LGN = '\033[92m'
    LYL = '\033[93m'
    LBL = '\033[94m'
    LMA = '\033[95m'
    LCY = '\033[96m'
    
    # Background
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ─── The Quote (Original, Woody-Style) ───
WOODY_QUOTE = (
    "I tried to find meaning in life, but the universe "
    "just sent me a restraining order."
)

# ─── ASCII Woody (minimalist glasses + neurotic posture) ───
WOODY_ART = [
    f"{C.GRY}       ╭─────────╮{C.RST}",
    f"{C.GRY}       │  ╭─╮ ╭─╮  │{C.RST}  {C.DIM}← thick frames, thicker anxiety{C.RST}",
    f"{C.GRY}       │  │●│ │●│  │{C.RST}  {C.DIM}← eyes darting for exits{C.RST}",
    f"{C.GRY}       │     ╰━╯  │{C.RST}  {C.DIM}← nervous smile{C.RST}",
    f"{C.GRY}       │  ╰─────╯  │{C.RST}",
    f"{C.GRY}       ╰─────────╯{C.RST}",
    f"{C.GRY}          │ │{C.RST}",
    f"{C.GRY}         ╱   ╲{C.RST}",
]

# ─── Decorative border pieces ───
TL, TR, BL, BR = '╭', '╮', '╰', '╯'
H, V = '─', '│'
TL2, TR2, BL2, BR2 = '┌', '┐', '└', '┘'
H2, V2 = '─', '│'

def supports_color() -> bool:
    """Check if terminal supports ANSI colors."""
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

def typewriter(text: str, delay: float = 0.02, color: str = '') -> None:
    """Print text with a typewriter effect."""
    if not supports_color():
        color = ''
        C.RST = ''
    for ch in text:
        sys.stdout.write(f"{color}{ch}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fade_in_lines(lines: list[str], delay: float = 0.08) -> None:
    """Print lines with a subtle fade-in stagger."""
    for i, line in enumerate(lines):
        # Stagger start
        time.sleep(delay * 0.5)
        # Print with slight color variation per line
        colors = [C.GRY, C.LBL, C.CYN, C.LCY, C.WHT, C.LYL, C.LMA, C.LGN]
        c = colors[i % len(colors)]
        print(f"{c}{line}{C.RST}")
        sys.stdout.flush()

def pulse_text(text: str, cycles: int = 3, interval: float = 0.4) -> None:
    """Make text pulse by alternating brightness."""
    if not supports_color():
        print(text)
        return
    for _ in range(cycles):
        sys.stdout.write(f"\r{C.BOLD}{C.YEL}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write(f"\r{C.DIM}{C.GRY}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write(f"\r{C.RST}{text}{C.RST}\n")

def build_quote_box(quote: str, width: int = 60) -> list[str]:
    """Build a pretty box around the quote with word-wrapping."""
    words = quote.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= width - 4:
            current += (" " if current else "") + w
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)
    
    box = []
    box.append(f"{C.LBL}{TL}{H * (width - 2)}{TR}{C.RST}")
    for line in lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        box.append(
            f"{C.LBL}{V}{C.RST}"
            f"{' ' * left_pad}{C.BOLD}{C.WHT}{line}{C.RST}{' ' * right_pad}"
            f"{C.LBL}{V}{C.RST}"
        )
    box.append(f"{C.LBL}{BL}{H * (width - 2)}{BR}{C.RST}")
    return box

def clear_screen() -> None:
    """Clear terminal screen."""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def hide_cursor() -> None:
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def show_cursor() -> None:
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

def main() -> None:
    if not supports_color():
        # Fallback: plain text
        print("\n" + "=" * 60)
        print(WOODY_QUOTE)
        print("=" * 60)
        print("\n    (imagine glasses and existential dread here)")
        return

    hide_cursor()
    try:
        clear_screen()
        
        # ─── Opening: Woody ASCII art fades in ───
        print(f"\n{C.DIM}{' ' * 10}◈ A Neurotic Transmission ◈{C.RST}\n")
        fade_in_lines(WOODY_ART, delay=0.06)
        
        # ─── Nervous pause ───
        time.sleep(0.5)
        
        # ─── Typewriter intro ───
        print(f"\n{C.ITALIC}{C.GRY}  internal monologue:{C.RST} ")
        typewriter("  \"Let me think... no, thinking causes anxiety...\"", 0.015, C.DIM + C.ITALIC)
        typewriter("  \"But I've already thought it. Damn.\"", 0.015, C.DIM + C.ITALIC)
        time.sleep(0.4)
        
        # ─── The Quote Box appears ───
        print(f"\n{C.CYN}  ═══ The Verdict ═══{C.RST}\n")
        quote_box = build_quote_box(WOODY_QUOTE, width=64)
        for line in quote_box:
            print(f"  {line}")
            sys.stdout.flush()
            time.sleep(0.05)
        
        # ─── Pulse the quote's core ───
        print()
        pulse_text("  →  The universe has blocked your number.  ←", cycles=2)
        
        # ─── Closing neurotic flourish ───
        print(f"\n{C.DIM}  ────────────────────────────────────────────────{C.RST}")
        taglines = [
            "  \"My analyst says I have a preoccupation with death.",
            "   Which is absurd. I'm preoccupied with NOT dying.\"",
            "",
            f"  {C.ITALIC}— Woody, probably, while checking his pulse{C.RST}",
        ]
        for tl in taglines:
            typewriter(tl, 0.01, C.GRY if '—' not in tl else C.LMA)
            time.sleep(0.1)
        
        # ─── Final blink ───
        print(f"\n{C.BLINK}{C.RED}  ∃x: Anxiety(x) ∧ ∀y: Meaning(y) → ¬Exists(y, x){C.RST}")
        time.sleep(1.5)
        print(f"{C.RST}\n")
        
    finally:
        show_cursor()

if __name__ == '__main__':
    main()