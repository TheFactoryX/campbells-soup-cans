"""
Campbell's Soup Can #1045
Produced: 2025-12-19 20:35:17
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Define ANSI colors
HEADER = '\033[95m'     # purple
QUOTE_COLOR = '\033[92m' # green
RESET = '\033[0m'
BOLD = '\033[1m'
EYE_COLOR = '\033[93m'   # yellow

# Thinking head ASCII art with colored eyes
print("  o" + EYE_COLOR + "OO" + RESET + "o  ")
print(" (" + EYE_COLOR + "o o" + RESET + ")")
print("  > ^ <  ")

# Decorative line above quote
print(HEADER + "~" * 30 + RESET)

# The philosophical quote
print(QUOTE_COLOR + "I'm not sure if I exist or if I'm just a character in someone else's existential crisis." + RESET)

# Decorative line below
print(HEADER + "-" * 30 + RESET)

# Attribution
print(HEADER + " - Probably Woody Allen" + RESET)