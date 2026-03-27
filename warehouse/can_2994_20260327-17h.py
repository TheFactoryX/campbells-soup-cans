"""
Campbell's Soup Can #2994
Produced: 2026-03-27 17:10:56
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ── ANSI colour codes ──────────────────────────────────────────────────────
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
MAGENTA= "\033[95m"
RESET  = "\033[0m"

# ── The quote (Woody Allen style) ───────────────────────────────────────
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# ── Simple type‑writer animation helper ───────────────────────────────────
def animate_print(s, delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ── Build a colourful framed box ────────────────────────────────────────WIDTH = 70
border_top    = f"{MAGENTA}╔{'═'*(WIDTH-2)}╗{RESET}"
border_bottom = f"{MAGENTA}╚{'═'*(WIDTH-2)}╝{RESET}"
border_mid    = f"{CYAN}║{RESET}{' '*(WIDTH-2)}{CYAN}║{RESET}"

# centre the quote inside the frame
quote_len = len(quote)
space_left = (WIDTH - 4 - quote_len) // 2centered  = " " * space_left + quote + " " * (WIDTH - 4 - quote_len - space_left)

frame_lines = [
    border_top,
    border_mid,
    f"{CYAN}║{YELLOW}{centered}{CYAN}║{RESET}",
    border_mid,
    border_bottom,
]

# ── A tiny animated header ───────────────────────────────────────────────
print(RED + "   _______" + RESET, end="", flush=True)
animate_print("   A Woody Allen Thought Bubble   ")
# clear the temporary line (works on most terminals)
print("\r\033[0K", end="", flush=True)

# ── Print the framed quote with a pleasant fade‑in ───────────────────────
for line in frame_lines:
    animate_print(line)

# ── A friendly sign‑off ─────────────────────────────────────────────────
print(RESET + "\nEnjoy the existential chuckle!" + RESET)