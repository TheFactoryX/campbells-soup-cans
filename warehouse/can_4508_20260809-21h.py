"""
Campbell's Soup Can #4508
Produced: 2026-08-09 21:48:08
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -------------------------------------------------------------
#  Woody Allen‑style philosophical quote, wrapped in a colorful
#  animated box.  Pure Python – no external dependencies.
# -------------------------------------------------------------
import sys, time

# ---------- ANSI colour codes ----------
RED  = "\033[91m"
CYAN = "\033[96m"
YEL  = "\033[93m"
MAG  = "\033[95m"
RESET = "\033[0m"

# ---------- Simple typewriter animation ----------
def typewriter(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ---------- Quote ----------
OWIE_QUOTE = (
    "I’m not afraid of death; I just don’t want to be there when it happens."
)

# ---------- Fancy box with colours ----------
box_width = len(OWIE_QUOTE) + 4
top    = f"{YEL}┌{'─' * box_width}┐{RESET}"
bottom = f"{YEL}└{'─' * box_width}┘{RESET}"
side   = f"{YEL}│{RESET}"

# Content with left/right padding
content = f"{CYAN}   {OWIE_QUOTE}   {RESET}"

# Build the coloured box lines
lines = [
    top,
    f"{side}{MAG}{content}{RESET}",
    bottom,
]

# ---------- Optional intro animation ----------
intro = f"{RED}...waiting for the inevitable...{RESET}"
typewriter(intro, delay=0.07)

# ---------- Print the coloured box ----------
for line in lines:
    sys.stdout.write(line + "\n")
    typewriter(line, delay=0)   # instant display (no delay needed)

# ---------- A little sign‑off ----------
signoff = f"{MAG}— Woody Allen, if he were a Python script{RESET}"
typewriter(signoff, delay=0.04)

# -------------------------------------------------------------
# End of program.
# -------------------------------------------------------------