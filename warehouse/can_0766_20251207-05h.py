"""
Campbell's Soup Can #766
Produced: 2025-12-07 05:32:10
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

YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def main():
    box_width = 50
    inner_width = box_width - 2

    def make_border(corner_start, corner_end):
        s = corner_start
        for _ in range(inner_width):
            if random.random() < 0.2:
                s += random.choice(['╌', '┄', '┈', '┄', '─', '╌'])
            else:
                s += '─'
        s += corner_end
        return s

    top_border = make_border('┌', '┐')
    bottom_border = make_border('└', '┘')
    
    quote_lines = [
        "Existence is like a bad relationship:",
        "I'm nervous, sweating, and hoping it ends—",
        "but I'm not sure I'll get a second chance."
    ]

    padded_lines = [line.center(inner_width) for line in quote_lines]

    def print_with_jitter(text, color, end='', newline_delay=0.0):
        print(color, end='', flush=True)
        for char in text:
            time.sleep(0.002 + random.random() * 0.006)
            print(char, end='', flush=True)
        if newline_delay > 0: time.sleep(newline_delay)
        print(RESET if end == '\n' else '', end=end, flush=True)

    print_with_jitter(top_border, YELLOW, '\n')
    
    for line in padded_lines:
        left_char = random.choice(['│', '┆', '┊', '┆']) if random.random() < 0.3 else '│'
        right_char = random.choice(['│', '┆', '┊', '┆']) if random.random() < 0.3 else '│'
        
        print(YELLOW, end='', flush=True)
        time.sleep(0.002 + random.random() * 0.006)
        print(left_char, end='', flush=True)
        
        print_with_jitter(line, CYAN, '')
        
        print(YELLOW, end='', flush=True)
        time.sleep(0.002 + random.random() * 0.006)
        print(right_char, end='', flush=True)
        
        print(RESET, end='\n')

    print_with_jitter(bottom_border, YELLOW, '\n')

    # Add a trembling effect at the end
    for _ in range(3):
        time.sleep(0.05)
        print(f"{YELLOW}  (I think I'm having an existential crisis...){RESET}", end='\r')
        time.sleep(0.05)
        print(" " * 40, end='\r')
    print(f"{YELLOW}  (I think I'm having an existential crisis...){RESET}")

if __name__ == "__main__":
    main()