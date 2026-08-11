"""
Campbell's Soup Can #4540
Produced: 2026-08-11 19:19:55
Worker: inclusionAI: Ling 3.0 Tiny (free) (inclusionai/ling-3.0-tiny:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
🍿  Woody Allen's Philosophy Machine  🍿

A single-file Python program that prints ONE funny,
neurotic, existential philosophical quote in Woody Allen's style.

Features:
- Animated starfield background
- Decorative ASCII frame
- Typewriter text effect
- Color-coded sections
- Sparkle effects
"""

import sys
import time
import random

# ── ANSI Color Codes ──────────────────────────────────
C_RED    = '\033[91m'
C_YELLOW = '\033[93m'
C_CYAN   = '\033[96m'
C_GREEN  = '\033[92m'
C_MAGENTA = '\033[95m'
C_WHITE  = '\033[97m'
C_BOLD   = '\033[1m'
C_DIM    = '\033[2m'
C_RESET  = '\033[0m'

def c(text, color=C_RESET):
    """Return colored text."""
    return f"{color}{text}{C_RESET}"

# ── Starry Background ──────────────────────────────────
def starfield(n=40):
    """Generate a random starry background."""
    for _ in range(n):
        sys.stdout.write(f"  {c(random.choice(['✦','★','☆','♦','◉']), C_CYAN)}")
        time.sleep(0.005)
    print()

# ── Decorative Frame ───────────────────────────────────
def frame(title, w=64):
    """Draw a beautiful ASCII frame."""
    border = '═' * w
    print(f"  {c(f'🍿  {title}  🍿', C_CYAN)}")
    print(f"  {' ' * 2}{c(border, MAGENTA)}")
    print(f"  {' ' * 2}{c(f'  {w}  ', C_WHITE)}")
    print(f"  {' ' * 2}{c(border, MAGENTA)}")
    print()

# ── Typewriter ─────────────────────────────────────────
def typewriter(text, delay=0.04, color=C_WHITE):
    """Print the quote character by character with a blink cursor."""
    sys.stdout.write(f"{c('  ', DIM)}")
    sys.stdout.flush()
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"\n{c('█', C_CYAN)}")
    time.sleep(0.25)
    sys.stdout.write(f"\n")

# ── Sparkle ────────────────────────────────────────────
def sparkles(n=15):
    """Add random sparkle marks to the output."""
    for _ in range(n):
        print(f"  {c(random.choice(['✦','★','☆','♦','◉']), C_YELLOW)}")
        time.sleep(0.03)

# ── Main ───────────────────────────────────────────────
def main():
    w = 64
    title = "🍿  Woody Allen's Philosophy Machine  🍿"

    # Background starfield
    starfield(35)

    # Decorative frame
    frame(title, w)

    # The main quote
    print(c("  1.  The Quote", C_YELLOW))
    typewriter(
        "I have an interesting relationship with my own thoughts. They're always arguing with me.",
        delay=0.03,
        color=C_WHITE
    )

    # Extra wisdom section
    print()
    print(c("  2.  Extra Wisdom", C_YELLOW))
    extras = [
        "    You're right. You are. This is the whole point.",
        "    Life is a bit like a jazz quartet - it's all about timing.",
        "    I think every person is extraordinary. Except when they have to pay taxes.",
        "    If I had the power to erase life, I would erase my own thoughts.",
        "    The universe is a vast, dark ocean. I am a small, anxious fish in it.",
        "    And yet, I keep typing, because that's what it means to be alive...",
    ]
    for ex in extras:
        print(f"    {ex}")

    # Closing
    print()
    print(f"  {c('─' * w, MAGENTA)}")
    print(f"  {c(f'☾  {w}  ☾', C_WHITE)}")
    print(f"  {c(f'  {DIM}Made with {BOLD}Python{RESET} and {DIM}very serious {RESET}', DIM)}")
    print(f"  {c(f'  {DIM}© 2024  Woody Allen Style  🍿', DIM)}")
    print()

if __name__ == '__main__':
    main()