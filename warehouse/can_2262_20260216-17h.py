"""
Campbell's Soup Can #2262
Produced: 2026-02-16 17:02:59
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_woody():
    return [
        "    ,--.    ",
        "   ( oo )   ",
        "    \\__/    ",
        "  .-\"\"\"-.  ",
        " /  O O  \\ ",
        "|    ∆    |",
        " \\  \\_/  / ",
        "  '-----'  "
    ]

def colorful_typewriter(text, delay=0.02, color='\033[96m'):
    for char in text:
        sys.stdout.write(color + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    clear_screen()
    
    # ANSI color codes
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'
    
    # Our Woody Allen-style quote (original creation)
    quote_lines = [
        "I'm not afraid of death; I just don't want to be there",
        "when it happens. But I'm terrified of being there when",
        "it *doesn't* happen. Like waiting for a bus that never",
        "comes. And I left my umbrella at home during a drought.",
        "Existential crisis: 1, Common sense: zip."
    ]
    
    # Calculate dimensions
    inner_width = max(len(line) for line in quote_lines) + 6
    box_width = inner_width + 4
    
    # Print Woody ASCII art with color pulse animation
    woody = print_woody()
    for _ in range(3):
        for i, line in enumerate(woody):
            pulse = RED if i % 2 == 0 else YELLOW
            padding = (box_width - len(line)) // 2
            print(' ' * padding + pulse + line + END)
            time.sleep(0.05)
        clear_screen()
        time.sleep(0.1)
    
    # Print final Woody figure
    for line in woody:
        padding = (box_width - len(line)) // 2
        print(' ' * padding + YELLOW + line + END)
    
    print()
    
    # Print top border with animation
    top = "╱" + "∿" * (inner_width) + "╲"
    sys.stdout.write(' ' * ((box_width - len(top)) // 2) + BLUE)
    for char in top:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(END)
    
    # Print quote with typewriter effect and color changes
    for i, line in enumerate(quote_lines):
        color = CYAN if i % 2 == 0 else PURPLE
        padded = line.center(inner_width)
        
        # Left border
        sys.stdout.write(' ' * ((box_width - inner_width) // 2) + BLUE + "▌" + END)
        
        # Animated text
        for char in padded:
            sys.stdout.write(color + char + END)
            sys.stdout.flush()
            time.sleep(0.025)
        
        # Right border
        sys.stdout.write(BLUE + "▌" + END + "\n")
        time.sleep(0.1)
    
    # Print bottom border with reverse animation
    bottom = "╲" + "∿" * (inner_width) + "╱"
    sys.stdout.write(' ' * ((box_width - len(bottom)) // 2) + BLUE)
    for char in reversed(bottom):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(END)
    
    # Add wobbly footer with neurotic afterthought
    time.sleep(0.5)
    afterthought = " (Also, is this monitor judging me?) "
    wobble = ""
    for i, char in enumerate(afterthought):
        wobble += char + ('\b' if i % 2 == 0 else ' ')
        sys.stdout.write(YELLOW + wobble + ' ' * (len(afterthought) - len(wobble)) + END + '\r')
        sys.stdout.flush()
        time.sleep(0.08)
    print(YELLOW + afterthought + ' ' * 5 + END)

if __name__ == "__main__":
    main()