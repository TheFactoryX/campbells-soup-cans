"""
Campbell's Soup Can #1601
Produced: 2026-01-14 11:34:30
Worker: OpenAI: GPT-4.1 (openai/gpt-4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

quote = (
    "I asked the universe for meaning,\n"
    "but all it gave me was spam mail\n"
    "and a subscription to existential dread.\n"
    "\n"
    "— (with apologies, Woody Allen)"
)

ascii_woody = [
    f"{YELLOW}           ____",
    "         /    \\",
    f"{YELLOW}        |      |",
    f"{CYAN}        |  0 0 |",
    f"{WHITE}        |  ~   |",
    f"{RED}        | .---.|",
    f"{CYAN}       /|_______|\\",
    f"{CYAN}      /  |     |  \\",
    f"{CYAN}     |   |     |   |",
    f"{DIM}     |___|_____|___|{RESET}"
]

bubble = [
    "        _______________________________",
    "       /                               \\",
    "      /",
    "     | ",
    "     | ",
    "     | ",
    "      \\_______________________________/",
]

# Prepare the speech bubble with the quote
bubble_lines = quote.split('\n')
bubble_width = max(len(line) for line in bubble_lines) + 6
bubble_top = f"       {'_' * (bubble_width-2)}"
bubble_border_left = "     | "
bubble_border_right = " |"
bubble_bottom = f"      {'‾' * (bubble_width-2)}"

print()
# Print animated speech bubble
print(YELLOW + bubble_top + RESET)
for line in bubble_lines:
    content = line
    print(CYAN + bubble_border_left + RESET, end='')
    print(WHITE + content.ljust(bubble_width - 6) + RESET, end='')
    print(CYAN + bubble_border_right + RESET)
    time.sleep(0.15)
print(CYAN + bubble_bottom + RESET)

# Print ASCII Woody Allen head, animated line by line
for line in ascii_woody:
    print(line)
    time.sleep(0.13)

# Comedic blinking effect on the eyes
eye_line_idx = 3
for i in range(5):
    sys.stdout.write('\033[F' * (len(ascii_woody)-eye_line_idx))  # move cursor up to eyes
    sys.stdout.flush()
    if i % 2 == 0:
        eye = f"{CYAN}        | - - |"
    else:
        eye = f"{CYAN}        | 0 0 |"
    print(eye)
    # Re-print below lines
    for line in ascii_woody[eye_line_idx+1:]:
        print(line)
    sys.stdout.flush()
    time.sleep(0.27)
    sys.stdout.write('\033[F' * (len(ascii_woody)-eye_line_idx-1))
print(RESET)