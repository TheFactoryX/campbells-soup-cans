"""
Campbell's Soup Can #2478
Produced: 2026-02-28 07:41:02
Worker: Google: Nano Banana Pro (Gemini 3 Pro Image Preview) (google/gemini-3-pro-image-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import os

# --- ANSI Escape Codes for Neurotic Visuals ---
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"

    FG_BLACK = "\033[30m"
    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_YELLOW = "\033[33m"
    FG_BLUE = "\033[34m"
    FG_MAGENTA = "\033[35m"
    FG_CYAN = "\033[36m"
    FG_WHITE = "\033[97m"
    
    BG_BLACK = "\033[40m"
    BG_BLUE = "\033[44m"

# The philosophically anxious quote
QUOTE_SEGMENTS = [
    (Style.FG_WHITE, "The eternal silence of these infinite spaces frightens me."),
    (Style.FG_YELLOW + Style.ITALIC, " Especially on a Tuesday."),
    (Style.FG_WHITE, "\nI mean, if the universe is really expanding,"),
    (Style.FG_CYAN + Style.BOLD, " why can't I ever find a decent parking spot in Manhattan?"),
]

WIDTH = 70

def clear_screen():
    """Clears terminal for dramatic effect."""
    os.system('cls' if os.name == 'nt' else 'clear')

def nervous_typewriter(text, style_code):
    """Typerwriter effect with neurotic hesitations."""
    sys.stdout.write(style_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Basic typing speed
        time.sleep(random.uniform(0.02, 0.06))
        # Occasional nervous pause, as if re-thinking life choices
        if random.random() < 0.03 and char in '.,? ':
             time.sleep(random.uniform(0.2, 0.5))
    sys.stdout.write(Style.RESET)

def print_centered(text, style=""):
    pad = max(0, (WIDTH - len(text)) // 2)
    print(f"{' ' * pad}{style}{text}{Style.RESET}")

def main():
    clear_screen()
    # Set background to black for film noir vibe
    sys.stdout.write(Style.BG_BLACK)
    print("\n" * 2)
    
    # --- Top Border (Jittery) ---
    border_chars = ["~", ".", ":", "?", "`"]
    top_border = "".join(random.choice(border_chars) for _ in range(WIDTH))
    print_centered(top_border, Style.FG_BLUE + Style.BOLD)
    
    # --- Header ---
    print()
    print_centered("[ From the crinkled notebooks of a very worried mind ]", Style.FG_CYAN + Style.ITALIC)
    print()
    
    # --- Jazzy Separator ---
    separator = "~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~"
    print_centered(separator, Style.FG_MAGENTA)
    print("\n")

    # --- The Main Event: The Quote ---
    margin_len = (WIDTH - 50) // 2
    margin = " " * margin_len

    for style, segment in QUOTE_SEGMENTS:
        # Handle internal newlines in segments for margin alignment
        lines = segment.split('\n')
        for i, line in enumerate(lines):
            if i > 0 or segment.startswith('\n'):
                 print() # Print unavoidable newline
            sys.stdout.write(margin)
            nervous_typewriter(line, style)
        # Slight pause between major thoughts
        time.sleep(0.3)

    print("\n\n")

    # --- Bottom Separator and Closing ---
    print_centered(separator, Style.FG_MAGENTA)
    print()
    bottom_border = "".join(random.choice(border_chars) for _ in range(WIDTH))
    print_centered(bottom_border, Style.FG_BLUE + Style.BOLD)
    
    # --- Final neurotic flourish ---
    print()
    sys.stdout.write(margin + "     ( nervously adjusts glasses ) ")
    # Blinking cursor at the end
    for _ in range(3):
        sys.stdout.write(f"{Style.FG_CYAN}{Style.BLINK}_{Style.RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.3)
            
    print(Style.RESET + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # If user interrupts, panic slightly.
        print(f"\n\n{Style.FG_RED}{Style.ITALIC}Oh god, you stopped it. Was it something I said? It was, wasn't it?{Style.RESET}\n")