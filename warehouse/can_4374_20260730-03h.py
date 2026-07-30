"""
Campbell's Soup Can #4374
Produced: 2026-07-30 03:32:14
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
Woody Allen Quote Generator - Neurotic Wisdom Edition
A single-file philosophical comedy experience.
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
    
    # Foreground
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# ─── The Quote (Original Woody Allen Style) ───
QUOTE_LINES = [
    "My therapist says I have a 'mortality fixation.'",
    "I told her that's ridiculous — I don't fixate on death,",
    "I fixate on the *inconvenience* of death.",
    "",
    "I mean, who's going to water my plants?",
    "Who'll return my library books by Thursday?",
    "And frankly, the afterlife sounds exhausting —",
    "all that eternity with no good deli nearby.",
    "",
    "So I'm not afraid of dying. I'm afraid of",
    "dying *before* I finish this sentence.",
    "Which, statistically, is... *gulp*... now.",
]

# ─── ASCII Art Elements ───
WOODY_FACE = [
    "       ╭─────────────╮",
    "       │  ┌───┐ ┌───┐ │",
    "       │  │ ● │ │ ● │ │   \"My analyst says I'm\"",
    "       │  └───┘ └───┘ │   \"obsessed with death.\"",
    "       │      ┌─┐     │   \"I said, 'Doc, I'm not\"",
    "       │      │ω│     │   \"obsessed. I'm just\"",
    "       │      └─┘     │   \"very attached to\"",
    "       │   ╭─────╮   │   \"not being dead.\"'",
    "       │   │     │   │",
    "       ╰───╯     ╰───╯",
]

NEUROTIC_SPIRAL = [
    "          @ @ @ @ @ @ @",
    "       @               @",
    "     @    ANXIETY      @",
    "    @    SPIRAL       @",
    "   @    ACTIVATED     @",
    "    @               @",
    "     @ @ @ @ @ @ @",
]

# ─── Animation Helpers ───
def typewriter(text: str, color: str = C.WHITE, delay: float = 0.02, end: str = '\n'):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def fade_in(text: str, color: str = C.CYAN, steps: int = 10):
    """Fade in text by gradually increasing brightness."""
    for i in range(steps + 1):
        brightness = int(255 * i / steps)
        # Simulate with color switching
        sys.stdout.write(f"\r{color}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def move_cursor(y: int, x: int):
    sys.stdout.write(f'\033[{y};{x}H')
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

# ─── Visual Effects ───
def draw_box(title: str, width: int = 60):
    """Draw a decorative box."""
    top = f"{C.BRIGHT_CYAN}╭{'─' * (width - 2)}╮{C.RST}"
    bottom = f"{C.BRIGHT_CYAN}╰{'─' * (width - 2)}╯{C.RST}"
    title_line = f"{C.BRIGHT_CYAN}│{C.RST} {C.BOLD}{C.YELLOW}{title.center(width - 4)}{C.RST} {C.BRIGHT_CYAN}│{C.RST}"
    return top, title_line, bottom

def print_woody_face():
    """Print the Woody ASCII face with colors."""
    for i, line in enumerate(WOODY_FACE):
        if i < 3:
            color = C.BRIGHT_YELLOW
        elif i < 6:
            color = C.BRIGHT_MAGENTA
        else:
            color = C.BRIGHT_CYAN
        # Center the face
        print(f"{color}{line.center(70)}{C.RST}")
        time.sleep(0.1)

def print_spiral():
    """Print animated anxiety spiral."""
    for line in NEUROTIC_SPIRAL:
        colors = [C.RED, C.BRIGHT_RED, C.MAGENTA, C.BRIGHT_MAGENTA, C.YELLOW, C.BRIGHT_YELLOW]
        colored = ''.join(random.choice(colors) + ch + C.RST if ch != ' ' else ' ' for ch in line)
        print(colored.center(70))
        time.sleep(0.08)

# ─── Main Sequence ───
def main():
    hide_cursor()
    try:
        clear_screen()
        
        # ─── Opening: Title Card ───
        print()
        top, title_line, bottom = draw_box("WOODY ALLEN'S NEUROTIC WISDOM", 64)
        print(top.center(70))
        print(title_line.center(70))
        print(bottom.center(70))
        print()
        
        # ─── Woody Face Reveal ───
        typewriter("  Loading existential dread...", C.GRAY, 0.03)
        time.sleep(0.5)
        print()
        print_woody_face()
        print()
        
        # ─── Anxiety Spiral ───
        typewriter("  Initializing anxiety spiral...", C.GRAY, 0.03)
        time.sleep(0.3)
        print()
        print_spiral()
        print()
        
        # ─── The Quote - Typewriter Style ───
        typewriter(f"  {C.BOLD}{C.ITALIC}And now, a thought...{C.RST}", C.BRIGHT_WHITE, 0.04)
        print()
        print(f"  {C.DIM}{'─' * 58}{C.RST}")
        print()
        
        for i, line in enumerate(QUOTE_LINES):
            if not line.strip():
                print()
                time.sleep(0.3)
                continue
            
            # Color coding for emotional beats
            if "therapist" in line.lower() or "analyst" in line.lower():
                color = C.BRIGHT_CYAN
                delay = 0.025
            elif "death" in line.lower() or "dying" in line.lower() or "mortality" in line.lower():
                color = C.BRIGHT_RED
                delay = 0.035
            elif "del" in line.lower() or "pastrami" in line.lower() or "library" in line.lower():
                color = C.BRIGHT_YELLOW
                delay = 0.025
            elif "gulp" in line.lower() or "now" in line.lower():
                color = C.BRIGHT_MAGENTA + C.BOLD
                delay = 0.08
            elif line.startswith("I ") or line.startswith("And ") or line.startswith("So "):
                color = C.WHITE
                delay = 0.025
            else:
                color = C.BRIGHT_WHITE
                delay = 0.02
            
            # Indent and typewrite
            sys.stdout.write(f"  {color}")
            sys.stdout.flush()
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write(f"{C.RST}\n")
            sys.stdout.flush()
            
            # Pause at key moments
            if "exhausting" in line or "statistically" in line:
                time.sleep(0.6)
            elif "gulp" in line:
                time.sleep(1.0)
            else:
                time.sleep(0.25)
        
        print()
        print(f"  {C.DIM}{'─' * 58}{C.RST}")
        print()
        
        # ─── Closing Flourish ───
        endings = [
            ("  *adjusts glasses nervously*", C.GRAY, 0.04),
            ("  *checks pulse*", C.GRAY, 0.04),
            ("  *orders extra life insurance*", C.BRIGHT_YELLOW, 0.03),
            ("  *wonders if deli delivers to the afterlife*", C.BRIGHT_CYAN, 0.03),
        ]
        
        for text, color, delay in endings:
            typewriter(text, color, delay)
            time.sleep(0.4)
        
        print()
        print()
        
        # ─── Final Signature ───
        sig_lines = [
            f"{C.DIM}─ Woody Allen (probably){C.RST}",
            f"{C.DIM}   As channeled by a Python script having an existential crisis{C.RST}",
        ]
        for line in sig_lines:
            print(line.center(70))
            time.sleep(0.2)
        
        print()
        
        # ─── Easter Egg: Blinking Cursor of Doom ───
        for _ in range(6):
            sys.stdout.write(f"\r  {C.BLINK}{C.BRIGHT_RED}■{C.RST}  Still alive?  {C.BLINK}{C.BRIGHT_RED}■{C.RST}")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write(f"\r  {C.BRIGHT_RED}■{C.RST}  Still alive?  {C.BRIGHT_RED}■{C.RST}")
            sys.stdout.flush()
            time.sleep(0.5)
        
        print()
        print()
        typewriter("  Okay, you're fine. For now. ", C.BRIGHT_GREEN, 0.03)
        typewriter("(But have you scheduled that checkup?)", C.YELLOW, 0.02)
        print()
        print()
        
    finally:
        show_cursor()
        sys.stdout.write(C.RST)
        sys.stdout.flush()

if __name__ == "__main__":
    # Check terminal capabilities
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print("WOODY ALLEN QUOTE:")
        for line in QUOTE_LINES:
            print(line)
        print("\n— Woody Allen (probably)")
    else:
        main()