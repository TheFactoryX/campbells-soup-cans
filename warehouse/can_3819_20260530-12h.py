"""
Campbell's Soup Can #3819
Produced: 2026-05-30 12:15:53
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

quote_lines = [
    f"{YELLOW}I told my therapist{I} I keep thinking about {RED}death{RESET}.",
    f"{GREEN}She said, 'That's normal.' I said, 'No, I think{RESET}",
    f"{CYAN}about it 23 hours a day. Isn't that a bit obsessive?\"{RESET}",
    f"{RED}She prescribed me a vacation. I said, 'Great! What's{RESET}",
    f"{YELLOW}the point? Eventually, I'll be in a {GREEN}box{RESET}. A very small one.",
    f"{BOLD}Probably with a view.'{RESET} She nodded. {RED}I hate therapists.{RESET}"
]

BOX_WIDTH = 60

def animate_line(line, color):
    centered = line.center(BOX_WIDTH - 2)
    sys.stdout.write("|")
    for char in centered:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.03)
    print("|")

# Fancy border
print("\n" + "╔" + "═"*BOX_WIDTH + "╗")
time.sleep(0.3)
animate_line("", RESET)

for i, line in enumerate(quote_lines):
    color = [YELLOW, GREEN, CYAN, RED, BOLD][i % 5]
    animate_line(line, color)
    time.sleep(0.2)

print("╚" + "═"*BOX_WIDTH + "╝")
time.sleep(0.3)
animate_line("", RESET)

# Additional ASCII art effect
print("\n\n  ___")
print(" /   \\")
print("|     |  ┌──────────────────────┐")
print(" \\___/   │    Existential Crisis │")
print("  |||    └──────────────────────┘")
print("  |||     /")
print("  ''''''''/")
print("\n")
time.sleep(0.5)
print(f"{RED} ┌─────────────────────────────────────────────────────────────────┐{RESET}")
time.sleep(0.1)
print(f"{GREEN} │ 'Life is full of misery... and it's all over much too soon.'      │{RESET}")
time.sleep(0.1)
print(f"{CYAN} └─────────────────────────────────────────────────────────────────┘{RESET}\n")