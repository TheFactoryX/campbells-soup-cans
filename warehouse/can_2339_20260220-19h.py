"""
Campbell's Soup Can #2339
Produced: 2026-02-20 19:06:27
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import textwrap
import random

def main():
    reset = '\033[0m'
    yellow = '\033[93m'
    cyan = '\033[96m'
    red = '\033[91m'
    bold = '\033[1m'
    
    quote = (
        "I'm not afraid of death; I'm afraid of arriving at the pearly gates\n"
        "only to discover they've lost my application. And honestly,\n"
        "what's the point of eternity if there's no coffee service?"
    )
    
    try:
        columns = os.get_terminal_size().columns
    except:
        columns = 80
    
    box_width = min(55, columns - 8)
    wrapper = textwrap.TextWrapper(width=box_width-4, expand_tabs=False)
    wrapped = wrapper.fill(quote)
    lines = [line.ljust(box_width-4) for line in wrapped.split('\n')]
    
    top = '╒' + '═' * (box_width-2) + '╕'
    bottom = '╘' + '═' * (box_width-2) + '╛'
    left_pad = ' ' * ((columns - box_width) // 2)
    
    face = ['(•_•)', '( •_•)>⌐■-■', '(⌐■_■)']
    
    print(f"\n{left_pad}{red}{face[0]}{reset}")
    time.sleep(0.3)
    print(f"{left_pad}{red}{face[1]}{reset}")
    time.sleep(0.4)
    print(f"{left_pad}{red}{face[2]}{reset}\n")
    time.sleep(0.2)
    
    print(f"{left_pad}{yellow}{top}{reset}")
    
    for line in lines:
        print(f"{left_pad}{yellow}│ {reset}", end='', flush=True)
        
        for char in line:
            delay = 0.008 + random.random() * 0.015
            print(f"{cyan}{char}{reset}", end='', flush=True)
            time.sleep(delay)
            
        print(f"{yellow} │{reset}")
        time.sleep(0.05)
    
    print(f"{left_pad}{yellow}{bottom}{reset}")
    time.sleep(0.3)
    footer = f"{left_pad}  {cyan}~ Woody's existential crisis, delivered hot and neurotic ~{reset}"
    print(footer)

if __name__ == "__main__":
    main()