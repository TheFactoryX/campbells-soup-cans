"""
Campbell's Soup Can #915
Produced: 2025-12-13 22:33:27
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
from itertools import cycle

# Colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# Woooty Allen inspired quote
quote = (
    "I've had a wonderful life filled with regret, but if I could live again I'd probably do everything "
    "differently - especially all the stuff I did last week. People should also invest lots of money in "
    "life insurance policies because, regardless of what you do, you're going to pay for it." + " -Woody Allen"
)

# Define terminal dimensions and box settings
TERMINAL_WIDTH = 80
BOX_WIDTH = 50
INNER_WIDTH = BOX_WIDTH - 2
BOX_START = (TERMINAL_WIDTH - BOX_WIDTH) // 2

# Wrap text function
def wrap_text(text, width):
    lines = []
    current = ""
    for word in text.split():
        if len(current) + len(word) + 1 > width:
            lines.append(current)
            current = word
        else:
            current = word if not current else current + " " + word
    if current:
        lines.append(current)
    return lines

# ASCII art
GUITAR = [
    "        =-",
    "    ,'`,-'",
    "   /`    |=",
    "  :    .  |",
    "   \\   \\ /",
    "    `--'`"
]

LOGO = [
    "      ___                     ___",
    "     /   \\                   /   \\",
    "    /  /\\ \\       /\x1b[36m***\x1b[0m/   /\\\x1b[36m***\x1b[0m",
    "   / /' \\ \\     / /\x1b[32m*****\x1b[0m/ /' \\",
    "  / /    \\ \\   / / /\x1b[34m***\x1b[0m/ /    \\",
    " / /      \\ \\ / / /\x1b[35m* */\x1b[0m/      \\",
    "/ /        \\ V / / /\x1b[31m**/\x1b[0m        \\",
    "\\_\\________\\/ /_/_/" + CYAN + " Wo" + RESET,
    "              `'" + MAGENTA + "oody " + RESET + CYAN + "Al" + RESET,
    "                 " + MAGENTA + "len" + RESET,
]

# Spinner animation
SPINNER = cycle(["\\", "|", "/", "-"])

# Print with colors
print(f"{GREEN}            Welc{MAGENTA}o{CYAN}m{GREEN}e to w{MAGENTA}o{CYAN}t{MAGENTA}y {CYAN}Anim{GREEN}ate{RESET}")
print(f"{BLUE}⣀⣄⣀⣄⡀⣀⣄⣀⣄⡀⣀⣄⣀⣄⡀⣀⣄⣀⣄⡀⣀⣄⣀⣄⡀⣀⣄⣀⣄⡀⣀⣄⣀⣄⡀⣀⣄{RESET}")
print(f"{MAGENTA}⡿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⡷{RESET}\n")

# Display guitar animation
for pos in range(4):
    print("\033[?25l")  # Hide cursor
    print(f"{YELLOW}" + "\n".join(GUITAR) + f"{RESET}")
    print(" " * 25 + f"{CYAN}{"^" * (pos+2)}{RESET}")
    time.sleep(0.3)
    print("\033[2J\033[H")  # Clear screen and move cursor
print("\033[?25h")  # Show cursor

# Display logo
print(f"\n{YELLOW}Generating philosophical ta{CYAN}ntrum{RESET}...")
print()
time.sleep(1)

for row in LOGO:
    print(f"{GREEN}   {row}{RESET}")
    time.sleep(0.05)

print(f"\n{RED}** I N I T I A T I N G   Q U O T E   A N I M A T I O N **{RESET}\n")

# Loading animation
print(f"{MAGENTA}Loading... {YELLOW}[", end='', flush=True)
for i in range(13):
    print(f"{CYAN}=", end='', flush=True)
    time.sleep(0.1)
    if i % 4 == 0:
        print(f"{MAGENTA}>{RESET}", end='', flush=True)
print(f"{MAGENTA}] OK{RESET}", flush=True)

# Display quote
wrapped_lines = wrap_text(quote, INNER_WIDTH)
print(f"\n{CYAN}" + "=" * (INNER_WIDTH + 2))
for line in wrapped_lines:
    print(f"{CYAN}| {line.center(INNER_WIDTH)} {CYAN}|")
print(f"{CYAN}" + "=" * (INNER_WIDTH + 2))

# Final message
print(f"\n{MAGENTA}Analysis complete{CHANGE_COLOR}...{RESET}")