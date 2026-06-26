"""
Campbell's Soup Can #4022
Produced: 2026-06-26 22:36:37
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def animate_print(s, delay=0.05):
    """Print the string character by character with a slight delay."""
    for ch in s:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    # ANSI color codes
    GREEN = '\033[1;32m'   # bright green
    CYAN = '\033[1;36m'    # bright cyan
    YELLOW = '\033[1;33m'  # bright yellow (unused but kept for mood)
    RESET = '\033[0m'      # reset all formatting

    inner_len = 90  # width of the box interior

    # The philosophical quote in Woody Allen's characteristic style
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    quote_display = f'"{quote}"'
    centered_quote = quote_display.center(inner_len)

    author = '- Woody Allen'
    centered_author = author.center(inner_len)

    # Build the box elements
    top_border = f"{GREEN}+{'-'*inner_len}+{RESET}"
    bottom_border = top_border  # same as top for a plain box

    line1 = f"{GREEN}|{CYAN}{centered_quote}{GREEN}|{RESET}"
    line2 = f"{GREEN}|{' '*inner_len}{GREEN}|{RESET}"  # empty separator line
    line3 = f"{GREEN}|{CYAN}{centered_author}{GREEN}|{RESET}"

    # Animate the appearance of the whole box
    animate_print(top_border)
    animate_print(line1)
    animate_print(line2)
    animate_print(line3)
    animate_print(bottom_border)

if __name__ == "__main__":
    main()