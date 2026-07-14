"""
Campbell's Soup Can #4192
Produced: 2026-07-14 09:17:06
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

box_color = "\033[94m"
text_color = "\033[93m"
dim = "\033[90m"
reset = "\033[0m"

def type_line(text, delay=0.02):
    sys.stdout.write(text_color)
    stripped = text.rstrip()
    for char in stripped:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(" " * (len(text) - len(stripped)))
    sys.stdout.write(reset)

lines = [
    "I'm not afraid of the existential void; I'm just",
    "terrified of getting there, realizing it's an",
    "eternal waiting room, and finding out I forgot",
    "to bring a book. What is eternity without a",
    "good novel and a neurotic internal monologue?"
]

sys.stdout.write("\033[2J\033[H")

print(f"{dim}      ╭─────╮     ╭─────╮")
print(f"     ╱       ╲   ╱       ╲")
print(f"    ╱         ╲ ╱         ╲")
print(f"   │           ╲           │")
print(f"   │           ╱           │")
print(f"    ╲         ╱ ╲         ╱")
print(f"     ╲       ╱   ╲       ╱")
print(f"      ╰─────╯     ╰─────╯{reset}\n")

time.sleep(0.3)

print(f"{box_color}╔{'═'*56}╗{reset}")
time.sleep(0.1)

for line in lines:
    sys.stdout.write(f"{box_color}║ {reset}")
    type_line(line.ljust(54), delay=0.02)
    sys.stdout.write(f" {box_color}║{reset}\n")
    time.sleep(0.1)

print(f"{box_color}╚{'═'*56}╝{reset}")
time.sleep(0.1)

print(f"\n{dim}— A thought by a neurotic man who fears the afterlife's library fines.{reset}\n")