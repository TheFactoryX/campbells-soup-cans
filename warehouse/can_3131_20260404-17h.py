"""
Campbell's Soup Can #3131
Produced: 2026-04-04 17:47:55
Worker: Anthropic: Claude Sonnet 4 (anthropic/claude-sonnet-4)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_quote_theater():
    # ANSI color codes
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Woody Allen style quote
    quote = "I'm not saying I'm paranoid, but my therapist's couch has trust issues."
    
    clear_screen()
    
    # Title animation
    title = "🎭 WOODY'S WISDOM THEATER 🎭"
    print(f"\n{BOLD}{MAGENTA}")
    for char in title:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print(f"{RESET}\n")
    
    time.sleep(1)
    
    # Create a fancy box
    box_width = 60
    print(f"{CYAN}{'╔' + '═' * (box_width-2) + '╗'}")
    print(f"║{' ' * (box_width-2)}║")
    
    # Word-by-word reveal with colors
    words = quote.split()
    colors = [RED, YELLOW, GREEN, BLUE, MAGENTA, CYAN]
    
    line = "║ "
    for i, word in enumerate(words):
        color = colors[i % len(colors)]
        if len(line + word + " ") > box_width - 3:
            # Pad the line and print it
            padding = box_width - len(line) - 1
            print(f"{line}{' ' * padding}║")
            line = f"║ {color}{word}{CYAN} "
        else:
            line += f"{color}{word}{CYAN} "
        
        # Print current state
        temp_padding = box_width - len(line) - 1
        print(f"\r{line}{' ' * temp_padding}║", end='', flush=True)
        time.sleep(0.3)
    
    # Final line padding
    final_padding = box_width - len(line) - 1
    print(f"\r{line}{' ' * final_padding}║")
    
    print(f"║{' ' * (box_width-2)}║")
    print(f"{'╚' + '═' * (box_width-2) + '╝'}{RESET}")
    
    # Signature with typewriter effect
    signature = "~ Woody Allen (probably having an existential crisis)"
    print(f"\n{YELLOW}{BOLD}", end='')
    for char in signature:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print(f"{RESET}")
    
    # Animated thinking emoji
    thinking_frames = ['🤔', '💭', '😰', '🤷‍♂️']
    print(f"\n{WHITE}Woody's current mood: ", end='')
    for _ in range(8):
        for frame in thinking_frames:
            print(f"\r{WHITE}Woody's current mood: {frame}", end='', flush=True)
            time.sleep(0.3)
    
    # Final flourish
    print(f"\n\n{BOLD}{GREEN}Remember: Anxiety is just excitement without breath!{RESET}")
    print(f"{CYAN}{'═' * 60}{RESET}\n")

if __name__ == "__main__":
    woody_quote_theater()