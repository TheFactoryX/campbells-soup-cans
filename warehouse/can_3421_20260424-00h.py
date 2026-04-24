"""
Campbell's Soup Can #3421
Produced: 2026-04-24 00:03:24
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
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
import random

# ANSI color helpers
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def reset():
    return "\033[0m"

def color_wrap(text, color):
    return f"{color}{text}{reset()}"

# A single Woody Allen‑style quote
QUOTE = (
    "I'm not afraid of death; I just don't want to be there when it happens."
)

def typewriter(text, delay=0.03):
    """Print text one character at a time with a random pastel color."""
    for ch in text:
        # pastel rainbow hue
        hue = random.randint(0, 360)
        # convert HSV to RGB (simple approximation for pastel)
        c = 255
        x = int(c * (1 - abs((hue / 60) % 2 - 1)))
        m = int(255 * 0.2)  # pastel shift
        if 0 <= hue < 60:
            r, g, b = c, x, 0
        elif 60 <= hue < 120:
            r, g, b = x, c, 0
        elif 120 <= hue < 180:
            r, g, b = 0, c, x
        elif 180 <= hue < 240:
            r, g, b = 0, x, c
        elif 240 <= hue < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        r, g, b = min(255, r + m), min(255, g + m), min(255, b + m)
        sys.stdout.write(color_wrap(ch, rgb(r, g, b)))
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline at end

def draw_box(width, height, border_char="*", fill_char=" "):
    """Return a list of strings forming a colored box."""
    lines = []
    # top border
    lines.append(border_char * width)
    # middle
    for _ in range(height - 2):
        lines.append(border_char + fill_char * (width - 2) + border_char)
    # bottom border
    lines.append(border_char * width)
    return lines

def main():
    term_width = 70   # fixed width for the box
    padding = 2       # space inside the box
    inner_width = term_width - 2 * padding

    # Center the quote inside the inner area (word‑wrap simple)
    words = QUOTE.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= inner_width:
            current = (current + " " + w).strip()
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    # Build box content
    content = []
    content.append(" " * padding)  # top empty line
    for line in lines:
        content.append(" " * padding + line.ljust(inner_width) + " " * padding)
    content.append(" " * padding)  # bottom empty line

    # Create the box
    box_height = len(content) + 2  # +2 for top/bottom borders
    box = draw_box(term_width, box_height, border_char=color_wrap("★", rgb(255,215,0)),
                   fill_char=" ")
    # Overwrite inner area with the content (colored quote)
    for i, line in enumerate(content, start=1):
        # replace the inner part of the box line
        inner = line
        box[i] = box[i][0] + inner + box[i][-1]

    # Print box with a little delay for fun
    for line in box:
        print(line)
        time.sleep(0.05)

    # Typewriter effect for the quote inside the box (already printed, now animate)
    # We'll re‑print the quote line by line with a typewriter effect over the existing box.
    # Move cursor up to rewrite the inner lines.
    sys.stdout.write(f"\033[{len(content)}A")  # move up to first inner line
    time.sleep(0.2)
    for line in lines:
        # rewrite each line with typewriter effect
        sys.stdout.write("\r" + " " * (term_width) + "\r")  # clear line
        sys.stdout.write(" " * padding)  # left padding
        typewriter(line, delay=0.04)
        sys.stdout.write(" " * padding)  # right padding (will be overwritten by newline)
        sys.stdout.flush()
        time.sleep(0.1)

    # Final reset
    print(reset())

if __name__ == "__main__":
    main()