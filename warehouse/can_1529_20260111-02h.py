"""
Campbell's Soup Can #1529
Produced: 2026-01-11 02:39:26
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
    ___   __   __.__  __                  
   /   | /  | /  ||__||  |   __           
  /    |/  | |  | | ||  | |  |__ __  ____
 /    /|  |_|  | | ||  | |  |  |  |  __   \
/    / |       | | ||  | |  |  |  |  | |  |
\ __ /  |____|  | | ||  | |__|  |__|  |_|  |
                                                
    Philosopher: W. Allen (Neurotic Edition)
"""

import sys
import time
import random

# ---------------------------------------------------------
# ANSI Color & Style Helpers
# ---------------------------------------------------------
class T:
    # Formatting
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    INVERT = "\033[7m"
    RESET = "\033[0m"
    
    # Colors (Foreground)
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"
    
    # Bright Colors
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

def cursor_hide():
    sys.stdout.write("\033[?25l")

def cursor_show():
    sys.stdout.write("\033[?25h")

def clear_screen():
    sys.stdout.write("\033[2J\033[H")

def move_cursor(x, y):
    sys.stdout.write(f"\033[{y};{x}H")

# ---------------------------------------------------------
# The Animation Logic
# ---------------------------------------------------------
def draw_frame(t):
    """
    Draws a single frame of the existential crisis.
    t: time step (float)
    """
    # Calculate Jitter (Neuroticism Factor)
    # Every frame, the Woody figure twitches slightly
    jitter_x = random.randint(-1, 1)
    jitter_y = random.randint(-1, 1)
    
    # Screen layout constants
    center_x = 30
    center_y = 6
    
    # --- 1. Draw The "Woody" ASCII Art ---
    # Base coordinates
    bx = center_x + jitter_x
    by = center_y + jitter_y
    
    # Colors that shift based on time
    skin = T.YELLOW if int(t) % 2 == 0 else T.BRIGHT_YELLOW
    glasses = T.CYAN
    suit = T.BLUE
    
    art_lines = [
        f"{T.RESET}                 {T.BOLD}{T.INVERT}  MIND  {T.RESET}",
        f"{T.GRAY}        (    (     )    )",
        f"{T.GRAY}       (   )  )  (   )   )",
        f"{T.GRAY}        ) (    ) (    ) (",
        f"{T.GRAY}       (           )    )",
        f"{T.GRAY}         (  )  (   )   (",
        f"{T.GRAY}        (__)  (__)  (__)",
        f"",
        f"         {glasses}┌──────┐{T.RESET}   {T.BOLD}I'm not", 
        f"         {glasses}│  ..  │{T.RESET}   {T.BOLD}afraid", 
        f"         {glasses}│  ||  │{T.RESET}   {T.BOLD}of death,",
        f"  {suit}┌───────{glasses}└──────┘{T.RESET}{suit}──┐{T.RESET}  {T.BOLD}I just",
        f"  {suit}│ {skin} o   o  {T.RESET}{suit}       │{T.RESET}  {T.BOLD}don't",
        f"  {suit}│ {skin}  ___   {T.RESET}{suit}       │{T.RESET}  {T.BOLD}want to",
        f"  {suit}│ {skin} /   \  {T.RESET}{suit}       │{T.RESET}  {T.BOLD}be there",
        f"  {suit}└─────── {skin} \___/   {T.RESET}{suit}──┘{T.RESET}  {T.BOLD}when it",
        f"          {skin}  | |{T.RESET}            {T.BOLD}happens.",
        f"          {skin}  | |{T.RESET}",
        f"          {skin} /   \{T.RESET}",
        f"         {skin}/_____\{T.RESET}"
    ]
    
    # --- 2. Draw The Scrolling Conveyor Belt of Despair ---
    # A text strip that loops at the bottom
    belt_text = " existential dread... ennui... taxes... minor inconveniences... mortality... "
    belt_width = 55
    shift = int(t * 2) % len(belt_text)
    visible_text = (belt_text + belt_text)[shift : shift + belt_width]
    
    # Alternate belt colors
    belt_color = T.BRIGHT_RED if int(t) % 2 == 0 else T.RED
    belt_line = f"{T.GRAY}╔══{'═'*belt_width}══╗"
    belt_mid = f"{T.GRAY}║ {belt_color}{visible_text}{T.GRAY} ║"
    belt_bot = f"{T.GRAY}╚══{'═'*belt_width}══╝"
    
    # --- 3. Render Everything ---
    # To avoid clearing screen constantly (which causes flicker),
    # we move cursor to top left and overwrite. 
    # Note: This assumes a terminal width of at least 65 cols.
    
    sys.stdout.write("\033[H") # Home cursor
    
    # Print ASCII Art
    for i, line in enumerate(art_lines):
        # Add dynamic spacing to create a "float" effect
        float_space = " " * (int(t + i) % 2) 
        print(float_space + line)
        
    # Print Spacer
    print("\n" * 1)
    
    # Print The Conveyor Belt
    print(" " * 5 + belt_line)
    print(" " * 5 + belt_mid)
    print(" " * 5 + belt_bot)
    
    # Print Footer / Status
    print(f"\n{T.GRAY}Press Ctrl+C to escape the simulation.{T.RESET}")

def main():
    try:
        cursor_hide()
        clear_screen()
        
        # Title Screen (Brief)
        print(f"{T.BOLD}{T.YELLOW}")
        print("  WOODY ALLEN: THE PYTHON EDITION")
        print(f"{T.RESET}")
        time.sleep(1.5)
        
        t = 0.0
        while True:
            draw_frame(t)
            t += 0.2
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        # Graceful Exit
        clear_screen()
        cursor_show()
        
        # Print the quote one last time statically, centered
        print("\n" * 4)
        print(f"{T.BOLD}{T.YELLOW}      'I don't want to achieve immortality through my work;")
        print(f"{T.BOLD}{T.YELLOW}       I want to achieve it through not dying.'")
        print(f"{T.GRAY}                  - Woody Allen{T.RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()