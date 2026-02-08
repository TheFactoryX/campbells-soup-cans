"""
Campbell's Soup Can #2128
Produced: 2026-02-08 23:46:34
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

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print with color using ANSI escape codes
def print_color(text, color_code, end='\n'):
    print(f"\033[{color_code}m{text}\033[0m", end=end)

# Function to print the animated quote with typewriter effect
def print_quote():
    # ASCII art frame with integrated thought bubble
    frame_top = [
        "      oooo             oooo",
        "     o8888o           o8888o",
        "    888'`88b.        ,88'`888",
        "    88'  `88b.      ,88'  `88",
        "    88    `88b.    ,88'    88",
        "    88     `88b.  ,88'     88",
        "    88      `88b,88'       88",
        "    88       `888'        88",
        "    88        `8'         88",
        "   o88o        .          o88o",
        "╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
    ]
    
    frame_bottom = "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"
    
    # Print frame top with animation
    for line in frame_top:
        for char in line:
            if char in ['o', 'O']:
                print_color(char, 96, end='')  # Cyan for 'o's in thought bubble
            elif char in ['╔', '═', '╗']:
                print_color(char, 93, end='')  # Light blue for frame
            else:
                print_color(char, 93, end='')  # Light blue for rest
            sys.stdout.flush()
            time.sleep(0.01)
        print()
    
    # Print empty line
    print_color("\n", 93)
    
    # The quote with different colors for different parts
    quote_parts = [
        ("  I don't mind dying, ", 90),          # Dark gray
        ("I just don't want to be there when it happens. ", 91),  # Light red
        ("It's like going to a party where you know nobody, ", 90),  # Dark gray
        ("and the host is mortality. ", 93),     # Light blue (emphasis)
        ("And the snacks are probably stale. ", 91),  # Light red
        ("And you can't leave because you're already dead. ", 90),  # Dark gray
        ("Which is awkward.", 93)                # Light blue (punchline)
    ]
    
    # Typewriter effect for the quote
    for text, color in quote_parts:
        for char in text:
            print_color(char, color, end='')
            sys.stdout.flush()
            time.sleep(0.03)
    
    # Print empty lines
    print_color("\n\n", 93)
    
    # Print frame bottom with animation
    for char in frame_bottom:
        print_color(char, 93, end='')  # Light blue
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
    # Add blinking cursor effect
    for i in range(5):
        print_color("\033[92m▶\033[0m", 92, end='')  # Green cursor
        sys.stdout.flush()
        time.sleep(0.3)
        print_color("\033[93m◀\033[0m", 93, end='')  # Yellow cursor
        sys.stdout.flush()
        time.sleep(0.3)
        print_color("\b \b", 0, end='')
        sys.stdout.flush()

# Function for opening animation
def opening_animation():
    # Woody Allen's name appearing one character at a time
    name = "WOODY ALLEN"
    for char in name:
        print_color(char, 95, end='')  # Light purple
        sys.stdout.flush()
        time.sleep(0.2)
    print_color("\n\n", 95)

# Function for fade-out effect
def fade_out():
    # Simple fade-out with decreasing color intensity
    fade_quotes = [
        ([
            ("  I don't mind dying, ", 37),        # Light gray
            ("I just don't want to be there when it happens. ", 37),
            ("It's like going to a party where you know nobody, ", 37),
            ("and the host is mortality. ", 37),
            ("And the snacks are probably stale. ", 37),
            ("And you can't leave because you're already dead. ", 37),
            ("Which is awkward.", 37)
        ], 0.3),
        ([
            ("  I don't mind dying, ", 90),        # Dark gray
            ("I just don't want to be there when it happens. ", 90),
            ("It's like going to a party where you know nobody, ", 90),
            ("and the host is mortality. ", 90),
            ("And the snacks are probably stale. ", 90),
            ("And you can't leave because you're already dead. ", 90),
            ("Which is awkward.", 90)
        ], 0.3),
        ([
            ("  I don't mind dying, ", 100),       # Darker gray
            ("I just don't want to be there when it happens. ", 100),
            ("It's like going to a party where you know nobody, ", 100),
            ("and the host is mortality. ", 100),
            ("And the snacks are probably stale. ", 100),
            ("And you can't leave because you're already dead. ", 100),
            ("Which is awkward.", 100)
        ], 0.3),
        ([
            ("  I don't mind dying, ", 0),         # Black (invisible)
            ("I just don't want to be there when it happens. ", 0),
            ("It's like going to a party where you know nobody, ", 0),
            ("and the host is mortality. ", 0),
            ("And the snacks are probably stale. ", 0),
            ("And you can't leave because you're already dead. ", 0),
            ("Which is awkward.", 0)
        ], 0.3)
    ]
    
    # Print frame top
    frame_top = [
        "      oooo             oooo",
        "     o8888o           o8888o",
        "    888'`88b.        ,88'`888",
        "    88'  `88b.      ,88'  `88",
        "    88    `88b.    ,88'    88",
        "    88     `88b.  ,88'     88",
        "    88      `88b,88'       88",
        "    88       `888'        88",
        "    88        `8'         88",
        "   o88o        .          o88o",
        "╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
    ]
    
    frame_bottom = "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"
    
    # Print frame top
    for line in frame_top:
        for char in line:
            if char in ['o', 'O']:
                print_color(char, 96, end='')  # Cyan for 'o's in thought bubble
            elif char in ['╔', '═', '╗']:
                print_color(char, 93, end='')  # Light blue for frame
            else:
                print_color(char, 93, end='')  # Light blue for rest
            sys.stdout.flush()
            time.sleep(0.005)
        print()
    
    # Print empty line
    print_color("\n", 93)
    
    # Fade out the quote
    for quote_parts, delay in fade_quotes:
        print_color("\n", 93)
        for text, color in quote_parts:
            print_color(text, color, end='')
        sys.stdout.flush()
        time.sleep(delay)
    
    # Print frame bottom
    for char in frame_bottom:
        print_color(char, 93, end='')  # Light blue
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    
    # Clear screen at the end
    clear_screen()

# Main function
def main():
    clear_screen()
    
    # Print opening animation
    opening_animation()
    
    # Print the animated quote
    print_quote()
    
    # Print some additional text at the bottom
    print_color("\n\n\n  Press any key to exit...", 92)  # Green
    input()
    
    # Fade-out effect
    fade_out()

if __name__ == "__main__":
    main()