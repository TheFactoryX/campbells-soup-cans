"""
Campbell's Soup Can #5283
Produced: 2026-11-28 02:41:20
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# Woody Allen color palette
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'

# Colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# Backgrounds
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Our neurotic masterpiece
QUOTE = "I told my therapist I want to live forever. He said, 'That's a long commitment — have you considered a gym membership instead?'"

WOODY_ASCII = r"""
      ╭─────────────────────────────────────────────╮
      │  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  │
      │  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█  │
      │  █░  ▄▄▄  ▄▄▄  ▄▄▄▄   ▄▄▄  ▄▄▄▄▄  ▄▄▄  ░█  │
      │  █░ █   █ █   █ █   █ █   █ █     █   █ ░█  │
      │  █░ █   █ █   █ █   █ █   █ █▄▄▄  █   █ ░█  │
      │  █░ █   █ █   █ █   █ █   █ █     █   █ ░█  │
      │  █░  ▀▀▀  ▀▀▀  ▀▀▀▀   ▀▀▀  ▀▀▀▀▀  ▀▀▀  ░█  │
      │  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█  │
      │  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  │
      ╰─────────────────────────────────────────────╯
"""

GLASSES = r"""
         ▄▄▄▄▄▄       ▄▄▄▄▄▄
        ██░░░░██     ██░░░░██
        ██░░░░██     ██░░░░██
        ▀▀▀▀▀▀       ▀▀▀▀▀▀
           \           /
            \         /
             \_______/
"""

THOUGHT_BUBBLE = r"""
      .-""""""""""""""""""""""""""""""""""-.
     /                                      \
    |                                       |
    |                                       |
     \                                      /
      '-....................................-'
"""

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def typewriter(text, delay=0.02, color=WHITE):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rainbow_text(text):
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    result = ""
    for i, char in enumerate(text):
        if char != ' ':
            result += f"{colors[i % len(colors)]}{char}{RESET}"
        else:
            result += ' '
    return result

def pulse_color(text, color, times=3):
    for _ in range(times):
        print(f"\r{color}{BOLD}{text}{RESET}", end='', flush=True)
        time.sleep(0.3)
        print(f"\r{DIM}{text}{RESET}", end='', flush=True)
        time.sleep(0.3)
    print(f"\r{color}{BOLD}{text}{RESET}")

def animate_entrance():
    clear_screen()
    hide_cursor()
    
    # Draw the frame slowly
    lines = WOODY_ASCII.strip('\n').split('\n')
    for i, line in enumerate(lines):
        move_cursor(i + 2, 5)
        color = CYAN if i % 2 == 0 else BLUE
        typewriter(line, 0.001, color)
        time.sleep(0.02)
    
    # Draw glasses
    glasses_lines = GLASSES.strip('\n').split('\n')
    for i, line in enumerate(glasses_lines):
        move_cursor(i + 2, 55)
        typewriter(line, 0.001, YELLOW)
        time.sleep(0.03)
    
    time.sleep(0.5)

def animate_quote():
    # Position for quote
    quote_row = 15
    quote_col = 10
    
    # Draw thought bubble
    bubble_lines = THOUGHT_BUBBLE.strip('\n').split('\n')
    for i, line in enumerate(bubble_lines):
        move_cursor(quote_row + i, quote_col)
        typewriter(line, 0.001, MAGENTA)
    
    # Type the quote inside bubble
    move_cursor(quote_row + 2, quote_col + 3)
    
    words = QUOTE.split(' ')
    line = ""
    line_count = 0
    max_width = 55
    
    for word in words:
        test_line = line + word + " "
        if len(test_line) > max_width and line:
            move_cursor(quote_row + 2 + line_count, quote_col + 3)
            typewriter(line.strip(), 0.015, BRIGHT_WHITE)
            line = word + " "
            line_count += 1
        else:
            line = test_line
    
    if line:
        move_cursor(quote_row + 2 + line_count, quote_col + 3)
        typewriter(line.strip(), 0.015, BRIGHT_WHITE)
    
    time.sleep(1)

def animate_signature():
    sig_row = 25
    sig_col = 35
    move_cursor(sig_row, sig_col)
    
    signature = "— Woody Allen (probably, maybe, I'm not sure, don't quote me on that)"
    typewriter(signature, 0.02, GRAY)
    
    time.sleep(0.5)
    
    # Add some neurotic footnotes
    footnotes = [
        "P.S. My therapist says I have 'commitment issues' with mortality.",
        "P.P.S. I'd join a gym but the towels smell like existential dread.",
        "P.P.P.S. Also, I left the oven on. Or was that a metaphor?"
    ]
    
    for i, note in enumerate(footnotes):
        move_cursor(sig_row + 2 + i, sig_col)
        typewriter(note, 0.01, DIM + ITALIC + CYAN)
        time.sleep(0.3)

def finale_animation():
    # Rainbow pulse on the quote
    move_cursor(30, 5)
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    for _ in range(2):
        for color in colors:
            move_cursor(30, 5)
            print(f"{color}{BOLD}{'═' * 60}{RESET}", end='', flush=True)
            time.sleep(0.08)
    
    move_cursor(31, 15)
    final_msg = "Life is divided into the horrible and the miserable. This was the miserable part. Enjoy!"
    typewriter(final_msg, 0.02, BRIGHT_YELLOW + BOLD)
    
    move_cursor(33, 20)
    typewriter("Press Ctrl+C to confront the void...", 0.03, DIM + BLINK + RED)

def main():
    try:
        animate_entrance()
        animate_quote()
        animate_signature()
        finale_animation()
        
        # Keep alive for a bit
        time.sleep(3)
        
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_screen()
        # One last neurotic goodbye
        print(f"\n{CYAN}{BOLD}")
        print("    ╔════════════════════════════════════════════════════════════╗")
        print("    ║  \"I don't want to achieve immortality through my work;    ║")
        print("    ║   I want to achieve it through not dying.\"                 ║")
        print("    ║                                                              ║")
        print("    ║                    — The Real Woody Allen                    ║")
        print("    ╚════════════════════════════════════════════════════════════╝")
        print(f"{RESET}\n")

if __name__ == "__main__":
    main()