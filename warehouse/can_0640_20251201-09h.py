"""
Campbell's Soup Can #640
Produced: 2025-12-01 09:43:17
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import sys
import time
import os

def colored(text, color):
    colors = {
        'red': '\033[91m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'reset': '\033[0m'
    }
    return colors[color] + text + colors['reset']

def centered_text(text, width=70):
    return text.center(width)

def animated_title(title):
    title_len = len(title)
    for i in range(1, title_len + 1):
        sys.stdout.write('\r' + title[:i])
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print('\r')

def main():
    title = colored("|||  BOO!  |||", 'red')
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    
    # ASCII art of wooden coffin
    coffin_art = [
        "      [1;33mWWWWWWWWWWWWWWWW[0m",
        "     [1;33mWW       [1;31mOS[0m[1;31mOSE[0m[1;33m       [0m",
        "     [1;33mWW[1;31m* [0m[1;31m*[0m[1;31m [0m[1;31m*[0m[1;33m[1;31m***[0m[1;33m        [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
        "     [1;33mWW[1;31m*[0m[1;31m                     [0m[1;33m      [0m",
    ]
    
    # Print animated title
    animated_title(title)
    
    # Calculate screen dimensions
    rows, cols = map(int, os.popen('stty size', 'r').read().split())
    
    # Clear screen
    sys.stdout.write('\033[2J\033[H')  # clear screen and move to top
    
    # Print animated coffin
    for line in coffin_art:
        print(line)
        time.sleep(0.03)
    
    # Print box around quote
    box_width = 50
    print()
    print('=' * box_width)
    print('|' + centered_text('' , box_width-2) + '|')
    print('|' + centered_text(colored(quote, 'blue'), box_width-2) + '|')
    print('=' * box_width)

if __name__ == "__main__":
    main()