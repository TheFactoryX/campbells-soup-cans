"""
Campbell's Soup Can #3493
Produced: 2026-04-29 04:03:14
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import textwrap

# ANSI Escape Codes for formatting and colors
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
CLEAR_SCREEN = '\033[2J\033[H'  # Clears terminal and moves cursor to top-left

def typewriter(text, delay=0.03, prefix='', suffix='', end='\n'):
    """Prints text with a retro typewriter animation, one character at a time."""
    print(prefix, end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(suffix, end='', flush=True)
    print(end, end='', flush=True)

if __name__ == '__main__':
    # Start with a fresh, cleared terminal
    print(CLEAR_SCREEN, end='', flush=True)

    # Header
    header = "WOODY ALLEN'S EXISTENTIAL QUOTE OF THE DAY"
    print(f'{BOLD}{YELLOW}{header.center(64)}{RESET}\n')

    # The Quote: Neurotic, self-deprecating, existential, very Woody
    quote = (
        "I told my therapist I was having an existential crisis. He said, "
        "'You’re just paying $250 an hour to catastrophize about nothing.' "
        "Which is a relief, because now I’m anxious about the invoice instead "
        "of the void—so that’s progress, right? I mean, at least the void "
        "doesn’t send a monthly statement with a late fee if you miss the meaning of life."
    )
    attribution = "— Woody Allen (unverified; I can’t afford a fact-checker)"

    # ASCII Box Settings (works on all terminals)
    box_width = 64
    inner_width = 60  # Space for text between box borders
    box_top = '+' + '-' * (box_width - 2) + '+'
    box_bottom = '+' + '-' * (box_width - 2) + '+'
    left_border = '|'
    right_border = '|'

    # Print box top
    print(box_top)

    # Wrap quote to fit inside the box
    wrapped_lines = textwrap.wrap(quote, width=inner_width)

    # Print each line of the quote with typewriter effect inside the box
    for line in wrapped_lines:
        # Left border + 1 space
        print(f'{left_border} ', end='', flush=True)
        # Typewrite only the visible text (no padding) in cyan
        typewriter(line, delay=0.03, prefix=CYAN, suffix=RESET, end='')
        # Instantly add padding spaces to fill the inner box width
        padding = ' ' * (inner_width - len(line))
        print(padding, end='', flush=True)
        # Right border + 1 space
        print(f' {right_border}')

    # Print box bottom
    print(box_bottom + '\n')

    # Print attribution, centered in yellow bold
    print(f'{BOLD}{YELLOW}{attribution.center(64)}{RESET}\n')

    # Brief "typing cursor" effect at the end
    print(f'{CYAN}_', end='', flush=True)
    time.sleep(1)
    print('\b ', end='', flush=True)  # Erase cursor after 1 second