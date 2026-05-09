"""
Campbell's Soup Can #3625
Produced: 2026-05-09 22:02:00
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys,time

def colored(txt, name):
    return colors.get(name, '') + txt + colors['reset']

colors = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m'
}

def typewrite(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

quote = "I'm not afraid of death; I just don't want to be there when it happens."
border_top = "╔═════════════════════════╗"
border_mid_left = "║  "
border_mid_right = "  ║"
border_bottom = "╚════════════════════════╝"

typewrite(colored(border_top, 'yellow'))
typewrite(colored(border_mid_left + quote + border_mid_right, 'cyan'))
typewrite(colored(border_bottom, 'yellow'))