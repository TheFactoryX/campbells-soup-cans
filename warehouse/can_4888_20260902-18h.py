"""
Campbell's Soup Can #4888
Produced: 2026-09-02 18:43:26
Worker: NVIDIA: Nemotron 3.5 Lightning (nvidia/nemotron-3.5-lightning)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote, visually enhanced with ANSI colors & ASCII."""

# ── ANSI escape codes for colors ──────────────────────────────────────────
R  = "\033[91m"  # red
G  = "\033[92m"  # green
Y  = "\033[93m"  # yellow
B  = "\033[94m"  # blue
M  = "\033[95m"  # magenta
C  = "\033[96m"  # cyan
W  = "\033[0m"   # reset
BOLD = "\033[1m"

# ── ASCII sidekick ────────────────────────────────────────────────────────
ascii_face = f"{G}(o_O){W}"

# ── The one Woody Allen vibe ──────────────────────────────────────────────
quote = (
    f"{Y}\"I'm not afraid of death. "
    f"I just don't want to be there when it happens. "
    f"The suspense is murder, honestly.\"{W}"
)

attr = f"{C}– A neurotic thought, probably{W}"

# ── Colored box borders ───────────────────────────────────────────────────
border_top = f"{M}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{W}"
border_bot = f"{M}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{W}"

# ── Output ────────────────────────────────────────────────────────────────
print(border_top)
print(f"{ascii_face}  {quote}")
print(f"{ascii_face}  {attr}")
print(border_bot)