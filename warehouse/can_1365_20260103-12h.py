"""
Campbell's Soup Can #1365
Produced: 2026-01-03 12:59:49
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def woody_quote():
    # ANSI escape codes for colors and styles
    class Style:
        BOLD = '\033[1m'
        ITALIC = '\033[3m'
        CYAN = '\033[36m'
        MAGENTA = '\033[35m'
        YELLOW = '\033[33m'
        END = '\033[0m'
        BLINK = '\033[5m'

    # Create ASCII art frame
    frame_top = r'''
  ____                            _     
 / ___|___  _ __  _ __ ___  _   _| |__  
| |   / _ \| '_ \| '__/ _ \| | | | '_ \ 
| |__| (_) | | | | | | (_) | |_| | |_) |
 \____\___/|_| |_|_|  \___/ \__,_|_.__/ 
'''
    
    quote = f"{Style.BOLD}{Style.MAGENTA}\"The universe is a terrifyingly large place{Style.END}{Style.BLINK},{Style.END}\n" \
            f"{Style.BOLD}{Style.MAGENTA}which is why I prefer to spend most of it inside{Style.END}\n" \
            f"{Style.BOLD}{Style.MAGENTA}worrying about whether I locked my apartment door.\"{Style.END}\n\n" \
            f"{Style.ITALIC}{Style.YELLOW}― Woody Allen (probably){Style.END}"

    # Print with animation
    for line in frame_top.split('\n'):
        print(f"{Style.CYAN}{line}{Style.END}")
        time.sleep(0.1)
    
    print("\n")
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    
    # Add blinking cursor effect at end
    time.sleep(1)
    print(f"\n\n{Style.BLINK}...{Style.END}")

if __name__ == "__main__":
    woody_quote()