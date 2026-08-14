"""
Campbell's Soup Can #4593
Produced: 2026-08-14 23:36:31
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
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
BRIGHT_BLACK = '\033[90m'
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

WOODY_QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\n"
    "It involves Russia."
)

WOODY_ASCII = r"""
      .--.
     /    \
    |  @@  |   <<< Neurotic Intellectual
    |  \/  |
     \____/
      |  |
     _|  |_
    (______)
"""

THOUGHT_BUBBLE = r"""
        .-^-.
       /     \
      |  :)   |
       \  ^  /
        '---'
"""

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=WHITE, delay=0.03, newline=True):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def fade_in(text, color=WHITE, steps=10):
    for i in range(steps + 1):
        intensity = i / steps
        r = int(255 * intensity)
        g = int(255 * intensity)
        b = int(255 * intensity)
        print(f"\r\033[38;2;{r};{g};{b}m{text}{RESET}", end='', flush=True)
        time.sleep(0.02)
    print()

def rainbow_text(text):
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    result = ""
    for i, char in enumerate(text):
        if char != ' ' and char != '\n':
            result += f"{colors[i % len(colors)]}{char}{RESET}"
        else:
            result += char
    return result

def draw_box(content_lines, border_color=CYAN, title="", title_color=YELLOW):
    max_len = max(len(line) for line in content_lines)
    if title:
        max_len = max(max_len, len(title) + 4)
    
    top = f"{border_color}╔{'═' * (max_len + 2)}╗{RESET}"
    bottom = f"{border_color}╚{'═' * (max_len + 2)}╝{RESET}"
    
    print(top)
    if title:
        title_line = f"{border_color}║{RESET} {title_color}{BOLD}{title.center(max_len)}{RESET} {border_color}║{RESET}"
        print(title_line)
        print(f"{border_color}╠{'═' * (max_len + 2)}╣{RESET}")
    
    for line in content_lines:
        padding = max_len - len(line)
        print(f"{border_color}║{RESET} {line}{' ' * padding} {border_color}║{RESET}")
    
    print(bottom)

def animate_woody_entrance():
    frames = [
        r"""
            \
             \
              \
               \
                \
                 \
                  \
                   \
                    \
                     \
                      \
                       \
                        \
                         \
                          \
                           \
                            \
        """,
        r"""
                        \
                         \
                          \
                           \
                            \
                             \
                              \
                               \
                                \
                                 \
                                  \
                                   \
                                    \
                                     \
                                      \
                                       \
                                        \
                                         \
                                          \
        """,
        r"""
                                                  \
                                                   \
                                                    \
                                                     \
                                                      \
                                                       \
                                                        \
                                                         \
                                                          \
                                                           \
                                                            \
                                                             \
                                                              \
                                                               \
                                                                \
                                                                 \
                                                                  \
        """,
    ]
    
    for frame in frames:
        clear_screen()
        print(f"{CYAN}{frame}{RESET}")
        time.sleep(0.15)

def main():
    hide_cursor()
    try:
        # Entrance animation
        animate_woody_entrance()
        
        clear_screen()
        
        # Draw Woody ASCII
        print(f"{MAGENTA}{BOLD}{WOODY_ASCII}{RESET}")
        time.sleep(0.5)
        
        # Typewriter the quote
        print(f"{CYAN}{'─' * 60}{RESET}")
        print()
        
        lines = WOODY_QUOTE.split('\n')
        for i, line in enumerate(lines):
            if i == 0:
                typewriter(line, YELLOW, delay=0.04)
            else:
                typewriter(line, BRIGHT_YELLOW, delay=0.05)
        
        print()
        print(f"{CYAN}{'─' * 60}{RESET}")
        print()
        
        # Thought bubble with existential follow-up
        followup = "Also, my analyst says I have a preoccupation with mortality.\nI told him, 'Doc, at my age, it's not a preoccupation.\nIt's a hobby.'"
        
        bubble_lines = [
            "  .-^-.",
            " /     \\",
            "|  💭  |",
            " \\     /",
            "  '---' "
        ]
        
        print(f"{BRIGHT_MAGENTA}{ITALIC}")
        for bline in bubble_lines:
            print(bline)
            time.sleep(0.1)
        print(f"{RESET}")
        
        typewriter(followup, BRIGHT_CYAN, delay=0.02)
        print()
        
        # Final box with "signature"
        draw_box([
            f"{ITALIC}— Woody Allen (probably){RESET}",
            f"{DIM}Delivered by a Python script having an existential crisis{RESET}"
        ], border_color=MAGENTA, title=" CERTIFIED NEUROTIC ", title_color=BRIGHT_YELLOW)
        
        # Sparkle effect at the end
        print()
        sparkles = ["✦", "✧", "★", "☆", "✦", "✧"]
        for _ in range(3):
            for sparkle in sparkles:
                print(f"\r{BRIGHT_YELLOW}{sparkle} {RESET}Thanks for listening to my internal monologue{BRIGHT_YELLOW} {sparkle}{RESET}", end='', flush=True)
                time.sleep(0.2)
        print()
        print()
        
    finally:
        show_cursor()

if __name__ == "__main__":
    main()