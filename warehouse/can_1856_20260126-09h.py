"""
Campbell's Soup Can #1856
Produced: 2026-01-26 09:49:14
Worker: OpenAI: GPT-5 (openai/gpt-5)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import shutil
import textwrap
import itertools

# ANSI helpers
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"

FG = {
    "black":"\033[30m","red":"\033[31m","green":"\033[32m","yellow":"\033[33m",
    "blue":"\033[34m","magenta":"\033[35m","cyan":"\033[36m","white":"\033[37m",
    "bright_black":"\033[90m","bright_red":"\033[91m","bright_green":"\033[92m",
    "bright_yellow":"\033[93m","bright_blue":"\033[94m","bright_magenta":"\033[95m",
    "bright_cyan":"\033[96m","bright_white":"\033[97m",
}

BG = {
    "black":"\033[40m","red":"\033[41m","green":"\033[42m","yellow":"\033[43m",
    "blue":"\033[44m","magenta":"\033[45m","cyan":"\033[46m","white":"\033[47m",
    "bright_black":"\033[100m","bright_red":"\033[101m","bright_green":"\033[102m",
    "bright_yellow":"\033[103m","bright_blue":"\033[104m","bright_magenta":"\033[105m",
    "bright_cyan":"\033[106m","bright_white":"\033[107m",
}

def clear_line():
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def type_out(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def pulse_border(text_lines, width, cycles=3, speed=0.08):
    # Animated marquee border
    colors = [FG["bright_magenta"], FG["bright_blue"], FG["bright_cyan"], FG["bright_yellow"]]
    top = "╭" + "─" * (width - 2) + "╮"
    bottom = "╰" + "─" * (width - 2) + "╯"
    for i in range(cycles):
        color = colors[i % len(colors)]
        sys.stdout.write(color + top + RESET + "\n")
        for ln in text_lines:
            sys.stdout.write(color + "│ " + RESET + ln.ljust(width - 4) + color + " │" + RESET + "\n")
        sys.stdout.write(color + bottom + RESET + "\n")
        sys.stdout.flush()
        time.sleep(speed)
        # Move cursor up to redraw (lines printed = len(text_lines)+2)
        sys.stdout.write(f"\033[{len(text_lines)+2}A")
    # Final static border in bright_magenta
    color = FG["bright_magenta"]
    sys.stdout.write(color + top + RESET + "\n")
    for ln in text_lines:
        sys.stdout.write(color + "│ " + RESET + ln.ljust(width - 4) + color + " │" + RESET + "\n")
    sys.stdout.write(color + bottom + RESET + "\n")
    sys.stdout.flush()

def spinner_line(message, duration=1.4):
    frames = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    it = itertools.cycle(frames)
    while time.time() < end_time:
        frame = next(it)
        sys.stdout.write(f"\r{FG['bright_blue']}{frame}{RESET} {DIM}{message}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    clear_line()

def blink_cursor(times=4, interval=0.12, color=FG["bright_yellow"]):
    for _ in range(times):
        sys.stdout.write(color + "▋" + RESET)
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(interval)

def wrap_colored(text, width, color=FG["bright_yellow"]):
    lines = textwrap.wrap(text, width=width)
    return [color + ln + RESET for ln in lines]

def faint_line(text):
    return DIM + text + RESET

def center_text(text, width):
    if len(text) >= width:
        return text
    pad = (width - len(text)) // 2
    return " " * pad + text

def main():
    # Terminal width and layout
    cols = shutil.get_terminal_size((80, 24)).columns
    max_box_width = max(40, min(76, cols - 4))
    
    # Disclaimer (policy-friendly)
    disclaimer = "Note: I can’t write in the exact style of any specific living author. Here’s an original quip with a neurotic, self‑deprecating, existential vibe."
    print(faint_line(disclaimer))
    
    # Spinner: "thinking"
    spinner_line("Contemplating the abyss (it contemplated back)...", duration=1.6)
    
    # Fun little title banner
    title = "Existential One‑Liner"
    ribbon = FG["bright_white"] + BG["bright_magenta"] + " " + title + " " + RESET
    print(center_text(ribbon, cols))
    print()

    # The quote (ONE quote)
    quote = (
        "I asked the universe for a sign; it sent a calendar invite titled "
        "'Existential Crisis (recurring),' and I clicked 'Maybe' because commitment makes me dizzy."
    )
    
    # Compose scene with a tiny jittery character
    actor_lines = [
        FG["bright_yellow"] + "      .-." + RESET,
        FG["bright_yellow"] + "     (o o)  " + FG["bright_cyan"] + "← me, bravely negotiating with infinity" + RESET,
        FG["bright_yellow"] + "  ooO--(_) " + RESET,
    ]
    for ln in actor_lines:
        print(ln)
    print()

    # Prepare the box with animated border
    wrapped = wrap_colored(quote, width=max_box_width - 4, color=FG["bright_yellow"])
    pulse_border(wrapped, width=max_box_width, cycles=4, speed=0.07)

    # Typewriter effect inside the box (redraw only the text lines)
    # Move cursor up to start of box content (2 header lines already printed above + box top)
    # We'll carefully retype the inner lines character-by-character.
    lines_to_move_up = len(wrapped) + 1  # move to the first inside line after the top border
    sys.stdout.write(f"\033[{lines_to_move_up}A")
    sys.stdout.flush()
    # Now we are on the top border; move one line down to first inside text line
    sys.stdout.write("\033[1B")
    sys.stdout.flush()

    # Retype each line with typewriter effect inside the existing borders
    for idx, ln in enumerate(wrapped):
        # Clear the inside line area but keep borders
        sys.stdout.write("\r" + FG["bright_magenta"] + "│ " + RESET)
        sys.stdout.flush()
        # Strip color to type characters gradually, but re-apply color char-by-char
        plain = ln.replace(FG["bright_yellow"], "").replace(RESET, "")
        for ch in plain:
            sys.stdout.write(FG["bright_yellow"] + ch + RESET)
            sys.stdout.flush()
            time.sleep(0.01)
        # Pad the rest with spaces to fit
        pad = (max_box_width - 4) - len(plain)
        if pad > 0:
            sys.stdout.write(" " * pad)
        sys.stdout.write(FG["bright_magenta"] + " │" + RESET)
        sys.stdout.flush()
        # Move to next line
        if idx < len(wrapped) - 1:
            sys.stdout.write("\n")
            sys.stdout.flush()

    # Move cursor to after the box bottom
    lines_below = (len(wrapped) - 1) + 1  # rest of inside lines already printed + bottom border
    sys.stdout.write(f"\n\033[1B")
    sys.stdout.flush()

    # Little blinking cursor to punctuate the anxiety
    print()
    sys.stdout.write(FG["bright_black"] + ITALIC + "processing feelings" + RESET + " ")
    blink_cursor(times=6, interval=0.08, color=FG["bright_cyan"])
    clear_line()

    # Final spotlight reveal
    spotlight = BG["bright_yellow"] + FG["black"] + " ★ " + RESET
    print(center_text(spotlight + BOLD + "There you have it: one trembling, philosophical chuckle." + RESET + " " + spotlight, cols))
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + FG["bright_black"] + "Existential escape acknowledged." + RESET)