"""
Campbell's Soup Can #4372
Produced: 2026-07-29 23:15:53
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

# Woody Allen quotes (original, in his neurotic style)
QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
    "My one regret in life is that I am not someone else.",
    "I don't believe in an afterlife, although I am bringing a change of underwear.",
    "The talent for being happy is appreciating and liking what you have, instead of what you don't have. Which is why I'm miserable.",
    "I'm not afraid of death. I just don't want to be there when it happens. Or have to pay for parking.",
    "Life is divided into the horrible and the miserable. The horrible are terminal cases. The miserable is everyone else. I'm both.",
    "I failed to make the chess team because of my height. They said I couldn't see the board. I told them I play by mail.",
    "There is no question that there is an unseen world. The problem is, how far is it from midtown? And is parking available?",
    "I have bad reflexes. I was once run over by a car being pushed by two guys.",
    "Money is better than poverty, if only for financial reasons. But it doesn't buy happiness. It buys a better class of misery.",
    "I don't want to achieve immortality through my work. I want to achieve it through not dying. Or at least a really good moisturizer.",
    "The food here is terrible. And such small portions! That's essentially my philosophy of existence.",
    "I'm at two with nature. Which is one better than being at one, because then you have a backup.",
    "If only God would give me some clear sign! Like making a large deposit in my name at a Swiss bank.",
    "I spent a year in philosophy class proving that I don't exist. The professor gave me a C. He said my logic was sound but my attendance was imaginary.",
]

# ANSI colors
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"

# Foreground colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

def clear_screen():
    print("\033[2J\033[H", end="")

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

def move_cursor(row, col):
    print(f"\033[{row};{col}H", end="")

def get_terminal_size():
    try:
        import os
        size = os.get_terminal_size()
        return size.columns, size.lines
    except:
        return 80, 24

def typewriter_effect(text, color=WHITE, delay=0.03, newline=True):
    for char in text:
        print(f"{color}{char}{RESET}", end="", flush=True)
        time.sleep(delay)
    if newline:
        print()

def fade_in_text(text, color=WHITE, steps=10):
    for i in range(steps + 1):
        alpha = i / steps
        r = int(255 * alpha)
        g = int(255 * alpha)
        b = int(255 * alpha)
        print(f"\r\033[38;2;{r};{g};{b}m{text}\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()

def draw_box(width, height, title="", color=CYAN):
    top = f"{color}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{color}╚{'═' * (width - 2)}╝{RESET}"
    middle = f"{color}║{' ' * (width - 2)}║{RESET}"
    
    print(top)
    if title:
        padding = (width - 2 - len(title)) // 2
        title_line = f"{color}║{RESET}{' ' * padding}{BOLD}{title}{RESET}{' ' * (width - 2 - padding - len(title))}{color}║{RESET}"
        print(title_line)
        print(middle)
    for _ in range(height - 3 if title else height - 2):
        print(middle)
    print(bottom)

def animate_woody_face():
    frames = [
        r"""
    (o.o)
    ( v )
   /     \
  |  ___  |
   \_____/
        """,
        r"""
    (-.-)
    ( v )
   /     \
  |  ___  |
   \_____/
        """,
        r"""
    (o.o)
    ( v )
   /     \
  |  ___  |
   \_____/
        """,
        r"""
    (O.O)
    ( v )
   /     \
  |  ___  |
   \_____/
        """,
    ]
    return frames

def main():
    hide_cursor()
    clear_screen()
    
    cols, rows = get_terminal_size()
    quote = random.choice(QUOTES)
    
    # Ensure we have enough space
    box_width = min(70, cols - 4)
    box_height = 12
    
    # Center position
    start_row = max(1, (rows - box_height) // 2)
    start_col = max(1, (cols - box_width) // 2)
    
    # Move to start position and draw box
    move_cursor(start_row, start_col)
    
    # Draw decorative top
    print(f"{BRIGHT_MAGENTA}{'✦' * (box_width // 2)}{RESET}")
    move_cursor(start_row + 1, start_col)
    
    # Title box
    title_lines = [
        f"{BRIGHT_YELLOW}┌{'─' * (box_width - 2)}┐{RESET}",
        f"{BRIGHT_YELLOW}│{RESET}{BRIGHT_CYAN}{BOLD}{' WOODY ALLEN SIMULATOR v1.0 '.center(box_width - 2)}{RESET}{BRIGHT_YELLOW}│{RESET}",
        f"{BRIGHT_YELLOW}│{RESET}{BRIGHT_BLACK}{' Neurotic Philosophy Division '.center(box_width - 2)}{RESET}{BRIGHT_YELLOW}│{RESET}",
        f"{BRIGHT_YELLOW}└{'─' * (box_width - 2)}┘{RESET}",
    ]
    
    for i, line in enumerate(title_lines):
        move_cursor(start_row + 1 + i, start_col)
        print(line)
    
    # Woody face animation
    face_frames = animate_woody_face()
    face_row = start_row + 6
    for frame_idx in range(8):  # 2 cycles
        frame = face_frames[frame_idx % len(face_frames)]
        for line_idx, line in enumerate(frame.strip().split('\n')):
            move_cursor(face_row + line_idx, start_col + (box_width - 18) // 2)
            print(f"{BRIGHT_GREEN}{line}{RESET}")
        time.sleep(0.3)
    
    # Clear face area and show quote
    quote_row = face_row
    for i in range(6):
        move_cursor(quote_row + i, start_col)
        print(" " * box_width)
    
    # Typewriter quote
    move_cursor(quote_row, start_col + 2)
    print(f"{BRIGHT_WHITE}{'\"'}{RESET}", end="", flush=True)
    
    # Word by word for more dramatic effect
    words = quote.split()
    x_pos = start_col + 3
    y_pos = quote_row
    
    for word_idx, word in enumerate(words):
        move_cursor(y_pos, x_pos)
        for char in word:
            print(f"{BRIGHT_YELLOW}{char}{RESET}", end="", flush=True)
            x_pos += 1
            time.sleep(0.02)
        # Space after word
        print(f"{BRIGHT_YELLOW} {RESET}", end="", flush=True)
        x_pos += 1
        # Check if we need to wrap
        if x_pos > start_col + box_width - 4:
            y_pos += 1
            x_pos = start_col + 3
    
    print(f"{BRIGHT_WHITE}\"{RESET}")
    
    # Decorative bottom
    move_cursor(quote_row + 3, start_col)
    print(f"{BRIGHT_MAGENTA}{'✦' * (box_width // 2)}{RESET}")
    
    # Footer
    move_cursor(quote_row + 4, start_col)
    footer = f"{DIM}{ITALIC}* existential crisis not included *{RESET}"
    padding = (box_width - len(footer) + 9) // 2  # +9 for ANSI codes
    print(" " * padding + footer)
    
    # Signature
    move_cursor(quote_row + 5, start_col)
    sig = f"{BRIGHT_BLACK}— Woody (probably){RESET}"
    padding = (box_width - len(sig) + 9) // 2
    print(" " * padding + sig)
    
    # Final sparkle animation
    for _ in range(3):
        for i in range(box_width):
            move_cursor(start_row, start_col + i)
            print(f"{BRIGHT_CYAN}✦{RESET}", end="", flush=True)
            move_cursor(quote_row + 3, start_col + i)
            print(f"{BRIGHT_CYAN}✦{RESET}", end="", flush=True)
            time.sleep(0.01)
        for i in range(box_width):
            move_cursor(start_row, start_col + i)
            print(f"{BRIGHT_MAGENTA}✦{RESET}", end="", flush=True)
            move_cursor(quote_row + 3, start_col + i)
            print(f"{BRIGHT_MAGENTA}✦{RESET}", end="", flush=True)
            time.sleep(0.01)
    
    move_cursor(rows, 1)
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f"\n{RED}Existence interrupted. Typical.{RESET}\n")
    except Exception as e:
        show_cursor()
        print(f"\n{RED}Error: {e}{RESET}")
        print(f"{YELLOW}Even my code has neuroses.{RESET}\n")