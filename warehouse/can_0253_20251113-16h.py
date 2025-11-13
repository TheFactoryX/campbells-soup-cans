"""
Campbell's Soup Can #253
Produced: 2025-11-13 16:40:58
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
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
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03, color=Colors.WHITE):
    """Create a typewriter effect for the text"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.END + '\n')

def wobble_text(text, wobble_count=3):
    """Create a slight wobble effect to represent neurosis"""
    wobble_chars = "∼"
    for i in range(wobble_count):
        for j in range(len(text)):
            # Move cursor back and forth
            sys.stdout.write(f"\033[1D\033[1C")
            sys.stdout.write(wobble_chars[j % len(wobble_chars)])
            sys.stdout.flush()
            time.sleep(0.05)
        # Return to normal
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()

def draw_frame(width, height, title="WOODY ALLEN ON LIFE"):
    """Draw an ASCII frame around the text"""
    # Top border
    print(Colors.CYAN + BOLD + "╔" + "═" * (width + 2) + "╗")
    print(Colors.CYAN + BOLD + "║" + " " * (width + 2) + "║")
    
    # Title
    title_padding = (width - len(title)) // 2
    print(Colors.CYAN + BOLD + "║" + " " * title_padding + Colors.YELLOW + title + Colors.CYAN + " " * (width - len(title) - title_padding) + "║")
    print(Colors.CYAN + BOLD + "║" + " " * (width + 2) + "║")
    
    # Content area
    for _ in range(height):
        print(Colors.CYAN + BOLD + "║" + " " * (width + 2) + "║")
    
    # Bottom border
    print(Colors.CYAN + BOLD + "╚" + "═" * (width + 2) + "╝" + Colors.END)

def main():
    # Clear screen
    clear_screen()
    
    # The Woody Allen-style quote
    quote = """To be or not to be? That's not really the question.
    The real question is: if I'm not being, who's going to pay my rent?
    And also, why do I always pick the wrong relationships?
    It's like the universe is playing some kind of cosmic joke on me,
    and I'm the straight man in a comedy that nobody finds funny."""
    
    # Create the visual presentation
    draw_frame(70, 10)
    
    # Add some visual flair
    print(Colors.MAGENTA + " " * 28 + "✧･ﾟ: *✧･ﾟ:*" + Colors.END)
    print(Colors.MAGENTA + " " * 20 + "WOODY ALLEN'S PHILOSOPHICAL MUSINGS" + Colors.END)
    print(Colors.MAGENTA + " " * 28 + "*:･ﾟ✧*:･ﾟ✧" + Colors.END)
    
    # Print the quote with typewriter effect
    typewriter_effect(quote, delay=0.02, color=Colors.YELLOW)
    
    # Add a neurotic foot note
    time.sleep(1)
    typewriter_effect("\n\nP.S. - I wrote this while eating a bagel and worrying about death.", 
                     delay=0.03, color=Colors.GREEN)
    
    # Final wobble effect for the entire quote
    time.sleep(1)
    wobble_text(quote.replace("\n", " ").replace("    ", " "))
    
    # Sign off
    print(Colors.BOLD + Colors.WHITE + "\n\n\t- Woody Allen (probably)" + Colors.END)

if __name__ == "__main__":
    main()