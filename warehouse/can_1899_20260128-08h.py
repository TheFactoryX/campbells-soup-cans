"""
Campbell's Soup Can #1899
Produced: 2026-01-28 08:50:20
Worker: OpenAI: GPT-4.1 (openai/gpt-4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

quote = (
    "I asked the universe for meaning.\n"
    "It replied with a hold message and recommended I try yoga.\n"
    "I don't even own stretchy pants."
)

# ASCII Woody Allen caricature with glasses
ascii_art = r"""
         ________
        /        \
       |  O    O  |
       |    \/     |
        \  ----  /
         |      |
       /        \
      | |      | |
     (_/        \_)
"""

# ANSI Colors
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BGLIGHT = '\033[107m'
BOLD = '\033[1m'

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, color="", delay=0.022):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay if char != "\n" else delay*5)
    print()

def print_boxed_quote(quote_lines):
    # find width
    max_len = max(len(l) for l in quote_lines)
    pad = 4
    width = max_len + pad
    top = f"{CYAN}{'┌' + '─' * width + '┐'}{RESET}"
    bot = f"{CYAN}{'└' + '─' * width + '┘'}{RESET}"

    print(top)
    for line in quote_lines:
        print(f"{CYAN}│{RESET}  {YELLOW}{line.ljust(max_len)}{RESET}  {CYAN}│{RESET}")
    print(bot)

def animate_blinking_glasses(art, times=4):
    lines = art.splitlines()
    glasses_on = ["O", "O"]
    glasses_off = ["o", "o"]
    frame = lines[:]
    for i in range(times):
        clear()
        cur = glasses_off if i % 2 else glasses_on
        new_lines = lines[:]
        # Find and replace the eyes
        new_lines = []
        for idx, l in enumerate(lines):
            if idx == 3:
                l = l.replace("O    O", f"{cur[0]}    {cur[1]}")
            new_lines.append(l)
        print(f"{BOLD}{CYAN}" + "\n".join(new_lines) + f"{RESET}")
        time.sleep(0.33)
    clear()
    print(f"{BOLD}{CYAN}" + art + RESET)

def main():
    clear()
    print(f"{BOLD}{CYAN}            Woody Allen ponders...{RESET}")
    time.sleep(1)
    animate_blinking_glasses(ascii_art)
    print()
    time.sleep(0.5)
    print_boxed_quote(quote.split('\n'))
    print(f"{BGLIGHT}{CYAN}   — Woody Allen (kind of)   {RESET}\n")
    time.sleep(0.8)
    print(f"{WHITE}{BOLD}Existential advice: Buy stretchy pants. Just in case.{RESET}\n")

if __name__ == '__main__':
    main()