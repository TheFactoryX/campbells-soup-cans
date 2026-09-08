"""
Campbell's Soup Can #4927
Produced: 2026-09-08 21:51:42
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Neurotic Existential Quote Generator™
A Woody Allen style philosophical disaster in pure Python.
"""

import time
import sys
import random

# ─── ANSI Escape Codes ───────────────────────────────────────────
class C:
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"
    BG_BLUE = "\033[44m"

# ─── Helpers ─────────────────────────────────────────────────────
def typewriter(text, color=C.WHITE, delay=0.025):
    """Print text one character at a time for dramatic effect."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_box(text, width=58):
    """Print a centered line inside a decorative box."""
    padded = f"  {text}  "
    side = width - len(padded) + len(text) + 2
    left = (side - len(padded)) // 2
    right = side - len(padded) - left
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.WHITE}{' '*left}{padded}{' '*right}{C.CYAN}{C.BOLD}║{C.RESET}")

def draw_border(width=58, char="═"):
    print(f"{C.CYAN}{C.BOLD}{char*width}{C.RESET}")

# ─── Main Display ────────────────────────────────────────────────
def main():
    # Clear-ish separator
    print("\n" * 2)

    # Animated top decoration
    typewriter(f"{C.YELLOW}{C.BOLD}     .-.      .-.      .-.      .-.      .-.", C.YELLOW, 0.01)
    typewriter(f"{C.YELLOW}{C.BOLD}    ( ^ )    ( ^ )    ( ^ )    ( ^ )    ( ^ )", C.YELLOW, 0.01)
    typewriter(f"{C.YELLOW}{C.BOLD}     '-'      '-'      '-'      '-'      '-'", C.YELLOW, 0.01)
    print()

    # Box header
    draw_border()
    slow_box(f"{C.BG_BLUE}{C.WHITE}{C.BOLD}   🧠  NEUROTIC EXISTENTIAL QUOTATION SYSTEM  🧠  {C.RESET}")
    draw_border()
    print()

    # The Quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print()
    typewriter(f"{C.MAGENTA}{C.BOLD}    \"{C.RESET}", C.MAGENTA, 0.01)
    typewriter(f"{C.RED}{C.BOLD}    {quote}{C.RESET}", C.RED, 0.025)
    typewriter(f"{C.MAGENTA}{C.BOLD}    \"{C.RESET}", C.MAGENTA, 0.01)
    print()

    # Attribution
    typewriter(f"{C.GREEN}{C.BOLD}         — Woody Allen (probably, while overthinking it){C.RESET}", C.GREEN, 0.02)
    print()

    draw_border()
    print()

    # Neurotic follow-up with delay
    time.sleep(0.5)
    followups = [
        "But seriously... what if the meaning of life is just to keep asking questions?",
        "I consulted a therapist. He said 'have you tried not existing?' I said 'too late.'",
        "The universe is expanding, and so is my existential dread.",
        "I used to think life was cruel and meaningless. Then I remembered I left the stove on.",
    ]
    chosen = random.choice(followups)
    typewriter(f"{C.YELLOW}    ↳ {chosen}{C.RESET}", C.YELLOW, 0.02)
    print()

    # Exit neurosis
    time.sleep(0.8)
    typewriter(f"{C.CYAN}{C.DIM}    [system note: this quote provides zero comfort]{C.RESET}", C.CYAN, 0.01)
    typewriter(f"{C.CYAN}{C.DIM}    [please consult your own neurosis for closure]{C.RESET}", C.CYAN, 0.01)
    print()
    draw_border(char="─")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}Typical. You couldn't even handle a quote.{C.RESET}")
        sys.exit(0)