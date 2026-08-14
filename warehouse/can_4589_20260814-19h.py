"""
Campbell's Soup Can #4589
Produced: 2026-08-14 19:57:35
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
class C:
    R = '\033[91m'    # Red
    G = '\033[92m'    # Green
    Y = '\033[93m'    # Yellow
    B = '\033[94m'    # Blue
    M = '\033[95m'    # Magenta
    C = '\033[96m'    # Cyan
    W = '\033[97m'    # White
    D = '\033[90m'    # Dim
    BD = '\033[1m'    # Bold
    UL = '\033[4m'    # Underline
    BLINK = '\033[5m'
    REV = '\033[7m'
    X = '\033[0m'     # Reset

# Woody Allen quote (original, in his neurotic style)
QUOTE = (
    "I told my therapist I'm having an identity crisis.\n"
    "She said, 'That'll be $200.' I said, 'For that price,\n"
    "can't you just tell me who I *am*? I'll save us both\n"
    "the co-pay and the existential dread.'"
)

# ASCII art frames for a little neurotic character
FRAMES = [
    r"""
     \ o /
      | |
     /   \  """,
    r"""
     \ - /
      | |
     /   \  """,
    r"""
     \ o /
      | |
     /   \  """,
    r"""
     \ @ /
      | |
     /   \  """,
]

# Speech bubble top
BUBBLE_TOP = r"""
    .---------------------------.
   /                           \"""

# Speech bubble bottom
BUBBLE_BOT = r"""
   \___________________________/
            |    |
           _'    '_"""

def clear_screen():
    print('\033[2J\033[H', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=C.W, delay=0.03, newline=True):
    for char in text:
        print(f"{color}{char}{C.X}", end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def animate_character(duration=2.0):
    """Animate the little neurotic guy"""
    start = time.time()
    frame_idx = 0
    while time.time() - start < duration:
        move_cursor(3, 2)
        print(f"{C.C}{FRAMES[frame_idx % len(FRAMES)]}{C.X}")
        frame_idx += 1
        time.sleep(0.4)

def draw_bubble_with_quote():
    """Draw the speech bubble with the quote typed out"""
    # Top of bubble
    print(f"{C.Y}{BUBBLE_TOP}{C.X}")
    
    # Quote lines with typing effect
    lines = QUOTE.split('\n')
    for i, line in enumerate(lines):
        print(f"{C.Y}   | {C.X}", end='')
        typewriter(line, color=C.W, delay=0.02, newline=True)
        if i < len(lines) - 1:
            print(f"{C.Y}   | {C.X}")
    
    # Bottom of bubble
    print(f"{C.Y}{BUBBLE_BOT}{C.X}")

def neurotic_thoughts():
    """Display some neurotic side thoughts"""
    thoughts = [
        "Wait, did I leave the stove on?",
        "Is that a lump? WebMD says it's cancer.",
        "My cholesterol is fine but my will to live...",
        "Should I have ordered the salad? Too late now.",
        "Everyone's judging my posture right now.",
        "Did I lock the door? The car? The casket?",
    ]
    
    print(f"\n{C.D}{C.BD}Internal Monologue:{C.X}\n")
    for thought in thoughts:
        prefix = random.choice([f"{C.R}💭{C.X}", f"{C.M}💭{C.X}", f"{C.B}💭{C.X}"])
        print(f"  {prefix} {C.D}{thought}{C.X}")
        time.sleep(0.5)

def main():
    hide_cursor()
    clear_screen()
    
    # Title
    print(f"\n{C.M}{C.BD}")
    print("    ╔═══════════════════════════════════════════════╗")
    print("    ║     WOODY ALLEN'S DAILY DOSE OF DREAD™       ║")
    print("    ╚═══════════════════════════════════════════════╝")
    print(f"{C.X}\n")
    
    # Animate character while "thinking"
    animate_character(1.5)
    
    # Draw bubble with quote
    draw_bubble_with_quote()
    
    # Show neurotic thoughts
    neurotic_thoughts()
    
    # Final sign-off
    print(f"\n{C.G}{C.BD}    — Prescribed daily. Side effects may include{C.X}")
    print(f"{C.G}      insomnia, hypochondria, and sudden urges{C.X}")
    print(f"{C.G}      to move to Manhattan and date your stepdaughter.{C.X}\n")
    
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f"\n{C.R}Interrupted. Great. Now I have anxiety *about* the interruption.{C.X}\n")
        sys.exit(0)