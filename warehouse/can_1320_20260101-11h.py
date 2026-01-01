"""
Campbell's Soup Can #1320
Produced: 2026-01-01 11:29:32
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def woody_print(text, color_code, delay=0.05):
    colors = {
        'yellow': '\033[93m',
        'red': '\033[91m',
        'cyan': '\033[96m',
        'reset': '\033[0m'
    }
    color = colors.get(color_code, colors['reset'])
    for char in text:
        sys.stdout.write(color + char + colors['reset'])
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote = """
    The universe is a vast, indifferent void – 
    but have you seen the WiFi bill? That's real terror.
    """
    author = "— Woody Allen's Neurotic Cousin"

    # ASCII art book
    woody_print(r'''
      _______
     /      /
    /      /
   /______/ 
  |      |  
  |  ?   |  
  |______|  
    ''', 'red', 0.01)

    time.sleep(0.5)
    
    # Print quote in a box
    lines = quote.strip().split('\n')
    max_len = max(len(line.strip()) for line in lines)
    
    woody_print('╔' + '═' * (max_len + 2) + '╗', 'cyan')
    for line in lines:
        padded = '║ ' + line.strip().center(max_len) + ' ║'
        woody_print(padded, 'yellow')
    woody_print('╚' + '═' * (max_len + 2) + '╝', 'cyan')
    
    time.sleep(0.3)
    woody_print('\n' + author.center(max_len + 4), 'red', 0.03)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nLife is meaningless anyway...")