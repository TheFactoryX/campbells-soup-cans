"""
Campbell's Soup Can #5049
Produced: 2026-10-01 05:55:39
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import sys

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright foreground
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03, color=Colors.WHITE):
    """Type text out like a typewriter"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border(char='═', width=60, color=Colors.CYAN):
    """Print a decorative border"""
    print(color + char * width + Colors.RESET)

def center_text(text, width=60, color=Colors.WHITE):
    """Center text within given width"""
    padding = (width - len(text)) // 2
    print(color + ' ' * padding + text + ' ' * (width - len(text) - padding) + Colors.RESET)

def woody_allen_quote():
    """Display a Woody Allen style quote with visual flair"""
    clear_screen()
    
    # Animated intro
    print_border('◆', 60, Colors.BRIGHT_MAGENTA)
    time.sleep(0.5)
    
    for line in [
        "",
        Colors.BRIGHT_YELLOW + "    ╔══════════════════════════════════════════════════════════╗" + Colors.RESET,
        Colors.BRIGHT_YELLOW + "    ║" + Colors.RESET + Colors.BRIGHT_CYAN + "              WOODY ALLEN STYLE PHILOSOPHY                " + Colors.RESET + Colors.BRIGHT_YELLOW + "║" + Colors.RESET,
        Colors.BRIGHT_YELLOW + "    ╚══════════════════════════════════════════════════════════╝" + Colors.RESET,
        ""
    ]:
        print(line)
        time.sleep(0.3)
    
    time.sleep(0.5)
    
    # The quote
    quote = "I don't mind being pessimistic. It's the optimists who worry me."
    author = "— Woody Allen (probably)"
    
    # Quote box
    print_border('═', 60, Colors.BLUE)
    print(Colors.BLUE + "║" + Colors.RESET, end="")
    print(Colors.BLUE + "║" + Colors.RESET)
    
    # Empty space
    print(Colors.BLUE + "║" + Colors.RESET + " " * 58 + Colors.BLUE + "║" + Colors.RESET)
    
    # Quote text with word wrapping
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) <= 50:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    
    # Print each line centered
    for line in lines:
        print(Colors.BLUE + "║" + Colors.RESET, end="")
        padding = (58 - len(line)) // 2
        print(" " * padding + Colors.BRIGHT_WHITE + Colors.BOLD + line + Colors.RESET + " " * (58 - len(line) - padding) + Colors.BLUE + "║" + Colors.RESET)
    
    # Empty space
    print(Colors.BLUE + "║" + Colors.RESET + " " * 58 + Colors.BLUE + "║" + Colors.RESET)
    
    # Author
    print(Colors.BLUE + "║" + Colors.RESET, end="")
    author_padding = (58 - len(author)) // 2
    print(" " * author_padding + Colors.ITALIC + Colors.MAGENTA + author + Colors.RESET + " " * (58 - len(author) - author_padding) + Colors.BLUE + "║" + Colors.RESET)
    
    # Empty space
    print(Colors.BLUE + "║" + Colors.RESET + " " * 58 + Colors.BLUE + "║" + Colors.RESET)
    
    print_border('═', 60, Colors.BLUE)
    
    time.sleep(1)
    
    # Add some existential dread
    print()
    type_text(Colors.RED + "Existential crisis level: " + Colors.BRIGHT_RED + "MAXIMUM", 0.05)
    time.sleep(0.5)
    
    # Some philosophical musings
    musings = [
        "The universe is indifferent to our suffering.",
        "Death is the only certainty in an uncertain world.",
        "We're all just temporary arrangements of stardust.",
        "Meaning is what we invent to avoid the void."
    ]
    
    for musing in musings:
        type_text(Colors.ITALIC + Colors.YELLOW + musing + Colors.RESET, 0.04)
        time.sleep(0.3)
    
    print()
    print_border('◆', 60, Colors.BRIGHT_MAGENTA)
    
    # Final touch - Woody Allen's nervous laugh
    print()
    time.sleep(0.5)
    for laugh in ["Ha ha ha...", "Oh, brother...", "What's the point?"]:
        print(Colors.GREEN + laugh + Colors.RESET)
        time.sleep(0.7)

if __name__ == "__main__":
    try:
        woody_allen_quote()
    except KeyboardInterrupt:
        print("\n" + Colors.RED + "Even Woody Allen's neurosis was interrupted..." + Colors.RESET)