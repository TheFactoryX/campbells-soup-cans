"""
Campbell's Soup Can #78
Produced: 2025-11-05 18:43:59
Worker: Qwen: Qwen2.5 VL 32B Instruct (free) (qwen/qwen2.5-vl-32b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Woody Allen Style Philosophical Quote Generator

A neurotic, funny, self-deprecating existential quote in Woody Allen's style.

- Uses ANSI escape codes for colors
- Features creative text layout and ASCII art
"""

# ANSI Color Codes (make this visually interesting!)
RESET = "\033[0m"
WHITE = "\033[1;37m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"

# ASCII Art Frame for the Quote
BOX_TOP = f"   {'*' * 46}"
BOX_LINE = f"  {CYAN}*{' ' * 44}*{RESET}"
BOX_BOTTOM = f"   {'*' * 46}"

# Woody Allen Style Quote
WOODY_QUOTE = """
    Life's like a giant, chaotic theater with me playing Hamlet in
    my underwear, desperately asking, "To be, or not to be?" while 
    forgetting my lines and hoping nobody notices I'm not wearing pants.
"""

# Main Code
def display_quote():
    """Displays the Woody Allen-style quote in a visually interesting way."""
    print(f"{BOX_TOP}\n")
    for line in WOODY_QUOTE.split("\n"):
        if line.strip().startswith("To be,"):
            # Make this line stand out with color and emphasis
            print(f"{BOX_LINE}\n{WHITE}{' ' * 8}{line.strip().replace('To be', f'{GREEN}{MAGENTA}To be{RESET}')}{' ' * 8}\n{BOX_LINE}")
        else:
            print(f"{BOX_LINE}\n{WHITE}{' ' * 8}{line.strip()}{' ' * 8}\n{BOX_LINE}")
    print(f"\n{BOX_BOTTOM}")
    print("\n" + " " * 20 + f"{RED}— Woody Allen (sort of){RESET}")


# Run the Program
if __name__ == "__main__":
    display_quote()