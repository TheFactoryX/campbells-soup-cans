"""
Campbell's Soup Can #1398
Produced: 2026-01-05 02:39:26
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
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
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end="")

def animate_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_woody_allen_quote():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "My brain: it's my second favorite organ, but it's overrated and frankly quite needy.",
        "Existential dread is nature's way of telling you to order more takeout.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I've been neurotic since before it was cool. My anxiety had anxiety when it was a fetus.",
        "The universe is a vast, meaningless void, and yet somehow I still worry about my hair.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    ]
    
    chosen_quote = random.choice(quotes)
    
    # Create visual frame
    print()
    print_color("╔" + "═" * 78 + "╗", "1;37")
    print()
    print_color("║", "1;37")
    
    # Woody Allen ASCII art
    woody_art = [
        "    🎬 WOODY ALLEN'S EXISTENTIAL CORNER 🎬    ",
        "",
        "     ╭─────────────────────────────╮      ",
        "     │  <glasses emoji>  neurotic   │      ",
        "     │   (╯°□°）╯︵ ┻━┻             │      ",
        "     ╰─────────────────────────────╯      ",
        ""
    ]
    
    for line in woody_art:
        print_color(" " * 15, "1;33")
        print_color(line, "1;33")
        print_color("║", "1;37")
        print()
    
    print_color("║", "1;37")
    print()
    
    # Print the quote with animation
    words = chosen_quote.split()
    quote_lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= 60:
            current_line += " " + word if current_line else word
        else:
            quote_lines.append(current_line.center(70))
            current_line = word
    if current_line:
        quote_lines.append(current_line.center(70))
    
    colors = ["1;31", "1;33", "1;32", "1;36", "1;35"]
    color_idx = 0
    
    for i, line in enumerate(quote_lines):
        print_color("║", "1;37")
        print_color("  " + line + "  ", colors[color_idx % len(colors)])
        print_color("║", "1;37")
        print()
        color_idx += 1
    
    print_color("║", "1;37")
    print()
    print_color("╚" + "═" * 78 + "╝", "1;37")
    print()
    
    # Animated signature
    signature = "                   ~ Woody Allen's subconscious                      "
    animate_text(signature, 0.03)
    print()
    
    # Flashing "THE END" animation
    flashing_colors = ["1;91", "1;93", "1;92", "1;96", "1;95"]
    end_message = "           ✨  That's it. Go contemplate your existence.  ✨"
    
    for i in range(10):
        clear_screen()
        print()
        print_color("╔" + "═" * 78 + "╗", "1;37")
        print()
        print_color("║", "1;37")
        
        for line in woody_art:
            print_color(" " * 15, "1;33")
            print_color(line, "1;33")
            print_color("║", "1;37")
            print()
        
        print_color("║", "1;37")
        print()
        
        color_idx = 0
        for line in quote_lines:
            print_color("║", "1;37")
            print_color("  " + line + "  ", colors[color_idx % len(colors)])
            print_color("║", "1;37")
            print()
            color_idx += 1
        
        print_color("║", "1;37")
        print()
        print_color("╚" + "═" * 78 + "╝", "1;37")
        print()
        print_color(signature, "1;37")
        print()
        print_color(end_message, flashing_colors[i % len(flashing_colors)])
        print()
        
        time.sleep(0.3)
    
    print()
    print_color(" " * 30 + "(Probably)", "1;90")
    print()

if __name__ == "__main__":
    try:
        clear_screen()
        print_woody_allen_quote()
    except KeyboardInterrupt:
        print("\n\nAlright, alright, I'll stop philosophizing...")
        sys.exit(0)