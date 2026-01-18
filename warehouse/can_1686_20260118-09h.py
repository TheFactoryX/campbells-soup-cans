"""
Campbell's Soup Can #1686
Produced: 2026-01-18 09:33:50
Worker: Deep Cogito: Cogito v2.1 671B (deepcogito/cogito-v2.1-671b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def print_slowly(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ",.!?\n":
            time.sleep(delay * 3)
        elif char not in " ":
            time.sleep(delay)

def animate_woody():
    colors = ['\033[95m', '\033[93m', '\033[91m', '\033[94m']
    end_color = '\033[0m'
    
    for i in range(5):
        for color in colors:
            print("\n" * 2)
            face = f"""{color}
            .-~~^-. 
            :      :    .-~~~-.
           :       :  .'        '.
           :       : :            :
            :     : :              :
             '---' .'   {i}         '
                  :                 :
                  :     .---.       :
                   :   /  .  \      :
                   :  :       :     |
______             /   :       :     |
\     \           /     \     /     / 
 \     \         /       \   /     /  
  \_____\_______/__________\_______/_____{end_color}"""
            
            print(face, end="\r")
            time.sleep(0.3)
            sys.stdout.flush()

    quote = """\033[92m
    "Life is full of misery and suffering 
    and it's all over much too soon— 
    which is probably for the best 
    because frankly, I don't think 
    I could handle much more of it."
    \033[0m"""
    
    time.sleep(0.5)
    print("\n" * 5)
    
    print_slowly(" " * 10 + "WOODY ALLEN SAYS...\n\n")
    
    time.sleep(1)
    print_slowly(quote, delay=0.05)
    
    print("\n" * 3)
    print(" " * 20 + "(rushes out nervously)")

if __name__ == "__main__":
    print()
    animate_woody()
    print()