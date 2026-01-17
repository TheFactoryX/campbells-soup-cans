"""
Campbell's Soup Can #1674
Produced: 2026-01-17 19:26:57
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
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

# ANSI escape codes for colors and styles
class Text:
    YELLOW = "\033[93m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_quote():
    # Original Woody Allen-style quote
    quote = "Life is " + Text.RED + "utterly meaningless" + Text.END + ", \nbut " + Text.GREEN + "at least the coffee's good" + Text.END + " – \nif you remember to buy milk."

    # ASCII art box dimensions
    height = 7
    width = max([len(line) for line in quote.split("\n")]) + 4
    
    # Animation sequence
    for i in range(1, height+1):
        clear_screen()
        
        # Draw top border
        if i == 1:
            print(Text.MAGENTA + "╔" + "═"*(width-2) + "╗" + Text.END)
        else:
            print(Text.MAGENTA + "║" + Text.END + " "*(width-2) + Text.MAGENTA + "║" + Text.END)
        
        # Reveal text progressively
        if i >= 3 and i <= 5:
            lines = quote.split("\n")
            line_num = i - 3
            padding = " " * ((width - len(lines[line_num]) - 2) // 2)
            print(Text.MAGENTA + "║" + Text.END + padding + Text.BOLD + Text.YELLOW + lines[line_num] + padding + Text.END + (" " if (width - len(lines[line_num])) % 2 else "") + Text.MAGENTA + "║" + Text.END)
        else:
            print(Text.MAGENTA + "║" + Text.END + " "*(width-2) + Text.MAGENTA + "║" + Text.END)
        
        # Draw bottom border
        if i == height:
            print(Text.MAGENTA + "╚" + "═"*(width-2) + "╝" + Text.END)
        
        time.sleep(0.3)
    
    print("\n" + Text.CYAN + "("*35 + ")" + Text.END)
    print(Text.BLUE + " "*12 + "🗯️  A Moment of Existential Clarity 🗯️" + Text.END)
    time.sleep(2)
    
    # Typing animation for attribution
    attribution = Text.WHITE + Text.UNDERLINE + "\n– Woody Allen probably never said this" + Text.END
    for char in attribution:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

if __name__ == "__main__":
    animate_quote()
    print("\n\n")  # Space at end for terminal prompt