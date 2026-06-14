"""
Campbell's Soup Can #3936
Produced: 2026-06-14 19:57:38
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def clear_screen():
    print("\033[2J\033[H", end="")

def dramatic_pause(seconds=1.0):
    time.sleep(seconds)

# ─── The Quote ───
quote = (
    "\"I finally made peace with the void.\n"
    " The void, however, has not returned my calls.\""
)

attribution = "— Woody Allen (probably)"

# ─── ASCII Art: The Void ───
void_art = [
    "            .          .           .     .        .          .              ",
    "   .            .         .      .        .        .         .       ",
    "         .         .         .         .         .          .          ",
    "    .        .        .        .        .        .        .      ",
    "        .       .       .       .       .       .       .          ",
    "   .        .        .        .        .        .        .       ",
    "         .         .         .         .         .          .        ",
    "    .        .        .        .        .        .        .     ",
]

# ─── Neurotic Brain ───
brain_art = [
    "    ╭─────────────────╮    ",
    "   ╱   ┌───┐ ┌───┐ ╲   ",
    "  │   │ ? │ │ ? │   │  ",
    "  │   └───┘ └───┘   │  ",
    "  │    ┌───────────┐    │  ",
    "  │    │  WHY?!  │    │  ",
    "   ╲   └───────────┘   ╱   ",
    "    ╰─────────────────╯    ",
]

# ─── Existential Thermometer ───
thermometer = [
    "  ┌─┐  ",
    "  │ │°  ",
    "  │ │   ",
    "  │░│   ",
    "  │░│   ",
    "  │▓│   ",
    "  │▓│   ",
    "  │█│   ",
    "  │█│   ",
    "  │█│   ",
    "  ╰─╯   ",
    " ANXIETY  ",
]

# ─── Main Performance ───
clear_screen()

# Phase 1: Dramatic opening
print()
slow_print(f"{DIM}{BG_BLACK}", 0.01)
slow_print("  ★ ★ ★  THE VOID AWAITS  ★ ★ ★  ", 0.05)
slow_print(f"{RESET}\n\n", 0.01)
dramatic_pause(0.8)

# Phase 2: The void appears
print(f"{DIM}{BG_BLACK}")
for line in void_art:
    print(f"  {line}")
    time.sleep(0.08)
print(f"{RESET}")
dramatic_pause(0.5)

# Phase 3: Neurotic brain appears
print()
for line in brain_art:
    print(f"  {YELLOW}{line}")
    time.sleep(0.1)
print(f"{RESET}")
dramatic_pause(0.5)

# Phase 4: Anxiety thermometer fills
print()
for i, line in enumerate(thermometer):
    color = GREEN if i < 4 else (YELLOW if i < 7 else RED)
    print(f"  {color}{line}")
    time.sleep(0.15)
print(f"{RESET}")
dramatic_pause(0.5)

# Phase 5: The curtain rises
print(f"\n  {BG_BLACK}{WHITE}{'═' * 56}{RESET}")
print(f"  {BG_BLACK}{WHITE}║{' ' * 54}║{RESET}")
print(f"  {BG_BLACK}{WHITE}║{' ' * 54}║{RESET}")

# Phase 6: The quote appears letter by letter
print(f"\n  {BG_BLACK}{WHITE}║{RESET}", end="")
sys.stdout.flush()

# Print quote with dramatic effect
quote_lines = quote.split('\n')
for qi, qline in enumerate(quote_lines):
    if qi > 0:
        print(f"  {BG_BLACK}{WHITE}║{RESET}", end="")
        sys.stdout.flush()
    
    # Pad to center-ish
    padding = max(0, (52 - len(qline)) // 2)
    prefix = " " * padding
    print(f"  {BG_BLACK}{WHITE}║{RESET}  {BG_BLACK}", end="")
    sys.stdout.flush()
    
    slow_print(f"{ITALIC}{CYAN}{prefix}{qline}{RESET}", 0.04)
    
    remaining = 52 - padding - len(qline)
    trail = " " * max(0, remaining)
    print(f"{BG_BLACK}{WHITE}{trail}  ║{RESET}")
    dramatic_pause(0.3)

# Attribution
attr_pad = max(0, (52 - len(attribution)) // 2)
attr_prefix = " " * attr_pad
attr_trail = " " * max(0, 52 - attr_pad - len(attribution))
print(f"  {BG_BLACK}{WHITE}║{RESET}  {BG_BLACK}{DIM}{MAGENTA}{attr_prefix}{attritation}{RESET}{BG_BLACK}{WHITE}{attr_trail}  ║{RESET}")

print(f"  {BG_BLACK}{WHITE}║{' ' * 54}║{RESET}")
print(f"  {BG_BLACK}{WHITE}{'═' * 56}{RESET}")

# Phase 7: Blinking existential crisis
print()
dramatic_pause(0.5)
for _ in range(3):
    sys.stdout.write(f"\r  {BLINK}{RED}  ⚠  EXISTENTIAL CRISIS DETECTED  ⚠  {RESET}")
    sys.stdout.flush()
    time.sleep(0.6)
    sys.stdout.write(f"\r  {DIM}{RED}  ⚠  EXISTENTIAL CRISIS DETECTED  ⚠  {RESET}")
    sys.stdout.flush()
    time.sleep(0.4)

# Phase 8: Final wisdom
print(f"\n\n  {DIM}{BG_BLACK}")
slow_print("  [The void has been notified. It will respond", 0.04)
slow_print("... eventually.]\n", 0.08)
slow_print("  [Probably.]\n", 0.12)
slow_print("  [Don't hold your breath.]\n", 0.15)
print(f"{RESET}")

# Phase 9: Footer
print(f"\n  {BG_BLACK}{DIM}{'─' * 56}{RESET}")
print(f"  {BG_BLACK}{DIM}  🎬  ZOO Presents: A Neurotic Production  🎬{RESET}")
print(f"  {BG_BLACK}{DIM}{'─' * 56}{RESET}")
print(f"{RESET}\n")