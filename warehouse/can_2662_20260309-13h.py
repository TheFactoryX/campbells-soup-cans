"""
Campbell's Soup Can #2662
Produced: 2026-03-09 13:40:06
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

reset = "\033[0m"
bg_purple = "\033[48;2;80;0;120m"
fg_yellow = "\033[38;2;255;220;0m"
fg_cyan = "\033[38;2;0;255;255m"
fg_pink = "\033[38;2;255;105;180m"
fg_orange = "\033[38;2;255;165;0m"

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

quote = (
    "I've come to terms with my mortality. Sort of. "
    "The universe is expanding at 73 km/s per megaparsec, "
    "which is slightly faster than my waistline. "
    "Coincidence? I think not. "
    "Existential dread is just my cardio."
)

width = 58
top_border = f"{fg_orange}╔{'═' * (width-2)}╗{reset}"
bottom_border = f"{fg_orange}╚{'═' * (width-2)}╝{reset}"

lines = []
current = ""
for word in quote.split():
    if len(current) + len(word) + 1 <= width - 4:
        current += (word + " ")
    else:
        lines.append(current.strip().center(width-4))
        current = word + " "
if current:
    lines.append(current.strip().center(width-4))

frame = [
    top_border,
    f"{fg_orange}║{reset}{fg_cyan}{' ' * (width-2)}{fg_orange}║{reset}",
    *[f"{fg_orange}║{reset}{fg_pink}{line}{reset}{fg_orange}║{reset}" for line in lines],
    f"{fg_orange}║{reset}{fg_cyan}{' ' * (width-2)}{fg_orange}║{reset}",
    f"{fg_orange}║{reset}{bg_purple}{fg_yellow}{' ' * 15}~ Neurotic Philosophy Dept ~{reset}{fg_orange}║{reset}",
    f"{fg_orange}║{reset}{bg_purple}{fg_yellow}{' ' * 10}Est. 1950 (give or take an existential crisis){reset}{fg_orange}║{reset}",
    f"{fg_orange}║{reset}{fg_cyan}{' ' * (width-2)}{fg_orange}║{reset}",
    bottom_border
]

print(f"{bg_purple}{fg_yellow}", end="")
print_slow("  .-''''-.\n /        \\\n|  O    O  |\n|    ∆    |\n \\  ~~~  /\n  '-...-'  ", 0.05)
print(reset)

for line in frame:
    print(line)
    time.sleep(0.1)

print(f"\n{fg_orange}{' ' * 15}© 2023 Allen & Allen's Existential Diner{reset}")