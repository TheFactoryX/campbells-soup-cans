"""
Campbell's Soup Can #4195
Produced: 2026-07-14 15:48:23
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

# Bright colors
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

# Cursor control
CLEAR_SCREEN = '\033[2J'
CURSOR_HOME = '\033[H'
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'
MOVE_UP = '\033[1A'
CLEAR_LINE = '\033[2K'

WOODY_QUOTE = (
    "I'm not afraid of death. "
    "I just don't want to be conscious "
    "for the Yelp reviews."
)

WOODY_ATTR = "— Woody Allen (probably)"

# ASCII art frame elements
TL = '╭'
TR = '╮'
BL = '╰'
BR = '╯'
H = '─'
V = '│'
TL_BOLD = '┏'
TR_BOLD = '┓'
BL_BOLD = '┗'
BR_BOLD = '┛'
H_BOLD = '━'
V_BOLD = '┃'

def clear_screen():
    sys.stdout.write(CLEAR_SCREEN + CURSOR_HOME)
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write(CURSOR_HIDE)
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write(CURSOR_SHOW)
    sys.stdout.flush()

def typewriter_print(text, color=WHITE, delay=0.03, end='\n'):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    if end:
        sys.stdout.write(end)
        sys.stdout.flush()

def gradient_text(text, colors, delay=0.02):
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def draw_frame(width, height, title="", color=CYAN):
    lines = []
    # Top border
    top = f"{color}{TL_BOLD}{H_BOLD * (width - 2)}{TR_BOLD}{RESET}"
    if title:
        title_str = f" {title} "
        pos = (width - len(title_str)) // 2
        top = f"{color}{TL_BOLD}{H_BOLD * pos}{RESET}{BOLD}{YELLOW}{title_str}{RESET}{color}{H_BOLD * (width - 2 - pos - len(title_str))}{TR_BOLD}{RESET}"
    lines.append(top)
    
    # Middle lines
    for _ in range(height - 2):
        lines.append(f"{color}{V_BOLD}{RESET}{' ' * (width - 2)}{color}{V_BOLD}{RESET}")
    
    # Bottom border
    lines.append(f"{color}{BL_BOLD}{H_BOLD * (width - 2)}{BR_BOLD}{RESET}")
    return lines

def animate_frame_appearance(frame_lines, delay=0.05):
    for i, line in enumerate(frame_lines):
        sys.stdout.write(f"\033[{i+1};1H{line}")
        sys.stdout.flush()
        time.sleep(delay)

def center_text(text, width):
    return text.center(width)

def main():
    hide_cursor()
    clear_screen()
    
    quote = WOODY_QUOTE
    attr = WOODY_ATTR
    
    # Calculate frame dimensions
    max_line_len = max(len(quote), len(attr))
    frame_width = max_line_len + 10
    frame_height = 9
    
    # Center on screen (assuming 80x24 terminal)
    term_width = 80
    term_height = 24
    start_col = (term_width - frame_width) // 2
    start_row = (term_height - frame_height) // 2
    
    # Draw empty frame first
    frame = draw_frame(frame_width, frame_height, " WOODY'S WISDOM ", MAGENTA)
    
    # Position frame
    for i, line in enumerate(frame):
        sys.stdout.write(f"\033[{start_row + i + 1};{start_col + 1}H{line}")
    sys.stdout.flush()
    time.sleep(0.3)
    
    # Animate quote appearing with typing effect inside frame
    quote_row = start_row + 3
    attr_row = start_row + 5
    text_start_col = start_col + 5
    
    # Neurotic lead-in
    neurotic_thoughts = [
        "Wait, is this quote too morbid?",
        "My analyst says I obsess over mortality...",
        "Should I have ordered the salad instead?",
        "The universe is expanding. My anxiety is expanding faster.",
        "Did I leave the stove on? The universe? Both?",
    ]
    
    thought_row = start_row + frame_height + 1
    for thought in neurotic_thoughts:
        sys.stdout.write(f"\033[{thought_row};{start_col + 1}H{BRIGHT_BLACK}{ITALIC}{thought.ljust(frame_width)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.8)
        sys.stdout.write(f"\033[{thought_row};{start_col + 1}H{' ' * frame_width}")
        sys.stdout.flush()
        time.sleep(0.2)
    
    # Now type the actual quote with a nice color gradient
    quote_colors = [CYAN, BRIGHT_CYAN, WHITE, BRIGHT_WHITE, YELLOW, BRIGHT_YELLOW]
    sys.stdout.write(f"\033[{quote_row};{text_start_col}H")
    sys.stdout.flush()
    
    for i, char in enumerate(quote):
        color = quote_colors[i % len(quote_colors)]
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.04)
    
    time.sleep(0.5)
    
    # Type attribution
    sys.stdout.write(f"\033[{attr_row};{text_start_col + 2}H")
    sys.stdout.flush()
    for char in attr:
        sys.stdout.write(f"{DIM}{ITALIC}{MAGENTA}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)
    
    time.sleep(0.8)
    
    # Add some decorative sparkles around the frame
    sparkles = ['✦', '✧', '⋆', '✺', '✹', '✶', '✷', '✸']
    sparkle_colors = [YELLOW, BRIGHT_YELLOW, MAGENTA, BRIGHT_MAGENTA, CYAN, BRIGHT_CYAN]
    
    for _ in range(15):
        row = random.randint(start_row, start_row + frame_height - 1)
        col = random.randint(start_col, start_col + frame_width - 1)
        sparkle = random.choice(sparkles)
        color = random.choice(sparkle_colors)
        sys.stdout.write(f"\033[{row + 1};{col + 1}H{color}{BOLD}{sparkle}{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Final pause with subtle pulsing effect on the quote
    for pulse in range(3):
        for brightness in [BRIGHT_WHITE, WHITE, DIM + WHITE, WHITE, BRIGHT_WHITE]:
            sys.stdout.write(f"\033[{quote_row};{text_start_col}H{brightness}{quote}{RESET}")
            sys.stdout.flush()
            time.sleep(0.15)
    
    # Show final message at bottom
    sys.stdout.write(f"\033[{term_height - 1};1H{BRIGHT_BLACK}{ITALIC}Press Enter to accept the void...{RESET}")
    sys.stdout.flush()
    
    show_cursor()
    input()
    clear_screen()
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f"\n{YELLOW}Interrupted. The void thanks you for your time.{RESET}\n")
    except Exception as e:
        show_cursor()
        print(f"\n{RED}Error: {e}{RESET}\n")