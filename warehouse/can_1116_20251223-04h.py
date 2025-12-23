"""
Campbell's Soup Can #1116
Produced: 2025-12-23 04:07:19
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

CYAN = '\033[36m'
YELLOW = '\033[33m'
RESET = '\033[0m'

thinking_face = [
    "   __",
    "  /  \\",  
    " (  o  )",
    "  \\__/",
]

print(CYAN + "\n".join(thinking_face) + RESET)

quote = "I'd rather be anxious than dead."
border = '+' + '-'*38 + '+'
print(CYAN + border)
print(CYAN + '| ' + YELLOW + quote.center(36) + RESET + CYAN + ' |')
print(CYAN + border)