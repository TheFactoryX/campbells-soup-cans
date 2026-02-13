"""
Campbell's Soup Can #2199
Produced: 2026-02-13 11:47:16
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_typing(text, delay=0.03, color='\033[95m'):
    for char in text:
        sys.stdout.write(color + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)

def main():
    width = 50
    quote = "I'm not afraid of death; I just don't want to be there when it happens. I'd rather be at a nice restaurant. The food is terrible, but at least I'm still alive! ...Wait, why am I talking about food? I'm having an existential crisis over a side salad."
    
    # ANSI color codes
    border = '\033[94m'
    text_color = '\033[95m'
    woody_color = '\033[93m'
    reset = '\033[0m'
    
    # Calculate lines for quote
    lines = []
    words = quote.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += (" " + word) if current_line else word
        else:
            lines.append(current_line.ljust(width))
            current_line = word
    if current_line:
        lines.append(current_line.ljust(width))
    
    # Print top border
    print(border + "┌" + "─" * width + "┐" + reset)
    
    # Print quote with typing effect
    for line in lines:
        print(border + "│" + reset, end="")
        print_typing(line, 0.025, text_color)
        print(border + "│" + reset)
    
    # Print bottom border
    print(border + "└" + "─" * width + "┘" + reset)
    
    # Print Woody figure with animation
    woody = [
        "  @---@      ",
        "  | O |      ",
        "  | _ |      ",
        "  `---'      ",
        "   / \\       ",
        "  /   \\      ",
        " /     \\     ",
        "v       v    "
    ]
    
    # Fade-in animation for Woody
    for i in range(10):
        sys.stdout.write('\033[2J\033[H')  # Clear screen
        print(border + "┌" + "─" * width + "┐" + reset)
        
        for line in lines:
            print(border + "│" + reset, end="")
            print(line, end="")
            print(border + "│" + reset)
        
        print(border + "└" + "─" * width + "┘" + reset)
        
        for j, w_line in enumerate(woody):
            if i > j:
                sys.stdout.write(woody_color + w_line[:i-j] + reset)
                if i-j < len(w_line):
                    sys.stdout.write(" " * (len(w_line) - (i-j)))
            else:
                sys.stdout.write(" " * len(w_line))
            sys.stdout.write("\n")
        
        sys.stdout.flush()
        time.sleep(0.08)
    
    # Final Woody with thought bubble
    sys.stdout.write('\033[2J\033[H')
    print(border + "┌" + "─" * width + "┐" + reset)
    
    for line in lines:
        print(border + "│" + reset, end="")
        print(line, end="")
        print(border + "│" + reset)
    
    print(border + "└" + "─" * width + "┘" + reset)
    
    print(woody_color + "  @---@      " + reset + "  ┌─────────────────────┐")
    print(woody_color + "  | O |      " + reset + "  │ What if the afterlife │")
    print(woody_color + "  | _ |      " + reset + "  │ is just a bad restaurant? │")
    print(woody_color + "  `---'      " + reset + "  └─────────────────────┘")
    print(woody_color + "   / \\       " + reset)
    print(woody_color + "  /   \\      " + reset)
    print(woody_color + " /     \\     " + reset)
    print(woody_color + "v       v    " + reset)
    
    # Final message
    print("\n" + text_color + "  *adjusts glasses*  " + reset + "I've been thinking about this while waiting for my soup...")

if __name__ == "__main__":
    main()