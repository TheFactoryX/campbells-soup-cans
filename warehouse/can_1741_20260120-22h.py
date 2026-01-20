"""
Campbell's Soup Can #1741
Produced: 2026-01-20 22:36:47
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
Single-file Python program that prints a funny philosophical quote
in Woody Allen's style, with ANSI color animations and ASCII art.

Run: python3 woody_quote.py
"""

import sys
import time
import random
import math
from typing import List

# ANSI color codes
class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    GRAY = "\033[90m"
    BG_DARK = "\033[48;5;236m"
    BG_LIGHT = "\033[48;5;240m"
    @staticmethod
    def rgb_fg(r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{g};{b}m"
    @staticmethod
    def rgb_bg(r: int, g: int, b: int) -> str:
        return f"\033[48;2;{r};{g};{b}m"
    @staticmethod
    def cursor_up(n: int) -> str:
        return f"\033[{n}A"
    @staticmethod
    def cursor_down(n: int) -> str:
        return f"\033[{n}B"
    @staticmethod
    def cursor_right(n: int) -> str:
        return f"\033[{n}C"
    @staticmethod
    def cursor_left(n: int) -> str:
        return f"\033[{n}D"
    CLEAR_LINE = "\033[2K"
    CLEAR_SCREEN = "\033[2J"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"

def get_terminal_size() -> (int, int):
    try:
        import shutil
        w, h = shutil.get_terminal_size()
        return w, h
    except Exception:
        return (80, 24)

def center_text(text: str, width: int) -> str:
    return text.center(width)

def chunk_string(text: str, chunk_len: int) -> List[str]:
    """Split string into fixed-length chunks without breaking words if possible."""
    words = text.split()
    chunks = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= chunk_len:
            current += (w if current == "" else " " + w)
        else:
            if current:
                chunks.append(current)
            current = w
    if current:
        chunks.append(current)
    if not chunks:
        chunks = [""]
    return chunks

def strip_ansi(s: str) -> str:
    import re
    return re.sub(r"\033\[[0-9;]*[a-zA-Z]", "", s)

def print_slow(text: str, delay: float = 0.02, color: str = ANSI.GRAY):
    """Print text with typewriter effect."""
    print(ANSI.HIDE_CURSOR, end="")
    try:
        for ch in text:
            sys.stdout.write(color + ch + ANSI.RESET)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    finally:
        sys.stdout.write(ANSI.SHOW_CURSOR)

def draw_progress_bar(width: int, duration: float, label: str, complete_color: str = ANSI.GREEN):
    """Draw a simple animated progress bar."""
    print(ANSI.HIDE_CURSOR, end="")
    try:
        step_delay = duration / width
        for i in range(width + 1):
            filled = int(i)
            bar = "[" + "=" * filled + "-" * (width - filled) + "]"
            percent = f"{int(100 * i / width)}%".rjust(4)
            text = f"{label} {bar} {percent}"
            sys.stdout.write(ANSI.CLEAR_LINE + ANSI.cursor_left(999))
            sys.stdout.write(complete_color + text + ANSI.RESET)
            sys.stdout.flush()
            time.sleep(step_delay)
        print()
    finally:
        sys.stdout.write(ANSI.SHOW_CURSOR)

def float_bubble(text: str, width: int, duration: float):
    """Make a speech bubble float vertically while pulsing colors."""
    lines = chunk_string(text, width - 8)
    bubble_top = " " + "_" * (width - 2)
    bubble_mid = []
    for ln in lines:
        pad = width - len(strip_ansi(ln)) - 6
        left_pad = pad // 2
        right_pad = pad - left_pad
        bubble_mid.append("| " + " " * left_pad + ln + " " * right_pad + " |")
    bubble_bottom = " " + "-" * (width - 2) + " "
    bubble = [bubble_top] + bubble_mid + [bubble_bottom]
    bubble_height = len(bubble)

    print(ANSI.HIDE_CURSOR, end="")
    try:
        start = time.time()
        t0 = start
        cycles = 6
        while (time.time() - start) < duration:
            elapsed = time.time() - t0
            # Vertical offset sine wave
            offset = int((math.sin(elapsed * 2.0) + 1) * (bubble_height // 2))
            # Color pulse
            r = int(128 + 127 * math.sin(elapsed * 3.0))
            g = int(128 + 127 * math.sin(elapsed * 3.0 + 2.0))
            b = int(128 + 127 * math.sin(elapsed * 3.0 + 4.0))
            col = ANSI.rgb_fg(r, g, b)

            sys.stdout.write(ANSI.CLEAR_SCREEN)
            # Print some vertical whitespace to simulate float
            for _ in range(offset):
                print()
            for line in bubble:
                sys.stdout.write(col + line + ANSI.RESET + "\n")
            sys.stdout.flush()
            time.sleep(0.1)
    finally:
        sys.stdout.write(ANSI.SHOW_CURSOR)

def rain_drops(chars: str, width: int, height: int, duration: float):
    """Falling characters animation (Matrix rain lite)."""
    print(ANSI.HIDE_CURSOR, end="")
    try:
        start = time.time()
        drops = [0] * width
        for i in range(width):
            drops[i] = random.randint(-height, 0)
        while (time.time() - start) < duration:
            sys.stdout.write(ANSI.CLEAR_SCREEN)
            # Randomly spawn new drops
            for i in range(width):
                if drops[i] < 0 and random.random() < 0.08:
                    drops[i] = random.randint(0, 3)
                elif drops[i] > -height and random.random() < 0.5:
                    drops[i] += 1
            # Draw grid
            for row in range(height):
                line = []
                for col in range(width):
                    if random.random() < 0.03:
                        line.append(ANSI.rgb_fg(100, 255, 100) + random.choice(chars) + ANSI.RESET)
                    else:
                        line.append(" ")
                sys.stdout.write("".join(line) + "\n")
            sys.stdout.flush()
            time.sleep(0.08)
    finally:
        sys.stdout.write(ANSI.SHOW_CURSOR)

def typewriter_quote(quote: str):
    """Show quote with typewriter and emphasize with colors."""
    # Split into segments to colorize
    segments = [
        (quote, ANSI.YELLOW),
    ]
    for text, col in segments:
        print_slow(text, delay=0.03, color=col)
    print()

def draw_eyebrows_ascii():
    """Print a simple ASCII face with animated blinking."""
    face = [
        r"  .--.  ",
        r" /  o \ ",
        r"| \ _/ |",
        r" \ _ _ /",
        r"  '--'  ",
    ]
    print(ANSI.HIDE_CURSOR, end="")
    try:
        for i in range(8):
            sys.stdout.write(ANSI.CLEAR_SCREEN)
            if i % 4 == 0:
                # Open eyes
                print(ANSI.rgb_fg(255, 200, 100) + "\n".join(face) + ANSI.RESET)
            else:
                # Blink (replace eyes with dashes)
                blink = [
                    r"  .--.  ",
                    r" / -- \ ",
                    r"| \ _/ |",
                    r" \ _ _ /",
                    r"  '--'  ",
                ]
                print(ANSI.rgb_fg(255, 200, 100) + "\n".join(blink) + ANSI.RESET)
            time.sleep(0.35)
    finally:
        sys.stdout.write(ANSI.SHOW_CURSOR)

def floating_thought_cloud():
    """Create an animated thought bubble with a philosophical Woody quote."""
    w, h = get_terminal_size()
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens."
    )
    bubble_width = min(60, w - 4)
    float_bubble(quote, bubble_width, 6.0)

def rain_intro():
    """Matrix-style rain for intro."""
    w, h = get_terminal_size()
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"
    rain_drops(chars, width=w, height=min(12, h - 6), duration=3.0)

def progress_intro():
    """A progress bar as a metaphor for existential dread."""
    w, h = get_terminal_size()
    label = "Processing existential dread"
    draw_progress_bar(min(40, w // 2), 2.5, label, complete_color=ANSI.MAGENTA)

def main():
    # Clear screen and hide cursor
    sys.stdout.write(ANSI.CLEAR_SCREEN)
    sys.stdout.flush()

    # Intro sequence: rain, then progress, then face
    rain_intro()
    progress_intro()
    draw_eyebrows_ascii()

    # Animated floating bubble with quote
    floating_thought_cloud()

    # Footer message
    print()
    print_slow(
        "Philosophy is just a way of being anxious in fancy words.",
        delay=0.02,
        color=ANSI.BLUE,
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(ANSI.SHOW_CURSOR + ANSI.RESET + "\n")
        sys.stdout.flush()
    except Exception as e:
        sys.stdout.write(ANSI.SHOW_CURSOR + ANSI.RESET + "\n")
        sys.stdout.flush()
        print(ANSI.RED + f"Oops: {e}" + ANSI.RESET, file=sys.stderr)