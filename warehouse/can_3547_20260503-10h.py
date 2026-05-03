"""
Campbell's Soup Can #3547
Produced: 2026-05-03 10:16:16
Worker: Baidu: Qianfan-OCR-Fast (free) (baidu/qianfan-ocr-fast:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
from itertools import cycle

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
ENDC = '\033[0m'

# ASCII Art Frame
FRAME_TOP = f"""
{MAGENTA}╔══════════════════════════════════════╗{ENDC}
{MAGENTA}║                                    ║{ENDC}
"""

FRAME_MIDDLE = f"""
{MAGENTA}║                                    ║{ENDC}
{YELLOW}║   {YELLOW}{BLUE}<< WOODY'S BITESIZE PHILOSOPHY MATRIOSHKA >> {BLUE}({YELLOW}...NUTS!) {ENDC}
"""

FRAME_MIDDLE_REPEATED = [FRAME_MIDDLE] * 5

FRAME_S_COORDS = [(x, y) for y in [1, 3, 5] for x in [30, 69, 98]]
FRAME_S = cycle(FRAME_S_COORDS)

# Create frame
FRAME_BASE = f"""
{MAGENTA}╚══════════════════════════════════════╝{ENDC}
"""

def clear_screen():
    """Clear the screen in a cross-platform way"""
    if sys.platform.startswith('win32'):
        import os
        os.system('cls')
    else:
        os.system('clear')

def cycle_frames():
    """Animate frame positions with a cute '3' effect"""
    for i in range(40):
        for j, coord in enumerate(FRAME_S):
            if j % 3 == i:
                NAME = [FRAME_MIDDLE[k:s for s in coord] for k in range(len(coord)+1)]
                for row_num, row in enumerate(NAME):
                    print(RED + row[0] + ' ' + row[1] + ' ' + END谀إيمحrow[2])
        time.sleep(0.15)
        sys.stdout.flush()

def print_woodys_quote():
    """Print Woody-style philosophical quote creatively"""
    clear_screen()
    
    print(FRAME_TOP, end='')
    while True:
        for line in FRAME_MIDDLE_REPEATED:
            print(line)
        print(FRAME_BASE)
        print()
        print("MAY BE??!!!")  # Woody's iconic reaction
        time.sleep(0.8)
        for char in "AND (BECAUSE) IT'S BORING, WE'RE ALSO GOING TO WATCH TIEBAD ALSO????":  # Mimicking Woody's sardonic nature
            print(RED + BLUE + char + " ", end='', flush=True)
            time.sleep(0.4)
            print(ENDC)
        time.sleep(0.8)
        print("... WOODY ALREADY SAID THAT: " + BLUE + RED + "WE'RE ALL ACTORS... OR MAYBE CLOWNS" + ENDC)
        
        break

if __name__ == "__main__":
    # First show the frame animation
    cycle_frames()
    
    # Then print Woody's quote
    print_woodys_quote()