"""
Campbell's Soup Can #2541
Produced: 2026-03-03 10:00:31
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

CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
ENDC = '\033[0m'

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Neurotic ASCII art
ascii_art = [
    f"{GREEN}    .-.{ENDC}              {RED}^__^{ENDC}",
    f"{GREEN}   (o o){ENDC}            {RED}(o o){ENDC}",
    f"{GREEN}  (  V  ){ENDC}  WHY {RED}<  \\/  >{ENDC}",
    f"{GREEN}   '--'{ENDC}  AM I {RED}-----{ENDC}  HERE?",
    f"{GREEN}  || ||{ENDC}   LIKE {RED}|| ||{ENDC}   THIS?"
]

# Print wobbling ASCII art with color shifts
for _ in range(3):
    for i, line in enumerate(ascii_art):
        shift = " " * (i % 3)
        sys.stdout.write(f"\r{shift}{line}{ENDC}")
        sys.stdout.flush()
        time.sleep(0.15)
sys.stdout.write("\n" + " "*5 + f"{BOLD}{YELLOW}Woody Allen's Existential Dilemma:{ENDC}\n\n")

# Philosophical quote in Woody's style
quote = "I don't suffer from existential dread; I enjoy every minute of it. It passes the time, and who knows? Maybe death will cancel me out as too depressing."

# Create a shaking, nervous box
width = len(quote) + 4
borders = [
    f"{CYAN}┌{'─' * width}┐{ENDC}",
    f"{CYAN}└{'─' * width}┘{ENDC}"
]

print(borders[0])
sys.stdout.write(f"{CYAN}│ {YELLOW}")

# Typewriter effect with nervous shaking
for i, char in enumerate(quote):
    offset = " " * (1 if i % 7 == 0 else 0)
    sys.stdout.write(f"\r{CYAN}│ {YELLOW}{quote[:i+1]}{offset} {' ' * (len(quote)-i-1)}")
    sys.stdout.flush()
    time.sleep(0.05 * (1.5 if i % 11 == 0 else 1))  # Extra shake every 11 characters

sys.stdout.write(f"\r{CYAN}│ {YELLOW}{quote} {ENDC}{CYAN}│{ENDC}\n")
print(borders[1])

# Final neurotic flourish
typewriter(f"\n{RED}P.S. Is this the end? Or have I finally achieved immortality through over-explaining?{ENDC}\n", 0.02)
sys.stdout.write(f"{BOLD}{'★ ' * 15}{ENDC}\n")