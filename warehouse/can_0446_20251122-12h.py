"""
Campbell's Soup Can #446
Produced: 2025-11-22 12:53:09
Worker: Qwen: Qwen3 235B A22B (free) (qwen/qwen3-235b-a22b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

BLUE = '\033[94m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def print_shaky_char(char, y_offset):
    """Print a character with slight vertical vibration"""
    vibration = "   \n  \n \n" if y_offset % 4 == 0 else "  \n \n\n   "
    sys.stdout.write(vibration + CYAN + char + RESET + '\r')
    sys.stdout.flush()
    time.sleep(0.005)

def main():
    # Woody Allen-style original philosophical quote
    quote = "I'm not afraid of death; I'm just terrified of being introduced as 'that guy who hasn't finished his bagel.'"
    
    # Create a neurotically vibrating film reel border
    lines = textwrap.wrap(quote, width=45)
    max_len = max(len(line) for line in lines)
    reel_width = max_len + 8
    
    # Print top film reel sprockets
    print(CYAN + "  o  " * (reel_width // 5) + RESET)
    print(BLUE + "┌" + "─" * reel_width + "┐" + RESET)
    
    # Print quote with nervous typewriter effect and border vibration
    for i, line in enumerate(lines):
        # Left sprocket vibration
        for _ in range(4):
            print_shaky_char("o", i)
        
        # Type out quote with neurotic hesitation (extra delay on commas)
        sys.stdout.write(BLUE + "│  " + YELLOW)
        for char in line.ljust(max_len):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03 if char in ',;' else 0.02)
            if char in ',;':
                time.sleep(0.05)  # Woody's trademark hesitation
        sys.stdout.write(RESET + "  " + BLUE + "│" + RESET)
        
        # Right sprocket vibration
        for _ in range(4):
            print_shaky_char("o", i)
        print()
    
    # Print bottom film reel sprockets with fading effect
    print(BLUE + "└" + "─" * reel_width + "┘" + RESET)
    end_sprockets = ""
    for _ in range(reel_width // 5):
        end_sprockets += "  o "
        sys.stdout.write(CYAN + end_sprockets + RESET + '\r')
        time.sleep(0.1)
    print(CYAN + "  o  " * (reel_width // 5) + RESET)
    
    # Final existential sigh
    time.sleep(0.5)
    print(YELLOW + "\n  (deep sigh) The universe is meaningless... " + 
          "but at least this coffee is adequately hot.\n" + RESET)

if __name__ == "__main__":
    main()