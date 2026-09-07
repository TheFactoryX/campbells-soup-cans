"""
Campbell's Soup Can #4920
Produced: 2026-09-07 16:27:54
Worker: inclusionAI: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
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
import os

# ─── ANSI Color Codes ────────────────────────────────────────────────
class C:
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    UNDER   = '\033[4m'
    RESET   = '\033[0m'
    BG_RED  = '\033[41m'
    BG_DIM  = '\033[2m'

# ─── Decorative ASCII Art ────────────────────────────────────────────
def draw_border(char='═', color=C.CYAN, width=78):
    print(color + char * width + C.RESET)

def art_pac_man():
    print(f"""
{C.YELLOW}{C.BOLD}
    ╔══════════════════════════════════════════════════════════════╗
    ║     ██████╗ ██╗   ██╗███████╗ █████╗ ███╗   ███╗           ║
    ║    ██╔════╝ ██║   ██║██╔════╝██╔══██╗████╗ ████║          ║
    ║    ██║      ██║   ██║█████╗  ███████║██╔████╔██║          ║
    ║    ██║      ██║   ██║██╔══╝  ██╔══██║██║╚██╔╝██║          ║
    ║    ╚██████╗ ╚██████╔╝███████╗██║  ██║██║ ╚═╝ ██║          ║
    ║     ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝          ║
    ║          ═══════ THE NEUROTIC PHILOSOPHER ═══════          ║
    ╚══════════════════════════════════════════════════════════════╝
{C.RESET}
""")

# ─── Typewriter Effect ───────────────────────────────────────────────
def typewriter(text, delay=0.03, color=C.WHITE, bold=False):
    prefix = C.BOLD if bold else ''
    suffix = C.RESET if bold else ''
    for ch in text:
        if ch == '\n':
            sys.stdout.write('\n')
        else:
            sys.stdout.write(prefix + color + ch + suffix)
        sys.stdout.flush()
        time.sleep(delay)
    print(C.RESET, end='')

def typewriter_colored(segments, delay=0.025):
    """segments is a list of (text, color) tuples"""
    for text, color in segments:
        for ch in text:
            if ch == '\n':
                sys.stdout.write('\n')
            else:
                sys.stdout.write(color + ch + C.RESET)
            sys.stdout.flush()
            time.sleep(delay)
    print()

# ─── Animated Flash Text ─────────────────────────────────────────────
def flash_text(text, colors, flashes=3):
    for _ in range(flashes):
        for color in colors:
            print(f"\r{color}{C.BOLD}{text}{C.RESET}", end='', flush=True)
            time.sleep(0.15)
    print(C.RESET)

# ─── Main Program ────────────────────────────────────────────────────
def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    # ── Intro Animation ────────────────────────────────────────────
    time.sleep(0.5)
    flash_text("A WOODY ALLEN PHILOSOPHICAL EXPERIENCE",
               [C.MAGENTA, C.CYAN, C.YELLOW, C.RED], flashes=4)
    time.sleep(0.3)

    draw_border(color=C.MAGENTA)

    art_pac_man()

    draw_border(color=C.BLUE)

    # ── The Quote ──────────────────────────────────────────────────
    time.sleep(0.5)
    print(f"{C.DIM}{' ':^78}{C.RESET}")
    print(f"{C.BLUE}{'─'*20}{C.DIM}  ☕  {C.BLUE}{'─'*20}{C.RESET}")
    print()

    # Build the quote in segments with different colors
    quote = (
        "I spent years searching for the meaning of life, "
        "and the only thing I found was that my therapist "
        "also charges by the hour for the same existential dread. "
        "The universe is expanding, just like my waistline—"
        "neither stops, and both are a cosmic disappointment. "
        "I don't mind facing death; I just don't want to be there "
        "when it happens, mainly because I forgot to return my "
        "library books and would feel even more inadequate about it."
    )

    # Break quote into color-coded chunks
    chunks = quote.split()
    colors_pool = [C.RED, C.CYAN, C.YELLOW, C.GREEN, C.MAGENTA, C.BLUE, C.WHITE]
    segments = []
    for i, word in enumerate(chunks):
        color = colors_pool[i % len(colors_pool)]
        segments.append((word + ' ', color))

    typewriter_colored(segments, delay=0.018)

    print()
    print(f"{C.BLUE}{'─'*20}{C.DIM}  ☕  {C.BLUE}{'─'*20}{C.RESET}")
    print()

    # ── Woody's Attribution ────────────────────────────────────────
    time.sleep(0.3)
    print(f"{C.DIM}{' ':^78}{C.RESET}")
    print(f"  {C.MAGENTA}{C.BOLD}— Woody Allen{'' * 50}{C.RESET}")
    print(f"  {C.DIM}(or at least, the version of him who really, "
          f"really should have gone to therapy sooner){C.RESET}")
    print()

    draw_border(color=C.RED)

    # ── Closing Wisdom ─────────────────────────────────────────────
    time.sleep(0.5)
    closing = [
        (f"\n{C.YELLOW}{C.BOLD}  💀  Remember: ", C.YELLOW),
        ("You only live once", C.RED),
        (", but if you do it right, once is enough", C.GREEN),
        (". Unless it's a Monday. Then you'll need at least ", C.CYAN),
        ("three", C.YELLOW),
        (".", C.RESET),
    ]
    for text, color in closing:
        for ch in text:
            sys.stdout.write(color + ch + C.RESET)
            sys.stdout.flush()
            time.sleep(0.04)
    print(C.RESET)

    time.sleep(0.3)
    print()
    draw_border(color=C.DIM)
    print(f"{C.DIM}{' ':^78}{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}  🎭  Thanks for your existential contemplation!  🎭{C.RESET}")
    print(f"{C.DIM}{' ':^78}{C.RESET}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}{C.BOLD}\n\n  [ Woody would say: 'I can't hear you — I'm too busy being neurotic.' ]\n{C.RESET}")
        sys.exit(0)