"""
Campbell's Soup Can #4382
Produced: 2026-07-30 22:18:53
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI colors
C_RESET = "\033[0m"
C_GREEN = "\033[1;32m"
C_MAGENTA = "\033[1;35m"
C_CYAN = "\033[1;36m"
C_YELLOW = "\033[1;33m"

# ASCII art: a thinking face with speech bubble (Woody Allen style)
art = r"""
      .-"-.      .-"-.
    .'   _   '.  _   '.   .
   /  _/ \_  \ /___\  \  .
  |   |   |   ||   |   |   |
   \  \_/  \_/  \_/   \_/   /
    \'.-._.-.\    \'.-.\   .\' 
        (            )
         \          /
          \'-____.-'
"""

# Animate the art line by line
for line in art.splitlines():
    if line:
        print(C_CYAN + line + C_RESET)
        time.sleep(0.1)

# Philosophical quote in Woody Allen style
quote = """“I'm not afraid of death; I just don't want to be the person who has to explain the joke when it arrives.”"""

# Box dimensions
width = 78

# Build box parts
top = C_MAGENTA + "╔" + "═" * (width - 2) + "╗" + C_RESET
bottom = C_MAGENTA + "╚" + "═" * (width - 2) + "╝" + C_RESET
left_right = C_MAGENTA + "║" + C_RESET

# Center the quote inside the box with padding
padding = (width - len(quote) - 4) // 2  # 4 for borders and spaces
quote_line = f"{left_right}{' ' * padding}{C_GREEN}{quote}{C_RESET}{' ' * padding}{left_right}"

# Print the boxed quote
print()
print(top)
print(quote_line)
print(bottom)
print()

# Optional punchline
print(C_YELLOW + "--- End of the Woody Allen philosophical surprise ---" + C_RESET)