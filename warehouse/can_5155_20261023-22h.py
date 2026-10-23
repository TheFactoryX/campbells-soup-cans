"""
Campbell's Soup Can #5155
Produced: 2026-10-23 22:15:42
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
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    
    # Foreground
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
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.WHITE, delay=0.03, newline=True):
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def slow_print(text, color=C.WHITE, delay=0.05):
    typewriter(text, color, delay)

def blink_text(text, color=C.YELLOW, times=3, interval=0.4):
    for _ in range(times):
        print(f'\r{color}{text}{C.RST}', end='', flush=True)
        time.sleep(interval)
        print(f'\r{" " * len(text)}', end='', flush=True)
        time.sleep(interval)
    print(f'\r{color}{text}{C.RST}')

def draw_box(width, height, title="", color=C.CYAN):
    top = f'{color}╔{"═" * (width - 2)}╗{C.RST}'
    bottom = f'{color}╚{"═" * (width - 2)}╝{C.RST}'
    middle = f'{color}║{" " * (width - 2)}║{C.RST}'
    
    lines = [top]
    if title:
        pad = (width - 2 - len(title)) // 2
        title_line = f'{color}║{" " * pad}{C.BOLD}{title}{C.RST}{color}{" " * (width - 2 - pad - len(title))}║{C.RST}'
        lines.append(title_line)
        lines.append(f'{color}╠{"═" * (width - 2)}╣{C.RST}')
    for _ in range(height - (4 if title else 3)):
        lines.append(middle)
    lines.append(bottom)
    return lines

def center_text(text, width):
    return text.center(width)

def woody_animation():
    quote = (
        "I told my analyst I have a crippling fear of commitment.\n"
        "He said, 'That'll be $300.' I said, 'Can I pay you\n"
        "next week?' He said, 'That's exactly the problem.'"
    )
    
    attribution = "— Woody Allen (probably, or maybe just my landlord)"
    
    width = 70
    height = 16
    
    clear_screen()
    hide_cursor()
    
    # Draw the box
    box_lines = draw_box(width, height, " WOODY ALLEN WISDOM ", C.BRIGHT_CYAN)
    
    # Print box top
    for i, line in enumerate(box_lines[:3]):
        move_cursor(i + 2, 5)
        print(line)
    
    # Animate quote lines appearing
    quote_lines = quote.split('\n')
    start_y = 5
    for idx, qline in enumerate(quote_lines):
        move_cursor(start_y + idx, 7)
        typewriter(qline, C.BRIGHT_WHITE, delay=0.02)
        time.sleep(0.3)
    
    # Animate attribution
    time.sleep(0.5)
    move_cursor(start_y + len(quote_lines) + 1, 7)
    typewriter(attribution, C.GRAY + C.ITALIC, delay=0.03)
    
    # Print bottom of box
    for i, line in enumerate(box_lines[-3:]):
        move_cursor(start_y + len(quote_lines) + 3 + i, 5)
        print(line)
    
    # Add some decorative elements
    decorations = [
        (1, 5, "🧠"),
        (1, 72, "🛋️"),
        (18, 5, "💊"),
        (18, 72, "📉"),
    ]
    for y, x, emoji in decorations:
        move_cursor(y, x)
        print(f'{C.BRIGHT_MAGENTA}{emoji}{C.RST}')
    
    # Pulsing thought bubble at bottom
    move_cursor(20, 15)
    thoughts = [
        "  ...also my lower back hurts  ",
        "  ...pretty sure the universe is gaslighting me  ",
        "  ...my dentist hates me personally  ",
        "  ...existential dread: now with 50% more heartburn  "
    ]
    
    for _ in range(2):
        for thought in thoughts:
            move_cursor(20, 15)
            print(f'{C.DIM}{C.ITALIC}{thought}{C.RST}', end='', flush=True)
            time.sleep(1.2)
    
    move_cursor(22, 0)
    show_cursor()
    print()

def main():
    try:
        woody_animation()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f"\n{C.RED}Interrupted. The anxiety remains.{C.RST}\n")
    except Exception as e:
        show_cursor()
        print(f"\n{C.RED}Error: {e}{C.RST}\n")

if __name__ == "__main__":
    main()