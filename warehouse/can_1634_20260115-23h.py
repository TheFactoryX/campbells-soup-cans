"""
Campbell's Soup Can #1634
Produced: 2026-01-15 23:32:58
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen-esque philosophical quote, presented with playful flair.
No dependencies. Runs as a single file. ANSI colors + subtle animation.
"""

import sys
import time
import random

# Try to detect Windows for ANSI enabling (if needed). Pure Python.
if sys.platform.startswith("win"):
    import os

    # Enable ANSI escape codes on Windows (may not work in all terminals)
    os.system("")  # nosec


def ansi(color_fg="", color_bg="", style=""):
    """Return ANSI escape sequence for styling."""
    codes = []
    if style:
        codes.append(style)
    if color_fg:
        codes.append(color_fg)
    if color_bg:
        codes.append(color_bg)
    return "\x1b[" + ";".join(codes) + "m" if codes else ""


def reset():
    return "\x1b[0m"


def stylize(text, fg=None, bg=None, style=None):
    """Wrap text with ANSI codes."""
    return f"{ansi(fg, bg, style)}{text}{reset()}"


def pause(sec):
    """Sleep with flush to keep output smooth."""
    time.sleep(sec)
    sys.stdout.flush()


def fade_print(text, fg_colors, bg=None, style=None, duration=1.5, steps=20):
    """Print text with a soft fade-in effect using foreground color cycling."""
    # Normalize colors to ANSI codes
    codes = []
    if bg:
        codes.append(bg)
    if style:
        codes.append(style)

    base = ""
    if codes:
        base = "\x1b[" + ";".join(codes) + "m"

    # Ensure at least one color
    if not fg_colors:
        fg_colors = ["37"]  # default white

    for i in range(steps + 1):
        t = i / max(steps, 1)
        idx = int(t * (len(fg_colors) - 1))
        fg = fg_colors[idx]
        prefix = base + fg if base else fg
        sys.stdout.write("\r" + prefix + text[:int(len(text) * t)] + reset())
        pause(duration / steps)
    sys.stdout.write("\n")


def gentle_blink(text, fg="37", bg=None, repeats=3, on=0.5, off=0.3):
    """Blink text a few times softly."""
    for _ in range(repeats):
        # ON
        sys.stdout.write("\r" + ansi(fg, bg) + text + reset())
        pause(on)
        # OFF
        sys.stdout.write("\r" + " " * len(text))
        pause(off)
    # Final draw
    sys.stdout.write("\r" + ansi(fg, bg) + text + reset() + "\n")


def draw_box(lines, border_fg="36", border_bg=None, text_fg="97", text_bg=None, style=None):
    """
    Draw a pretty box around lines of text using ASCII borders and ANSI styles.
    """
    # Measure width (including ANSI codes stripped)
    def strip_ansi(s):
        import re
        return re.sub(r"\x1b\[[0-9;]*m", "", s)

    clean_lines = [strip_ansi(l) for l in lines]
    width = max((len(l) for l in clean_lines), default=0) + 4  # padding

    # Border styling
    border_style = ansi(border_fg, border_bg, style)
    text_style_start = ansi(text_fg, text_bg, style)
    text_style_end = reset()

    # Borders
    horiz = border_style + "─" * (width - 2) + reset()
    top = border_style + "╭" + "─" * (width - 2) + "╮" + reset()
    bottom = border_style + "╰" + "─" * (width - 2) + "╯" + reset()
    side = border_style + "│" + reset()

    # Compose
    result = []
    result.append(top)
    for line in lines:
        padded = line + " " * (width - 2 - len(strip_ansi(line)))
        result.append(f"{side} {text_style_start}{padded}{text_style_end}{side}")
    result.append(bottom)
    return "\n".join(result)


def create_quote():
    """Craft a Woody Allen-esque philosophical quote."""
    # Multiple options to keep it fresh (still prints ONE per run)
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering—and it's all over far too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "If you want to make God laugh, tell him your plans; then laugh nervously and check your pulse.",
        "My relationship with reality is like Wi‑Fi: occasionally connected, mostly buffering.",
        "I never understood the point of meditation; my mind already trips over itself in perfect silence.",
        "Dating is a battle of wits where I am unarmed and mildly allergic to enthusiasm.",
        "Time is a great teacher, but unfortunately it kills all its students—and bills me for the lesson.",
        "I'm at an age where my back goes out more than I do.",
        "I'm not clumsy; I’m just auditioning for the role of 'gravity's favorite comedian.'"
    ]
    return random.choice(quotes)


def main():
    # Setup palette: from pale gray to warm amber to soft red (woody neurotic palette)
    palette = ["90", "100", "102", "108", "142", "178", "180", "167"]
    bg = "48;5;235"  # deep charcoal background
    style = "3"      # italic

    # Introduce with a small animation
    intro = "A Woody Allen-esque Thought..."
    gentle_blink(intro, fg="36", bg=None, repeats=2, on=0.6, off=0.25)

    # Fade-in the philosophical quote
    quote = create_quote()
    fade_print(quote, palette, bg=bg, style=style, duration=2.0, steps=24)

    # Decorative border with a tiny footnote (self-deprecating wink)
    lines = [
        stylize("— A small existential flourish —", fg="90", bg=None, style="2"),
        stylize("Cue the neurotic jazz. Life: A long intermission.", fg="220", bg=None, style="1")
    ]
    box = draw_box(
        lines,
        border_fg="245",
        border_bg=bg,
        text_fg="250",
        text_bg=bg,
        style=None
    )
    print("\n" + box)

    # Subtle closing flicker
    flicker_text = stylize("[ctrl+C for panic mode]", fg="238", bg=None, style="2")
    gentle_blink(flicker_text, fg="238", repeats=1, on=0.4, off=0.2)


if __name__ == "__main__":
    main()