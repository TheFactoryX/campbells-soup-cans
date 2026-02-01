"""
Campbell's Soup Can #1986
Produced: 2026-02-01 14:45:14
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

# ANSI color codes
class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woody():
    # Woody Allen silhouette with animated glasses
    woody = [
        Colors.CYAN + "    O    " + Colors.END,
        Colors.CYAN + "   /|\\   " + Colors.END,
        Colors.CYAN + "   / \\   " + Colors.END,
        Colors.YELLOW + "  /___\\  " + Colors.END,
        Colors.YELLOW + "  |   |  " + Colors.END,
        Colors.YELLOW + "  |___|  " + Colors.END,
    ]
    
    for i in range(2):
        for j, line in enumerate(woody):
            if j == 1:  # The head line with glasses
                time.sleep(0.1)
                if i % 2 == 0:
                    modified_line = line.replace("/|\\", "/|\\")
                else:
                    modified_line = line.replace("/|\\", "|")
                print(Colors.BLUE + "║" + Colors.END + " " * 25 + modified_line + " " * (45) + Colors.BLUE + "║" + Colors.END)
            else:
                print(Colors.BLUE + "║" + Colors.END + " " * 25 + line + " " * (45) + Colors.BLUE + "║" + Colors.END)
        time.sleep(0.2)

def print_quote():
    # ASCII art border
    border = Colors.BLUE + "╔" + "═" * 70 + "╗" + Colors.END
    side = Colors.BLUE + "║" + Colors.END
    
    # Title with typewriter effect
    type_text(Colors.BOLD + Colors.MAGENTA + "\nWOODY ALLEN ON LIFE AND DEATH...\n" + Colors.END, 0.05)
    
    print()
    print(border)
    
    # Draw Woody Allen
    draw_woody()
    
    # Main quote with different colors for different parts
    quote = Colors.BOLD + Colors.CYAN + "I'm not afraid of death, I'm just afraid that I'll waste my life" + Colors.END
    quote2 = Colors.YELLOW + "worrying about death and then die anyway without having really lived." + Colors.END
    quote3 = Colors.MAGENTA + "It's like buying a movie ticket and spending the whole time worrying about" + Colors.END
    quote4 = Colors.GREEN + "the parking meter. You miss the show! And the popcorn's expensive!" + Colors.END
    quote5 = Colors.RED + " Woody Allen's Guide to Existential Dread" + Colors.END
    
    # Print the quote with typewriter effect
    type_text(side + " " * 3 + quote + " " * (70 - len(quote) - 4) + side, 0.02)
    type_text(side + " " * 3 + quote2 + " " * (70 - len(quote2) - 4) + side, 0.02)
    type_text(side + " " * 3 + quote3 + " " * (70 - len(quote3) - 4) + side, 0.02)
    type_text(side + " " * 3 + quote4 + " " * (70 - len(quote4) - 4) + side, 0.02)
    
    print(side + " " * 70 + side)
    print(side + " " * 27 + quote5 + " " * (70 - len(quote5) - 30) + side)
    
    print(Colors.BLUE + "╚" + "═" * 70 + "╝" + Colors.END)
    print()

def main():
    # Print the quote
    print_quote()
    
    # Add a philosophical footer with typewriter effect
    time.sleep(1)
    type_text(Colors.GREEN + "\nAs he once said: 'I'd rather be a superb meteor, every atom of me in magnificent glow, than a sleepy and permanent planet.'" + Colors.END, 0.03)
    type_text(Colors.ITALIC + Colors.CYAN + "\n...And now, if you'll excuse me, I have to go worry about whether my life insurance premiums are too high." + Colors.END)
    print()

if __name__ == "__main__":
    main()