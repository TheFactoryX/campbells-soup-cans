"""
Campbell's Soup Can #5180
Produced: 2026-10-28 21:05:55
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

# ─── ANSI Color Palette ───
class C:
    RST = "\033[0m"
    BLD = "\033[1m"
    DIM = "\033[2m"
    ITL = "\033[3m"
    UL  = "\033[4m"
    BLK = "\033[30m"
    RED = "\033[31m"
    GRN = "\033[32m"
    YLW = "\033[33m"
    BLU = "\033[34m"
    MAG = "\033[35m"
    CYN = "\033[36m"
    WHT = "\033[37m"
    BG_BLK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GRN = "\033[42m"
    BG_YLW = "\033[43m"
    BG_BLU = "\033[44m"
    BG_MAG = "\033[45m"
    BG_CYN = "\033[46m"
    BG_WHT = "\033[47m"

# ─── The Quote ───
WOODY_QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. "
    "It involves Russia. And peace. Mostly Russia."
)

# ─── Woody-style ASCII portrait ───
WOODY_ART = r"""
       ╭────────────╮
       │  (•_•)     │
       │  <)  )╯    │  "I have a hypochondriac's imagination
       │  /  \      │   and a philosopher's budget."
       ╰────────────╯
"""

# ─── Decorative border pieces ───
TL, TR, BL, BR = "╭", "╮", "╰", "╯"
H, V = "─", "│"
SPARKLES = ["✦", "✧", "★", "☆", "⋆", "✶", "✸", "✹"]

def typewriter(text: str, color: str = C.WHT, delay: float = 0.018, jitter: float = 0.006):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter))
    print()

def sparkle_line(width: int, color: str = C.MAG) -> str:
    """Generate a line of random sparkles."""
    return "".join(random.choice([f"{color}{s}{C.RST}" for s in SPARKLES] + [" "]*3) for _ in range(width))

def print_boxed_quote(quote: str, width: int = 72):
    """Print the quote inside a fancy animated box."""
    lines = []
    words = quote.split()
    line = ""
    for w in words:
        if len(line) + len(w) + 1 > width - 4:
            lines.append(line.strip())
            line = w + " "
        else:
            line += w + " "
    if line:
        lines.append(line.strip())

    # Top border with sparkles
    print(f"\n{C.CYN}{TL}{H * (width - 2)}{TR}{C.RST}")
    print(f"{C.CYN}{V}{C.RST} {sparkle_line(width - 4)} {C.CYN}{V}{C.RST}")

    # Quote lines with typewriter effect
    for i, l in enumerate(lines):
        padding = " " * (width - 4 - len(l))
        sys.stdout.write(f"{C.CYN}{V}{C.RST} {C.YLW}{C.ITL}")
        sys.stdout.flush()
        typewriter(l, color=C.YLW, delay=0.012)
        sys.stdout.write(f"{C.RST}{padding} {C.CYN}{V}{C.RST}\n")

    # Bottom sparkle line + border
    print(f"{C.CYN}{V}{C.RST} {sparkle_line(width - 4)} {C.CYN}{V}{C.RST}")
    print(f"{C.CYN}{BL}{H * (width - 2)}{BR}{C.RST}\n")

def neurotic_footer():
    """A little neurotic post-script."""
    footers = [
        "My analyst says I have a preoccupation with death. \nHe also says I owe him $800. I paid him. With Monopoly money.",
        "The universe is indifferent. My landlord is not. \nGuess which one sends threatening letters?",
        "I've developed a new philosophy: \n'I think, therefore I am... probably overthinking this.'",
        "God is silent. My mother is not. \nCoincidence? I think not.",
    ]
    chosen = random.choice(footers)
    print(f"{C.DIM}{C.MAG}— {chosen}{C.RST}\n")

def main():
    # Clear screen (ANSI)
    print("\033[2J\033[H", end="")

    # Title banner
    title = "  W O O D Y   A L L E N   W I S D O M  "
    banner_w = len(title) + 4
    print(f"{C.BLD}{C.BLU}{TL}{H * (banner_w - 2)}{TR}{C.RST}")
    print(f"{C.BLD}{C.BLU}{V}{C.RST}{C.BLD}{C.YLW}{title}{C.RST}{C.BLD}{C.BLU}{V}{C.RST}")
    print(f"{C.BLD}{C.BLU}{BL}{H * (banner_w - 2)}{BR}{C.RST}\n")

    # ASCII Woody
    for line in WOODY_ART.strip().split("\n"):
        print(f"{C.GRN}{line}{C.RST}")
        time.sleep(0.08)

    print(f"{C.DIM}─" * 60 + f"{C.RST}\n")

    # The main event
    print_boxed_quote(WOODY_QUOTE, width=74)

    # Neurotic footer
    neurotic_footer()

    # Final sparkle
    print(f"{C.CYN}{'✦ ' * 30}{C.RST}")
    print(f"{C.BLD}{C.WHT}  (Press Ctrl+C to escape existential dread){C.RST}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}Aborted. Even the code has commitment issues.{C.RST}\n")
        sys.exit(0)