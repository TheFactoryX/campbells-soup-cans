"""
Campbell's Soup Can #5011
Produced: 2026-09-23 11:38:10
Worker: inclusionAI: Ling 3.0 Flash VL (free) (inclusionai/ling-3.0-flash-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophical Quote Generator
A visually rich, animated terminal experience — pure Python, zero dependencies.
"""

import sys
import time
import itertools
import threading

# ── ANSI Color Palette ──────────────────────────────────────────────
class C:
    RED     = '\033[91m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    GREEN   = '\033[92m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    RESET   = '\033[0m'
    BLINK   = '\033[5m'
    INV     = '\033[7m'
    UNDERL  = '\033[4m'

# ── ASCII Art: Neurotic Philosopher ─────────────────────────────────
PHILOSOPHER = f"""
{C.CYAN}{C.BOLD}
    ╭─────────╮
    │  o  o   │{C.RESET}{C.YELLOW}
    │    <    │  {C.RESET}{C.CYAN}∧＿∧
    │  ╭───╮  │{C.RESET}{C.YELLOW}  (ｏ′ε′｀) つ・゜゜・。
    │  │   │  │{C.RESET}{C.CYAN}  /　　　　  ＼
    ╰──┴───┴──╯{C.RESET}{C.YELLOW} ⊹⊹⊹⊹⊹⊹⊹⊹⊹⊹⊹{C.RESET}{C.CYAN}  なんかメンタルがやばい
{C.RESET}"""

# ── Decorative Frame ────────────────────────────────────────────────
def frame_block(color=C.MAGENTA):
    return f"{color}█{C.RESET}"

def build_frame(width=72):
    corner = f"{C.MAGENTA}╔{C.RESET}"
    corner_end = f"{C.MAGENTA}╗{C.RESET}"
    side = f"{C.MAGENTA}║{C.RESET}"
    bottom = f"{C.MAGENTA}╚{C.RESET}"
    bottom_end = f"{C.MAGENTA}╝{C.RESET}"

    top = corner + "═" * (width - 2) + corner_end
    bot = bottom + "═" * (width - 2) + bottom_end
    return top, bot, side

# ── Animated Typewriter ─────────────────────────────────────────────
def typewriter(text, char_delay=0.035, color=C.WHITE, bold=True):
    prefix = f"{C.BOLD if bold else ''}{color}"
    for i, ch in enumerate(text):
        sys.stdout.write(prefix + ch + C.RESET)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write(C.RESET)

# ── Color-cycling print ─────────────────────────────────────────────
def rainbow_print(text, delay=0.02):
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    for i, ch in enumerate(text):
        if ch == '\n':
            sys.stdout.write('\n')
            continue
        col = colors[i % len(colors)]
        sys.stdout.write(f"{C.BOLD}{col}{ch}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C.RESET)

# ── Blinking emphasis ───────────────────────────────────────────────
def print_with_blink_sections(plain_text, blink_sections, base_color=C.WHITE):
    """Print text where certain substrings blink."""
    idx = 0
    for section in blink_sections:
        start, end = section
        # Print plain part before this section
        plain_part = plain_text[idx:start]
        sys.stdout.write(f"{C.BOLD}{base_color}{plain_part}{C.RESET}")
        sys.stdout.flush()
        # Print blinking part
        blink_part = plain_text[start:end]
        for _ in range(6):
            sys.stdout.write(f"{C.BLINK}{C.RED}{C.BOLD}{blink_part}{C.RESET}")
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write(f"{C.BOLD}{base_color}{blink_part}{C.RESET}")
            sys.stdout.flush()
            time.sleep(0.2)
        idx = end
    # Remaining text
    sys.stdout.write(f"{C.BOLD}{base_color}{plain_text[idx:]}{C.RESET}")
    sys.stdout.flush()

# ── Spinner animation for dramatic pause ────────────────────────────
def spinner(duration=1.2):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{C.YELLOW}{C.BOLD}{frames[i % len(frames)]}{C.RESET} ")
        sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    sys.stdout.write(" " * 20 + "\r")
    sys.stdout.flush()

# ── Dotted separator with animation ─────────────────────────────────
def animated_dots(width=70, color=C.CYAN):
    dots = f"{color}·{C.RESET}"
    line = ""
    for i in range(width):
        line += dots
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(0.008)
    sys.stdout.write(C.RESET)

# ── Main Program ────────────────────────────────────────────────────
def main():
    # Hide cursor during animation
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

    try:
        width = 72
        top, bot, side = build_frame(width)

        # ── PHASE 1: Title ──────────────────────────────────────────
        sys.stdout.write("\n\n")
        print(f"{C.MAGENTA}{C.BOLD}{' WOODY '.center(width - 2, '─')}{C.RESET}")
        print(f"{C.YELLOW}{'A Philosophical Output'.center(width - 2, ' ')}{C.RESET}")
        print(f"{C.MAGENTA}{'═' * (width - 2)}{C.RESET}\n")

        # ── PHASE 2: ASCII Art ──────────────────────────────────────
        print(PHILOSOPHER)
        time.sleep(0.5)

        print(f"\n{top}")
        print(f"{side}{'─' * (width - 2)}{side}")

        # ── PHASE 3: Decorative line ────────────────────────────────
        animated_dots(width - 2, C.MAGENTA)
        print()

        # ── PHASE 4: The Quote ──────────────────────────────────────
        quote = (
            "Existence is a tiny, insignificant speck "
            "in an indifferent universe — and somehow, "
            "that's the funniest thing I've ever heard."
        )

        label = f" {C.UNDERL}{C.YELLOW}THE QUOTE{C.RESET}{C.BOLD} {C.GREEN}"
        padded = label.center(width - 2)
        print(f"{side}{padded}{side}")

        print(f"{side}{'─' * (width - 2)}{side}")

        # Print the quote with dramatic intro
        time.sleep(0.3)
        intro = "    "
        sys.stdout.write(f"{side}{C.DIM}{intro}")
        sys.stdout.flush()
        time.sleep(0.5)

        # Typewriter effect for the quote
        typewriter(quote, char_delay=0.04, color=C.WHITE, bold=True)

        # Punchline section — blink the key words
        print(f"\n\n{side}{C.DIM}    {C.RESET}", end="")
        punchline = (
            "that's the funniest thing "
            "I've ever heard."
        )
        # Actually let's re-print punchline with blink
        sys.stdout.write(f"{C.DIM}Well, the kicker is — and I want "
                         f"you to really hear this — {C.RESET}")
        sys.stdout.flush()
        time.sleep(0.4)

        # Blink the philosophical punchline
        blink_text = "the universe doesn't even know we're here"
        print_with_blink_sections(
            f" {blink_text}, ",
            [(1, len(blink_text) + 1)],
            base_color=C.RED
        )
        sys.stdout.write(f" {C.YELLOW}{C.BOLD}which really just proves my point{C.RESET}")
        sys.stdout.flush()

        print()
        time.sleep(0.3)

        # ── PHASE 5: More dots ──────────────────────────────────────
        animated_dots(width - 2, C.BLUE)
        print()

        # ── PHASE 6: Sub-quote / meta comment ───────────────────────
        meta = f"{C.GREEN}{C.DIM}{side}  \"I'd rather be in Philadelphia.\" — W.A.  {C.RESET}"
        meta = meta.ljust(width) + side
        print(meta)

        print(f"{side}{'─' * (width - 2)}{side}")

        # ── PHASE 7: Dramatic pause with spinner ────────────────────
        sys.stdout.write(f"{side}  ")
        spinner(1.5)
        sys.stdout.write(f"{C.YELLOW}{C.BOLD}  Existential dread: loaded{C.RESET}")
        print(f"{' ' * 20}{side}")

        # ── PHASE 8: Bottom frame ───────────────────────────────────
        print(f"{side}{'─' * (width - 2)}{side}")
        animated_dots(width - 2, C.RED)
        print()
        print(f"{side}{C.MAGENTA}{' THE END '.center(width - 2, ' ')}{C.RESET}{side}")
        print(bot)

        # ── PHASE 9: Final credit with rainbow ──────────────────────
        print()
        rainbow_print(
            "  ╭─── Quote generated at " + time.strftime("%H:%M:%S") + " ───╮\n"
            "  │ Every existential crisis is just growth in disguise.    │\n"
            "  │ (This crisis, however, is mostly about laundry.)         │\n"
            "  ╰──────────────────────────────────────────────────────────╯",
            delay=0.005
        )
        print(f"\n{C.DIM}{C.CYAN}  ☕  System note: Woody would've preferred a coffee.{C.RESET}")

    finally:
        # Show cursor again
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()


if __name__ == "__main__":
    main()