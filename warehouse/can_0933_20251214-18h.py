"""
Campbell's Soup Can #933
Produced: 2025-12-14 18:43:07
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
import math

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_centered(text, width=80):
    padding = (width - len(text)) // 2
    if padding < 0:
        padding = 0
    print(" " * padding + text)

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_framed_quote():
    # Define colors
    colors = {
        "title": "95",    # Bright magenta
        "subtitle": "36",  # Cyan
        "frame": "34",    # Blue
        "quote": "33",    # Yellow
        "author": "35",   # Magenta
        "highlight": "91", # Bright red
        "art": "32",      # Green
    }
    
    # ASCII art frame with corners
    top_bottom = "═" * 70
    corner_t = "╔"
    corner_b = "╚"
    corner_r = "╗"
    corner_l = "╝"
    
    # Woody Allen ASCII art
    woody_art = [
        "      ___      ",
        "     (o o)     ",
        "    / V \\     ",
        "   /|___|\\    ",
        "     |||      ",
        "    // \\\\     ",
        "   //   \\\\    ",
        "  //     \\\\   "
    ]
    
    # Neurotic thought bubble
    thought_bubble = [
        "   .-.    ",
        "  (o.o)   ",
        "  > ^ <   ",
        "   '-'    "
    ]
    
    # Woody Allen-style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. It's like being the last one at a party you didn't even want to attend in the first place. And I'm pretty sure someone ate all the good dip."
    
    words = quote.split()
    max_line_length = 60
    indent = " " * 10
    
    # Animation sequence
    for frame in range(40):
        clear_screen()
        
        # Animated title
        title_color = colors["title"]
        if frame % 10 < 5:
            title_color = "96"  # Bright cyan
        print_centered(colored("WOODY WISDOM", title_color))
        print_centered(colored("Philosophical Musings", colors["subtitle"]))
        
        # Frame with animated corners
        corners = {
            "tl": corner_t,
            "tr": corner_r,
            "bl": corner_b,
            "br": corner_l
        }
        
        # Animate corners
        if frame % 20 < 10:
            corners["tl"] = "╔"
            corners["tr"] = "╗"
            corners["bl"] = "╚"
            corners["br"] = "╝"
        else:
            corners["tl"] = "+"
            corners["tr"] = "+"
            corners["bl"] = "+"
            corners["br"] = "+"
            
        print_centered(colored(f"{corners['tl']}{top_bottom}{corners['tr']}", colors["frame"]))
        
        # Empty space
        print()
        
        # Print quote with highlighting and automatic line wrapping
        current_line = indent
        current_length = len(indent)
        highlight_word = frame % len(words)
        
        for i, word in enumerate(words):
            word_with_space = word + " "
            word_length = len(word_with_space)
            
            if current_length + word_length > max_line_length:
                print_centered(current_line, 70)
                current_line = indent + word_with_space
                current_length = len(indent) + word_length
            else:
                current_line += word_with_space
                current_length += word_length
            
            # Highlight the specific word
            if i == highlight_word:
                highlight_colors = ["91", "92", "93", "94", "95", "96"]
                word_color = highlight_colors[(i + frame) % len(highlight_colors)]
                print_centered(colored(current_line, word_color), 70)
                time.sleep(0.02)  # Brief pause to highlight
                current_line = indent + word_with_space
                current_length = len(indent) + word_length
        
        if current_line.strip():
            print_centered(current_line, 70)
        
        # Empty space
        print()
        print()
        
        # Animated thought bubble
        for j, line in enumerate(thought_bubble):
            if frame % 8 < 4:
                print_centered(colored(line, colors["art"]))
            else:
                # Blinking effect
                if j == 1:
                    print_centered(colored("  (o.o)   ", colors["art"]))
                else:
                    print_centered(colored(line, colors["art"]))
        
        # Connection line to Woody
        connection = "     |     "
        if frame % 6 < 3:
            connection = "     |     "
        else:
            connection = "    /|     "
        print_centered(colored(connection, colors["art"]))
        
        # Woody Allen ASCII art with animation
        for i, line in enumerate(woody_art):
            if i == len(woody_art) - 1:
                # Animated feet
                bounce = " " * (2 * abs(int(2 * math.sin(frame * 0.2))))
                wiggle = " " * (abs(int(2 * math.sin(frame * 0.5))))
                print_centered(colored(bounce + wiggle + line, colors["author"]))
            elif i == 3:
                # Animated eyes
                if frame % 8 < 4:
                    modified_line = line[:4] + "o o" + line[7:]
                else:
                    modified_line = line[:4] + "> <" + line[7:]
                print_centered(colored(modified_line, colors["author"]))
            else:
                print_centered(colored(line, colors["author"]))
        
        # Author with animation
        author_line = "— Woody Allen"
        if frame % 8 < 4:
            print_centered(colored(author_line, colors["author"]))
        else:
            # Sliding author name
            slide = " " * (frame % 4)
            print_centered(colored(slide + author_line, colors["author"]))
        
        # Frame bottom with animated corners
        print_centered(colored(f"{corners['bl']}{top_bottom}{corners['br']}", colors["frame"]))
        
        # Animated footer
        footer = "Life is divided into two parts: the horrible and the miserable."
        if frame % 12 < 6:
            print_centered(colored(footer, colors["subtitle"]))
        else:
            print_centered(colored(footer.lower(), colors["subtitle"]))
        
        time.sleep(0.1)
    
    # Keep the final display
    input("\n" + " " * 35 + colored("Press Enter to exit...", colors["title"]))

if __name__ == "__main__":
    print_framed_quote()