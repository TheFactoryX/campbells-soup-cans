"""
Campbell's Soup Can #4839
Produced: 2026-08-25 18:56:45
Worker: MiniMax: MiniMax M3 (free) (minimax/minimax-m3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"
REVERSE = "\033[7m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BG_BLACK = "\033[40m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"

def clear():
    sys.stdout.write("\033[2J\033[H")

def slow_print(text, color=WHITE, delay=0.04, style=""):
    full_style = style + color
    sys.stdout.write(full_style)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

def centered(text, width=70):
    return text.center(width)

# A tiny Woody Allen, blinking and sweating
woody_art = f"""
{BOLD}{YELLOW}        .-----.
       /       \\
      |  O   O  |
      |    >    |
      |  \\___/  |
       \\       /
        `-----'{RESET}
{BLINK}{RED}     (nervously sweating){RESET}
"""

# The quote
quote = ("I don't know the meaning of life, but I suspect it involves "
         "a great deal of disappointment, some low-fat yogurt, "
         "and at least one good therapist.")

attribution = "~ Woody Allen (probably, while fidgeting)"

# Build a fancy box
box_top = f"{BOLD}{CYAN}+" + "-" * 68 + f"+{RESET}"
box_mid = f"{BOLD}{CYAN}|{RESET}"
box_bot = f"{BOLD}{CYAN}+" + "-" * 68 + f"+{RESET}"

# Animation: panic dots
def panic_dots():
    for i in range(8):
        dots = "." * ((i % 4))
        spaces = " " * (3 - len(dots))
        sys.stdout.write(f"\r{BOLD}{RED}    panicking{dots}{spaces} {RESET}")
        sys.stdout.flush()
        time.sleep(0.35)
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()

# Main show
clear()
print()
slow_print(centered("A NEUROTIC MEDITATION", 70), MAGENTA, 0.05, BOLD)
print()
slow_print(centered("(or, the universe, briefly explained)", 70), DIM, 0.03, ITALIC)
print()
print()

# Show Woody with blinking eyes
slow_print(woody_art, WHITE, 0.01)
print()
panic_dots()

# Draw the quote box
print(box_top)
quote_line1 = "\" " + quote + " \""
# Wrap manually for the box
words = quote_line1.split()
lines = []
current = ""
for w in words:
    if len(current) + len(w) + 1 <= 66:
        current = (current + " " + w).strip()
    else:
        lines.append(current)
        current = w
lines.append(current)

for line in lines:
    padded = " " + line + " " * (68 - len(line) - 1)
    print(f"{box_mid} {ITALIC}{YELLOW}{padded}{RESET}{box_mid}")
print(box_top)
print()

slow_print(centered(attribution, 70), CYAN, 0.04, BOLD)
print()
slow_print(centered("...and now, back to your existential dread.", 70), DIM, 0.03, ITALIC)
print()
print(f"{BLINK}{GREEN}  **{RESET} {BOLD}have a nice day {ITALIC}(or don't){RESET} {BLINK}{GREEN}**{RESET}")
print()