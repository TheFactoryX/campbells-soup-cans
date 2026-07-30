"""
Campbell's Soup Can #4379
Produced: 2026-07-30 16:49:46
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import math

# ANSI escape codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSED = '\033[7m'
RESET = '\033[0m'

def clear_screen():
    print('\033[2J\033[H', end='')

def slow_print(text, color=BOLD, delay=0.025):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_frame_line(char, width, color):
    print(f"{color}{char * width}{RESET}")

def print_centered(text, width, color=BOLD):
    lines = text.split('\n')
    for line in lines:
        padding = max(0, (width - len(line)) // 2)
        print(f"{color}{' ' * padding}{line}{RESET}")

def print_woody_head():
    art = f"""
{RED}          __
{RED}         /  \\      _{WHITE}~_{RED}_
{RED}        / .. \\    / {WHITE}·   ·{RED} \\
{RED}       | (--) |   | {WHITE}  ◯   {RED}  |
{RED}        \\ .. /    {DIM}\\_ ◯ _/{RESET}
{RED}         \\__/      {DIM}  ||  {RESET}
{RED}                     {DIM} ||  {RESET}
{RED}               {DIM}    ..::.{RESET}
"""
    print(art)

def print_quote_box(quote, author):
    width = 68
    horizontal = '═'
    vertical = '║'
    corner_tl = '╔'
    corner_tr = '╗'
    corner_bl = '╚'
    corner_br = '╝'
    tee_left = '╠'
    tee_right = '╣'
    tee_top = '╦'
    tee_bottom = '╩'

    def colored_border(s, c=CYAN):
        return f"{BOLD}{c}{s}{RESET}"

    print()
    print(colored_border(corner_tl + horizontal * (width - 2) + corner_tr))
    print(colored_border(vertical + ' ' * (width - 2) + vertical))

    title = "  🌌  DEEP THOUGHTS FROM THE ABYSS  🌌  "
    pad_left = (width - 2 - len(title)) // 2
    pad_right = width - 2 - len(title) - pad_left
    print(colored_border(vertical + ' ' * pad_left + BOLD + YELLOW + title + RESET + ' ' * pad_right + vertical))

    print(colored_border(tee_left + horizontal * (width - 2) + tee_right))
    print(colored_border(vertical + ' ' * (width - 2) + vertical))

    # Quote text with quotation marks
    print(colored_border(vertical + f"  {GREEN}\"{RESET}", end=''))
    remaining = width - 2 - 4 - len(f'"') - 2
    slow_print(quote[:remaining], MAGENTA, 0.015)

    quote_rest = ""
    words = quote.split()
    current_line = ''
    for word in words:
        test = current_line + (' ' if current_line else '') + word
        if len(test) > width - 8:
            print(colored_border(vertical + ' ' * 3 + f"{RESET}{GREEN}{BOLD}{current_line}{RESET}", end=''))
            print()
            current_line = word
        else:
            current_line = test
    if current_line:
        print(colored_border(vertical + ' ' * 3 + f"{RESET}{GREEN}{BOLD}{current_line}{RESET}", end=''))
        print()

    print(colored_border(vertical + f"{' ' * (width - 3 + 1)}\"{RESET}{GREEN}{RESET}" + ' ' * (width - 2 - (width - 3 + 1) - 1) + vertical))

    print(colored_border(vertical + ' ' * (width - 2) + vertical))

    # Author
    author_text = f"  — {YELLOW}{BOLD}{author}{RESET}"
    print(colored_border(vertical + ' ' * ((width - 2 - len(author_text)) // 2) + author_text + ' ' * (width - 2 - len(author_text) - (width - 2 - len(author_text)) // 2) + vertical))
    print(colored_border(vertical + ' ' * (width - 2) + vertical))

    print(colored_border(tee_left + horizontal * (width - 2) + tee_right))
    print(colored_border(vertical + ' ' * (width // 2 - 10) + f"{DIM}{WHITE}🍂  Contemplate your existence  🍂{RESET}" + ' ' * (width // 2 - 12) + vertical))
    print(colored_border(vertical + ' ' * (width - 2) + vertical))
    print(colored_border(corner_bl + horizontal * (width - 2) + corner_br))

def print_reflection(quote):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    lines = quote.split()
    print(f"\n{DIM}")
    for i, word in enumerate(lines):
        c = colors[i % len(colors)]
        reflected = word[::-1]
        print(f"  {c}{'  ' * i}{reflected}{DIM}")
    print(RESET)

def print_philosophical_punchlines():
    punchlines = [
        f"\n  {YELLOW}{BOLD}   🌀 The universe is indifferent. So am I, mostly. 🌀{RESET}",
        f"\n  {CYAN}     \"I have succeeded in life by never making a decision{RESET}",
        f"      {CYAN}      I could regret. That's called 'strategic paralysis.'\"{RESET}",
        f"\n  {BLINK}{RED}      💀 We are all just suspended between meaning and absurdity 💀{RESET}",
    ]
    for p in punchlines:
        slow_print(p, WHITE, 0.02)
        time.sleep(0.3)

def print_ascii_mirror():
    mirror = f"""
{DIM}
         ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
       ~  Everything is meaningless  ~
     ~   except for this quote, somehow   ~
   ~    ...or maybe it isn't either    ~
 ~      ¯\\_(ツ)_/¯  ...literally     ~
       ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
{RESET}
"""
    print(mirror)

def main():
    clear_screen()

    # Title animation
    title = "✦  W O O D Y  A L L E N  ' S  C O N S O L E  ✦"
    for i in range(len(title) + 1):
        sys.stdout.write(f"\r{BOLD}{YELLOW}{title[:i]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.015)
    print()

    time.sleep(0.3)

    # Woody ASCII art
    print_woody_head()
    time.sleep(0.3)

    # Decorative line
    print(f"\n{BOLD}{CYAN}{'─' * 68}{RESET}")
    print_centered(f"{BOLD}{RED}⚠  WARNING: EXISTENTIAL CONTENT AHEAD  ⚠{RESET}", 68, RED)
    print(f"{BOLD}{CYAN}{'─' * 68}{RESET}")
    print()

    # The quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "Woody Allen (with neurotic additions)"

    print_quote_box(quote, author)

    time.sleep(0.4)

    # Reflection effect
    print_reflection(quote)

    time.sleep(0.3)

    # Bonus ASCII mirror
    print_ascii_mirror()

    time.sleep(0.3)

    # Final punchlines
    print_philosophical_punchlines()

    # Closing
    print(f"\n{BOLD}{DIM}{'~' * 68}{RESET}")
    slow_print(f"\n  {BLUE}Remember: The meaning of life is that there is no meaning.{RESET}", CYAN, 0.02)
    slow_print(f"  {BLUE}  But at least we have good haircuts and neuroses.{RESET}", CYAN, 0.02)
    print(f"\n  {DIM}{'~' * 68}{RESET}")
    print()
    slow_print(f"  {GREEN}{BOLD}Thank you for contemplating the void with me. 🍂{RESET}", GREEN, 0.02)
    print(f"\n  {DIM}  (Press Enter to exit...){RESET}", end='')
    input()

if __name__ == "__main__":
    main()