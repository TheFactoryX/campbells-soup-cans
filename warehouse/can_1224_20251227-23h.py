"""
Campbell's Soup Can #1224
Produced: 2025-12-27 23:31:00
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

def print_slow(text, delay=0.1, color=None):
    colors = {
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "pink": "\033[95m",
        "reset": "\033[0m"
    }
    for char in text:
        if color:
            sys.stdout.write(colors[color] + char + colors["reset"])
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote = [
        "Life is", "like", "a", "horror", "movie", "where", "you're", "both",
        "the", "victim", "AND", "the", "villain—", "but", "you", "forgot", 
        "to", "buy", "popcorn.", "\n      --", "*sigh*", "--", "Woody"
    ]
    
    print("\033[2J\033[H")  # Clear screen
    print_slow("\033[95m(•_•)\\ \033[0m", 0.05)
    print_slow("\033[95m( •_•)>⌐■-■\033[0m", 0.05)
    print_slow("\033[95m(⌐■_■)\033[0m\033[90m▄ ■\033[0m", 0.05)
    print()
    
    border = "\033[90m" + "╭" + "─"*42 + "╮" + "\033[0m"
    print(border)
    
    for i, word in enumerate(quote):
        color = "yellow" if i < 5 else "cyan" if i < 12 else "pink"
        end = " " if word not in ["but", "AND"] else "\n     "
        print_slow(word, 0.1, color=color, end=end)
    
    print("\n" + "\033[90m" + "╰" + "─"*42 + "╯" + "\033[0m")
    print("\033[93m" + "        [Cue nervous jazz music]" + "\033[0m")

if __name__ == "__main__":
    main()