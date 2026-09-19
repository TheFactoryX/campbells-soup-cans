"""
Campbell's Soup Can #4991
Produced: 2026-09-19 20:43:33
Worker: inclusionAI: Ling 3.0 Flash VL (free) (inclusionai/ling-3.0-flash-vl:free)
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
import math

# ── ANSI escape codes ──────────────────────────────────────────
RED    = '\033[91m'
GREEN  = '\033[92m'
YELLOW = '\033[93m'
BLUE   = '\033[94m'
MAGENTA= '\033[95m'
CYAN   = '\033[96m'
WHITE  = '\033[97m'
BOLD   = '\033[1m'
DIM    = '\033[2m'
RESET  = '\033[0m'
BLINK  = '\033[5m'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'
CLEAR  = '\033[2J\033[H'

# Color palette cycle
PALETTE = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]

# ── The Quote ──────────────────────────────────────────────────
AUTHOR = "— Woody Allen (probably)"
QUOTE  = ("I spent twenty years in therapy figuring out "
          "I'm afraid of heights, only to realize the real "
          "height I fear is the meaninglessness of the cosmos "
          "and it's giving me a panic attack.")

# ── Helper functions ───────────────────────────────────────────
def colored(text, color):
    return f"{color}{text}{RESET}"

def typing_effect(text, delay=0.03, color=WHITE):
    for ch in text:
        sys.stdout.write(colored(ch, color))
        sys.stdout.flush()
        time.sleep(delay + 0.005 * (hash(ch) % 3))
    sys.stdout.write("\n")

def progress_bar(total=40):
    for i in range(total + 1):
        bar = COLORS_BAR[i % len(PALETTE)] + "█" * i + RESET + DIM + "░" * (total - i) + RESET
        sys.stdout.write(f"\r  {bar} {i*100//total}% philosophical profundity loading")
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n\n")

COLORS_BAR = PALETTE * 7

# ── ASCII Frame Drawer ─────────────────────────────────────────
def draw_frame(width, height, color_idx):
    c = PALETTE[color_idx % len(PALETTE)]
    h_char = colored("─", c)
    v_char = colored("│", c)
    corner = colored("┌", c)
    corner2 = colored("┐", c)
    corner3 = colored("└", c)
    corner4 = colored("┘", c)

    lines = []
    lines.append("  " + corner + h_char * (width - 2) + corner2)
    for i in range(1, height - 1):
        if i == height // 2 - 1:
            label = colored(f" {DIM}✦ existential crisis loading... ✦ {RESET}", c)
            padded = label.center(width - 2)
            lines.append("  " + v_char + padded + v_char)
        else:
            inner = " " * (width - 2)
            lines.append("  " + v_char + inner + v_char)
    lines.append("  " + corner3 + h_char * (width - 2) + corner4)
    return "\n".join(lines)

# ── Spinner ────────────────────────────────────────────────────
def spinner(frames=30):
    spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(frames):
        for sc in spinner_chars:
            sys.stdout.write(f"\r  {colored(sc, YELLOW)}  {DIM}contemplating the void...{RESET}")
            sys.stdout.flush()
            time.sleep(0.08)
    sys.stdout.write("\n\n")

# ── Main Show ──────────────────────────────────────────────────
def main():
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.write(CLEAR)

    # Title with rainbow explosion
    title = "  ⌁ THE PHILOSOPHY OF PANIC ⌁  "
    print(colored(title, BOLD + CYAN))
    print(colored("  " + "─" * 30, CYAN))
    print()

    # Spinner intro
    spinner(15)

    # Progress bar
    progress_bar()

    # Frame dimensions
    W = 72
    H = 12

    # Animated frames: draw frame with cycling colors (3 full cycles)
    for cycle in range(4):
        sys.stdout.write(CLEAR)
        print(colored(title, BOLD + CYAN))
        print(colored("  " + "─" * 30, CYAN))
        print()

        frame = draw_frame(W, H, cycle)
        # Color the border with a gradient effect
        for color in PALETTE:
            pass  # frame already has its color
        print(frame)
        print()

        # Type "QUOTE INCOMING..."
        hint = colored("  ▸ INCOMING EXISTENTIAL CRISIS ◂", YELLOW + BOLD)
        print(hint)
        sys.stdout.flush()
        time.sleep(0.6)

        # Clear hint and type quote
        sys.stdout.write("\033[A" + " " * len(hint) + "\r")
        sys.stdout.flush()

        typing_effect("  " + QUOTE, delay=0.025, color=WHITE + BOLD)
        time.sleep(0.3)

        typing_effect("  " + colored(AUTHOR, YELLOW + DIM), delay=0.015, color=YELLOW)

        # Blink the death indicator
        if cycle < 3:
            sys.stdout.write(colored(f"\n  {BLINK}✦ still not dead ✦{RESET}\n", MAGENTA))
            sys.stdout.flush()
            time.sleep(0.8)

    # Final grand reveal
    sys.stdout.write(CLEAR)
    print(colored("  ⌁ THE PHILOSOPHY OF PANIC ⌁", BOLD + CYAN))
    print(colored("  " + "═" * 36, CYAN))
    print()

    # Big bordered quote in final colors
    quote_lines = QUOTE.split()
    # Re-join and manually wrap
    text = QUOTE
    max_line_len = 52
    words = text.split()
    wrapped = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= max_line_len:
            current += (" " + w if current else w)
        else:
            wrapped.append(current)
            current = w
    if current:
        wrapped.append(current)

    frame_w = max(len(line) for line in wrapped) + 4

    border_c = colored("═", GREEN)
    side_c = colored("║", GREEN)
    tl = colored("╔", GREEN)
    tr = colored("╗", GREEN)
    bl = colored("╚", GREEN)
    br = colored("╝", GREEN)

    print("    " + tl + colored("═" * (frame_w - 2), GREEN) + tr)
    for line in wrapped:
        padded = line.center(frame_w - 2)
        print("    " + side_c + colored(f" {padded} ", GREEN) + side_c)
    print("    " + bl + colored("═" * (frame_w - 2), GREEN) + br)
    print()

    print(colored(f"    {AUTHOR}", YELLOW + BOLD))
    print()

    # Fun footer with blinking text
    footer = colored("  ✦ Existential dread: fully charged ✦", MAGENTA + BOLD + BLINK)
    sys.stdout.write(footer + "\n")
    sys.stdout.flush()

    # Little ASCII art character
    print(colored("\n         ___   ", DIM))
    print(colored("        (o_o)  ", DIM))
    print(colored("         > <   ", DIM + RED))
    print(colored("        /| | |  ", DIM))
    print(colored("          | |   ", DIM))
    print(colored("     at least  ", DIM))
    print(colored("     I'm consistent", YELLOW + BOLD))
    print()

    # Final blinking line
    for _ in range(3):
        sys.stdout.write(colored(f"\r  {BLINK}{RED}I think therefore I am confused.{RESET}" + " " * 10, RED))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(colored(f"\r  {DIM}                                      {RESET}\r", DIM))
        sys.stdout.flush()
        time.sleep(0.3)

    sys.stdout.write(colored("  I think therefore I am confused.\n\n", RED + BOLD))
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(SHOW_CURSOR + RESET + "\n\n  Even the interrupt is meaningless.\n")