"""
Campbell's Soup Can #227
Produced: 2025-11-12 13:03:04
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
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

def print_with_typewriter(text, delay=0.05):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_woody_allen_quote():
    # ANSI color codes
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'reset': '\033[0m'
    }
    
    # Clear screen with a fun effect
    print('\033[2J\033[H', end='')  # Clear screen and move cursor to top-left
    
    # Print header with animations
    header = f"{colors['magenta']}{colors['bold']}"
    header += "╔" + "═" * 58 + "╗\n"
    header += "║" + " " * 58 + "║\n"
    header += "║"
    header += " " * 10
    for char in "WOODY ALLEN'S NEUROTIC WISDOM":
        header += f"{colors['cyan']}{char}{colors['magenta']}"
        sys.stdout.write(header[-1:])
        sys.stdout.flush()
        time.sleep(0.08)
    header += " " * 10 + "║\n"
    header += "║" + " " * 58 + "║\n"
    header += "╚" + "═" * 58 + "╝"
    print(header + colors['reset'])
    
    print("\n" * 2)
    
    # The quote (original Woody Allen-style)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    attribution = "— Woody Allen (probably while lying awake at 3 AM)"
    
    # Print quote box with shaky effect
    box_width = 60
    quote_lines = [
        "I'm not afraid of death; I just don't want to be there when",
        "it happens. I mean, who wants to be the last one at the",
        "party? Especially when the cleanup crew arrives. And",
        "what if there's an afterlife and it's just like Newark?",
        "Only with worse parking."
    ]
    
    # Draw animated box
    print(f"{colors['yellow']}╔", end="")
    for _ in range(box_width - 2):
        print("═", end="", flush=True)
        time.sleep(0.02)
    print("╗")
    
    # Print quote with jitter effect
    for line in quote_lines:
        padding = box_width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        
        # Add slight "jitter" to simulate neurotic energy
        jitter_offset = random.randint(-1, 1)
        actual_left = max(1, left_pad + jitter_offset)
        actual_right = max(1, right_pad - jitter_offset)
        
        print(f"║{' ' * actual_left}{colors['white']}{line}{' ' * actual_right}║{colors['yellow']}")
        time.sleep(0.3)
    
    print(f"╚", end="")
    for _ in range(box_width - 2):
        print("═", end="", flush=True)
        time.sleep(0.02)
    print("╝")
    
    # Print attribution with fade-in effect
    print("\n")
    for i in range(3):
        print(" " * (62 + i), end="")
        print(f"{colors['blue']}{attribution}{colors['reset']}")
        time.sleep(0.4)
    
    # Add some philosophical doodles
    doodles = [
        "    ☠️   ⚰️   🕰️   💊   🛋️   📖   🔍",
        "   (•_•) <(‽)─┤ ╟─   (•_•) (⌐■_■)",
        "   Existential dread: brought to you by anxiety!",
        "   ※ Follow me on SchopenhauerSpace for more content ※"
    ]
    
    print(f"\n{colors['green']}")
    for doodle in doodles:
        print_with_typewriter(" " * random.randint(5, 15) + doodle, 0.03)
    print(colors['reset'])
    
    # Final neurotic afterthought
    afterthought = "\n   P.S. On second thought, maybe I should've said something\n   more profound. Or at least checked my facts. What if\n   I'm wrong about death? What if there IS an afterlife\n   and they're all judging my quotes? Oh God."
    
    print(f"{colors['red']}{afterthought}{colors['reset']}")

if __name__ == "__main__":
    print_woody_allen_quote()