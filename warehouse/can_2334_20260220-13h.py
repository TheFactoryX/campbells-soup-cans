"""
Campbell's Soup Can #2334
Produced: 2026-02-20 13:33:33
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def woodya():
    # Woody Allen's neurotic existential quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "- Woody Allen"
    
    # Clear screen with fancy effect
    sys.stdout.write("\033[2J\033[H")
    time.sleep(0.3)
    
    # Get terminal width
    try:
        width = min(80, int(os.popen('stty size', 'r').read().split()[1])) if 'posix' in sys.builtin_module_names else 80
    except:
        width = 80
    
    # Create a wobbly border (Allen's neuroticism in visual form)
    border_chars = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▂']
    
    # Animated intro
    print("\033[36m", end="")  # Cyan for neurotic anxiety
    for i in range(14):
        sys.stdout.write('\r' + ' '*(width//2-20) + border_chars[i]*40)
        time.sleep(0.05)
    print("\033[0m")
    time.sleep(0.2)
    
    # Center the box
    box_width = min(70, width-4)
    left_pad = (width - box_width) // 2
    
    # Print top border with wobble
    sys.stdout.write(' '*left_pad)
    for i in range(14):
        char = border_chars[(i+2) % 14]
        sys.stdout.write(f"\033[33m{char}\033[0m")  # Gold border
        time.sleep(0.01)
    print()
    
    # Print quote with dramatic pacing
    words = quote.split()
    current_line = ""
    line_num = 0
    
    for word in words:
        test_line = current_line + " " + word if current_line else word
        if len(test_line) <= box_width - 6:  # Account for padding
            current_line = test_line
        else:
            # Print current line with animation
            print(' '*left_pad + "\033[32m│\033[0m", end="")  # Green bar
            
            # Typewriter effect for each word in line
            for w in current_line.split():
                for char in w:
                    sys.stdout.write(f"\033[1;33m{char}\033[0m")  # Bold yellow text
                    time.sleep(random.uniform(0.01, 0.05))
                sys.stdout.write(" ")
                time.sleep(0.03)
            
            # Pad to box width
            padding = box_width - 6 - len(current_line)
            print(' '*padding + "\033[32m│\033[0m")
            time.sleep(0.1)
            current_line = word
            line_num += 1
    
    # Print last line
    if current_line:
        print(' '*left_pad + "\033[32m│\033[0m", end="")
        for w in current_line.split():
            for char in w:
                sys.stdout.write(f"\033[1;33m{char}\033[0m")
                time.sleep(random.uniform(0.01, 0.05))
            sys.stdout.write(" ")
        padding = box_width - 6 - len(current_line)
        print(' '*padding + "\033[32m│\033[0m")
    
    # Empty line for visual separation (Allen's existential pause)
    time.sleep(0.3)
    print(' '*left_pad + "\033[32m│\033[0m" + ' '*(box_width-4) + "\033[32m│\033[0m")
    
    # Author with signature flourish
    time.sleep(0.2)
    author_pad = box_width - 6 - len(author)
    print(' '*left_pad + "\033[32m│\033[0m", end="")
    for char in author:
        sys.stdout.write(f"\033[2;36m{char}\033[0m")  # Dim cyan signature
        time.sleep(0.05)
    print(' '*author_pad + "\033[32m│\033[0m")
    
    # Bottom border with reverse animation
    time.sleep(0.2)
    sys.stdout.write(' '*left_pad)
    for i in range(14):
        char = border_chars[(12-i) % 14]
        sys.stdout.write(f"\033[33m{char}\033[0m")
        time.sleep(0.01)
    print("\n")
    
    # Final existential fade
    time.sleep(0.5)
    print("\033[90m" + ' '*((width-48)//2) + "⊕ Nothing is as profound as the fear of being inconsequential ⊕\033[0m\n")

if __name__ == "__main__":
    try:
        import os
        woodya()
    except KeyboardInterrupt:
        print("\n\033[31m[Cancelled - even Woody Allen would understand]\033[0m")
    except:
        print("\033[31m[Existential error: the universe is indifferent to this program]\033[0m")