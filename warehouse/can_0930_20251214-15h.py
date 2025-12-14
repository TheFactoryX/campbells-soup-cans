"""
Campbell's Soup Can #930
Produced: 2025-12-14 15:31:10
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

# Woody Allen's Philosophical Quote Generator
# A visually playful presentation with ANSI colors and ASCII art

RESET = '\033[0m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'

def colored_text(text, color):
    return f"{color}{BOLD}{text}{RESET}"

# ASCII art of Woody's iconic glasses
woody_glasses = r"""
     /\_/\  
    ( ´·ᴥ·｀ )
     > ^ <
"""

# Philosophical quote in Woody Allen's style
quote = "The only thing standing between me and eternal happiness is every single decision I've ever made."

# Create a fancy bordered box
box_width = 60
horizontal_border = '╔' + '═' * (box_width - 2) + '╗'
inner_border = '║' + ' ' * (box_width - 2) + '║'

print(colored_text(woody_glasses, CYAN))

print(colored_text(horizontal_border, RED))
print(f"{RED}║{YELLOW}{' ' * (box_width - 4)}{RESET}{RED}║{RESET}")
print(f"{RED}║{YELLOW}{quote.center(box_width - 4)}{RESET}{RED}║{RESET}")
print(f"{RED}║{YELLOW}{' ' * (box_width - 4)}{RESET}{RED}║{RESET}")
print(colored_text(horizontal_border, RED))

print(colored_text("\n- Woody Allen (probably)", BLUE))