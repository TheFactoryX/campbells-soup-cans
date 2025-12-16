"""
Campbell's Soup Can #980
Produced: 2025-12-16 21:32:59
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI Color and Style Constants
class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # Colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"
    
    # Backgrounds
    BG_RED = "\033[41m"
    BG_YELLOW = "\033[43m"

def get_terminal_size():
    try:
        cols, lines = os.get_terminal_size()
        return cols, lines
    except:
        return 80, 24

import os

def animate_text(text, color=ANSI.WHITE, speed=0.04):
    """Prints text character by character with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{ANSI.RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_centered(text, width=80, color=ANSI.WHITE, bold=False, italic=False):
    """Prints text centered within a specific width."""
    style = ""
    if bold: style += ANSI.BOLD
    if italic: style += ANSI.ITALIC
    
    # Calculate padding
    stripped_text = text.encode('ascii', 'ignore').decode('utf-8').replace('\033', '') # rough length check
    actual_len = len(text)
    # This is a rough approximation for centering if not using raw len
    # Let's just use the provided width for centering logic
    
    # Simple centering:
    pad = (width - len(text)) // 2
    if pad < 0: pad = 0
    padding = " " * pad
    
    print(f"{style}{padding}{color}{text}{ANSI.RESET}")

def draw_ascii_art():
    """Draws a sad stick figure philosopher with ANSI colors."""
    # Using fixed width block for alignment
    print(f"\n{ANSI.GRAY}{' ' * 15} __")
    print(f"{' ' * 14}{ANSI.WHITE}/  \\")
    print(f"{' ' * 13}{ANSI.GRAY}|  |")
    print(f"{' ' * 13}{ANSI.GRAY}|  |")
    print(f"{' ' * 13}{ANSI.GRAY}|  |")
    print(f"{' ' * 13}{ANSI.GRAY}|  |")
    print(f"{' ' * 12}{ANSI.GRAY}/    \\")
    print(f"{' ' * 11}{ANSI.GRAY}/      \\")
    print(f"{' ' * 11}{ANSI.GRAY}|  O  O |  {ANSI.GRAY}<--- Existential Gaze")
    print(f"{' ' * 11}{ANSI.GRAY}|   -   |")
    print(f"{' ' * 11}{ANSI.GRAY}\\  ---  /")
    print(f"{' ' * 12}{ANSI.GRAY}'------'")
    print()

def main():
    # The Quote
    quote = '"My brain is my second favorite organ."'
    
    # Clear screen (optional, but dramatic)
    # os.system('cls' if os.name == 'nt' else 'clear') 
    # We won't clear to preserve the context if run in a terminal, but we can scroll.
    
    # 1. Intro Animation
    print("\n" * 2)
    animate_text("Initializing Neurosis...", ANSI.GRAY, 0.05)
    time.sleep(0.5)
    animate_text("Loading Insecurities...", ANSI.GRAY, 0.05)
    time.sleep(0.5)
    
    # 2. The Main Event
    cols = 80
    
    # Draw Header Box
    header = "WOODY ALLEN BOT v1.0"
    print(f"{ANSI.BG_YELLOW}{' ' * cols}{ANSI.RESET}")
    print(f"{ANSI.BG_YELLOW}{ANSI.BLACK}{ANSI.BOLD}{header.center(cols)}{ANSI.RESET}")
    print(f"{ANSI.BG_YELLOW}{' ' * cols}{ANSI.RESET}")
    
    # Draw Body Box (Top)
    print(f"{ANSI.YELLOW}│{ANSI.RESET}{' ' * (cols-2)}{ANSI.YELLOW}│{ANSI.RESET}")
    
    # The Quote (centered with style)
    # We use string formatting to center it roughly
    msg = f" {ANSI.MAGENTA}{ANSI.BOLD}{ANSI.ITALIC}{quote}{ANSI.RESET} "
    padding = " " * ((cols - len(msg) - 2) // 2)
    print(f"{ANSI.YELLOW}│{ANSI.RESET}{padding}{msg}{padding}{ANSI.YELLOW}│{ANSI.RESET}")
    
    # ASCII Art Section
    draw_ascii_art()
    
    # Bottom Box
    print(f"{ANSI.YELLOW}│{ANSI.RESET}{' ' * (cols-2)}{ANSI.YELLOW}│{ANSI.RESET}")
    print(f"{ANSI.YELLOW}└{'─' * (cols-2)}┘{ANSI.RESET}")
    
    # 3. Footer Animation
    print()
    animate_text("System shutting down due to panic...", ANSI.GRAY, 0.05)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{ANSI.RED}Caught existential dread. Exiting...{ANSI.RESET}")