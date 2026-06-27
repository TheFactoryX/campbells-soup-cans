"""
Campbell's Soup Can #4028
Produced: 2026-06-27 14:55:13
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

# ANSI Color Codes
class C:
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    BLINK = '\033[5m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033[2J\033[H'

# Woody Allen quote (original, in his style)
QUOTE = (
    "I took a speed-reading course and finished 'War and Peace' in twenty minutes. "
    "It involves Russia."
)

ATTRIBUTION = "— Woody Allen (probably, or maybe just my therapist pretending to be him)"

# ASCII Art Frames
FRAMES = [
    r"""
    ╔═══════════════════════════════════════════════════════════════════╗
    ║  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ║
    ║  █  WOODY ALLEN QUOTE GENERATOR v1.0  █  "Anxiety Included"  █  ║
    ║  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ║
    ╚═══════════════════════════════════════════════════════════════════╝
    """,
    r"""
     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
     █  WOODY ALLEN QUOTE GENERATOR v1.0  █  "Anxiety Included"  █
     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """,
]

WOODY_FACE = r"""
        ╭─────────────╮
        │  (•_•)      │  <-- Me, overthinking this quote
        │  <)  )╯     │
        │  /   \      │
        ╰─────────────╯
"""

NEUROTIC_THOUGHTS = [
    "Wait, did I leave the stove on?",
    "Is 'it involves Russia' profound or just lazy?",
    "My analyst says I have a preoccupation with death. Also my dentist.",
    "Should I have ordered the salad instead?",
    "Death is nature's way of saying 'your table is ready.'",
    "I'm not a hypochondriac, I'm just... preemptively diagnosed.",
    "My therapist has a therapist. His therapist has a yacht.",
]

def typewriter(text, color=C.W, delay=0.02, newline=True):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def print_centered(text, color=C.W, width=70):
    """Print text centered."""
    padding = (width - len(text)) // 2
    print(f"{color}{' ' * padding}{text}{C.RESET}")

def animate_face():
    """Show Woody face with blinking."""
    for _ in range(3):
        print(C.CLEAR, end='')
        print(f"{C.C}{FRAMES[1]}{C.RESET}")
        print(f"{C.Y}{WOODY_FACE}{C.RESET}")
        time.sleep(0.4)
        print(C.CLEAR, end='')
        print(f"{C.C}{FRAMES[1]}{C.RESET}")
        print(f"{C.Y}        ╭─────────────╮\n        │  (-_-)      │  <-- Blinking existentially\n        │  <)  )╯     │\n        │  /   \\      │\n        ╰─────────────╯{C.RESET}")
        time.sleep(0.3)

def main():
    # Clear screen
    print(C.CLEAR, end='')
    
    # Show header
    print(f"{C.C}{C.BOLD}{FRAMES[0]}{C.RESET}")
    
    # Neurotic preamble
    print(f"\n{C.M}{C.ITALIC}Initializing existential dread...{C.RESET}\n")
    time.sleep(0.5)
    
    for thought in random.sample(NEUROTIC_THOUGHTS, 3):
        print(f"  {C.DIM}⟳ {thought}{C.RESET}")
        time.sleep(0.4)
    
    print(f"\n{C.Y}{'─' * 70}{C.RESET}\n")
    
    # Type the quote
    print(f"  {C.BOLD}{C.W}Quote:{C.RESET} ", end='')
    sys.stdout.flush()
    typewriter(QUOTE, color=C.G, delay=0.015, newline=True)
    
    print()
    
    # Type attribution
    print(f"  {C.DIM}{C.ITALIC}", end='')
    typewriter(ATTRIBUTION, color=C.M, delay=0.02, newline=True)
    print(f"{C.RESET}", end='')
    
    print(f"\n{C.Y}{'─' * 70}{C.RESET}\n")
    
    # Final neurotic sign-off
    signoffs = [
        "Anyway, I have a 3 PM panic attack scheduled. Gotta run.",
        "Time to go argue with my pharmacist about generic Xanax.",
        "My mother would say: 'You're wasting your potential.' She's right.",
        "I'd stay and chat, but my anxiety has separation anxiety.",
    ]
    print(f"  {C.C}{C.ITALIC}{random.choice(signoffs)}{C.RESET}\n")
    
    # Little animation at the end
    for i in range(3):
        dots = "." * (i + 1)
        print(f"\r  {C.DIM}Existential crisis loading{dots}{' ' * 3}{C.RESET}", end='')
        sys.stdout.flush()
        time.sleep(0.4)
    
    print(f"\r  {C.G}✓ Existential crisis loaded successfully. Enjoy your neurosis!{C.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}Interrupted. Even my code has commitment issues.{C.RESET}\n")
        sys.exit(0)