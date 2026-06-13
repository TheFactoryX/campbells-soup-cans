"""
Campbell's Soup Can #3929
Produced: 2026-06-13 22:18:42
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    DIM = '\033[2m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'
    UP = '\033[A'
    HIDE_CURSOR = '\033[?25l'
    SHOW_CURSOR = '\033[?25h'

# Woody Allen ASCII portrait
WOODY = f"""
{C.C}       ╭─────────────╮
      │  {C.Y}@ @{C.C}     │  ← glasses, obviously
      │  {C.M}  ▼ {C.C}     │  ← nose (slightly deviated)
      │  {C.Y}╰──╯{C.C}     │  ← mouth (mumbling)
      │ {C.DIM}│││││{C.C}   │  ← hair (neurotic curls)
      ╰─────────────╯
      {C.Y}  \"{C.G}I'm not paranoid!{C.Y}\"  
      {C.Y}  \"{C.G}Everyone really IS{C.Y}
      {C.Y}   {C.G}out to get me!{C.Y}\" {C.RESET}
"""

# The quote - original Woody Allen style
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' "
    "in twenty minutes.\n"
    "It involves Russia."
)

SECOND_PART = (
    "\nMy therapist says I have a preoccupation with death.\n"
    "I told her: 'Doc, at my age, it's not a preoccupation—\n"
    "it's a scheduling conflict.'"
)

def typewriter(text, color=C.W, delay=0.02, newline_delay=0.4):
    """Print text with typewriter effect."""
    sys.stdout.write(color)
    sys.stdout.flush()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == '\n':
            time.sleep(newline_delay)
        else:
            time.sleep(delay + random.uniform(-0.01, 0.01))
    sys.stdout.write(C.RESET)
    sys.stdout.flush()

def animate_eyes(frames=6):
    """Animate Woody's eyes blinking."""
    eyes = ['@ @', 'o o', '- -', 'o o', '@ @', '@ @']
    for i in range(frames):
        sys.stdout.write(f"\r{C.C}      │  {C.Y}{eyes[i]}{C.C}     │  ")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write(f"\r{C.C}      │  {C.Y}@ @{C.C}     │  ")
    sys.stdout.flush()

def draw_box(title, content, color=C.C, width=52):
    """Draw a fancy colored box."""
    horizontal = "═" * (width - 2)
    print(f"\n{color}╔{horizontal}╗")
    print(f"║ {C.BOLD}{C.Y}{title.center(width - 4)}{C.RESET}{color} ║")
    print(f"╠{horizontal}╣")
    for line in content.split('\n'):
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"║ {' ' * left_pad}{C.W}{line}{C.RESET}{color}{' ' * right_pad} ║")
    print(f"╚{horizontal}╝{C.RESET}\n")

def neurotic_loader():
    """A neurotic loading animation."""
    thoughts = [
        "Analyzing existential dread...",
        "Checking if stove is off...",
        "Replaying awkward moment from 1987...",
        "Wondering if death is just a long nap...",
        "Calculating cholesterol in air...",
        "Formulating witty comeback... 20 years late...",
    ]
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    print(f"{C.HIDE_CURSOR}{C.DIM}")
    for i, thought in enumerate(thoughts):
        for _ in range(8):
            for s in spinner:
                sys.stdout.write(f"\r{C.M}{s} {C.C}{thought}{C.RESET}")
                sys.stdout.flush()
                time.sleep(0.04)
    sys.stdout.write(f"\r{' ' * 60}\r")
    sys.stdout.flush()
    print(f"{C.SHOW_CURSOR}{C.RESET}")

def main():
    # Clear screen
    sys.stdout.write(C.CLEAR)
    
    # Title banner
    banner = f"""
{C.M}{C.BOLD}    ╔══════════════════════════════════════════════════════════╗
    ║  {C.Y}WOODY ALLEN'S DAILY DOSE OF NEUROTIC WISDOM™{C.M}        ║
    ║  {C.C}Prescription: Take with anxiety, refill indefinitely  {C.M}║
    ╚══════════════════════════════════════════════════════════╝{C.RESET}
"""
    print(banner)
    time.sleep(0.5)
    
    # Neurotic loader
    neurotic_loader()
    time.sleep(0.3)
    
    # Show Woody
    print(WOODY)
    time.sleep(0.3)
    
    # Animate eyes once
    animate_eyes()
    time.sleep(0.2)
    
    # The quote in a fancy box
    draw_box(
        "TODAY'S PHILOSOPHICAL GEM",
        QUOTE,
        C.M
    )
    
    # Typewriter effect for the main quote
    typewriter("  ", C.W, 0)
    typewriter(QUOTE.split('\n')[0], C.Y, 0.03)
    time.sleep(0.3)
    typewriter("\n  " + QUOTE.split('\n')[1], C.G, 0.04)
    time.sleep(0.8)
    
    # Second part - typewriter
    print()
    typewriter(SECOND_PART, C.C, 0.025)
    time.sleep(1)
    
    # Final neurotic footer
    footer_lines = [
        f"{C.DIM}─" * 50,
        f"{C.R}Side effects may include:{C.RESET}",
        f"  {C.Y}•{C.RESET} Sudden urge to move to Manhattan",
        f"  {C.Y}•{C.RESET} Inability to enjoy anything without guilt",
        f"  {C.Y}•{C.RESET} Converting all joy into anxiety",
        f"  {C.Y}•{C.RESET} Dating your adopted daughter (wait, no...)",
        f"{C.DIM}─" * 50,
        f"\n{C.M}Remember: {C.BOLD}Life doesn't imitate art.{C.RESET}{C.M}",
        f"It imitates bad television.{C.RESET}\n",
    ]
    
    for line in footer_lines:
        print(line)
        time.sleep(0.15)
    
    # Final blink
    for _ in range(3):
        sys.stdout.write(f"\r{C.BLINK}{C.R}  *existential dread intensifies*{C.RESET}   ")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r{' ' * 40}\r")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print(f"\n{C.G}Session complete. Your neuroses have been validated.{C.RESET}")
    print(f"{C.DIM}Bill: $350. Cash only. I don't trust banks. Or digital. Or you.{C.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}\nInterrupted. Even my code has commitment issues.{C.RESET}")
        sys.exit(130)