"""
Campbell's Soup Can #3487
Produced: 2026-04-28 17:02:25
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import textwrap

# ANSI Escape Codes (24-bit color, no external deps)
RESET = "\033[0m"
BOLD = "\033[1m"
OLIVE_GREEN = "\033[38;2;82;99;72m"  # Muted border color
BEIGE = "\033[38;2;245;242;230m"     # Warm quote text color
DARK_TEAL = "\033[38;2;47;62;70m"    # Title/signature color

# Original Woody Allen-style neurotic existential quote
quote = (
    "I’m not afraid of death—I just don’t want to be there when it happens, mostly because "
    "I’d spend the first hour complaining about the temperature, the next three hours "
    "psychoanalyzing the grim reaper’s mommy issues, and by the time we get to the afterlife "
    "I’ll have already annoyed everyone into wishing I’d stayed home. Also, I still haven’t "
    "finished my brisket, and wasting food is a sin, even if you’re dead."
)

# Wrap quote to fit a neat box width
WRAP_WIDTH = 50
wrapped_lines = textwrap.wrap(quote, width=WRAP_WIDTH)
max_line_len = max(len(line) for line in wrapped_lines)
inner_width = max_line_len + 2  # 1 space padding on each side of text

# Print styled title
print(f"{DARK_TEAL}{BOLD}WOODY ALLEN (ALLEGEDLY) SAID:{RESET}")
print()

# Blinking cursor pre-animation
for _ in range(3):
    print(f"\r{OLIVE_GREEN}_{RESET}", end="", flush=True)
    time.sleep(0.3)
    print(f"\r{OLIVE_GREEN} {RESET}", end="", flush=True)
    time.sleep(0.3)
print()

# Draw empty box borders (text will be typed inside)
top_border = f"{OLIVE_GREEN}┌{'─' * inner_width}┐{RESET}"
bottom_border = f"{OLIVE_GREEN}└{'─' * inner_width}┘{RESET}"

print(top_border)
for _ in wrapped_lines:
    empty_line = f"{OLIVE_GREEN}│{RESET}{BEIGE} {' ' * max_line_len} {RESET}{OLIVE_GREEN}│{RESET}"
    print(empty_line)
print(bottom_border)

# Move cursor up to first empty line inside the box
print(f"\033[{len(wrapped_lines) + 1}A", end="", flush=True)

# Typewriter effect: render quote character-by-character inside the box
for i, line in enumerate(wrapped_lines):
    if i == 0:
        # First line: move right past left border + padding
        print(f"\033[2C", end="", flush=True)
    else:
        # Navigate to next line, return to text start position
        print(f"\033[1B", end="", flush=True)
        print(f"\033[{max_line_len + 2}D", end="", flush=True)
        print(f"\033[2C", end="", flush=True)
    
    # Type line in beige with slight delay
    print(f"{BEIGE}", end="", flush=True)
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print(f"{RESET}", end="", flush=True)

# Move cursor below the box for signature
print(f"\033[2B", end="", flush=True)
print()

# Print signature
print(f"{DARK_TEAL}{BOLD}— Woody Allen (probably){RESET}")
print()