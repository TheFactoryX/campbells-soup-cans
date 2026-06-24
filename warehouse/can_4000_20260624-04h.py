"""
Campbell's Soup Can #4000
Produced: 2026-06-24 04:36:01
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
    D = '\033[90m'      # Dark Gray
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'
    CURSOR_HIDE = '\033[?25l'
    CURSOR_SHOW = '\033[?25h'
    SAVE_POS = '\033[s'
    RESTORE_POS = '\033[u'

WOODY_QUOTE = (
    "The universe is indifferent to my existence, "
    "which is fine — I'm barely indifferent to it myself. "
    "Though I did pre-pay for a cemetery plot. "
    "Good investment. Property values never go down. "
    "Unlike my therapist's opinion of me."
)

WOODY_ASCII = r"""
        .--.
       /    \
      |  @ @ |     *neurotic sigh*
      |      |
      | \__/ |
       \____/
        ||||
      __||||__
     /        \
    |  WOODY   |
    |  MODE:   |
    |  ACTIVE  |
     \________/
"""

ANXIETY_FRAMES = [
    "[░░░░░░░░░░] 0%  - \"Is this chest pain or indigestion?\"",
    "[█░░░░░░░░░] 10% - \"Definitely indigestion. Or cancer.\"",
    "[██░░░░░░░░] 25% - \"WebMD says 6 months. I'll take 7.\"",
    "[███░░░░░░░] 37% - \"Did I lock the door? The stove? My soul?\"",
    "[████░░░░░░] 50% - \"My analyst says I catastrophize. He's wrong. We're all going to die.\"",
    "[█████░░░░░] 62% - \"But first, taxes.\"",
    "[██████░░░░] 75% - \"Why did I say 'you too' when the waiter said 'enjoy your meal'? 1987.\"",
    "[███████░░░] 85% - \"The void stares back. It has my eyes. And my student loans.\"",
    "[████████░░] 95% - \"Quote loading... existential dread buffering...\"",
    "[██████████] 100% - \"AH. THERE IT IS.\"",
]

def typewriter(text, color=C.W, delay=0.02, jitter=0.015):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter))
    print()

def print_centered(text, color=C.W, width=70):
    """Print text centered."""
    padding = (width - len(text)) // 2
    print(f"{color}{' ' * padding}{text}{C.RESET}")

def draw_box(lines, color=C.C, width=70):
    """Draw a box around lines."""
    print(f"{color}╔{'═' * (width - 2)}╗{C.RESET}")
    for line in lines:
        visible_len = len(line)
        # Strip ANSI for length calculation
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = width - 2 - len(clean)
        left = padding // 2
        right = padding - left
        print(f"{color}║{C.RESET}{' ' * left}{line}{' ' * right}{color}║{C.RESET}")
    print(f"{color}╚{'═' * (width - 2)}╝{C.RESET}")

def anxiety_animation():
    """Run the anxiety loading animation."""
    print(f"{C.CURSOR_HIDE}", end='')
    for frame in ANXIETY_FRAMES:
        sys.stdout.write(f"\r{C.Y}{C.BOLD}{frame}{C.RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.6))
    print(f"\n{C.CURSOR_SHOW}", end='')

def main():
    # Clear screen
    print(f"{C.CLEAR}", end='')
    
    # Title banner
    print(f"{C.M}{C.BOLD}")
    print("    ╔══════════════════════════════════════════════════════════════╗")
    print("    ║  WOODY ALLEN QUOTE GENERATOR v1.0 (UNLICENSED THERAPY)     ║")
    print("    ╚══════════════════════════════════════════════════════════════╝")
    print(f"{C.RESET}")
    
    # ASCII Art
    for line in WOODY_ASCII.strip().split('\n'):
        print(f"{C.C}{line}{C.RESET}")
        time.sleep(0.08)
    
    print()
    
    # Anxiety animation
    print(f"{C.DIM}Initializing neurotic subsystem...{C.RESET}\n")
    anxiety_animation()
    
    print()
    time.sleep(0.5)
    
    # The quote reveal with dramatic buildup
    print(f"{C.D}{'─' * 70}{C.RESET}")
    print(f"{C.BOLD}{C.Y}   And now, a moment of clarity (billed at $450/hour):{C.RESET}")
    print(f"{C.D}{'─' * 70}{C.RESET}")
    print()
    
    # Typewriter the quote in chunks for effect
    chunks = [
        (C.W, "The universe is indifferent to my existence, "),
        (C.D, "which is fine — "),
        (C.C, "I'm barely indifferent to it myself. "),
        (C.Y, "Though I did pre-pay for a cemetery plot. "),
        (C.G, "Good investment. "),
        (C.M, "Property values never go down. "),
        (C.R, "Unlike my therapist's opinion of me."),
    ]
    
    for color, chunk in chunks:
        typewriter(chunk, color=color, delay=0.035, jitter=0.02)
        time.sleep(0.15)
    
    print()
    print(f"{C.D}{'─' * 70}{C.RESET}")
    
    # Post-quote neurotic footer
    print()
    footers = [
        f"{C.DIM}* Quote not FDA approved. Side effects may include: nausea, ",
        f"  derealization, sudden urge to call your mother, and ",
        f"  the realization that you're wearing two different socks.{C.RESET}",
        "",
        f"{C.DIM}— Generated at {time.strftime('%H:%M:%S')} by a script ",
        f"that also worries it's not good enough{C.RESET}",
    ]
    
    for line in footers:
        print(line)
        time.sleep(0.1)
    
    # Final easter egg
    print()
    time.sleep(0.8)
    print(f"{C.BLINK}{C.R}► SYSTEM ERROR: EXISTENTIAL DREAD OVERFLOW ◄{C.RESET}")
    time.sleep(0.3)
    print(f"{C.DIM}(Just kidding. Or am I? *checks pulse*){C.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}Interrupted. Typical. Even my own programs abandon me.{C.RESET}")
        sys.exit(130)