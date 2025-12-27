"""
Campbell's Soup Can #1218
Produced: 2025-12-27 17:31:47
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Neurotic Masterpiece in Python
Run this. It worries about everything. Even its own existence.
"""

import sys
import time
import random

# --- Configuration ---
DELAY = 0.03
COLUMN_WIDTH = 70
PALETTE = {
    "neurotic_red": "\033[91m",
    "anxious_yellow": "\033[93m",
    "existential_blue": "\033[94m",
    "muted_white": "\033[90m",
    "bold": "\033[1m",
    "blink": "\033[5m",
    "reset": "\033[0m",
    "bg": "\033[48;5;234m", # Dark grey background
    "fg": "\033[38;5;250m", # Light grey text
    "highlight": "\033[48;5;88m"
}

# --- The ASCII Art (Neurotic Edition) ---
# I spent too much time on this. I hope you're happy.
ART_LINES = [
    "     .--.  .--.      .--.   ",
    "    /..  \\/..  \\    /..  \\  ",
    "   ( oo ) ( oo )   ( oo )  ",
    "   | oo | | oo |   | oo |  ",
    "   | oo | | oo |   | oo |  ",
    "   | .. | | .. |   | .. |  ",
    "   '^^^' '^^^'     '^^^'   ",
    "      ||      ||      ||   ",
    "     _||_    _||_    _||_  ",
    "    [__]    [__]    [__]   ",
]

def type_writer(text, color_code, speed=0.03):
    """Types out text with dramatic pauses."""
    for char in text:
        print(f"{color_code}{char}", end='', flush=True)
        time.sleep(speed * random.uniform(0.8, 1.5))
    print(PALETTE["reset"])

def print_centered(text, width=COLUMN_WIDTH, fill_char=" "):
    """Centers text with padding."""
    print(text.center(width))

def draw_frame():
    """Draws the visual border."""
    # Top border
    print(PALETTE["muted_white"] + "╔" + "═" * (COLUMN_WIDTH - 2) + "╗")
    
    # Empty row
    print("║" + " " * (COLUMN_WIDTH - 2) + "║")
    
    # The ASCII Art Row (Centered)
    # We calculate the width of the art roughly
    art_width = 27 
    padding = (COLUMN_WIDTH - 2 - art_width) // 2
    space = " " * padding
    
    for line in ART_LINES:
        print("║" + space + PALETTE["neurotic_red"] + line + PALETTE["muted_white"] + " " * (COLUMN_WIDTH - 2 - art_width - padding) + "║")
    
    # Separator
    print("╠" + "═" * (COLUMN_WIDTH - 2) + "╣")
    
    # The Quote Area
    # We will manually line break the quote to fit the box
    print("║" + " " * (COLUMN_WIDTH - 2) + "║")

def run():
    """The Main Drama."""
    
    # 1. Clear screen (optional, but looks better)
    print("\033[2J\033[H", end="") 
    
    # 2. Draw the box and ASCII
    draw_frame()
    
    # 3. The Quote Setup
    quote_lines = [
        "I'm not afraid of death,",
        "I just don't want to be there",
        "when the maintenance mode kicks in."
    ]
    
    # 4. Print the Quote with typing effect
    for i, line in enumerate(quote_lines):
        # Calculate indentation to look centered in the box
        # 2 borders + padding
        current_len = len(line)
        padding_len = ((COLUMN_WIDTH - 2) - current_len) // 2
        prefix = "║" + " " * padding_len
        
        # Print the prefix
        print(prefix, end="")
        
        # Print the typed text
        type_writer(f"{PALETTE['bold']}{PALETTE['anxious_yellow']}{line}", PALETTE["anxious_yellow"], speed=0.04)
        
        # If it's the last line, add a dramatic cursor blinking
        if i == len(quote_lines) - 1:
            time.sleep(0.5)
            # Backtrack to replace the last line's end with a blinking cursor
            # (This is a visual hack, we just append a cursor on the next line for effect)
            sys.stdout.write("\033[F") # Move cursor up
            sys.stdout.write("\033[K") # Clear line
            print(prefix + f"{PALETTE['bold']}{PALETTE['anxious_yellow']}{line} {PALETTE['neurotic_red']}{PALETTE['blink']}...wait, what?{PALETTE['reset']}")
            
    # 5. Closing the box
    print("║" + " " * (COLUMN_WIDTH - 2) + "║")
    print("╚" + "═" * (COLUMN_WIDTH - 2) + "╝")
    
    # 6. The Footer (The meta-commentary)
    print()
    print_centered(f"{PALETTE['muted_white']}Execution time: {time.strftime('%H:%M:%S')} | Status: {PALETTE['neurotic_red']}Overthinking{PALETTE['reset']}")
    print_centered(f"{PALETTE['muted_white']}System ready. Nervous breakdown pending...{PALETTE['reset']}")
    print()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(f"\n{PALETTE['neurotic_red']}Ah! You interrupted me! Just like my mother!{PALETTE['reset']}")

# End of File.
# I hope this meets your existential requirements. If not, I'll worry about it later.