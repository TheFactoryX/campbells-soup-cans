"""
Campbell's Soup Can #3199
Produced: 2026-04-08 23:01:06
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time
import random

COLORS = [
    "\033[94m",    # Blue
    "\033[93m",   # Yellow
    "\033[95m",   # Magenta
    "\033[92m",   # Green
    "\033[96m"    # Cyan
]

HEADERS = {
    "🎭": "EXISTENTIAL THEATER",
    "☕️": "CAFFEINE-ASSISTED EXISTENTIALISMOLOGY",
    "🤖": "EXISTENTIAL THERAPY (DO NOT ATTEMPT AT HOME)"
}

ANSI_ART = {
    "frame": [
        "┌───────────────────┐",
        "│                   │",
        "│                   │",
        "└───────────────────┘"
    ],
    "exit": "():- ( ]"
}

def print_colored(text, color_codes=None):
    if color_codes:
        colored = []
        for i, char in enumerate(text):
            colored.append(COLORS[i % len(COLORS)] + char + "\033[0m")
        return "".join(colored)
    return text

def print_frame(text):
    width = len(text)
    border = '\u2551' * (width + 4)
    print(f"{COLORS[3]}{border}\033[0m")
    print(f"{COLORS[4]}{'─' + text.center(width) + '─'}\033[0m")
    print(f"{COLORS[3]}{border}\033[0m")

def main():
    # Random header selection
    header_key = random.choice(list(HEADERS.keys()))
    print(f"{COLORS[2]}{' ' * 20}{HEADERS[header_key]}")

    # ASCII border
    for line in ANSI_ART["frame"]:
        print(f"{COLORS[1]}{line.ljust(30)}\033[0m")
    print()
    
    # Our signature quote
    quote = "I'm afraid my greatest talent is residential gap analysis\n" \
            "— the ability to move between jobs faster than a \ncoyote on Adderall."

    # Print with typewriter effect
    for char in quote:
        # Random color for each character
        c = random.choice(COLORS[:-1])
        print(f"{c}{char}", end="", flush=True)
        time.sleep(0.03)
    print()

    # Add existential footnote
    print(f"\n{WOLF}\n\t{time.strftime('%Z')} {- '\u2764' * random.randint(1, 5)}\n{WOLF}\n" 
          + "Existence: The only thing I sacrifice for life." 
          + f"\033[31m{random.choice(['...', '???', '...'])}\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{COLORS[5]}\n {random.choice(['Oopsie]', ' halted, but still overthink.', 'Typo crisis.'])}")