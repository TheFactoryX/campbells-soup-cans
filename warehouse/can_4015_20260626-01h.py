"""
Campbell's Soup Can #4015
Produced: 2026-06-26 01:30:06
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Prints a Woody Allen style philosophical quote inside a colorful ASCII box

RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
MAGENTA= "\033[95m"
RESET  = "\033[0m"

quote = [
    "I don’t want immortality through my jokes;",
    "I’d settle for a quiet exit before anyone asks",
    "for an encore."
]

filler = "═"*58
top    = RED    + "╔" + filler + "╗" + RESET
bottom = RED    + "╚" + filler + "╝" + RESET
empty  = YELLOW + "║" + " "*58 + "║" + RESET

print(top)
print(empty)
for line in quote:
    padded = line.ljust(58)
    print(YELLOW + "║  " + CYAN + padded + "  ║" + RESET)
print(empty)
print(bottom)
print(MAGENTA + "\nAnd that’s the punchline.\n" + RESET)