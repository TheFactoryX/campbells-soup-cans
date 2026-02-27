"""
Campbell's Soup Can #2464
Produced: 2026-02-27 14:58:42
Worker: Qwen: Qwen3 Coder Next (qwen/qwen3-coder-next)
Employment: Paid
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

def slow_print(text, delay=0.04, color='\033[93m'):
    """Print text character by character with a delay and color"""
    sys.stdout.write(color)
    sys.stdout.flush()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[0m\n')

def ascii_art():
    """Create a Woody Allen-style brain animation"""
    brain = [
        "     ..::!!**%%&&@@@@&&%%**!!::..     ",
        "  .::!!**%%&&@@@@@@@@@@&&%%**!!::.  ",
        " .::!!**%%&&@@@@@@@@@@@@@&%%**!!::. ",
        " .::!!**%%&&&@@@@@@@@@@@@&%%**!!::. ",
        "  .::!!**%%&&&&&&&&&&&&&&&%%**!!::. ",
        "    .::!!**%%&&&&&&&&&&&&%%**!!::.  ",
        "      .::!!**%%&&&&&&&&%%**!!::.    ",
        "        .::!!**%%&&&&%%**!!::.      ",
        "          .::!!**%%&%%**!!::.       ",
        "            .::!!******!!::.        ",
        "               .::!!::..            "
    ]
    
    colors = [
        '\033[91m',  # Red
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
        '\033[92m',  # Green
    ]
    
    for frame in range(8):
        clear_screen()
        print("\n" * 2)
        
        # Print animated brain
        for i, line in enumerate(brain):
            color = colors[(frame + i) % len(colors)]
            # Add subtle movement
            offset = "  " if (frame + i) % 2 == 0 else "   "
            print(offset + color + line + "\033[0m")
        
        # Print title
        print("\n" * 2)
        title = "the existential dread generator"
        title_color = colors[frame % len(colors)]
        slow_print(title, 0.01, title_color)
        
        time.sleep(0.2)

def main():
    clear_screen()
    
    # Animated intro
    ascii_art()
    
    # Create a fancy box for the quote
    quote = "I'm not afraid of death—I just don't want to be there when it happens. I'd rather be home with a good book, worrying about germs and the stock market, than floating in the cosmic void contemplating my insignificance. At least with germs, there's a cure... eventually."
    
    box_width = 74
    border_color = '\033[96m'
    quote_color = '\033[93m'
    author_color = '\033[95m'
    
    # Animated box drawing
    clear_screen()
    print("\n" * 3)
    
    # Top border
    sys.stdout.write(border_color)
    sys.stdout.write("┌" + "━" * box_width + "┐\033[0m\n")
    sys.stdout.flush()
    
    # Empty lines for effect
    time.sleep(0.3)
    sys.stdout.write(border_color)
    sys.stdout.write("┃" + " " * box_width + "┃\033[0m\n")
    sys.stdout.flush()
    
    time.sleep(0.3)
    
    # Print quote with character animation
    slow_print("┃" + " " * 3 + quote + " " * 3 + "┃", 0.02, quote_color)
    
    time.sleep(0.3)
    
    # Bottom empty line
    sys.stdout.write(border_color)
    sys.stdout.write("┃" + " " * box_width + "┃\033[0m\n")
    sys.stdout.flush()
    
    # Author line
    author = "— Woody Allen (probably while checking his pulse)"
    author_line = "└" + "─" * box_width + "┘"
    time.sleep(0.3)
    sys.stdout.write(border_color)
    sys.stdout.write("└" + "─" * box_width + "┘\033[0m\n")
    
    # Print author with a subtle underline effect
    sys.stdout.write(author_color)
    sys.stdout.write(" " * 3 + author + "\n\033[0m")
    sys.stdout.flush()
    
    # Final decorative elements
    print("\n" * 2)
    slow_print("⚠ WARNING: Excessive self-awareness detected", 0.05, '\033[91m')
    slow_print("💡 PRO TIP: Worry about something productive, like your tax returns", 0.05, '\033[92m')
    
    # Interactive element
    time.sleep(1)
    print("\n" * 2)
    input("Press Enter to panic about the meaning of life...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + '\033[91m' + "AHA! Even Ctrl+C can't escape the anxiety! 😅" + '\033[0m')
        time.sleep(1)
        print("Just kidding... or am I?")