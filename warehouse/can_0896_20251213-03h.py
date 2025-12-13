"""
Campbell's Soup Can #896
Produced: 2025-12-13 03:56:01
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI color codes
RESET = '\033[0m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'

# Woody Allen-style quote
QUOTE = "I'd love to avoid responsibility, but the only way to do that is to stop breathing—and I've always been terrible at holding my breath."

# Decorative elements
TOP_DECOR = f"{CYAN}  __      __  {MAGENTA}~~~ existential anxiety buffet ~~~{RESET}"
BOTTOM_DECOR = f"{CYAN}  ╭───────────────╮ {MAGENTA}*~* tiny trauma included *~*{RESET}"
GLASSES = f"{YELLOW}  ̄◡̄"{RESET}

def colored_box(text, border_color=GREEN, text_color=YELLOW):
    """Create a fancy colored box around text"""
    width = len(text) + 4
    top_border = f"{border_color}╔{'═' * width}╗{RESET}"
    middle = f"{border_color}║ {text_color}{text.center(width)} {border_color}║{RESET}"
    bottom_border = f"{border_color}╚{'═' * width}╝{RESET}"
    return f"\n{top_border}\n{middle}\n{bottom_border}\n"

# Create animated entrance
print(f"{MAGENTA}")
print(" " * 20 + "┌───────────────────┐")
print(" " * 20 + "│   Woody Whispers   │")
print(" " * 20 + "└───────────────────┘")
time.sleep(0.8)

print(f"\n{CYAN}")
for _ in range(3):
    print(" " * 15 + "・".join(["◦" for _ in range(10)])
    time.sleep(0.3)

print(TOP_DECOR)
print(GLASSES)
print(colored_box(QUOTE))
print(BOTTOM_DECOR)

# Add playful footer
print(f"\n{BLUE}P.S. Don't worry—{RESET} this philosophical crisis comes with {MAGENTA}free neurosis{RESET}.")
print(f"{BLUE}Just don't blame me when you overthink this.{RESET}")