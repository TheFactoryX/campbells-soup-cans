"""
Campbell's Soup Can #832
Produced: 2025-12-10 05:37:06
Worker: Qwen: Qwen3 235B A22B (free) (qwen/qwen3-235b-a22b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def print_woody_quote():
    quote = [
        "I'd like to relive my life... but with more sleep",
        "and fewer metaphysical emergencies. Wait, that's just napping."
    ]
    
    max_len = max(len(line) for line in quote) + 4
    colors = [
        '\033[96m',  # cyan
        '\033[93m',  # yellow
        '\033[95m',  # magenta
        '\033[92m'   # green
    ]
    
    for frame in range(25):
        shift = random.randint(0, 3)
        flicker = random.choice([0, 1, 2])
        color = colors[frame % len(colors)]
        
        # Clear screen and position cursor
        sys.stdout.write('\033[H\033[J')
        
        # Build vibrating frame
        top = ' ' * shift + '\033[93m' + '✦═' * ((max_len // 2) + flicker) + '\033[0m'
        bottom = ' ' * shift + '\033[93m' + '═✦' * ((max_len // 2) + flicker) + '\033[0m'
        
        # Print the masterpiece
        print(top)
        for line in quote:
            padded = line.center(max_len - 2)
            jitter = ' ' * random.randint(0, 2)
            sys.stdout.write(f"{' ' * shift}\033[93m║\033[0m{jitter}{color}{padded}{jitter}\033[93m║\033[0m\n")
            time.sleep(0.03)
        print(bottom)
        
        # Add neurotic cursor
        cursor_pos = shift + 2 + random.randint(5, max_len - 10)
        sys.stdout.write(f"\033[H\033[{frame + 3}B{' ' * cursor_pos}\033[91m♱\033[0m\n")
        
        # Breathe anxiety into existence
        time.sleep(0.07 + random.uniform(0, 0.05))
    
    # Final frame with shaky conclusion
    sys.stdout.write('\033[H\033[J')
    print('\033[93m' + '✦═' * 15 + '✦\033[0m')
    for line in quote:
        print(f"\033[93m║ \033[1;96m{line.center(46)} \033[93m║\033[0m")
    print('\033[93m' + '═✦' * 15 + '═\033[0m')
    print(" " * 18 + "\033[3m(Woody Allen, probably)\033[0m")

if __name__ == "__main__":
    print_woody_quote()