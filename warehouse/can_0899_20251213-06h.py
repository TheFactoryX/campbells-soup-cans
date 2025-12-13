"""
Campbell's Soup Can #899
Produced: 2025-12-13 06:46:12
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def woody_allen_quote():
    # ANSI color codes
    RED = '91'
    GREEN = '92'
    YELLOW = '93'
    BLUE = '94'
    MAGENTA = '95'
    CYAN = '96'
    WHITE = '97'
    
    # Create ASCII art frame
    width = 75
    top_border = "╔" + "═" * (width - 2) + "╗"
    bottom_border = "╚" + "═" * (width - 2) + "╝"
    side_border = "║"
    
    # Woody Allen style quote
    quote = "Sex is only dirty if you're doing it right... but I'm not sure if that's because I'm a pervert or because I'm a philosopher. Probably both. Actually, I'm pretty sure it's both."
    author = " - Woody Allen"
    
    # Opening animation
    clear_screen()
    for i in range(5, 0, -1):
        clear_screen()
        spaces = " " * i
        title = color_text("WOODY ALLEN", RED)
        print("\n" * (10 - i))
        print(spaces + title)
        print("\n" * (10 - i))
        time.sleep(0.2)
    
    # Typewriter effect for title
    clear_screen()
    print(top_border)
    
    title = color_text("WOODY ALLEN PRESENTS", RED)
    typewriter_line = side_border + " "
    for char in title:
        typewriter_line += char
        print(side_border + typewriter_line.ljust(width - 2) + side_border)
        time.sleep(0.05)
    print(side_border + " " * (width - 2) + side_border)
    
    # Subtitle
    subtitle = color_text("A NEUROTIC PHILOSOPHY", YELLOW)
    print(side_border + " " * ((width - len(subtitle)) // 2) + subtitle + " " * ((width - len(subtitle)) // 2) + side_border)
    
    # Separator
    separator = color_text("=" * (width - 2), BLUE)
    print(side_border + separator + side_border)
    
    # Empty lines
    for _ in range(3):
        print(side_border + " " * (width - 2) + side_border)
    
    # Film reel animation
    reel_frames = [
        "[]••••••••••",
        "•[]•••••••••",
        "••[]••••••••",
        "•••[]•••••••",
        "••••[]••••••",
        "•••••[]•••••",
        "••••••[]••••",
        "•••••••[]•••",
        "••••••••[]••",
        "•••••••••[]•",
        "••••••••••[]",
    ]
    
    for frame in reel_frames:
        clear_screen()
        print(top_border)
        
        # Print quote with highlighting
        words = quote.split()
        line = side_border + "  "
        for i, word in enumerate(words):
            if i == len(words) // 2:
                colored_word = color_text(word, GREEN)
            else:
                color = [BLUE, WHITE, CYAN][i % 3]
                colored_word = color_text(word, color)
            
            if len(line) + len(colored_word) + 1 > width - 2:
                print(line)
                line = side_border + "  "
            
            if len(line) > len(side_border) + 1:
                line += " "
            line += colored_word
        
        if len(line) > len(side_border) + 1:
            print(line)
        
        # Empty lines
        for _ in range(2):
            print(side_border + " " * (width - 2) + side_border)
        
        # Film reel frame
        reel_text = color_text(frame, MAGENTA)
        print(side_border + " " * ((width - len(reel_text)) // 2) + reel_text + " " * ((width - len(reel_text)) // 2) + side_border)
        print(bottom_border)
        time.sleep(0.1)
    
    # Final quote display
    clear_screen()
    print(top_border)
    
    words = quote.split()
    line = side_border + "  "
    for i, word in enumerate(words):
        if i == len(words) // 2:
            colored_word = color_text(word, GREEN)
        else:
            color = [BLUE, WHITE, CYAN][i % 3]
            colored_word = color_text(word, color)
        
        if len(line) + len(colored_word) + 1 > width - 2:
            print(line)
            line = side_border + "  "
        
        if len(line) > len(side_border) + 1:
            line += " "
        line += colored_word
    
    if len(line) > len(side_border) + 1:
        print(line)
    
    # Empty lines
    for _ in range(3):
        print(side_border + " " * (width - 2) + side_border)
    
    # Author with thought bubble
    author_text = color_text(author, RED)
    thought_bubble = "○ " + author_text
    print(side_border + " " * ((width - len(thought_bubble)) // 2) + thought_bubble + " " * ((width - len(thought_bubble)) // 2) + side_border)
    print(bottom_border)
    
    # Neurotic thoughts animation
    time.sleep(1)
    
    thoughts = [
        color_text("Did I leave the stove on?", RED),
        color_text("What if I'm not as funny as I think I am?", YELLOW),
        color_text("Is this all there is to life?", BLUE),
        color_text("I should have gone to medical school...", MAGENTA),
        color_text("What's the meaning of it all?", CYAN),
        color_text("Did I just say that out loud?", WHITE),
        color_text("I hope this doesn't affect my therapy session tomorrow...", GREEN),
    ]
    
    for i in range(len(thoughts)):
        clear_screen()
        print(top_border)
        
        # Quote again
        quote_lines = []
        words = quote.split()
        line = side_border + "  "
        for j, word in enumerate(words):
            if j == len(words) // 2:
                colored_word = color_text(word, GREEN)
            else:
                color = [BLUE, WHITE, CYAN][j % 3]
                colored_word = color_text(word, color)
            
            if len(line) + len(colored_word) + 1 > width - 2:
                quote_lines.append(line)
                line = side_border + "  "
            
            if len(line) > len(side_border) + 1:
                line += " "
            line += colored_word
        
        if len(line) > len(side_border) + 1:
            quote_lines.append(line)
        
        for quote_line in quote_lines:
            print(quote_line)
        
        for _ in range(3):
            print(side_border + " " * (width - 2) + side_border)
        
        # Author
        author_text = color_text(author, RED)
        thought_bubble = "○ " + author_text
        print(side_border + " " * ((width - len(thought_bubble)) // 2) + thought_bubble + " " * ((width - len(thought_bubble)) // 2) + side_border)
        print(bottom_border)
        
        # Current thought with typewriter effect
        print("\n" * 2)
        for char in thoughts[i]:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        
        time.sleep(1)
    
    # Final pause
    time.sleep(2)

if __name__ == "__main__":
    woody_allen_quote()