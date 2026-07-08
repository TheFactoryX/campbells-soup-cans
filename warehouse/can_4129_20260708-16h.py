"""
Campbell's Soup Can #4129
Produced: 2026-07-08 16:49:41
Worker: MiniMax: MiniMax M2 (minimax/minimax-m2)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# A tiny, colorful Woody-Allen-esque philosophical moment.
import sys
import time
import shutil

# ANSI color codes
RESET = "\x1b[0m"
BRIGHT = "\x1b[1m"
DIM = "\x1b[2m"
BORDER = "\x1b[38;5;201m"   # vivid magenta for the box
ACCENT = "\x1b[38;5;45m"    # teal for accents
QUOTE = "\x1b[38;5;222m"    # warm yellow for the quote
AUTHOR = "\x1b[38;5;75m"    # light blue for attribution
SHADOW = "\x1b[48;5;236m"   # subtle shadow background for the box

def term_size(fallback=(80, 24)):
    try:
        w, h = shutil.get_terminal_size(fallback=fallback)
        return max(10, w), max(5, h)
    except Exception:
        return fallback

def clear_line():
    # Return to column 0 and clear the line
    return "\r\x1b[K"

def delay_for_char(ch):
    if ch in ".,!?;:":
        return 0.06
    if ch == " ":
        return 0.02
    return 0.03

def fit_quote(quote, width):
    # Simple word wrap that respects the width
    words = quote.split()
    lines = []
    current = []
    for w in words:
        if not current:
            current.append(w)
            continue
        cand = " ".join(current + [w])
        if len(cand) > width:
            lines.append(" ".join(current))
            current = [w]
        else:
            current.append(w)
    if current:
        lines.append(" ".join(current))
    return lines

def draw_box_top(width):
    print(f"{BORDER}┌{'─' * (width - 2)}┐{RESET}", flush=True)

def draw_box_middle(line, width, left="│", right="│"):
    print(f"{BORDER}{left}{RESET}{line:{}>{width}}{BORDER}{right}{RESET}", flush=True)

def draw_box_bottom(width):
    print(f"{BORDER}└{'─' * (width - 2)}┘{RESET}", flush=True)

def print_shadow(width, height):
    # Print a soft shadow beneath the box to give it some depth
    shadow_line = f"{SHADOW} {'─' * (width - 2)} {RESET}"
    empty_line = f"{SHADOW}{' ' * width}{RESET}"
    print(clear_line() + empty_line, end="", flush=True)
    print(clear_line() + shadow_line, end="", flush=True)
    # Move back up to continue printing above the shadow
    print(f"\x1b[{height+1}A", end="", flush=True)

def animate_quote_in_box(lines):
    # Build the empty box first
    width, _ = term_size()
    inner = max(10, min(78, width - 6))  # inner text width
    box_width = inner + 4
    top = f"{BORDER}┌{'─' * (box_width - 2)}┐{RESET}"
    bottom = f"{BORDER}└{'─' * (box_width - 2)}┘{RESET}"
    sideL = f"{BORDER}│{RESET}"
    sideR = f"{BORDER}│{RESET}"

    # Precompute centered lines (for a static fallback, though we animate)
    centered = []
    for ln in lines:
        if len(ln) > inner:
            ln = ln[:inner]
        centered.append(" " * ((inner - len(ln)) // 2) + ln)

    # Print the frame
    print(top)
    for _ in lines:
        print(f"{sideL}{' ' * inner}{sideR}", flush=True)
    print(bottom)

    # Soft shadow (purely visual)
    print_shadow(box_width, len(lines) + 2)

    # Move cursor to the top inside the box to start typing
    print(f"\x1b[{len(lines)}A", end="")  # go up to the top line of the box interior
    print(f"{BORDER}│{RESET}", end="", flush=True)
    print(" " * ((inner - len(lines[0])) // 2), end="", flush=True)

    # Typewriter animation line by line
    for i, raw_line in enumerate(lines):
        # Compute left padding so the text is centered
        pad = max(0, (inner - len(raw_line)) // 2)
        # Move to the start of the current interior line
        # Up to top interior line
        print(f"\x1b[{i}A", end="")
        # Move to the inside of the left border
        print(f"{BORDER}│{RESET}", end="")
        # Print the left padding
        print(" " * pad, end="")
        sys.stdout.flush()

        # Type each character
        for ch in raw_line:
            print(f"{QUOTE}{ch}{RESET}", end="", flush=True)
            time.sleep(delay_for_char(ch))
        # After finishing the line, move down to next line
        # Ensure the right border is drawn if the line was shorter
        remaining = inner - (pad + len(raw_line))
        if remaining > 0:
            print(" " * remaining, end="", flush=True)
        print(f"{BORDER}│{RESET}", flush=True)

    # Add a small caption beneath the box (not part of the quote)
    caption = "A WOODY ALLEN MOMENT"
    cap_pad = max(0, (box_width - 2 - len(caption)) // 2)
    print(f"\x1b[B", end="")  # move one line below the box
    print(f"{clear_line()}{' ' * cap_pad}{ACCENT}{BRIGHT}{caption}{RESET}")

def main():
    # Woody-Allen-esque quote
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "I'd also consider not being anywhere near the RSVP list."
    )
    # If terminal is too narrow, we'll still try; wrap to inner width
    width, _ = term_size()
    inner = max(10, min(78, width - 6))
    lines = fit_quote(quote, inner)

    # ASCII garnish (top flair)
    flair = [
        "   _   ",
        "  (')  ",
        "  /-\\  ",
        "  \"/\\\" ",
    ]
    for line in flair:
        pad = max(0, (width - len(line)) // 2)
        print(f"{ACCENT}{line:>{pad + len(line)}}{RESET}")

    animate_quote_in_box(lines)

    # Tiny flourish at the end (one blink)
    print(f"{DIM}...{RESET}")
    for _ in range(1):
        sys.stdout.write("\x1b[5m")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\x1b[25m")
        sys.stdout.flush()

if __name__ == "__main__":
    main()