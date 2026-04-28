"""
Campbell's Soup Can #3485
Produced: 2026-04-28 09:34:04
Worker: inclusionAI: Ling-2.6-flash (free) (inclusionai/ling-2.6-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Woody Allen style quote
quote = (
    "I'm not scared of the existential void;\n"
    "I just wish it had taken out the trash\n"
    "before it came for me."
)

# Colors
BG = "\033[48;2;15;15;40m"
FG = "\033[38;2;255;200;100m"
HIGHLIGHT = "\033[38;2;255;100;150m"
RESET = "\033[0m"
BOLD = "\033[1m"

def type_print(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(text_lines, width=60):
    top = "┌" + "─" * width + "┐"
    sep = "│"
    bottom = "└" + "─" * width + "┘"
    padding = (width - len(line)) // 2 for line in text_lines
    result = [top]
    for line in text_lines:
        padding = (width - len(line)) // 2
        result.append(sep + " " * padding + line + " " * (width - len(line) - padding) + sep)
    result.append(bottom)
    return "\n".join(result)

# Clear screen and hide cursor
sys.stdout.write("\033[2J\033[H\033[?25l")
sys.stdout.flush()

# Animation: fade-in lines
lines = quote.split("\n")
for i in range(1, len(lines) + 1):
    print(BG + "\033[H")  # home cursor
    box_content = lines[:i]
    framed = draw_frame(box_content)
    print(FG + framed + RESET)
    type_print(box_content[-1], delay=0.05)
    time.sleep(0.5)

# Footer quote
footer = HIGHLIGHT + BOLD + "— Woody Allen (probably, while checking his alarm for the 47th time)" + RESET
print("\n" + " " * 18 + footer)

# Tiny ASCII art: anxious philosopher
art = r"""

        ,--.
    __/'    `\
  ,'  O      O  `,
 :                 :
 |      ^_^      / |
 :       (_)     :
  `._         _.'
    `-------'

     (  existential crisis in progress  )
"""
print(HIGHLIGHT + art + RESET)

# Fade-out
time.sleep(1)
for _ in range(5):
    print("\033[1A\033[2K", end="")
    time.sleep(0.1)

# Reset cursor
sys.stdout.write("\033[?25h")
sys.stdout.flush()