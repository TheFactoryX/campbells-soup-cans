"""
Campbell's Soup Can #3339
Produced: 2026-04-18 11:01:25
Worker: Elephant (openrouter/elephant-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# --- Config ---
DELAY = 0.03
BG = "\033[48;2;15;15;40m"
FG = "\033[38;2;220;220;200m"
HIGHLIGHT = "\033[38;2;255;100;100m"
YELLOW = "\033[38;2;255;200;50m"
RESET = "\033[0m"
BOLD = "\033[1m"

QUOTE = (
    "I'm not afraid of death; I just don't want to be there "
    "when it happens. It's such a waste of an exit."
)

def type_print(text, delay=DELAY):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(text_line, width=70):
    top = "┌" + "─" * (width - 2) + "┐"
    mid = "│" + text_line.center(width - 2) + "│"
    bot = "└" + "─" * (width - 2) + "┘"
    return top + "\n" + mid + "\n" + bot

def center_canvas():
    # Clear and center-ish by padding top
    padding = "\n" * 3
    sys.stdout.write(BG + RESET)
    sys.stdout.write(padding)

def animate_cylon():
    """Slide a cyan bar across the top like a cheap TV intro."""
    width = 60
    for i in range(width + 10):
        bar = "\033[46m" + " " * i + "═" * (width - i + 1) + "\033[0m"
        sys.stdout.write("\033[2K\r" + bar)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def draw_quote_box(quote):
    lines = []
    lines.append("        " + draw_frame(" WOODY'S WISDOM ", 62))
    lines.append("        " + draw_frame(" ", 62))
    wrapped = wrap_text(quote, 56)
    for line in wrapped:
        lines.append("        " + draw_frame(line, 62))
    lines.append("        " + draw_frame(" ", 62))
    lines.append("        " + draw_frame(" — Woody Allen (pretending to be deep)", 62))
    return "\n".join(lines)

def wrap_text(text, width):
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= width:
            current = (current + " " + w).strip() if current else w
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines

def main():
    os.system("" if sys.platform != "win32" else "cls")
    center_canvas()

    # Cylon intro
    print("\033[2K\r", end="")
    animate_cylon()

    # Header with color
    center_canvas()
    print()
    print(BG + " " * 24 + HIGHLIGHT + BOLD + " 🧠 WOODY LOGIC 🧠 " + RESET + " " * 24 + RESET)
    print()

    # Animated typing
    print(BG)
    print(" " * 18 + YELLOW + "Sometimes the journey is the problem..." + RESET)
    print()
    time.sleep(0.5)
    print(" " * 10 + HIGHLIGHT + "               ┌────────────────────────────┐" + RESET)
    time.sleep(0.3)
    print(" " * 10 + HIGHLIGHT + "               │  LOADING EXISTENTIAL CRED  │" + RESET)
    time.sleep(0.3)
    print(" " * 10 + HIGHLIGHT + "               └────────────────────────────┘" + RESET)
    time.sleep(0.5)
    for _ in range(3):
        print("\033[2K\r" + " " * 10 + HIGHLIGHT + "   ⚡ spark ⚡  ⚡ insight ⚡  ⚡ panic ⚡" + RESET, end="", flush=True)
        time.sleep(0.2)
        print("\033[2K\r" + " " * 10 + HIGHLIGHT + "   ⚡ denial  ⚡  ⚡ delay ⚡  ⚡ more delay ⚡" + RESET, end="", flush=True)
        time.sleep(0.2)
    print()

    # Quote box
    print(draw_quote_box(QUOTE))

    # Footer with color
    print()
    print(" " * 10 + FG + "If it scares you, it might be a good idea." + RESET)
    print(" " * 14 + FG + "— Woody Allen (probably) —" + RESET)
    print()
    print(BG + " " * 60 + RESET)

if __name__ == "__main__":
    main()