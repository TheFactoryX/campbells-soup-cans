"""
Campbell's Soup Can #450
Produced: 2025-11-22 16:35:45
Worker: xAI: Grok 4.1 Fast (x-ai/grok-4.1-fast)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'

def typewriter(text, delay=0.04, color=''):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Colors.RESET)

def thinking_animation():
    icons = ['🤔', '😟', '😵‍💫', '🤯']
    for _ in range(3):
        for i, icon in enumerate(icons):
            dots = '.' * (i + 1)
            sys.stdout.write(f'\r{Colors.BOLD}{Colors.PURPLE}{icon} Woody ponders{dots}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.4)
    print('\r' + ' ' * 50 + '\r')

def main():
    # Clear screen for drama
    print('\033[2J\033[H', end='')
    
    # Marquee title with spin-in effect
    title = "  WOODY ALLEN'S NEUROTIC NIGHTMARE  "
    width = len(title) + 4
    top_bottom = '═' * width
    print(Colors.BOLD + Colors.CYAN + '╔' + top_bottom + '╗' + Colors.RESET)
    for _ in range(3):
        print(Colors.CYAN + '║' + Colors.RESET + ' ' * width + Colors.CYAN + '║' + Colors.RESET)
    print(Colors.BOLD + Colors.CYAN + '║  ' + Colors.RESET + title.center(width - 2) + Colors.CYAN + '  ║' + Colors.RESET)
    for _ in range(2):
        print(Colors.CYAN + '║' + Colors.RESET + ' ' * width + Colors.CYAN + '║' + Colors.RESET)
    print(Colors.BOLD + Colors.CYAN + '╚' + top_bottom + '╝' + Colors.RESET)
    print()
    
    # Thinking animation
    thinking_animation()
    
    # The quote box
    quote = "The universe is merely a bad joke, and I'm the punchline that nobody gets."
    q_width = len(quote) + 6
    print(Colors.BOLD + Colors.GREEN + '╔' + '═' * q_width + '╗' + Colors.RESET)
    print(Colors.GREEN + '║  ' + Colors.RESET, end='')
    typewriter(Colors.BOLD + Colors.ITALIC + Colors.YELLOW + quote, 0.035, Colors.BOLD + Colors.ITALIC + Colors.YELLOW)
    print(Colors.GREEN + '  ║' + Colors.RESET)
    print(Colors.BOLD + Colors.GREEN + '╚' + '═' * q_width + '╝' + Colors.RESET)
    
    # Fade out stars
    print()
    stars = ['✦', '✧', '✩', '✪']
    for _ in range(20):
        star = stars[(_//5) % 4]
        sys.stdout.write('\r' + Colors.WHITE + star * 4 + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.08)
    print('\r')

if __name__ == "__main__":
    main()