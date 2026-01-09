"""
Campbell's Soup Can #1485
Produced: 2026-01-09 02:28:20
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def woody_allen_quote():
    # ANSI Colors and styles
    RESET = "\033[0m"
    BOLD = "\033[1m"
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
    
    # Cursor and Screen controls
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    CLEAR_SCREEN = "\033[2J"
    HOME = "\033[H"
    
    # Quote parts (split for dramatic typing effect)
    # "I don't want to achieve immortality through my work; 
    #  I want to achieve it through not dying."
    quote_lines = [
        "I don't want to achieve immortality",
        "through my work;",
        "I want to achieve it",
        "through not dying."
    ]
    
    # ASCII Art of a neurotic stick figure
    # Slightly vibrating and looking worried
    art_lines = [
        f"{CYAN}    o   {RESET}   (My conscience is killing me)",
        f"{CYAN}   /|\\  {RESET}   (But my doctor says I can't have the guilt)",
        f"{CYAN}   / \\  {RESET}   (Without a prescription)",
    ]

    def type_text(text, color=BRIGHT_WHITE, speed=0.03):
        """Types out text character by character."""
        for char in text:
            sys.stdout.write(f"{color}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n")

    def typewriter_effect(text, color=BRIGHT_WHITE):
        """Simulates a typewriter hitting keys hard."""
        sys.stdout.write("    ")
        for char in text:
            sys.stdout.write(f"\b{color}{char}{RESET}")
            sys.stdout.flush()
            # Random pauses to simulate human typing
            pause = random.uniform(0.05, 0.12)
            # Random bold flashes (like the typewriter key hitting hard)
            if random.random() > 0.8:
                sys.stdout.write(f"\b\033[1;37m{char}\033[0m")
                sys.stdout.flush()
            time.sleep(pause)

    def draw_box(text, width=50):
        """Draws a fancy box around the text."""
        top_border = f"{BRIGHT_MAGENTA}╔{'═' * (width - 2)}╗{RESET}"
        bottom_border = f"{BRIGHT_MAGENTA}╚{'═' * (width - 2)}╝{RESET}"
        side = f"{BRIGHT_MAGENTA}║{RESET}"
        
        sys.stdout.write(f"{HOME}{top_border}\n")
        
        # Calculate padding to center the text
        # Since we are printing in chunks, we just print the side
        # The text printing function handles the content
        
        return top_border, bottom_border, side

    def main_animation():
        print(CLEAR_SCREEN)
        print(HIDE_CURSOR)
        
        # 1. Setup the stage
        print(f"\n\n")
        print(f"    {BOLD}{YELLOW}THE EXISTENTIAL CRISIS TERMINAL 1.0{RESET}")
        print(f"    {BRIGHT_BLACK}Copyright (c) Neurotic Systems Inc.{RESET}")
        time.sleep(1.5)
        
        print(f"\n    {BRIGHT_BLACK}[SYSTEM] Booting up anxiety module...{RESET}")
        time.sleep(0.8)
        print(f"    {BRIGHT_BLACK}[SYSTEM] Loading self-doubt... {BRIGHT_RED}FAILED{RESET}{BRIGHT_BLACK}. Retrying...{RESET}")
        time.sleep(0.8)
        print(f"    {BRIGHT_BLACK}[SYSTEM] Loading self-doubt... {BRIGHT_GREEN}SUCCESS{RESET}{BRIGHT_BLACK}.{RESET}")
        time.sleep(0.5)
        
        print(f"\n    {BRIGHT_BLACK}[SYSTEM] Initiating verbal diarrhea...{RESET}")
        time.sleep(1.0)
        
        # 2. The Setup (The Comic's "So...")
        print(f"\n    {MAGENTA}<<<{RESET} ")
        sys.stdout.flush()
        time.sleep(0.5)
        
        # 3. The Quote (Typewriter style)
        border_width = 52
        
        # Top border
        print(f"\n    {BRIGHT_MAGENTA}╔{'═' * (border_width)}╗{RESET}")
        
        # The Quote
        line_colors = [BRIGHT_CYAN, BRIGHT_YELLOW, BRIGHT_RED, BRIGHT_GREEN]
        
        # Line 1
        print(f"    {BRIGHT_MAGENTA}║{RESET}  {line_colors[0]}", end="")
        sys.stdout.flush()
        typewriter_effect(quote_lines[0], line_colors[0])
        time.sleep(0.2)
        
        # Line 2 (Indented more)
        print(f"    {BRIGHT_MAGENTA}║{RESET}      {line_colors[1]}", end="")
        sys.stdout.flush()
        typewriter_effect(quote_lines[1], line_colors[1])
        time.sleep(0.3)
        
        # Line 3
        print(f"    {BRIGHT_MAGENTA}║{RESET}  {line_colors[2]}", end="")
        sys.stdout.flush()
        typewriter_effect(quote_lines[2], line_colors[2])
        time.sleep(0.2)
        
        # Line 4 (The punchline)
        print(f"    {BRIGHT_MAGENTA}║{RESET}      {BOLD}{line_colors[3]}", end="")
        sys.stdout.flush()
        typewriter_effect(quote_lines[3], line_colors[3])
        
        # Bottom border
        print(f"    {BRIGHT_MAGENTA}╚{'═' * (border_width)}╝{RESET}")
        
        # 4. The ASCII Art Reaction (Vibrating slightly)
        time.sleep(0.5)
        print(f"\n")
        for _ in range(3):
            for i, line in enumerate(art_lines):
                # Shift position slightly to simulate vibration
                offset = random.randint(0, 1)
                spaces = " " * offset
                print(f"    {spaces}{line}")
            time.sleep(0.2)
            if _ < 2:
                # Move cursor up to overwrite
                sys.stdout.write("\033[3A") 
                sys.stdout.flush()
        
        # Final Newline
        print("\n")
        
        # 5. Cursor blinking cursor cursor cursor...
        cursor_x = "   "
        sys.stdout.write(cursor_x)
        for _ in range(3):
            sys.stdout.write(f"{BRIGHT_RED}{BOLD}█{RESET}")
            sys.stdout.flush()
            time.sleep(0.4)
            sys.stdout.write(f"\b {RESET}")
            sys.stdout.flush()
            time.sleep(0.4)
            
        print("\n\n")
        print(SHOW_CURSOR)

    try:
        main_animation()
    except KeyboardInterrupt:
        print(SHOW_CURSOR)
        print(f"\n{YELLOW}Existential dread interrupted by user (Ctrl+C).{RESET}")

if __name__ == "__main__":
    woody_allen_quote()