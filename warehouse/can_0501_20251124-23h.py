"""
Campbell's Soup Can #501
Produced: 2025-11-24 23:30:05
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def woody_quote():
    colors = {
        'red': '\033[91m',
        'yellow': '\033[93m',
        'blink': '\033[5m',
        'reset': '\033[0m'
    }
    
    quote = [
        "  The universe is probably just a random cosmic joke,  ",
        "   but here I am - late to therapy again, wearing      ",
        "  mismatched socks, and worrying about whether ants    ",
        "    judge us for stressing over things like death.     "
    ]
    
    frame_top = f"{colors['red']}┌──────────────────────────────────────────────────────┐{colors['reset']}"
    frame_bottom = f"{colors['red']}└──────────────────────────────────────────────────────┘{colors['reset']}"
    frame_side = f"{colors['red']}│{colors['reset']}"
    
    print("\n"*2)
    print(frame_top)
    
    for line in quote:
        sys.stdout.write(frame_side)
        for char in line:
            sys.stdout.write(f"{colors['yellow']}{char}{colors['reset']}")
            sys.stdout.flush()
            time.sleep(0.03)
        print(frame_side.rstrip())
        time.sleep(0.3)
    
    print(frame_bottom)
    print(f"\n{colors['blink']}       _{colors['reset']}\n")

woody_quote()