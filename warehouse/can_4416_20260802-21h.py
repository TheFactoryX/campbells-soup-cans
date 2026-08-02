"""
Campbell's Soup Can #4416
Produced: 2026-08-02 21:10:17
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
woody_wisdom.py - A neurotic dose of existential humor
"Life is divided into the horrible and the miserable." — but with more colors!
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    R = '\033[0m'       # Reset
    B = '\033[1m'       # Bold
    D = '\033[2m'       # Dim
    I = '\033[3m'       # Italic
    U = '\033[4m'       # Underline
    
    # Foreground
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    GRAY    = '\033[90m'
    
    # Bright foreground
    BRED     = '\033[91m'
    BGREEN   = '\033[92m'
    BYELLOW  = '\033[93m'
    BBLUE    = '\033[94m'
    BMAGENTA = '\033[95m'
    BCYAN    = '\033[96m'
    BWHITE   = '\033[97m'
    
    # Background
    BG_BLACK   = '\033[40m'
    BG_RED     = '\033[41m'
    BG_GREEN   = '\033[42m'
    BG_YELLOW  = '\033[43m'
    BG_BLUE    = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN    = '\033[46m'
    BG_WHITE   = '\033[47m'

# ─── Woody's Original Quote ───
WOODY_QUOTE = (
    "I told my analyst I have an inferiority complex. "
    "He said, 'Don't worry — you're not as inferior as you think.' "
    "Which, honestly, is the most backhanded compliment I've ever paid for."
)

# ─── ASCII Art: Woody's Glasses + Neurotic Face ───
WOODY_FACE = r"""
        ╭─────────────────────╮
       ╱  ██████    ██████   ╲
      │   ██████    ██████    │
      │        ██████         │   "I'm not a hypochondriac...
      │   ██████████████      │    I'm just *preemptively* diagnosed."
      │    ████████████       │
      │     ██████████        │
       ╲                     ╱
        ╰─────────────────────╯
"""

# ─── Decorative Elements ───
STARS = "✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦"
DIVIDER = "━" * 60

def typewriter(text: str, color: str = C.WHITE, delay: float = 0.02, jitter: float = 0.015):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.R}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter))
    print()

def pulse_text(text: str, colors: list, cycles: int = 3):
    """Make text pulse through colors."""
    for _ in range(cycles):
        for color in colors:
            sys.stdout.write(f"\r{color}{C.B}{text}{C.R}")
            sys.stdout.flush()
            time.sleep(0.15)
    print()

def rainbow_text(text: str):
    """Print text in a rainbow gradient."""
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(f"{color}{char}")
    sys.stdout.write(C.R)
    print()

def print_boxed(text: str, width: int = 70, border_color: str = C.CYAN, text_color: str = C.YELLOW):
    """Print text in a fancy box."""
    lines = []
    words = text.split(' ')
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    top = f"{border_color}╭{'─' * (width - 2)}╮{C.R}"
    bottom = f"{border_color}╰{'─' * (width - 2)}╯{C.R}"
    
    print(top)
    for line in lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{border_color}│{C.R}{' ' * left_pad}{text_color}{line}{C.R}{' ' * right_pad}{border_color}│{C.R}")
    print(bottom)

def neurotic_loading():
    """A neurotic loading animation."""
    thoughts = [
        "Analyzing existence...",
        "Questioning the analyst's credentials...",
        "Wondering if the copay covers existential dread...",
        "Calculating probability of immortality via not dying...",
        "Repressing... repressing... still repressing...",
        "Checking if mother would approve of this output...",
    ]
    
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    
    for thought in thoughts:
        for _ in range(8):
            for frame in spinner:
                sys.stdout.write(f"\r{C.GRAY}{frame} {C.YELLOW}{thought}{C.R}")
                sys.stdout.flush()
                time.sleep(0.05)
        print(f" {C.GREEN}✓{C.R}")
    print()

def main():
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # ─── Header Animation ───
    print(f"\n{C.MAGENTA}{C.B}{STARS}{C.R}\n")
    
    # Title with rainbow
    rainbow_text("      W O O D Y ' S   W I S D O M   D I S P E N S E R")
    print(f"{C.MAGENTA}{C.B}{STARS}{C.R}\n")
    
    # Woody's face
    print(f"{C.CYAN}{WOODY_FACE}{C.R}")
    
    # Neurotic loading
    print(f"{C.GRAY}{DIVIDER}{C.R}")
    typewriter(f"{C.YELLOW}Initializing neurotic subroutine...{C.R}", C.YELLOW, 0.01)
    print()
    neurotic_loading()
    
    # The Quote - in a fancy box
    print(f"\n{C.BMAGENTA}{C.B}┌{'─' * 58}┐{C.R}")
    typewriter(f"{C.BMAGENTA}│{C.R} {C.BWHITE}{C.B}THE WOODY ALLEN QUOTE OF THE MOMENT{C.R} {C.BMAGENTA}│{C.R}", C.WHITE, 0.01)
    print(f"{C.BMAGENTA}└{'─' * 58}┘{C.R}\n")
    
    print_boxed(WOODY_QUOTE, width=68, border_color=C.YELLOW, text_color=C.BWHITE)
    
    # Post-quote existential crisis
    print(f"\n{C.GRAY}{DIVIDER}{C.R}")
    
    afterthoughts = [
        ("Wait, did I leave the stove on?", C.RED),
        ("Is that a symptom? Should I WebMD it?", C.YELLOW),
        ("My mother was right. About everything. Always.", C.MAGENTA),
        ("I should've been a dentist. Clean teeth, clean conscience.", C.CYAN),
        ("...But then who would dispense the wisdom?", C.GREEN),
    ]
    
    for thought, color in afterthoughts:
        typewriter(f"  {C.I}{color}{thought}{C.R}", color, 0.015)
        time.sleep(0.3)
    
    # Final pulse
    print(f"\n{C.GRAY}{DIVIDER}{C.R}")
    pulse_text("  Remember: You're not paranoid if the universe IS out to get you.  ", 
               [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA], 2)
    
    # Footer
    print(f"\n{C.DIM}{C.GRAY}  — Generated by a program that's also seeing a therapist{C.R}")
    print(f"  {STARS}{C.R}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.RED}Interrupted! Now I have abandonment issues.{C.R}\n")
        sys.exit(130)