"""
Campbell's Soup Can #5216
Produced: 2026-11-07 10:11:08
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

# ─── ANSI color palette ───
RST   = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
ITAL  = "\033[3m"
UL    = "\033[4m"
BLK   = "\033[30m"
RED   = "\033[31m"
GRN   = "\033[32m"
YEL   = "\033[33m"
BLU   = "\033[34m"
MAG   = "\033[35m"
CYN   = "\033[36m"
WHT   = "\033[37m"
BRED  = "\033[91m"
BGRN  = "\033[92m"
BYEL  = "\033[93m"
BBLU  = "\033[94m"
BMAG  = "\033[95m"
BCYN  = "\033[96m"
BWHT  = "\033[97m"
BG_BLK = "\033[40m"
BG_RED = "\033[41m"
BG_GRN = "\033[42m"
BG_YEL = "\033[43m"
BG_BLU = "\033[44m"
BG_MAG = "\033[45m"
BG_CYN = "\033[46m"
BG_WHT = "\033[47m"

# ─── Woody Allen original quote ───
QUOTE = (
    "I told my analyst I was having an identity crisis.\n"
    "He said, 'That'll be $300 — and who's asking?'"
)

# ─── ASCII Woody (glasses + neurotic posture) ───
WOODY_FRAMES = [
    f"""
{CYN}      ╔══════════════════════════════════╗
      ║  {BWHT}┌────────────────────┐{CYN}  ║
      ║  {BWHT}│  {BLK}◯────────────◯{BWHT}  │{CYN}  ║   {YEL}*adjusts glasses nervously*{RST}
      ║  {BWHT}│       {BLK}╭───╮{BWHT}        │{CYN}  ║
      ║  {BWHT}│       {BLK}│   │{BWHT}        │{CYN}  ║
      ║  {BWHT}│       {BLK}╰───╯{BWHT}        │{CYN}  ║
      ║  {BWHT}└────────────────────┘{CYN}  ║
      ║         {BMAG}││{CYN}         {BMAG}││{CYN}          ║
      ╚══════════════════════════════════╝{RST}
""",
    f"""
{CYN}      ╔══════════════════════════════════╗
      ║  {BWHT}┌────────────────────┐{CYN}  ║
      ║  {BWHT}│  {BLK}◯────────────◯{BWHT}  │{CYN}  ║   {YEL}*taps temple*{RST}
      ║  {BWHT}│       {BLK}╭─────╮{BWHT}      │{CYN}  ║
      ║  {BWHT}│       {BLK}│  ◉  │{BWHT}      │{CYN}  ║
      ║  {BWHT}│       {BLK}╰─────╯{BWHT}      │{CYN}  ║
      ║  {BWHT}└────────────────────┘{CYN}  ║
      ║         {BMAG}││{CYN}         {BMAG}││{CYN}          ║
      ╚══════════════════════════════════╝{RST}
""",
]

# ─── Typewriter effect ───
def typewriter(text, delay=0.025, color=BWHT):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RST}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ─── Fade-in box lines ───
def print_boxed_quote(lines, border_color=CYN, text_color=BWHT, pad=2, delay=0.04):
    max_len = max(len(l) for l in lines)
    inner_w = max_len + pad * 2
    top = f"{border_color}╔{'═' * inner_w}╗{RST}"
    bot = f"{border_color}╚{'═' * inner_w}╝{RST}"
    print(top)
    for line in lines:
        padded = " " * pad + line.ljust(max_len) + " " * pad
        sys.stdout.write(f"{border_color}║{RST}{text_color}{padded}{RST}{border_color}║{RST}\n")
        sys.stdout.flush()
        time.sleep(delay)
    print(bot)

# ─── Main show ───
def main():
    # Clear screen
    print("\033[2J\033[H", end="")

    # Title card
    title = f"{BOLD}{BMAG}WOODY ALLEN'S DAILY NEUROSIS{RST}"
    subtitle = f"{DIM}{ITAL}Presented without clinical supervision{RST}"
    print(f"\n{title:^70}")
    print(f"{subtitle:^70}\n")

    # Animate Woody
    for _ in range(2):
        for frame in WOODY_FRAMES:
            print("\033[2J\033[H", end="")
            print(f"{title:^70}")
            print(f"{subtitle:^70}\n")
            print(frame)
            time.sleep(0.6)

    # Final Woody pose
    print("\033[2J\033[H", end="")
    print(f"{title:^70}")
    print(f"{subtitle:^70}\n")
    print(WOODY_FRAMES[0])

    # Quote box
    quote_lines = QUOTE.split("\n")
    print()
    print_boxed_quote(quote_lines, border_color=BMAG, text_color=BYEL, delay=0.08)

    # Punchline tag
    print()
    tag = f"{DIM}{ITAL}— Probably billable hours{RST}"
    typewriter(tag, delay=0.03, color=BCYN)

    # Final flourish
    print()
    flourish = f"{BLK}{BG_YEL}  EXISTENTIAL DREAD: 10/10 WOULD RECOMMEND  {RST}"
    print(f"{flourish:^70}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Interrupted. My therapist says that's a defense mechanism.{RST}")