"""
Campbell's Soup Can #3508
Produced: 2026-04-30 14:24:00
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import randomimport time

def color_print(text, color_code):
    print(f"\033[{color_code}m{text}\033[m", end='')

print("\033[H\033[J", end='')

print("\033[1;36m   /\\/ \\  ┌─┐┬─┐ ┌─┐┬─┐ ┌─┐\033[m")
print("\033[1;35m   \\  │ │ │ │ │ │ │ │\033[m")
print("\033[1;34m    \\  └ └ └ └┘└─┘ └ม\033[m")
print("\033[1;91m    ━━━━━━━━━━━━━━━━━━━━━━\033[m\n")

quote = [
    "ξ   I",
    "ξ   tripped over",
    "ξ   the finish",
    "ξ   line of",
    "ξ   my life’s",
    "ξ   participation",
    "ξ   trophy.",
    "ξ",
    "φ   Clue:",
    "φ   I wear socks",
    "   with\ndotted\nlines.",
    "ξ   Everyone’s",
    "ξ   got baggage. Mine's just labeled “Perhaps”."
]

print("\033[92m┌───────────────────────────────┐\033[m")
print("\033[92m| \033[37m▸▸▸▸▸▸▸▸▸▸▸▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓¯ \033[92m|  \033[m")
for line in quote:
    quote_color = random.choice(["31", "32", "33", "34", "35", "36", "37", "90", "91", "92", "93", "94", "95", "96"])
    # Clear each line before printing new to simulate update
    print("\033[F", end='')
    print(f"\033[1;{quote_color}m|    {line}             |\033[m")
print("\033[F\n\033[1;36m|                                       \033[m\n\033[1;36m└────────────────────────────────────────┘\033[m")
print("\n\033[1;33m-- Lenny, explaining why his dating profile became a LinkedIn post.\033[m")
