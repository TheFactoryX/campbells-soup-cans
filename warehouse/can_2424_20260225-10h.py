"""
Campbell's Soup Can #2424
Produced: 2026-02-25 10:11:57
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, random, sys

# ANSI color codes
FG_BLUE    = "\033[94m"
FG_RED     = "\033[91m"
FG_GREEN   = "\033[92m"
FG_YELLOW  = "\033[93m"
FG_MAGENTA = "\033[95m"
FG_CYAN    = "\033[96m"
FG_BLACK   = "\033[90m"
FG_WHITE   = "\033[97m"
RESET      = "\033[0m"

def random_fg():
    return random.choice([FG_BLUE, FG_RED, FG_GREEN, FG_YELLOW, FG_MAGENTA, FG_CYAN, FG_BLACK, FG_WHITE])

def random_bg():
    return "\033[4" + str(random.randint(0,7)) + "m"

def coffee_cup():
    lines = [
        "\n" + FG_CYAN + "     ____" + RESET + "   (" + FG_MAGENTA + "W" + RESET + ")\n",
        FG_CYAN + "   /      \\" + RESET + "    (" + FG_MAGENTA + "W" + RESET + ")\n",
        FG_CYAN + "  /        \\" + RESET + "    (" + FG_MAGENTA + "W" + RESET + ")\n",
        FG_CYAN + " |          |" + RESET + "    (" + FG_MAGENTA + "W" + RESET + ")\n",
        FG_CYAN + " |          |" + RESET + "    (" + FG_MAGENTA + "W" + RESET + ")\n",
        FG_CYAN + "  \\        /" + RESET + "    (" + FG_MAGENTA + "W" + RESET + ")\n",
        FG_CYAN + "   \\______/ " + RESET + "    (" + FG_MAGENTA + "W" + RESET + ")\n"
    ]
    for line in lines:
        print(line, flush=True)
        time.sleep(random.uniform(0.03, 0.1))

def typewriter(text, delay=0.02):
    for ch in text:
        if ch.isspace():
            print(" ", end="", flush=True)
            time.sleep(delay*0.5)
            continue
        fg = random_fg()
        bg = random_bg()
        print(f"{fg}{bg}{ch}{RESET}", end="", flush=True)
        time.sleep(delay)
    print()  # newline after full quote

def main():
    # Intro banner
    banner = [
        FG_CYAN + "   __      __   " + RESET,
        FG_CYAN + "  / /\\    / /   " + RESET,
        FG_CYAN + "  \\ \\ \\__ / /    " + RESET,
        FG_CYAN + "   \\ \\_// /     " + RESET,
        FG_CYAN + "    \\____/      " + RESET,
        "— Woody Allen's Thought Machine —"
    ]
    for line in banner:
        print(line, flush=True)
        time.sleep(0.2)

    # Coffee cup animation
    coffee_cup()

    # Woody‑Allen‑style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print(FG_RED + quote + RESET)
    typewriter(quote, delay=0.03)

    # Closing “flashing” animation
    print("\n" + FG_YELLOW + "☕ Enjoy the moment!" + RESET)
    for _ in range(5):
        print(FG_YELLOW + "☕" + RESET, end="", flush=True)
        time.sleep(0.5)
        print("\b ", end="", flush=True)  # wipe coffee symbol
        time.sleep(0.5)

if __name__ == "__main__":
    main()