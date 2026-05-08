"""
Campbell's Soup Can #3610
Produced: 2026-05-08 21:29:25
Worker: Baidu Qianfan: CoBuddy (free) (baidu/cobuddy:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI escape codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[97m"

def color_cycle(text: str, colors: list, delay: float = 0.08) -> None:
    """Print *text* cycling through *colors* with a short *delay* between changes."""
    for c in colors:
        sys.stdout.write(f"{c}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main() -> None:
    # ── ASCII art frame ───────────────────────────────────────
    frame = [
        f"{CYAN}╔{'═' * 60}╗{RESET}",
        f"{CYAN}║{WHITE}{'Woody Allen on Life, the Universe, and My Keys':^60}{RESET}{CYAN}║{RESET}",
        f"{CYAN}║{WHITE}{'':^60}{RESET}{CYAN}║{RESET}",
        f"{CYAN}╚{'═' * 60}╝{RESET}",
    ]
    for line in frame:
        sys.stdout.write(line + "\n")
    sys.stdout.flush()
    time.sleep(0.4)

    # ── Animated bouncing dot ─────────────────────────────────
    dot = f"{GREEN}●{RESET}"
    for i in range(61):
        sys.stdout.write(
            f"\r{CYAN}╠{'─' * i}{dot}{'─' * (60 - i)}╣{RESET}"
        )
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write("\n")
    sys.stdout.flush()
    time.sleep(0.3)

    # ── The quote (color‑cycled) ──────────────────────────────
    quote = (
        "I'm not afraid of death; I just don't want to be there "
        "when it happens."
    )
    colors = [RED, YELLOW, GREEN, BLUE, MAGENTA, CYAN]
    sys.stdout.write(f"{DIM}{BOLD}Woody says:{RESET} ")
    sys.stdout.flush()
    color_cycle(quote, colors, delay=0.07)

    # ── Blinking asterisks ────────────────────────────────────
    for _ in range(3):
        sys.stdout.write(f"{YELLOW}*{RESET}")
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write(f"\b{RESET}{DIM} {RESET}")
        sys.stdout.flush()
        time.sleep(0.25)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()