"""
Campbell's Soup Can #2249
Produced: 2026-02-15 21:39:52
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, os, time, random

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    sys.stdout.write("\n" * 5)
    sys.stdout.flush()

def colorful_header(text):
    for word in text.split():
        fg = random.choice([30,31,32,33,34,35,36,37])
        bg = random.choice([40,41,42,43,44,45,46,47])
        sys.stdout.write(f"\x1b[{fg};{bg}m{word}\x1b[0m ")
    sys.stdout.flush()
    time.sleep(0.5)

def ascii_art():
    art = '''
   __
  /  \
  (    )   |___
   \__/   /   |
         /   |
        /____|
'''
    for i, line in enumerate(art.splitlines()):
        bg = 40 + i % 8
        sys.stdout.write(f"\x1b[38;5;{bg}m{line}\x1b[0m\n")
    sys.stdout.flush()
    time.sleep(0.4)

def print_boxed(message):
    border = "─"
    width = len(message)
    top = f"╭{border * width}╮"
    middle = f"│{message}│"
    bottom = f"╰{border * width}╯"

    # Flicker animation
    for _ in range(10):
        fg_top   = random.choice([30,31,32,33,34,35,36,37])
        bg_top   = random.choice([40,41,42,43,44,45,46,47])
        fg_mid   = random.choice([30,31,32,33,34,35,36,37])
        bg_mid   = random.choice([40,41,42,43,44,45,46,47])
        fg_bot   = random.choice([30,31,32,33,34,35,36,37])
        bg_bot   = random.choice([40,41,42,43,44,45,46,47])
        style_top = f"\x1b[{fg_top};{bg_top}m"
        style_mid = f"\x1b[{fg_mid};{bg_mid}m"
        style_bot = f"\x1b[{fg_bot};{bg_bot}m"
        reset = "\x1b[0m"
        sys.stdout.write(style_top + top + reset + "\n")
        sys.stdout.write(style_mid + middle + reset + "\n")
        sys.stdout.write(style_bot + bottom + reset + "\n")
        sys.stdout.flush()
        time.sleep(0.07)

    # Final steady box
    sys.stdout.write("\x1b[31;40m" + top + "\x1b[0m\n")
    sys.stdout.write("\x1b[33;44m" + middle + "\x1b[0m\n")
    sys.stdout.write("\x1b[35;46m" + bottom + "\x1b[0m\n")
    sys.stdout.flush()

def rainbow_print(text):
    sys.stdout.write("\x1b[1m")
    for c in text:
        fg = random.choice([30,31,32,33,34,35,36,37])
        bg = random.choice([40,41,42,43,44,45,46,47])
        sys.stdout.write(f"\x1b[{fg};{bg}m{c}\x1b[0m")
        sys.stdout.flush()
        time.sleep(0.025)
    sys.stdout.write("\x1b[0m\n")
    sys.stdout.flush()

def main():
    clear_screen()
    colorful_header("Woody Allen's Existential Comedy")
    ascii_art()
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print_boxed(quote)
    rainbow_print(quote)
    sys.stdout.write("Press Enter to exit...")
    sys.stdout.flush()
    sys.stdin.read(1)

if __name__ == "__main__":
    main()