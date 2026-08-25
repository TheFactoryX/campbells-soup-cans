"""
Campbell's Soup Can #4835
Produced: 2026-08-25 15:05:01
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
    BRIGHT_BLACK = '\033[90m'
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

# Woody Allen ASCII glasses
GLASSES = [
    "    ╔══════════════════════════════════════╗",
    "    ║  ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄  ║",
    "    ║ ██████████    ██████████ ║",
    "    ║ ██████████    ██████████ ║",
    "    ║  ▀▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀  ║",
    "    ║        ▄▄▄▄▄▄▄▄▄▄▄▄        ║",
    "    ║       ███████████████       ║",
    "    ║        ▀▀▀▀▀▀▀▀▀▀▀▀        ║",
    "    ╚══════════════════════════════════════╝",
]

# Original Woody Allen-style quote
QUOTE = "I told my therapist I have an inferiority complex. He said, 'Don't worry, you're not *that* inferior.'"

ATTRIBUTION = "— Woody Allen (probably)"

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.BRIGHT_WHITE, delay=0.03, newline=True):
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def rainbow_text(text):
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA, C.BRIGHT_RED]
    result = ""
    for i, char in enumerate(text):
        result += f"{colors[i % len(colors)]}{char}"
    return result + C.RST

def pulse_color(text, colors, cycles=3):
    for _ in range(cycles):
        for color in colors:
            move_cursor(15, 2)
            sys.stdout.write(f"{color}{text}{C.RST}")
            sys.stdout.flush()
            time.sleep(0.15)

def draw_box(width, height, y, x, color=C.CYAN):
    top = f"{color}┌{'─' * (width - 2)}┐{C.RST}"
    middle = f"{color}│{' ' * (width - 2)}│{C.RST}"
    bottom = f"{color}└{'─' * (width - 2)}┘{C.RST}"
    
    move_cursor(y, x)
    print(top)
    for i in range(height - 2):
        move_cursor(y + 1 + i, x)
        print(middle)
    move_cursor(y + height - 1, x)
    print(bottom)

def animate_glasses():
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    for frame in range(12):
        clear_screen()
        color = colors[frame % len(colors)]
        print(f"\n{color}")
        for line in GLASSES:
            print(line)
        print(f"{C.RST}")
        time.sleep(0.08)

def main():
    hide_cursor()
    try:
        # Phase 1: Glasses animation
        animate_glasses()
        
        # Phase 2: Typewriter quote in a box
        clear_screen()
        print()
        
        # Draw decorative box
        box_width = 70
        box_height = 7
        box_y = 3
        box_x = 5
        
        draw_box(box_width, box_height, box_y, box_x, C.BRIGHT_CYAN)
        
        # Type the quote inside the box
        move_cursor(box_y + 2, box_x + 3)
        typewriter("“", C.BRIGHT_YELLOW, 0.05, newline=False)
        
        words = QUOTE.split()
        line = ""
        line_y = box_y + 2
        line_x = box_x + 4
        max_width = box_width - 8
        
        for i, word in enumerate(words):
            test_line = line + (" " if line else "") + word
            if len(test_line) > max_width:
                move_cursor(line_y, line_x)
                typewriter(line, C.BRIGHT_WHITE, 0.02)
                line_y += 1
                line = word
            else:
                line = test_line
        
        if line:
            move_cursor(line_y, line_x)
            typewriter(line, C.BRIGHT_WHITE, 0.02)
        
        move_cursor(line_y, line_x + len(line) + 1)
        typewriter("”", C.BRIGHT_YELLOW, 0.05)
        
        # Attribution
        move_cursor(box_y + 5, box_x + (box_width - len(ATTRIBUTION)) // 2)
        typewriter(ATTRIBUTION, C.BRIGHT_BLACK + C.ITALIC, 0.04)
        
        # Phase 3: Pulsing effect on the quote
        time.sleep(0.5)
        pulse_colors = [C.BRIGHT_CYAN, C.BRIGHT_MAGENTA, C.BRIGHT_YELLOW, C.BRIGHT_GREEN]
        
        # Make the glasses wink
        for _ in range(3):
            clear_screen()
            print()
            for line in GLASSES:
                print(f"{C.BRIGHT_CYAN}{line}{C.RST}")
            print()
            # Reprint quote with pulsing
            move_cursor(box_y + 2, box_x + 3)
            print(f"{C.BRIGHT_YELLOW}“{C.RST}{C.BRIGHT_WHITE}{QUOTE}{C.RST}{C.BRIGHT_YELLOW}”{C.RST}")
            move_cursor(box_y + 5, box_x + (box_width - len(ATTRIBUTION)) // 2)
            print(f"{C.BRIGHT_BLACK}{C.ITALIC}{ATTRIBUTION}{C.RST}")
            time.sleep(0.3)
            
            clear_screen()
            print()
            winked = [
                "    ╔══════════════════════════════════════╗",
                "    ║  ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄  ║",
                "    ║ ██████████    ██████████ ║",
                "    ║ ██████████    ██████████ ║",
                "    ║  ▀▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀  ║",
                "    ║        ▄▄▄▄▄▄▄▄▄▄▄▄        ║",
                "    ║       ███████████████       ║",
                "    ║        ▀▀▀▀▀▀▀▀▀▀▀▀        ║",
                "    ║          ~~~~~~~            ║   ← wink!",
                "    ╚══════════════════════════════════════╝",
            ]
            for line in winked:
                print(f"{C.BRIGHT_MAGENTA}{line}{C.RST}")
            print()
            move_cursor(box_y + 2, box_x + 3)
            print(f"{C.BRIGHT_YELLOW}“{C.RST}{C.BRIGHT_WHITE}{QUOTE}{C.RST}{C.BRIGHT_YELLOW}”{C.RST}")
            move_cursor(box_y + 5, box_x + (box_width - len(ATTRIBUTION)) // 2)
            print(f"{C.BRIGHT_BLACK}{C.ITALIC}{ATTRIBUTION}{C.RST}")
            time.sleep(0.3)
        
        # Final rainbow finale
        clear_screen()
        print("\n" * 2)
        for line in GLASSES:
            print(f"{rainbow_text(line)}")
        print()
        
        # Rainbow quote
        quote_display = f"“{QUOTE}”"
        centered = quote_display.center(60)
        print(f"{rainbow_text(centered)}")
        print()
        print(f"{rainbow_text(ATTRIBUTION.center(60))}")
        print("\n" * 2)
        
        # Final neurotic thought
        final_thoughts = [
            "Anyway, I have a 2:00 PM anxiety attack penciled in...",
            "My analyst says I exaggerate. I told him, 'That's what *she* said.'",
            "I'm not a hypochondriac, I'm an *aspiring* hypochondriac.",
            "If only God would give me a sign... like a deposit slip.",
        ]
        time.sleep(1)
        move_cursor(18, 2)
        typewriter(random.choice(final_thoughts), C.BRIGHT_BLACK + C.ITALIC, 0.04)
        print("\n")
        
    finally:
        show_cursor()
        print(f"{C.RST}", end='')

if __name__ == "__main__":
    main()