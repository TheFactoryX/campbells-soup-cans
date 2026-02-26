"""
Campbell's Soup Can #2440
Produced: 2026-02-26 09:05:39
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

# ---------- ANSI colour codes ----------
C_RED  = "\033[31m"
C_GREEN= "\033[32m"
C_YEL  = "\033[33m"
C_BLUE = "\033[34m"
C_MAG  = "\033[35m"
C_CYAN = "\033[36m"
C_WHITE= "\033[37m"
C_BOLD = "\033[1m"
RST    = "\033[0m"

# ---------- Helper ----------
def slow_print(s, delay=0.03):
    """Print character by character for a type‑writer effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def boxed(txt, col=""):
    """Return *txt* wrapped in a coloured box."""
    lines = txt.split("\n")
    w = max(len(l) for l in lines) + 4
    top = f"{col}+{'-'*(w-2)}{col}"
    bot = top
    middle = "\n".join(f"{col}| {l.ljust(w-4)}{col}" for l in lines)
    return f"{top}\n{middle}\n{bot}{RST}"

# ---------- Woody Allen‑style quote ----------
quote = (
    "I’m not afraid of death; I just keep forgetting where "
    "I put the thing that makes me alive."
)

# ---------- Visual presentation ----------
slow_print("\n" + C_BOLD + C_YEL + "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒" + RST + "\n")
time.sleep(0.2)
print(boxed( C_BOLD + C_MAG + quote + RST, col=C_CYAN ))
slow_print("\n" + C_BOLD + C_RED + "*Bang!*  (the universe pauses, waiting for a punchline)" + RST + "\n")