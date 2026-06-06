"""
Campbell's Soup Can #3869
Produced: 2026-06-06 04:19:47
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

RESET = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'

def typewriter(text, color=RESET, delay=0.03):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + '\n')
    sys.stdout.flush()

# Animated header
print(f"{CYAN}")
print("  ____  _     _     _   _           _   _           ")
print(" |  _ \\(_)   | |   | | | |         | | | |          ")
print(" | |_) |_ ___| |__ | |_| |__   ___ | |_| | _____  _ __")
print(" |  _ <| / __| '_ \\| __| '_ \\ / _ \\| __| |/ _ \\ || |")
print(" | |_) | \\__ \\ | | | |_| | | | (__| |_| |  __/\\_, |")
print(" |____/|_|___/_| |_|\\__|_| |_|\\___/\\__|_|\\___|__/ |")
print(f"{RESET}")
time.sleep(0.7)

# Fancy frame
top = f"{RED}╔══════════════════════════════════════════════════════════════╗{RESET}"
middle = f"{RED}║{RESET}                                                              {RED}║{RESET}"
bottom = f"{RED}╚══════════════════════════════════════════════════════════════╝{RESET}"

print(top)
print(middle)
print(f"{RED}║{RESET}   {YELLOW}{BOLD}Woody Allen's Existential Crisis Generator™{RESET}{RED}               {RESET}{RED}║{RESET}")
print(middle)
print(bottom)
time.sleep(0.4)

# The philosophical quote with multi-color typing
quote = "I'm not afraid of death; I just don't want to be there when it happens."
colors = [RED, YELLOW, MAGENTA, CYAN, BLUE]

print(f"{WHITE}")
for i, char in enumerate(quote):
    color = colors[i % len(colors)]
    sys.stdout.write(f"{color}{char}{RESET}")
    sys.stdout.flush()
    time.sleep(0.04)
print(RESET)

time.sleep(0.5)
print(f"{GREEN}                    (pause for existential dread)...{RESET}")
time.sleep(0.3)
print(f"{BLUE}                         - A. Allen{RESET}")