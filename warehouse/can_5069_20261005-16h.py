"""
Campbell's Soup Can #5069
Produced: 2026-10-05 16:01:01
Worker: Meta: Muse Glimmer 30B (meta/muse-glimmer-30b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

RESET = "\033[0m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
DIM = "\033[2m"

QUOTES = [
    "I'm not afraid of death; I'm just afraid of being in the room when it happens and having to make small talk.",
    "I finally understood the meaning of life. It means to be too nervous to go to the bathroom in a public building.",
    "I don't want immortality through my work, I want immortality by not dying and having to cancel my therapy appointments.",
    "Existential dread is just anxiety with a better vocabulary and worse health insurance.",
    "I used to think I was indecisive, but now I'm not so sure. And that's the real neurosis.",
    "Life is full of misery, loneliness, and suffering, and it's all over much too soon. Also, my knees hurt."
]

quote = random.choice(QUOTES)

def type_text(text, delay=0.02, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def box(text, color=CYAN):
    lines = text.split("\n")
    width = max(len(l) for l in lines) + 4
    top = f"{color}┌{'─'*(width-2)}┐{RESET}"
    bottom = f"{color}└{'─'*(width-2)}┘{RESET}"
    print(top)
    for l in lines:
        padded = l.ljust(width-3)
        print(f"{color}│ {RESET}{MAGENTA}{padded}{RESET}{color}│{RESET}")
    print(bottom)

print(f"{DIM}thinking...{RESET}", end="")
for _ in range(3):
    time.sleep(0.4)
    sys.stdout.write(".")
    sys.stdout.flush()
print("\n")

print(f"{YELLOW}Woody Allen Wisdom™{RESET}")
time.sleep(0.3)

box(quote, CYAN)

print(f"\n{DIM}— Woody Allen{RESET}")