"""
Campbell's Soup Can #2636
Produced: 2026-03-08 07:01:24
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import textwrap
import time

# ANSI color codes for terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Woody Allen style quote (neurotic, self-deprecating, philosophical)
QUOTE = "I don't want to achieve immortality through my work; I want to achieve it through not dying. But then I remember I'm already dead, and that's just a theory."

# Format with a decorative frame
BOX_WIDTH = 80
TOP_BORDER = f"{RED}╔{'═' * (BOX_WIDTH - 2)}╗{RESET}"
BOTTOM_BORDER = f"{RED}╚{'═' * (BOX_WIDTH - 2)}╝{RESET}"

# Wrap the quote to fit within the box
wrapped_quote = textwrap.wrap(QUOTE, width=BOX_WIDTH - 4)
full_text = "\n".join(wrapped_quote)

# Print animated ASCII art header
print(f"\n{YELLOW}   .-\"\"\"-.\n  /        \\\n /          \\\n|  \\    /  \\  |\n|    \\__/    |\n \\          / \n  \\        / \n   \\______/  \n{RESET}")

# Print top border with animated "loading" effect
print(TOP_BORDER)
for _ in range(3):
    print(f"{RED}║{YELLOW}{' ' * (BOX_WIDTH - 4)}{RED}║{RESET}")
    time.sleep(0.1)
    print(f"\033[1A\033[K{RED}║{YELLOW}{' ' * (BOX_WIDTH - 4)}{RED}║{RESET}")
    time.sleep(0.1)
print(f"{RED}║{YELLOW}{' ' * (BOX_WIDTH - 4)}{RED}║{RESET}")

# Print quote character by character with typing effect
print(GREEN, end='')
for char in full_text:
    print(char, end='', flush=True)
    time.sleep(0.03 if char.isalnum() else 0.07)
print(RESET)

# Print bottom border with "philosophical" flourish
print(BOTTOM_BORDER)
print(f"{YELLOW}  I'm not dead yet, but I've been working on the concept for 30 years.{RESET}")

# Final animated sparkles
print("\033[1A\033[K" + " " * (BOX_WIDTH - 2))
for _ in range(4):
    print(f"\033[1A\033[K{YELLOW}{' ' * (BOX_WIDTH // 2 - 1)}*{RESET}", end='')
    time.sleep(0.2)
    print(f"\033[1A\033[K{YELLOW}{' ' * (BOX_WIDTH // 2 - 1)}*{RESET}", end='')
    time.sleep(0.2)
print(f"{YELLOW}{' ' * (BOX_WIDTH // 2 - 1)}*{RESET}")