"""
Campbell's Soup Can #1641
Produced: 2026-01-16 08:47:55
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
A Woody Allen-esque philosophical quote, delivered with a dash of color and motion.
No external dependencies — just pure Python.
"""

import time
import random
import sys

# ANSI helpers
def ansi(code: str) -> str:
    return f"\033[{code}m"

def style_text(text: str, fg=None, bg=None, bold=False, italic=False, underline=False, blink=False) -> str:
    codes = []
    if bold: codes.append("1")
    if italic: codes.append("3")
    if underline: codes.append("4")
    if blink: codes.append("5")
    if fg:
        if isinstance(fg, int):
            codes.append(f"38;5;{fg}")
        elif isinstance(fg, str) and fg.startswith("#"):
            r = int(fg[1:3], 16)
            g = int(fg[3:5], 16)
            b = int(fg[5:7], 16)
            codes.append(f"38;2;{r};{g};{b}")
    if bg:
        if isinstance(bg, int):
            codes.append(f"48;5;{bg}")
        elif isinstance(bg, str) and bg.startswith("#"):
            r = int(bg[1:3], 16)
            g = int(bg[3:5], 16)
            b = int(bg[5:7], 16)
            codes.append(f"48;2;{r};{g};{b}")
    return ansi(";".join(codes)) + text + ansi("0")

def terminal_size():
    try:
        import shutil
        cols, lines = shutil.get_terminal_size()
        return cols, lines
    except Exception:
        return 80, 24

# A gentle, neurotic typewriter effect
def typewriter_print(text, speed=0.025, color="#FFD700", cursor_blink=True):
    for ch in text:
        # Sometimes the cursor hesitates (anxiety)
        if ch in ".,":
            time.sleep(speed * 2)
        sys.stdout.write(style_text(ch, fg=color))
        sys.stdout.flush()
        time.sleep(random.uniform(speed * 0.7, speed * 1.3))
    if cursor_blink:
        for _ in range(3):
            sys.stdout.write(style_text("▌", fg="#FF8C00", blink=True))
            sys.stdout.flush()
            time.sleep(0.15)
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            time.sleep(0.15)
    sys.stdout.write("\n")

def jittery_print(text, color="#FFD700"):
    # Prints with a slight random horizontal jitter to simulate neurotic typing
    for ch in text:
        if ch == " ":
            sys.stdout.write(" ")
        else:
            offset = random.choice(["", "", "", "\033[1C", "\033[2C", "\b"])
            sys.stdout.write(offset + style_text(ch, fg=color))
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.06))
    sys.stdout.write("\n")

def draw_ascii_microphone(width=40):
    # A tiny stage mic with dramatic lighting
    base = [
        r"      .-''''-.     ",
        r"     /  _   _ \    ",
        r"    |  (o) (o) |   ",
        r"    |     >    |   ",
        r"     \  ._.'  /    ",
        r"      '-....-'     ",
        r"         | |       ",
        r"         | |       ",
        r"        _|_|_      "
    ]
    # Center align in width
    margin = max(0, (width - max(len(l) for l in base)) // 2)
    for line in base:
        print(" " * margin + style_text(line, fg="#C0C0C0"))

def draw_box(text, width=60):
    """
    Draw a theatrical box around the quote with subtle colored borders.
    """
    padding = 2
    content_width = width - 2 - (padding * 2)
    # Wrap text manually
    words = text.split()
    lines = []
    current = []
    for w in words:
        if len(" ".join(current + [w])) <= content_width:
            current.append(w)
        else:
            lines.append(" ".join(current))
            current = [w]
    if current:
        lines.append(" ".join(current))

    # Colors
    border_fg = "#8A2BE2"  # BlueViolet
    title_fg = "#FFD700"   # Gold
    text_fg = "#87CEEB"    # SkyBlue

    # Top border
    print(style_text("╭" + "─" * (width - 2) + "╮", fg=border_fg))

    # Title
    title = " WOODY ALLEN STYLE PHILOSOPHY "
    side = (width - 2 - len(title)) // 2
    print(style_text("│", fg=border_fg)
          + style_text(" " * side + title + " " * (width - 2 - side - len(title)), bg="#121212", fg=title_fg, bold=True)
          + style_text("│", fg=border_fg))

    # Divider
    print(style_text("├" + "─" * (width - 2) + "┤", fg=border_fg))

    # Quote lines
    for i, line in enumerate(lines):
        padded = line.center(content_width)
        if i == 0:
            print(style_text("│", fg=border_fg)
                  + style_text(" " * padding + padded + " " * padding, fg=text_fg, italic=True, bg="#0E0E0E")
                  + style_text("│", fg=border_fg))
        else:
            print(style_text("│", fg=border_fg)
                  + style_text(" " * padding + padded + " " * padding, fg="#B0E0E6", italic=True, bg="#0E0E0E")
                  + style_text("│", fg=border_fg))

    # Bottom border
    print(style_text("╰" + "─" * (width - 2) + "╯", fg=border_fg))

def pulse_text(text, colors=["#FFD700", "#FFA500", "#FF8C00", "#FF6347"]):
    """
    Print text with pulsating colors. Simulates stage lights changing.
    """
    for ch in text:
        c = random.choice(colors)
        sys.stdout.write(style_text(ch, fg=c, bold=True))
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")

def cursor_back(n=1):
    sys.stdout.write(f"\033[{n}D")

def theatrical_lights(width=60, cycles=2, speed=0.06):
    """
    A tiny stage light effect across the terminal.
    """
    base = " " * width
    for _ in range(cycles):
        for i in range(width):
            left = style_text(base[:i], fg="#111111")
            mid = style_text("★", fg="#FFD700", bold=True)
            right = style_text(base[i+1:], fg="#111111")
            sys.stdout.write("\r" + left + mid + right)
            sys.stdout.flush()
            time.sleep(speed)
        for i in range(width - 1, -1, -1):
            left = style_text(base[:i], fg="#111111")
            mid = style_text("★", fg="#FFD700", bold=True)
            right = style_text(base[i+1:], fg="#111111")
            sys.stdout.write("\r" + left + mid + right)
            sys.stdout.flush()
            time.sleep(speed)
    sys.stdout.write("\r" + " " * width + "\r\n")

def main():
    # Clear screen (optional) — use a gentle fade instead
    # print("\033[2J", end="")

    width, height = terminal_size()
    stage_width = min(width - 4, 70)

    print()
    theatrical_lights(width=stage_width, cycles=1, speed=0.05)
    draw_ascii_microphone(stage_width)
    print()

    # The philosophical quote (in Woody Allen's voice)
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens, "
        "and frankly, I'd prefer a refund if consciousness ends with a cosmic 'no refunds' policy."
    )

    # Display in a fancy box
    draw_box(quote, width=stage_width)

    print()
    # Add a neurotic postscript in a jittery typewriter
    jittery_print("— delivered with existential anxiety and a suspiciously hopeful glimmer.", "#FF8C00")

    # A final, self-deprecating curtain call
    typewriter_print("Good night, and if you're out there, please don't applaud; I'm easily startled.", speed=0.035, color="#FFD700")

if __name__ == "__main__":
    main()