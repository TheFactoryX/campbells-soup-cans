"""
Campbell's Soup Can #1478
Produced: 2026-01-08 17:43:40
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, color, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        if char == '.':
            time.sleep(0.2)
        elif char == ',':
            time.sleep(0.1)
        else:
            time.sleep(delay)
    sys.stdout.write('\033[0m\n')
    sys.stdout.flush()

def woody_quote():
    # Colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # Box drawing characters
    horizontal = '═'
    vertical = '║'
    corner_tl = '╔'
    corner_tr = '╗'
    corner_bl = '╚'
    corner_br = '╝'
    
    clear_screen()
    
    # Print top border with animation
    for i in range(77):
        sys.stdout.write(CYAN + corner_tl + horizontal * i + ' ' * (76 - i) + corner_tr + END + '\r')
        sys.stdout.flush()
        time.sleep(0.02)
    print()
    
    # Title
    print(vertical + ' ' + BOLD + YELLOW + "WOODY ALLEN ON LIFE" + END + ' ' * (71 - len("WOODY ALLEN ON LIFE")) + vertical)
    
    # Separator
    print(vertical + WHITE + ' ' * 76 + END + vertical)
    
    # Woody Allen ASCII art
    woody = [
        "      ,--./,-.",
        "     / #      \\",
        "    |          |",
        "    |   O   O  |",
        "    |     ,    |",
        "     \\   '-'  /",
        "      `-----`"
    ]
    
    for line in woody:
        print(vertical + WHITE + '  ' + line + ' ' * (74 - len(line)) + END + vertical)
    
    # Another separator
    print(vertical + WHITE + ' ' * 76 + END + vertical)
    
    # Main quote with typing effect
    quote = vertical + WHITE + '  ' + ITALIC + "\"I tried to be a philosopher once, but I couldn't make a living at it. So I settled for neurosis, which pays much better if you're willing to work overtime.\"" + END
    type_text(quote, WHITE, 0.02)
    
    # Another separator
    print(vertical + WHITE + ' ' * 76 + END + vertical)
    
    # Signature with animation
    for _ in range(3):
        sys.stdout.write(vertical + RED + '  ' + BOLD + '- Woody Allen' + END + ' ' * (71 - len('- Woody Allen')) + vertical + '\r')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(vertical + WHITE + '  ' + BOLD + '- Woody Allen' + END + ' ' * (71 - len('- Woody Allen')) + vertical + '\r')
        sys.stdout.flush()
        time.sleep(0.5)
    
    # Bottom border with animation
    print()
    for i in range(77):
        sys.stdout.write(CYAN + corner_bl + horizontal * i + ' ' * (76 - i) + corner_br + END + '\r')
        sys.stdout.flush()
        time.sleep(0.02)
    print()

if __name__ == "__main__":
    woody_quote()