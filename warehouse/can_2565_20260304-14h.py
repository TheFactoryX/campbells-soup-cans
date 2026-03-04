"""
Campbell's Soup Can #2565
Produced: 2026-03-04 14:58:07
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_typing(text, delay=0.03, color=""):
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

BLUE = "\033[94m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

woody_quote = (
    "I'm not afraid of death; I'm afraid of the paperwork it will generate. "
    "And let's face it, the afterlife is just another bureaucracy with worse lighting "
    "and absolutely no decent espresso."
)

inner_width = 50
top_bottom = "┌" + ("─" * inner_width) + "┐"
frame_color = BLUE
text_color = YELLOW

print("\n" * 5)
print_typing(f"{' ' * 20}WOODY ALLEN PRESENTS...", 0.06, MAGENTA)
time.sleep(1)

print(f"\n{frame_color}{' ' * 18}{top_bottom}{RESET}")

lines = []
current = ""
for word in woody_quote.split():
    if len(current) + len(word) + 1 <= inner_width:
        current += (" " + word) if current else word
    else:
        lines.append(current)
        current = word
if current: lines.append(current)

for line in lines:
    padding = " " * ((inner_width - len(line)) // 2)
    print(frame_color + " " * 18 + "│" + " " * (len(padding)) + RESET, end="")
    print_typing(line, 0.04, text_color)
    print(frame_color + " " * (inner_width - len(line) - len(padding)) + "│" + RESET)
    time.sleep(0.3)

print(f"{frame_color}{' ' * 18}└" + ("─" * inner_width) + "┘{RESET}")

# Mini film projector animation below the frame
time.sleep(1)
film_strip = [
    "    ╭──────╮    ╭──────╮    ╭──────╮    ╭──────╮    ",
    "    │  ()  │    │  ()  │    │  ()  │    │  ()  │    ",
    "    ╰──────╯    ╰──────╯    ╰──────╯    ╰──────╯    ",
    "  ╭────────────────────────────────────────────────╮",
    "  │  _   _  ___  ___  ___  _   _  ___  ___  ___  _  │",
    "  │ | | | |/ _ \\/ _ \\/ _ \\| | | |/ _ \\/ _ \\/ _ \\| | │",
    "  │ | |_| | |_| |_| |_| |_| |_| | |_| |_| |_| |_| | │",
    "  │  \\___/ \\___/\\___/\\___/ \\___/ \\___/\\___/\\___/\\___/ │",
    "  ╰────────────────────────────────────────────────╯"
]

for i in range(3):
    for frame in film_strip:
        sys.stdout.write('\r' + ' ' * 100 + '\r')
        sys.stdout.write(f"{' ' * 15}{MAGENTA}{frame}{RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
    time.sleep(0.3)

print(f"\n{' ' * 15}{MAGENTA}Woody Says:{RESET}{YELLOW} Existence is a terrible idea - why would anyone invent it?{RESET}")
time.sleep(2)