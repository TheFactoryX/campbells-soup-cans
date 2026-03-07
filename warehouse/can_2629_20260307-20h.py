"""
Campbell's Soup Can #2629
Produced: 2026-03-07 20:40:41
Worker: AllenAI: Olmo 3 32B Think (allenai/olmo-3-32b-think)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# ANSI color codes
BG_BLACK = '\033[40m'
TEXT_WHITE = '\033[37m'
TEXT_GREEN = '\033[32m'
TEXT_CYAN = '\033[36m'
HEADER_COLOR = '\033[95m'
RESET = '\033[0m'

# Thought bubble ASCII art
thought_art = "         __\n     _/  \\_\n   ,'     ',.\n"

# The quote
quote = "I'm not paranoid, but if everyone is out to get me, I'm the most popular guy in town."
quote_length = len(quote)
padding = 4
total_width = quote_length + padding * 2 + 2

# Print thought bubble
print(TEXT_CYAN + thought_art + RESET)

# Print header
print(HEADER_COLOR + " Woody Allen's Existential Crisis " + RESET)
print()

# Print box borders and content
# Top border
border = '+' + '-' * (total_width - 2) + '+'
print(BG_BLACK + TEXT_WHITE + border + RESET)

# Middle line with quote
middle = '|' + quote.center(total_width - 2) + '|'
print(BG_BLACK + TEXT_GREEN + middle + RESET)

# Bottom border
print(BG_BLACK + TEXT_WHITE + border + RESET)