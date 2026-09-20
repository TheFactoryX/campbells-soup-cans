"""
Campbell's Soup Can #4997
Produced: 2026-09-20 19:27:09
Worker: Free Models Router (openrouter/free)
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

# ── ANSI Color Codes ──
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
MAGENTA = '\033[95m'
CYAN    = '\033[96m'
WHITE   = '\033[97m'
BOLD    = '\033[1m'
DIM     = '\033[2m'
ITALIC  = '\033[3m'
UNDER   = '\033[4m'
RESET   = '\033[0m'

# ── Color Pool for Cycling ──
COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]

def slow_print(text, delay=0.03, color=None):
    """Typewriter effect with optional color cycling."""
    for char in text:
        if color:
            c = random.choice(COLORS)
            sys.stdout.write(f"{c}{char}{RESET}")
        else:
            sys.stdout.write(f"{color}{char}{RESET}" if color else char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def colored(text, color):
    return f"{color}{text}{RESET}"

def art_line(char, length=60, color=CYAN):
    return colored(char * length, color)

# ═══════════════════════════════════════════════════════════════
#                        THE SHOW BEGINS
# ═══════════════════════════════════════════════════════════════

# Clear-ish effect
print("\n" * 2)

# ── ASCII Art Title ──
print(colored("   ██████╗  █████╗  ██████╗  ██████╗  ██╗  ██╗", RED, ))
time.sleep(0.1)
print(colored("   ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗ ██║ ██╔╝", GREEN))
time.sleep(0.1)
print(colored("   ██║  ██║███████║██║   ██║██████╔╝  ╚████╔╝ ", YELLOW))
time.sleep(0.1)
print(colored("   ██║  ██║██╔══██║██║   ██║██╔══██╗   ╚██╔╝  ", BLUE))
time.sleep(0.1)
print(colored("   ██████╔╝██║  ██║╚██████╔╝██║  ██║    ██║   ", MAGENTA))
time.sleep(0.1)
print(colored("   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝   ", CYAN))
print()
time.sleep(0.5)

# ── Decorative Border ──
print(art_line("═", 62, MAGENTA))
print(art_line("║", 1, CYAN) + colored("  🧠  A Woody Allen Production  🧠  ", BOLD + WHITE) + art_line("║", 1, CYAN))
print(art_line("═", 62, MAGENTA))
print()
time.sleep(0.5)

# ── The Quote (Typewriter with colors) ──
quote = (
    "I'm not afraid of death; "
    "I just don't want to be there when it happens.\n\n"
    "The universe is under no obligation "
    "to make sense to you.\n\n"
    "I'm not paranoid — it's just that "
    "everyone is out to get me.\n\n"
    "80% of life is just showing up.\n\n"
    "I spent most of my money on liquor, "
    "prostitutes, and fast living. "
    "The rest I just wasted."
)

# Print quote character by character with color cycling
slow_print("", 0)
for i, ch in enumerate(quote):
    if ch == '\n':
        print()
    else:
        color = COLORS[i % len(COLORS)]
        sys.stdout.write(f"{BOLD}{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(0.025)

print()
time.sleep(0.5)

# ── Bottom Border ──
print(art_line("═", 62, YELLOW))
print(colored("  — Woody Allen (sort of, in his mind)  ", DIM + ITALIC))
print(art_line("═", 62, YELLOW))
print()

# ── Animated existential footer ──
footers = [
    "I wonder if I'll still be me when I'm dead.",
    "My therapist says I have a preoccupation with vengeance. We'll see about that.",
    "I'm not returning your call.",
    "I've had a perfectly terrible education.",
    "I'm terrified of women — as the saying goes, 90% of them are...",
]

print(colored("  💭 ", CYAN + BOLD) + colored("EXISTENTIAL TREMBLING:", BLUE + BOLD))
time.sleep(0.3)
for _ in range(3):
    line = random.choice(footers)
    color = random.choice(COLORS)
    sys.stdout.write(f"  {color}{DIM}{line}{RESET}\n")
    sys.stdout.flush()
    time.sleep(0.8)

print()
print(colored("  ─── End of Universe ─── ", DIM + CYAN))
print()