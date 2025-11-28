"""
Campbell's Soup Can #575
Produced: 2025-11-28 09:33:31
Worker: Meituan: LongCat Flash Chat (free) (meituan/longcat-flash-chat:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import os
import sys
import itertools

def clear():
    # Clear screen (works on most terminals)
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.08, color="\033[97m"):
    for char in text:
        print(color + char + "\033[0m", end='', flush=True)
        time.sleep(delay)
    print()

def draw_funny_philosopher():
    # ASCII art philosopher with anxious expression & coffee
    art = r"""
                 ___
               ,'   '.
              / @   @ \   ("I'm not depressed, it's just my resting existentialist face.")
             (  >   <  )
              |       |       /|
              |  .-.  |      / \..
               \/   \/       \___)
        ______  ||||         )  |
       /      \ ||||        /  /     ☕ "It's 5am somewhere in my psyche..."
      |  ||    |\||||       |  |
      |  ||    | ||||       |_/|
      |__||____|_||||       /__)
     /            |//      |__ \\
    /_____________/ |      |__)
                 ||
                __||
           _____|__|
    """
    for line in art.splitlines():
        print("\033[93m" + line + "\033[0m")
        time.sleep(0.05)

def draw_woody_box():
    quote = (
        "I took a course in existential dread. On the first day,\n"
        "I dropped it. I don't need the credits to fail at life."
    )
    
    # Wrap text in box with color cycling border
    width = max(len(line) for line in quote.splitlines()) + 6
    top_bottom = "┌" + "─" * (width-2) + "┐"
    middle = "│  " + (" " * (width-6)) + "  │"
    
    colors = [
        "\033[91m", "\033[93m",  "\033[92m", 
        "\033[96m", "\033[95m", "\033[97m"
    ]
    
    for color in itertools.cycle(colors):
        clear()
        draw_funny_philosopher()
        print("\n" + color + top_bottom)
        print(middle)
        
        for line in quote.splitlines():
            print(f"│  \033[97m{line:<{width-6}}\033[0m" + color + "  │")
        
        print(middle)
        print("└" + "─" * (width-2) + "┘" + "\033[0m")
        
        # Floating ellipses of doom... slowly filling with neurosis
        neurosis = "..." * (int(time.time() * 2) % 4 + 1)
        print(f"\033[90m(no one will ever love me{neurosis})\033[0m")
        
        time.sleep(0.2)
        
        # Escape after 10 seconds or first keypress (if stdin is terminal)
        if os.isatty(sys.stdin.fileno()):
            try:
                import select
                if select.select([sys.stdin], [], [], 0)[0]:
                    break
            except:
                if int(time.time() - start_time) > 10:
                    break
        else:
            if int(time.time() - start_time) > 10:
                break

if __name__ == "__main__":
    start_time = time.time()
    
    # First: dramatic single-line buildup
    print("\033[2J\033[H")  # Clear and home
    animate_text("PROOF THAT EXISTENCE IS MOSTLY...", 0.12, "\033[95m")
    time.sleep(0.5)
    animate_text("...WAITING FOR YOUR COFFEE TO COOL", 0.08, "\033[93m")
    time.sleep(1)
    print("\n")
    
    # Then go to full box animation
    draw_woody_box()
    
    # Final blow: self-deprecating epilogue
    clear()
    print("\033[90m\n\n")
    print(" "*30 + "P.S. This program contains")
    print(" "*32 + "more bugs than my psyche.")
    print(" "*33 + "(Just ignore the segfault.)")
    print("\033[0m\n")
    time.sleep(1.5)
    
    # Fade out
    for _ in range(3):
        print()
        time.sleep(0.3)
    sys.stdout.write("\033[2J")  # Clear one last time
    sys.stdout.write("\033[30m...and that, folks, is why therapy is cheaper than existentialism." + "\033[0m\033[1A\r")
    time.sleep(0.5)
    sys.exit(0)