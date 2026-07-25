"""
Campbell's Soup Can #4329
Produced: 2026-07-25 23:12:41
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

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLUE = "\033[44m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

def slow_print(text, color, delay=0.02):
    """Print text character by character with a delay."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(symbol, color, width):
    """Draw a decorative frame line."""
    print(color + symbol * width + RESET)

def draw_corner(symbol, color):
    """Draw a corner."""
    return color + symbol + RESET

def draw_side(symbol, color, fill_char=" "):
    """Draw a side with fill."""
    return color + symbol + fill_char * 72 + symbol + RESET

# ─── Main Program ───

print()
print()

# Title banner
draw_frame("═", CYAN, 80)

# Animated title
title = "🌿  W O O D Y  A L S E N  P H I L O S O P H Y  🌿"
slow_print(title.center(80), MAGENTA, 0.01)

draw_frame("═", CYAN, 80)
print()

# Decorative art
art_lines = [
    f"{BLUE}    ██████{RESET}  {YELLOW}█████{RESET}    {BLUE}███{RESET}{YELLOW}██████{RESET}   {BLUE}█████{RESET}",
    f"{BLUE}    ██{RESET}{CYAN}░░░░░{RESET}{YELLOW}███{RESET}    {BLUE}███{RESET}{CYAN}░████{RESET}   {BLUE}███{RESET}",
    f"{BLUE}    ██{RESET}{CYAN}░░░░░░░{RESET}{YELLOW}███{RESET}  {BLUE}███{RESET}{CYAN}░░░████{RESET}   {BLUE}██{RESET}",
    f"{BLUE}    ██{RESET}{CYAN}░░░░░░░{RESET}{YELLOW}███{RESET}  {BLUE}███{RESET}{CYAN}░░░░██{RESET}   {BLUE}██{RESET}",
    f"{BLUE}    ██{RESET}{CYAN}░░░░░░░{RESET}{YELLOW}███{RESET}  {BLUE}███{RESET}{CYAN}░░░████{RESET}   {BLUE}██{RESET}",
    f"{BLUE}    ██{RESET}{CYAN}░░░░░░░{RESET}{YELLOW}███{RESET}{BLUE} █████████{RESET}{CYAN}░░░████{RESET}   {BLUE}██{RESET}",
    f"{BLUE}    ███████{RESET}{YELLOW}████████{RESET}{BLUE}████████{RESET}{CYAN}████████{RESET}",
]
for line in art_lines:
    slow_print("  " + line, "", 0.001)

print()
draw_frame("─", DIM, 80)
print()

# The Quote Box
quote_box_width = 74

# Top of box
draw_frame("╔", RED, 1)
print(" " + RED + "═" * (quote_box_width) + "╗" + RESET)

# Quote lines with animation
quote_lines = [
    ("I", "I"),
    ("'m", "not"),
    ("afraid", "afraid"),
    ("of", "of"),
    ("death,", "death."),
    ("I", "I"),
    ("just", "just"),
    ("don't", "don't"),
    ("want", "want"),
    ("to", "to"),
    ("be", "be"),
    ("there", "there"),
    ("when", "when"),
    ("it", "it"),
    ("happens.", "happens..."),
    ("", "    ── Woody"),
    ("", "      Allen"),
]

# Actually let's do a proper quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."
subtitle = "― Woody Allen (probably, while checking if his door was locked)"

# Draw the quote in a box
print(f"  {RED}║{RESET}" + " ".center(quote_box_width) + f" {RED}║{RESET}")
print(f"  {RED}║{RESET}" + " ♪ existential dread ♪ ".center(quote_box_width, " ") + f" {RED}║{RESET}")
print(f"  {RED}║{RESET}" + " ".center(quote_box_width) + f" {RED}║{RESET}")

# Print the quote word by word with colors cycling through
words = quote.split(" ")
colors_cycle = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

print(f"  {RED}║{RESET}", end="")
for i, word in enumerate(words):
    color = colors_cycle[i % len(colors_cycle)]
    formatted_word = f"{color}{word}{RESET}"
    print(f" {formatted_word}", end="")
    sys.stdout.flush()
    time.sleep(0.05)
print(f" {RED}║{RESET}")

# Blank line
print(f"  {RED}║{RESET}" + " ".center(quote_box_width) + f" {RED}║{RESET}")

# Subtitle
print(f"  {RED}║{RESET}" + f"{DIM}{subtitle}{RESET}".center(quote_box_width) + f" {RED}║{RESET}")

# Bottom of box
print(" " + RED + "═" * (quote_box_width) + "╝" + RESET)

print()
draw_frame("─", DIM, 80)
print()

# Bonus philosophical fragments
fragments = [
    f"{YELLOW}   \"If life gives you lemons, sell them and buy a puppy.\"{RESET}",
    f"{CYAN}   \"The only thing worse than being talked about is{RESET}",
    f"{CYAN}    not being talked about AND having bad posture.\"{RESET}",
    f"{GREEN}   \"To be or not to be — that is a question I ask{RESET}",
    f"{GREEN}    myself every morning while staring at the ceiling.\"{RESET}",
    f"{BLUE}   \"I would give anything not to be neurotic, but{RESET}",
    f"{BLUE}    I just can't help myself. That's the problem.\"{RESET}",
]

for frag in fragments:
    slow_print(frag, "", 0.03)

print()
draw_frame("─", DIM, 80)
print()

# Closing message
closing = "💭  Remember: The universe is laughing at you. But that's okay. 🪦"
slow_print(closing.center(80), BG_YELLOW + "\033[30m" + BOLD + " " * len(closing) + " " + RESET, 0)
# Redraw with colors
print(BG_YELLOW + "\033[30m" + BOLD + closing.center(80) + RESET)

print()
draw_frame("═", CYAN, 80)

# Final animated footer
footer = "  ✨  Existential dread served fresh.  ✨  "
slow_print(footer.center(80), MAGENTA, 0.03)
draw_frame("═", CYAN, 80)

print()
print(f"{DIM}  (Press Enter to exit, or just suffer in silence...){RESET}")
sys.stdin.readline()