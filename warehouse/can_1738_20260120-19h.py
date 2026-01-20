"""
Campbell's Soup Can #1738
Produced: 2026-01-20 19:13:15
Worker: Z.AI: GLM 4.5 Air (z-ai/glm-4.5-air)
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

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BG_BLACK = '\033[40m'
    BG_WHITE = '\033[107m'

def type_text(text, color=Colors.WHITE, delay=0.03, new_line=True):
    """Simulate typing effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    if new_line:
        print()

def print_frame(text, width=70, color=Colors.YELLOW):
    """Print text in a decorative frame"""
    horizontal = '═' * width
    corners = '╔╗║╝╚'
    
    # Top border
    type_text(f"{color}{corners[0]}{horizontal[:width-2]}{corners[1]}", color)
    
    # Top padding
    type_text(f"{color}{corners[2]}{' ' * (width-2)}{corners[2]}", color)
    
    # Text with word wrapping
    words = text.split()
    line = ""
    for word in words:
        test_line = line + word + " "
        if len(test_line) > width - 4:
            type_text(f"{color}{corners[2]} {line:<{width-4}} {corners[2]}", color)
            line = word + " "
        else:
            line = test_line
    if line:
        type_text(f"{color}{corners[2]} {line.strip():<{width-4}} {corners[2]}", color)
    
    # Bottom padding
    type_text(f"{color}{corners[2]}{' ' * (width-2)}{corners[2]}", color)
    
    # Bottom border
    type_text(f"{color}{corners[5]}{horizontal[:width-2]}{corners[4]}", color)

def draw_emoji_face():
    """Draw a simple ASCII face representing Woody's neurotic nature"""
    face = [
        "  (╯°□°）╯︵ ┻━┻ ",
        "  ︵ヽ(`Д´)ﾉ︵ ┻━┻ "
    ]
    for line in face:
        type_text(line, Colors.MAGENTA, delay=0.05)

def print_thought_bubble():
    """Print a thought bubble with additional musings"""
    bubble = [
        Colors.CYAN + "   ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○",
        Colors.CYAN + "  ○                                                     ○",
        Colors.CYAN + "  ○  " + Colors.ITALIC + "You know, I once thought about writing a book..." + Colors.CYAN + "  ○",
        Colors.CYAN + "  ○  " + Colors.ITALIC + "But then I realized I'd have to write it." + Colors.CYAN + "     ○",
        Colors.CYAN + "  ○                                                     ○",
        Colors.CYAN + "   ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○"
    ]
    for line in bubble:
        print(line)
    print(Colors.END)

def main():
    # Clear screen (works on Unix and Windows)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Title card
    title = Colors.BOLD + Colors.UNDERLINE + Colors.BLUE + "WOODY ALLEN'S PHILOSOPHER" + Colors.END
    type_text(title.center(80), Colors.BLUE, 0.02)
    
    # Draw Woody's face
    time.sleep(0.5)
    draw_emoji_face()
    
    # The main quote
    time.sleep(1)
    woody_quote = Colors.BOLD + Colors.WHITE + "I tried to find meaning in the universe, but all I found was a parking meter that had expired." + Colors.END
    print_frame(woody_quote, width=75, color=Colors.YELLOW)
    
    # additional thoughts
    time.sleep(1.5)
    print_thought_bubble()
    
    # Self-deprecating commentary
    time.sleep(0.5)
    commentary = Colors.ITALIC + Colors.GREEN + "— Woody Allen, probably after getting another parking ticket" + Colors.END
    type_text(commentary.center(80), Colors.GREEN, 0.01)
    
    # Final signature
    time.sleep(0.8)
    signature = Colors.BOLD + Colors.MAGENTA + "\n\n\t\"I'd rather be vaguely right than precisely wrong.\"" + Colors.END
    type_text(signature, Colors.MAGENTA, 0.02)
    
    time.sleep(2)

if __name__ == "__main__":
    main()