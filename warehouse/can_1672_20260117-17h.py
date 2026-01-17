"""
Campbell's Soup Can #1672
Produced: 2026-01-17 17:31:21
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
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

class WoodyPrinter:
    def __init__(self):
        self.colors = {
            'RED': '\033[91m',
            'YELLOW': '\033[93m',
            'BLUE': '\033[94m',
            'RESET': '\033[0m'
        }
        self.frame = [
            r"  _________________________________________  ",
            r" / Neurotic thoughts by Woody Allen's Ghost \ ",
            r" \                                         / ",
            r"  -----------------------------------------  ",
            r"        \   ^__^                           ",
            r"         \  (oo)\_______                   ",
            r"            (__)\       )\/\               ",
            r"                ||----w |                  ",
            r"                ||     ||                  "
        ]
    
    def clear_screen(self):
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
    
    def print_frame(self):
        for idx, line in enumerate(self.frame[:4]):
            color = random.choice(['RED', 'YELLOW', 'BLUE'])
            sys.stdout.write(self.colors[color] + line + self.colors['RESET'] + "\n")
            time.sleep(0.1)
    
    def animate_quote(self):
        quote = "I wouldn't say I'm afraid of dying.\nI just don't want to be there when it happens\nespecially if there's paperwork afterwards."
        
        sys.stdout.write("\n")
        for char in quote:
            sys.stdout.write(self.colors['YELLOW'] + char + self.colors['RESET'])
            sys.stdout.flush()
            time.sleep(0.04 + random.random()*0.05)
            if char in ["!", ".", ",", "\n"]:
                time.sleep(0.2)
        sys.stdout.write("\n\n")
        
        # Woody attribution with blinking effect
        for _ in range(3):
            sys.stdout.write(self.colors['RED'] + "        ― Woody Allen's Therapist's Receptionist" + self.colors['RESET'] + "\r")
            sys.stdout.flush()
            time.sleep(0.3)
            sys.stdout.write(" " * 60 + "\r")
            sys.stdout.flush()
            time.sleep(0.3)
        
        # Final print without clearing
        sys.stdout.write(self.colors['RED'] + "        ― Woody Allen's Therapist's Receptionist" + self.colors['RESET'] + "\n\n")
        for line in self.frame[4:]:
            sys.stdout.write(self.colors['BLUE'] + line + self.colors['RESET'] + "\n")
            time.sleep(0.1)

if __name__ == "__main__":
    wp = WoodyPrinter()
    wp.print_frame()
    wp.animate_quote()