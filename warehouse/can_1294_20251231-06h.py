"""
Campbell's Soup Can #1294
Produced: 2025-12-31 06:50:32
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

quote = "I'm not afraid of death; I just don't want to be there when it does."

# Thinking face ASCII art
face_art = """
     ,------,
   /        \\
  |  o    o  |
   \\  `-----'  /
    `--------'
"""

border = '+' + '-' * 68 + '+'
content_line = f"|{quote.center(68)}|"

# ANSI codes
print("\033[40m", end='')  # black background

# Print face art in yellow
print("\033[93m", end='')
print(face_art, end='')
print("\033[0m", end='')

# Print top border in yellow
print("\033[93m", end='')
print(border)
print("\033[0m", end='')

# Print content in bright red
print("\033[91m", end='')
print(content_line)
print("\033[0m", end='')

# Print bottom border in yellow
print("\033[93m", end='')
print(border)
print("\033[0m", end='')

# Reset all
print("\033[0m", end='')