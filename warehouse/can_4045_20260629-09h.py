"""
Campbell's Soup Can #4045
Produced: 2026-06-29 09:58:57
Worker: OpenAI: GPT-5.4 Nano (openai/gpt-5.4-nano)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# A single-file, no-deps, playful “Woody-ish” neurotic philosophy print.
# (Original quote generated below; formatting is the fun part.)

import sys
import time
import random

def ansi(code: str) -> str:
    return f"\033[{code}m"

RESET = ansi("0")
BOLD = ansi("1")
DIM = ansi("2")

COLORS = [
    "91",  # bright red
    "93",  # bright yellow
    "92",  # bright green
    "96",  # bright cyan
    "95",  # bright magenta
    "94",  # bright blue
]

# Cute ASCII “existential brain” + question mark
BRAIN = [
    "          .-\"\"\"-.",
    "       .-'  _   _ '-.",
    "     .'   _(_)_(_)_  '.",
    "    /    (o)  (o)     \\",
    "   ;      .-.__.-.     ;",
    "   |     /  .--.  \\    |",
    "   |    |  (____) |   |",
    "   ;     \\   --   /    ;",
    "    \\      '-..-'     /",
    "     '.              .'",
    "       '-.______. -' ",
]

QUOTE = (
    "I’m not afraid of death—"
    " I’m afraid of living with the certainty that I’ve misunderstood everything. "
    "Which is comforting, in a panic-attack kind of way."
)

def color_cycle_text(text: str, steps: int = 18, seed: int | None = None) -> str:
    """Return a string with ANSI-colored characters to create a lively banner."""
    rng = random.Random(seed)
    out = []
    for i, ch in enumerate(text):
        if ch == " ":
            out.append(ch)
            continue
        c = COLORS[(i + rng.randint(0, 2)) % len(COLORS)]
        out.append(ansi(f"{c}m") + ch)
    out.append(RESET)
    return "".join(out)

def print_frame(t: float):
    """Render a little animated thought bubble with a ticking cursor."""
    width = 60
    # Bubble top
    border_col = COLORS[int((t * 3) % len(COLORS))]
    border = ansi(f"{border_col}m") + "┌" + ("─" * (width - 2)) + "┐" + RESET
    mid_l = ansi(f"{border_col}m") + "│" + RESET
    mid_r = ansi(f"{border_col}m") + "│" + RESET

    # Animate the “?” and cursor
    q = "?"
    q_color = COLORS[int((t * 5) % len(COLORS))]
    q_str = ansi(f"{q_color}m") + q + RESET

    cursor_chars = ["∙  ", "∙∙ ", "∙∙∙", " .. ", "  . "]
    cursor = cursor_chars[int((t * 6) % len(cursor_chars))]

    # Two lines of “philosophy”
    line1 = f"  {q_str}  I keep asking: what if the universe is just one long, anxious joke?  "
    line1 = line1[:width - 2].ljust(width - 2)

    line2 = f"  {cursor}  {DIM}breathe.{RESET} {BOLD}try not to overthink.{RESET}"
    line2 = line2[:width - 2].ljust(width - 2)

    sys.stdout.write("\033[2J\033[H")  # clear + home
    sys.stdout.write(border + "\n")
    sys.stdout.write(mid_l + line1 + mid_r + "\n")
    sys.stdout.write(mid_l + line2 + mid_r + "\n")
    sys.stdout.write(ansi(f"{border_col}m") + "└" + ("─" * (width - 2)) + "┘" + RESET + "\n")

def wrap_quote(text: str, width: int = 62):
    words = text.split()
    lines = []
    cur = []
    cur_len = 0
    for w in words:
        # +1 for space
        add = len(w) + (1 if cur else 0)
        if cur_len + add > width:
            lines.append(" ".join(cur))
            cur = [w]
            cur_len = len(w)
        else:
            cur.append(w)
            cur_len += add
    if cur:
        lines.append(" ".join(cur))
    return lines

def main():
    # Title banner with color
    title = "NEUROTIC THOUGHT BUBBLE"
    header = color_cycle_text(title, seed=42)
    tagline = f"{ansi('36m')}{BOLD}Existential comedy for one (you).{RESET}"

    # Animate for a brief moment
    for i in range(10):
        t = i / 10
        print_frame(t)
        time.sleep(0.07)

    # Final quote “card”
    width = 62
    lines = wrap_quote(QUOTE, width=width)

    border_col = COLORS[-1]
    border_col2 = COLORS[2]
    top = ansi(f"{border_col2}m") + "┏" + ("━" * (width)) + "┓" + RESET
    bottom = ansi(f"{border_col2}m") + "┗" + ("━" * (width)) + "┛" + RESET

    sys.stdout.write("\033[2J\033[H")  # clear + home
    sys.stdout.write(header + "\n" + tagline + "\n\n")

    # Brain ASCII
    brain_col = ansi(COLORS[1] + "m")  # green/yellow-ish
    sys.stdout.write(brain_col + "\n".join(BRAIN) + RESET + "\n\n")

    sys.stdout.write(top + "\n")
    for ln in lines:
        # Left gutter and right gutter
        ln = ln.ljust(width)
        sys.stdout.write(
            ansi(border_col + "m") + "┃" + RESET +
            ansi("97m") + " " + RESET +
            ansi("93m") + ln + RESET +
            ansi(border_col + "m") + " " + "┃" + RESET + "\n"
        )
    sys.stdout.write(bottom + "\n\n")

    # Closing flourish
    flourish = random.choice([
        "If life is a question, I’m the guy sweating over the punctuation.",
        "I overthink, therefore I accidentally exist.",
        "Some people find meaning. I find typos in my own soul."
    ])
    flourish_col = ansi(COLORS[3] + "m") + BOLD + flourish + RESET

    # Tiny wiggle animation on flourish
    for k in range(6):
        sys.stdout.write("\r" + flourish_col + ansi("2m") + " " + RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()