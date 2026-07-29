"""
Campbell's Soup Can #4362
Produced: 2026-07-29 00:08:59
Worker: Ling-3.0-flash (free) (inclusionai/ling-3.0-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import math

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def slow_print(text, delay=0.03, color=""):
    for char in text:
        if color:
            sys.stdout.write(f"\033[{color}m{char}\033[0m")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def flash_text(text, color, times=3, delay=0.15):
    for _ in range(times):
        print(f"\r{colored(text, color)}", end="", flush=True)
        time.sleep(delay)
        print(f"\r{' ' * len(text)}", end="", flush=True)
        time.sleep(delay)
    print(f"\r{colored(text, color)}", flush=True)

# Determine terminal width
try:
    TERMINAL_WIDTH = shutil.get_terminal_size().columns
except:
    TERMINAL_WIDTH = 65

import shutil
TERMINAL_WIDTH = max(shutil.get_terminal_size().columns, 65)

def print_box(content_lines, border_color, title=""):
    box_width = max(len(line) for line in content_lines) + 4
    title_line = ""
    if title:
        t = f" {title} "
        total_pad = box_width - len(t) - 2
        left_pad = total_pad // 2
        right_pad = total_pad - left_pad
        title_line = colored("╔" + "═" * left_pad + t + "═" * right_pad + "╗", border_color)
    else:
        title_line = colored("╔" + "═" * (box_width - 2) + "╗", border_color)

    print(title_line)
    for line in content_lines:
        padding = box_width - len(colored("", border_color)) - len(line) - 2
        # Recalculate without ANSI
        clean_line = "\033[0m".join(line.split("\033[")) if "\033[" in line else line
        # Simpler approach: just pad
        visible_len = len(line)
        for code in [f"\033[{c}m" for c in range(10, 100)]:
            visible_len += line.count(code)
        # Even simpler: just use the raw line length minus ANSI escapes
        raw = line.replace("\033[0m", "")
        for c in range(90, 100):
            raw = raw.replace(f"\033[{c}m", "")
        visible = len(raw)
        pad_needed = box_width - 2 - visible
        left_p = pad_needed // 2
        right_p = pad_needed - left_p
        print(colored("║" + " " * left_p, border_color) + line + colored(" " * right_p + "║", border_color))
    bottom = colored("╚" + "═" * (box_width - 2) + "╝", border_color)
    print(bottom)

# ─── ASCII ART ───
def draw_walter():
    art_lines = [
        "        _______________",
        "       |  .---------.  |",
        "       | /  ___   _  \\ |",
        "       ||  (   ) (   ) ||",
        "       |||   \\_Y_/   |||",
        "       |||  .-------. |||",
        "       ||\\  |       |  /||",
        "       || \\ |  o  o | / ||",
        "       ||  \\|  \\_/  |/  ||",
        "       ||   |   ~~~   |  ||",
        "       ||___|_________|___||",
        "       '-----'------'-----'",
        "      /                  \\",
        "     /   neurotic         \\",
        "    |     soul             |",
        "     \\                    /",
        "      '.____________._.'",
    ]
    return art_lines

def draw_thinking():
    return [
        "         .---.",
        "        | ??? |",
        "         '---'",
        "          |||",
        "         \\|/|",
        "          |||",
    ]

def draw_worms():
    return [
        "    ~ ~ ~ ~ ~",
        "   ~~~ ~ ~~~ ~",
        "  ~ ~~~ ~ ~~~  ~",
        "   ~ ~~~ ~ ~~~ ~",
        "    ~ ~ ~ ~ ~",
    ]

# ─── COLORS ───
Cyan = "96"
Yellow = "93"
Red = "91"
Green = "92"
Magenta = "95"
Blue = "94"
White = "97"
BrightWhite = "1"
Dim = "2"

# ─── ANIMATION SEQUENCE ───
print()
print()

# Screen wipe effect
print(colored("\n" * 3, Dim))
time.sleep(0.2)

# The thinking doodle
thinking = draw_thinking()
for line in thinking:
    print(" " * 12 + colored(line, Yellow))
    time.sleep(0.1)

time.sleep(0.3)
print("\033[2J\033[H")  # Clear screen

# Draw the nervous worm
worms = draw_worms()
for line in worms:
    print(" " * 18 + colored(line, Green))
    print(" " * 18 + colored(line, Cyan))
time.sleep(0.2)
print("\033[2J\033[H")

# Draw Walter
art = draw_walter()
for line in art:
    print(" " * 8 + colored(line, White))
    time.sleep(0.04)

time.sleep(0.4)
print("\033[2J\033[H")

# ─── THE QUOTE BOX ───
quote = "I'd like to live forever,"
sub1 = "but I think I got that wrong."
sub2 = "Death is just nature's"
sub3 = "way of telling you:"
sub4 = "\"your reservation was for today.\""

flash_text("  *ahem* ", Yellow, times=2)
time.sleep(0.2)

# Build quote lines with color
quote_lines = [
    colored(quote, Yellow),
    colored(sub1, Red),
    colored(sub2, Cyan),
    colored(sub3, Magenta),
    colored(sub4, Green),
]

print_box(quote_lines, Yellow, " W O O D Y ' S   P H I L O S O P H Y ")

time.sleep(0.5)

# Footer lines
print()
footer_lines = [
    colored("   - As dictated by my neurosis, at 3 AM on a Tuesday", Dim),
    colored("   - \"I've consulted a therapist. He's also neurotic.\"", Dim),
    colored("   - Please don't tell me this is profound. I'm sensitive.", Dim),
]
for line in footer_lines:
    print(" " + line)
    time.sleep(0.2)

print()
print(colored("       ...and that's the bottom line.", Magenta))
time.sleep(0.5)
print(colored("       Woody says: \"I am not a very good person,", Yellow))
print(colored("       but I am a very good typist.\"", Yellow))

print()
print(colored("  ~ click click ~", Dim))
print()