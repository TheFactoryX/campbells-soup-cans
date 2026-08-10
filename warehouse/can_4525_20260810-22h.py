"""
Campbell's Soup Can #4525
Produced: 2026-08-10 22:55:58
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def print_rainbow(text):
    """Print text character by character with rainbow colors."""
    colors = ['\033[91m', '\033[93m', '\033[92m', 
              '\033[96m', '\033[95m', '\033[94m']
    for idx, char in enumerate(text):
        color = colors[idx % len(colors)]
        sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
    sys.stdout.write('\033[0m\n')  

def main():
    lines = [
        "I'm not afraid of death,",
        "I just don't want to be there when it happens."
    ]
    
    max_len = max(len(line) for line in lines)
    border_color = '\033[1;36m'
    reset = '\033[0m'
    
    top = f"{border_color}╔{'═'*max_len}╗{reset}"
    print(top)
    
    for line in lines:
        left = f"{border_color}║ {reset}"
        right = f"{border_color}║{reset}"
        
        sys.stdout.write(left)
        print_rainbow(line)
        sys.stdout.write(right + '\n')
    
    bottom = f"{border_color}╚{'═'*max_len}╝{reset}"
    print(bottom)

if __name__ == "__main__":
    main()