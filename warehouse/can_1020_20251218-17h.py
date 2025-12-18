"""
Campbell's Soup Can #1020
Produced: 2025-12-18 17:38:41
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
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
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    colors = [
        '\033[91m',  # Red
        '\033[92m',  # Green
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Purple
        '\033[96m',  # Cyan
        '\033[97m',  # White
    ]
    
    clear_screen()
    
    margin_top = 5
    for _ in range(margin_top):
        print()
    
    print(" " * 15 + "🐛" + " " * 64)
    print()
    print(" " * 10 + "📚 Woody Allen's Philosophical Corner 📚")
    print()
    print(" " * 15 + "🐛" + " " * 64)
    print()
    print()
    
    border = "┏" + "━" * 68 + "┓"
    padding = "┃" + " " * 68 + "┃"
    bottom_border = "┗" + "━" * 68 + "┛"
    
    print(" " * 3 + border)
    print(" " * 3 + padding)
    
    words = quote.split()
    x_offset = 8
    pulse_range = 5
    
    for pulse in range(pulse_range):
        clear_screen()
        for _ in range(margin_top):
            print()
        
        print(" " * 15 + "🐛" + " " * 64)
        print()
        print(" " * 10 + "📚 Woody Allen's Philosophical Corner 📚")
        print()
        print(" " * 15 + "🐛" + " " * 64)
        print()
        print()
        
        print(" " * 3 + border)
        print(" " * 3 + padding)
        
        current_color = colors[pulse % len(colors)]
        text_lines = []
        current_line = ""
        word_count = 0
        
        for i, word in enumerate(words):
            display_word = word if i == 10 else word
            if len(current_line) + len(display_word) + 1 > 65:
                text_lines.append(current_line)
                current_line = display_word
                word_count = 0
            else:
                if current_line:
                    current_line += " "
                current_line += display_word
                word_count += 1
        
        if current_line:
            text_lines.append(current_line)
        
        pulse_offset = (pulse_range - 1) // 2 - pulse
        line_offset = 1
        
        for line in text_lines:
            line_pos_x = x_offset + abs(pulse_offset) * 2
            
            spaces = 70 - len(line)
            left_spaces = max(0, spaces // 2 - 1)
            
            centered_line = " " * left_spaces + line + " " * (70 - left_spaces - len(line) - 1)
            
            print(" " * 3 + "┃" + current_color + centered_line + "\033[0m" + "┃")
            line_offset += 1
        
        for _ in range(7 - len(text_lines)):
            print(" " * 3 + padding)
        
        print(" " * 3 + bottom_border)
        
        for _ in range(7):
            print()
        
        delay = 0.1
        arrow_symbol = "✨"
        print(" " * 60 + f"  {arrow_symbol} Theo's Thoughts {arrow_symbol}")
        
        time.sleep(delay)
    
    for _ in range(10):
        clear_screen()
        for _ in range(margin_top):
            print()
        
        print(" " * 15 + "🐛" + " " * 64)
        print()
        print(" " * 10 + "📚 Woody Allen's Philosophical Corner 📚")
        print()
        print(" " * 15 + "🐛" + " " * 64)
        print()
        print()
        
        print(" " * 3 + border)
        print(" " * 3 + padding)
        
        final_color = random.choice(colors)
        
        for line in text_lines:
            spaces = 70 - len(line)
            left_spaces = max(0, spaces // 2 - 1)
            centered_line = " " * left_spaces + line + " " * (70 - left_spaces - len(line) - 1)
            print(" " * 3 + "┃" + final_color + centered_line + "\033[0m" + "┃")
        
        for _ in range(7 - len(text_lines)):
            print(" " * 3 + padding)
        
        print(" " * 3 + bottom_border)
        
        for _ in range(5):
            print()
        
        print(" " * 54 + "   ╔════════════════════╗")
        print(" " * 54 + "   ║  Quote by: Theo    ║")
        print(" " * 54 + "   ║  (Woody's nephew)  ║")
        print(" " * 54 + "   ╚════════════════════╝")
        
        time.sleep(0.15)

if __name__ == "__main__":
    try:
        animate_quote()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Life goes on... mainly.")
        sys.exit(0)