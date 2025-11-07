"""
Campbell's Soup Can #124
Produced: 2025-11-07 20:30:27
Worker: Qwen: Qwen3 30B A3B (free) (qwen/qwen3-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not neurotic, I'm just in a constant state of existential panic about my neurosis."

# ANSI color codes
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# ASCII art of a banana
banana_art = """
      _.-^^---....,,--
  _-         _-         _-
  \\      /\\      /\\      /\\
   \\    \\        /        \\    /
    \\    \\______/        \\    /
     \\    (O)         (O)    /
      \\        \\           \\
       \\        \\           \\
        \\_________________\\
"""

print(f"{YELLOW}{banana_art}{RESET}")

# Create a border with animated blinking
border_length = len(quote) + 4
border = '*' * border_length
for _ in range(3):
    print(f"{CYAN}{border}{RESET}")
    print(f"{CYAN}* {YELLOW}\033[5m{quote}\033[0m {CYAN}*{RESET}")
    print(f"{CYAN}{border}{RESET}")
    time.sleep(1)
    # Clear the printed lines
    print("\033[2A\033[0J", end='')