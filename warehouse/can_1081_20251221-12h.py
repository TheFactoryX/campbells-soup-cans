"""
Campbell's Soup Can #1081
Produced: 2025-12-21 12:58:10
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

width = 50
border = '+' + '-' * (width - 2) + '+'
colors = {
    'yellow': '\033[33m',
    'reset': '\033[0m',
    'cyan': '\033[36m',
    'green': '\033[32m',
}

print(f"{colors['yellow']}{border}{colors['reset']}")
print(f"{colors['cyan']}|          Woody Allen's Quote          |{colors['reset']}")
art = [
    "   O",
    "  /|\\",
    " / | \\",
    "/__|__\\",
]
for line in art:
    print(f"{colors['cyan']}| {line.center(48)} |{colors['reset']}")
print(f"{colors['cyan']}|                                        |{colors['reset']}")
print(f"{colors['green']}| I think, therefore I\'m confused.     |{colors['reset']}")
print(f"{colors['cyan']}|                                        |{colors['reset']}")
print(f"{colors['yellow']}{border}{colors['reset']}")