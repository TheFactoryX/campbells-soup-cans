"""
Campbell's Soup Can #2692
Produced: 2026-03-10 23:42:28
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

# ANSI escape codes for colors
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
    ITALIC = '\033[3m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_frame(text):
    """Creates a fancy frame around text"""
    border_color = Colors.CYAN
    text_color = Colors.MAGENTA
    
    # Top border
    print(border_color + "╔" + "═" * 72 + "╗" + Colors.END)
    
    # Title
    print(border_color + "║" + Colors.END + " " * 30 + Colors.BOLD + Colors.YELLOW + "WOODY ALLEN" + Colors.END + " " * 30 + border_color + "║" + Colors.END)
    print(border_color + "║" + Colors.END + " " * 30 + Colors.BOLD + Colors.YELLOW + "PHILOSOPHY" + Colors.END + " " * 30 + border_color + "║" + Colors.END)
    
    # Empty line
    print(border_color + "║" + " " * 72 + "║" + Colors.END)
    
    # Text with wrapping
    words = text.split()
    line = ""
    for word in words:
        if len(line + word) < 68:
            line += word + " "
        else:
            print(border_color + "║" + Colors.END + "  " + text_color + line + Colors.END + " " * (72 - len(line) - 4) + border_color + "║" + Colors.END)
            line = word + " "
    
    if line:
        print(border_color + "║" + Colors.END + "  " + text_color + line + Colors.END + " " * (72 - len(line) - 4) + border_color + "║" + Colors.END)
    
    # Bottom border
    print(border_color + "╚" + "═" * 72 + "╝" + Colors.END)

def woody_art():
    """ASCII art representation of Woody Allen"""
    art = """
    {0}      .--.
     |o_o |
     |:_/ |
    //   \\ \\
   (|     | )
  /'\\_   _/`\\
  /___\\=)___\\{1}
    """.format(
        Colors.YELLOW, Colors.END
    )
    type_text(art)

def main():
    clear_screen()
    
    # Woody Allen ASCII art
    woody_art()
    
    # Pause for effect
    time.sleep(1)
    
    # The Woody Allen style quote
    quote = """I'm not afraid of death; I'm just afraid of dying before I get to finish telling you how much I hate my neurotic life.
    
    You know, I was once at a therapist's office, and he said to me, "Woody, you have a deep-seated fear of mortality." And I said, "No kidding? 
    I thought it was just a fear of commitment and spiders!" The truth is, life is full of misery, loneliness, and suffering - and it's all over much too soon.
    
    But hey, look on the bright side - at least we're not hamsters. They run on wheels all day and what do they get? A little pellet of food. 
    I mean, what's the point of that? At least in show business, we get awards, recognition, and occasionally, a decent table at Sardi's."""
    
    # Display the quote in a fancy frame
    woody_frame(quote)
    
    # Add a signature
    print("\n" + Colors.ITALIC + Colors.CYAN + "                 - Woody Allen, probably while worrying about something" + Colors.END)
    
    # Add a final animated message
    messages = [
        "NEUROSIS: IT'S NOT JUST FOR BREAKFAST ANYMORE!",
        "I'D WORRY ABOUT THAT... IF I HAD THE TIME!",
        "ANXIETY: MY CONSTANT AND FAITHFUL COMPANION",
        "IF I'M NOT WORRIED, SOMETHING MUST BE WRONG!"
    ]
    
    for i, msg in enumerate(messages):
        color = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE][i % 4]
        print("\r" + " " * 30 + "\r" + Colors.BOLD + color + msg + Colors.END, end="")
        time.sleep(1.5)
        print("\r" + " " * 30 + "\r", end="")

if __name__ == "__main__":
    main()