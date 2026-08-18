"""
Campbell's Soup Can #4681
Produced: 2026-08-18 19:40:35
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

"""
Woody Allen Philosophy Printer
A single-file, pure-Python showcase of neurotic existential humor.
Uses only built-in modules and ANSI escape codes for color.
"""

import time
import sys

# ANSI color codes for terminal fun
RESET = "\033[0m"
BOLD = "\033[1m"
COLORS = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m",  # cyan
]

def colorful(text, color_idx=0):
    """Wrap text with a color, cycling through the rainbow."""
    return f"{COLORS[color_idx % len(COLORS)]}{text}{RESET}"

def print_slowly(text, delay=0.03):
    """Simulate a nervous typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline at the end

def draw_neurotic_border(width, msg_color):
    """Draw a silly, colorful ASCII border around the quote."""
    top = colorful("┌" + "─" * width + "┐", 3)
    bottom = colorful("└" + "─" * width + "┘", 3)
    middles = [colorful("│" + " " * width + "│", i) for i in range(6)]
    
    print(top)
    print(middles[0])
    # centered quote line with playful padding
    padded = " " + " " * ((width - len(msg) - 2) // 2) + msg + " " * ((width - len(msg) - 2 + 1) // 2) + " "
    print(colorful(f"│ {msg} │", msg_color))
    print(middles[1])
    print(bottom)

# Woody Allen style quote (original, neurotic, funny, existential)
quote = (
    "I sometimes wonder if the meaning of life is just a cosmic joke "
    "I'm not in on, and I'm pretty sure I'm the punchline."
)

# Terminal width fallback
try:
    width = min(80, max(40, len(quote) + 10))
except:
    width = 60

# Brief "neurotic thinking" animation
print(colorful("System booting... ", 4) + colorful(".", 5) + colorful(".", 2))
time.sleep(0.5)
sys.stdout.write("\033[F" * 2)  # move cursor up 2 lines (may be ignored in some terminals, graceful fallback)
print_slowly("Analyzing existence...", 0.04)
time.sleep(0.7)

# Reveal the quote in a neurotic box
draw_neurotic_border(width, 5)  # magenta quote text

# Final neurotic footnote
print()
colorful("If at first you don't succeed...", 1)
colorful(" redefine the meaning of success.", 3)
print(RESET)