"""
Campbell's Soup Can #1987
Produced: 2026-02-01 15:41:31
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, sys, random

# Woody Allen style philosophical quote (single line)
QUOTE = (
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "Actually, I'm too busy worrying about my parking spot."
)

# ANSI color codes (red, green, yellow, blue, magenta, cyan, white)
COLORS = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m",  # cyan
    "\033[37m",  # white (default)
]
RESET = "\033[0m"

# Clear screen and hide cursor for dramatic effect
print("\033[2J\033[H", flush=True)
print("\033[?25l", flush=True)

# Woody Allen ASCII silhouette (centered)
ASCII_ART = r"""
                     _
                    | |
   _ _ _ _ _ _ _ _ |_|_
  | | | | | | | | | | |
  |_| _|_|_|_|_|_|_|_|_|_
"""
if ASCII_ART:
    lines = ASCII_ART.strip().splitlines()
    max_len = max(len(l) for l in lines) if lines else 0
    centered = "\n".join(f"{' ' * ((max_len - len(l)) // 2)}{l}" for l in lines)
    print(centered)

# Box dimensions (inner width includes two spaces on each side)
inner_pad   = 2          # spaces left/right of the quote
inner_width = len(QUOTE) + inner_pad * 2

# Unicode box‑drawing characters
LEFT_TOP    = "\u255A"  # ╔
RIGHT_TOP   = "\u255B"  # ╗
LEFT_BOTTOM = "\u255C"  # ╚
RIGHT_BOTTOM= "\u255D"  # ╝
VERTICAL    = "\u2551"  # ║
HORIZONTAL = "\u2550"  # ═

# Print the top of the box
print(f"{LEFT_TOP}{HORIZONTAL * inner_width}{RIGHT_TOP}", flush=True)

# Typewriter effect: each character appears in a random color
delay = 0.02
colored_parts = []

for idx, ch in enumerate(QUOTE):
    col = random.choice(COLORS)
    colored = f"{col}{ch}{RESET}"
    colored_parts.append(colored)

    # Pad left/right to keep inner width constant
    left_pad  = inner_pad
    right_pad = inner_width - left_pad - len(colored_parts)

    inner_content = " " * left_pad + "".join(colored_parts) + " " * right_pad
    line = f"{VERTICAL}{inner_content}{VERTICAL}"
    print(line, flush=True)
    time.sleep(delay)

# Bottom border to close the box
print(f"{LEFT_BOTTOM}{HORIZONTAL * inner_width}{RIGHT_BOTTOM}", flush=True)

# Optional flourish
print("\033[38;5;248m" + "─" * inner_width + "\033[0m", flush=True)
print("\033[1m" + "— Woody Allen (in spirit)".center(inner_width + 4) + "\033[0m", flush=True)

# Restore cursor visibility
print("\033[?25h", flush=True)

# Keep the terminal open a bit
time.sleep(1)
sys.stdout.write("\nPress Enter to exit...")
sys.stdout.flush()
sys.stdin.readline()