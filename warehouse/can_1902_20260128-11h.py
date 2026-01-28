"""
Campbell's Soup Can #1902
Produced: 2026-01-28 11:35:42
Worker: Google: Gemini 2.5 Flash Preview 09-2025 (google/gemini-2.5-flash-preview-09-2025)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI escape codes for colors and styles
class C:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GREY = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    INVERSE = '\033[7m'

def typewriter_print(text, delay=0.015, color=C.WHITE):
    """Prints text one character at a time."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C.RESET)

def main():
    # The Woody Allen-esque quote
    quote = (
        "My greatest fear is that I'll be reincarnated as myself. "
        "And then have to date myself. "
        "The existential terror is almost manageable, but the scheduling is a nightmare."
    )

    lines = quote.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    padding = 4
    width = max_len + 2 * padding
    
    # --- Visual Setup ---
    
    print(C.CYAN + "\n" + "=" * 80 + C.RESET)
    
    # Title Ticker (simulating marquee/ticker tape)
    title = " THE WOODY-BOT 3000 (Anxiety Edition) "
    
    print(C.YELLOW + C.BOLD + "\n" + f"{title:^{80}}" + C.RESET)
    time.sleep(0.5)

    # --- Box Frame Animation ---
    
    box_color = C.GREY
    corner = "+"
    horizontal = "-"
    vertical = "|"

    # Top boundary
    top_bar = corner + horizontal * width + corner
    
    # Print animated top box line
    sys.stdout.write(box_color)
    typewriter_print(top_bar + "\n", delay=0.005, color=box_color)

    # Content lines
    bg_color = C.INVERSE + C.BLUE
    
    for line in lines:
        padded_line = f" {line:^{max_len}} "
        
        # Start of line (vertical bar)
        sys.stdout.write(box_color + vertical + C.RESET)
        sys.stdout.flush()
        
        # Print the quote line itself with typewriter effect and colors
        typewriter_print(f"{padded_line}", delay=0.03, color=C.MAGENTA + C.BOLD + C.ITALIC)
        
        # End of line (vertical bar)
        sys.stdout.write(box_color + vertical + "\n" + C.RESET)
        sys.stdout.flush()
        time.sleep(0.1)

    # Bottom boundary
    bottom_bar = corner + horizontal * width + corner
    typewriter_print(bottom_bar + "\n", delay=0.005, color=box_color)

    print(C.CYAN + "=" * 80 + C.RESET)
    print(C.GREY + C.ITALIC + f"{'-- End Transmission, now searching for misplaced optimism --':^80}" + C.RESET)
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(C.RESET + "\nProcess interrupted. Probably for the best.")