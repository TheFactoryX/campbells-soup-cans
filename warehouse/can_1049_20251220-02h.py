"""
Campbell's Soup Can #1049
Produced: 2025-12-20 02:16:19
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

quote = "I'm so neurotic, I've started to doubt my own paranoia."

brain_art = (
"      __\n"
"     /  \\\n"
"    | oo |\n"
"     \\  /\n"
"      \\\\/\n"
)

brain_color = "\033[93m"
border_color = "\033[92m"
text_color = "\033[96m"
reset = "\033[0m"

border_width = 60

print(brain_color + brain_art + reset, end='')

print(border_color + "+" + "-"*(border_width-2) + "+" + reset)

inner = quote.center(border_width - 2)
print(text_color + "|" + inner + "|" + reset)

print(border_color + "+" + "-"*(border_width-2) + "+" + reset)