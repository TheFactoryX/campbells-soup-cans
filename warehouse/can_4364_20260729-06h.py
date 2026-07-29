"""
Campbell's Soup Can #4364
Produced: 2026-07-29 06:44:55
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
ENDC = "\033[0m"

# The split parts of the quote
quote_parts = [
    RED + "I'm not afraid of death..." + ENDC,
    GREEN + "I just don't want to be there when it happens." + ENDC,
    MAGENTA + "Wait, think about it:" + ENDC,
    "\n" + YELLOW + "               __" + ENDC,
    CYAN + "           ,-'  /  \\" + ENDC,
    YELLOW + "        ,-" + RED + "   ___|" + ENDC,
    WHITE + "     ,-" + GREEN + "  /    \\" + ENDC,
    RED + "   ,-\\ " + BLUE + " /      \\" + ENDC,
    WHITE + "   '-'   " + CYAN + "/        \\" + ENDC,
    RED + "   '-'    " + MAGENTA + "\\        /" + ENDC,
    GREEN + "    '-'   " + BLUE + "  \\_____/  \\" + ENDC,
    BLUE + "           ,-" + MAGENTA + "  /  \\" + ENDC,
    GREEN + "        ,-'  \\  /" + ENDC,
    RED + "       '-'    \\/  \\" + ENDC,
    CYAN + "        '" + RED + "   |  /" + ENDC,
    YELLOW + "         /" + GREEN + " \\/  \\" + ENDC,
    RED + "        ('`" + BLUE + "   |  /" + ENDC,
    CYAN + "        /  " + YELLOW + "\\/  \\/  \\" + ENDC,
    WHITE + "       /" + RED + "    |  /\\|_/\\" + ENDC,
    RESET + "       |   \\|  / \\ \_ _/" + ENDC
]

# Print top border
print(YELLOW + "█" * 60 + ENDC)

# Print first two parts immediately
print(quote_parts[0])
print(quote_parts[1])
print(quote_parts[2])
print()

# Countdown timer
for i in range(3, 0, -1):
    print(f"    Countdown: {i}...", end='\r')
    sys.stdout.flush()
    time.sleep(1)
time.sleep(0.5)
print()

# Animated ASCII brain
print(CYAN + "    .-~~~.           .-~~~.  .-~~~. .-~~~." + ENDC)
print(YELLOW + "  .      \\        .      \\  .      \\      " + ENDC)
print(RED + "  |    __ \\      |    __ \\  |    __ \\      " + ENDC)
print(MAGENTA + "  |   |  | \\`--. |   |  | \\`--. | \\`--.      " + ENDC)
print(WHITE + "  |   |  \\_\\   / |   |  \\_\\   / |   \\      " + ENDC)
print(RED + "  |  \\_____ //  / |   \\_____ //  / / __     " + ENDC)
print(GREEN + "  \\  \\____/  /  / \\   / __\\  /  / /(_)\\    " + ENDC)
print(BLUE + "   \\  /    /  /  \\ \\  \\__/  /  / --'   \\   " + ENDC)
print(MAGENTA + "    \\/    /  /    \\ \\       /  / --'     \\\\ \\" + ENDC)
print(CYAN + "        /  /      \\ \\      |\\ |              \\ \\" + ENDC)
print(WHITE + "         /  /        \\ \\     -|-   Here it's" + ENDC)
print(BLUE + "         \\/           \\ \\|_|_|_|  clearly:" + ENDC)
print(RED + "         \\/            \\ /"))

# Show final part with color transition
color_transition = [
    BLUE + quote_parts[3] + ENDC,
    MAGENTA + quote_parts[3] + ENDC,
    CYAN + quote_parts[3] + ENDC
]
for part in color_transition:
    print(part)
    time.sleep(0.2)
    print("\033[1A")  # Move cursor up one line