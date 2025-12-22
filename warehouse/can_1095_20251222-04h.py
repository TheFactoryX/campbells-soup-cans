"""
Campbell's Soup Can #1095
Produced: 2025-12-22 04:52:46
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

YELLOW = '\033[93m'
GREEN = '\033[92m'
BLUE = '\033[94m'
ENDC = '\033[0m'

WIDTH = 64
quote = "Existential dread? I call it remembering I left the stove on."

face = [
    "    __",
    "   /  \\",
    "( o.o)",
    "  \\  /",
    "   |"
]

for line in face:
    print(YELLOW + line + ENDC)

print(YELLOW + '+' + '-'*(WIDTH-2) + '+' + ENDC)

content = '|' + quote.center(WIDTH-2) + '|'
print(GREEN + content + ENDC)

print(YELLOW + '+' + '-'*(WIDTH-2) + '+' + ENDC)

author_line = " - A Neurotic Philosopher"
print('\n' + BLUE + author_line.center(WIDTH) + ENDC)