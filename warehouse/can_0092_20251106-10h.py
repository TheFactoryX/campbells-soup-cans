"""
Campbell's Soup Can #92
Produced: 2025-11-06 10:39:09
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

def colored_text(text, color):
    """Function to print colored text using ANSI escape codes"""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'reset': '\033[0m'
    }
    return colors.get(color, '') + colors.get('bold', '') + text + colors['reset']

def typewriter_effect(text, color='white', delay=0.05):
    """Function to create a typewriter effect"""
    for char in text:
        sys.stdout.write(colored_text(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Function to clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def random_color():
    """Function to get a random color"""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    return random.choice(colors)

def animate_text(text, times=3):
    """Function to animate text with random colors"""
    for _ in range(times):
        # Clear the line
        sys.stdout.write('\r' + ' ' * 80)
        sys.stdout.flush()
        
        # Print with random color
        color = random_color()
        sys.stdout.write('\r' + colored_text(text, color))
        sys.stdout.flush()
        time.sleep(0.5)
    
    # Final print in white
    print('\r' + colored_text(text, 'white') + ' ' * (80 - len(text)))

def draw_box(text, color='cyan'):
    """Function to draw a box around text"""
    lines = text.split('\n')
    max_length = max(len(line) for line in lines) + 4
    
    # Top border
    print(colored_text('╔' + '═' * max_length + '╗', color))
    
    # Text with side borders
    for line in lines:
        padding = ' ' * (max_length - len(line) - 2)
        print(colored_text(f'║ {line}{padding} ║', color))
    
    # Bottom border
    print(colored_text('╚' + '═' * max_length + '╝', color))

def scrolling_quote(text, color='yellow'):
    """Function to create a scrolling quote effect"""
    # Calculate the width of the terminal (default to 80 if unable to determine)
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80
    
    # Add padding to the quote
    padded_text = ' ' * 10 + text + ' ' * 10
    
    # Scroll the text
    for i in range(len(padded_text) - terminal_width + 1):
        # Clear the line
        sys.stdout.write('\r' + ' ' * terminal_width)
        sys.stdout.flush()
        
        # Extract the visible portion of the text
        visible_text = padded_text[i:i+terminal_width]
        
        # Print with color
        sys.stdout.write('\r' + colored_text(visible_text, color))
        sys.stdout.flush()
        time.sleep(0.05)
    
    print()

def main():
    # Clear screen
    clear_screen()
    
    # Title with animation
    title = "WOODY ALLEN'S PHILOSOPHICAL MUSINGS"
    print()
    animate_text(title, 5)
    
    print()
    
    # Woody Allen ASCII art
    woody = [
        "       .--. ",
        "       |o_o | ",
        "       |:_/ | ",
        "      //   \\ \\ ",
        "     (|     | ) ",
        "    /'\\_   _/`\\ ",
        "    \\___)=(___/ "
    ]
    
    for line in woody:
        print(colored_text(line, 'magenta'))
    
    print()
    
    # The quote
    quote = "I spend so much time worrying about whether I'm happy that I don't have time to actually be happy. It's like being on a diet where you only eat diet books."
    
    # Print quote with scrolling effect
    scrolling_quote(quote)
    
    print()
    
    # Animated subtitle
    subtitle = "A moment of existential dread brought to you by neurosis"
    animate_text(subtitle, 3)
    
    print()
    
    # Woody Allen's signature
    signature = "                                 - Woody Allen"
    typewriter_effect(signature, 'cyan', 0.03)
    
    print()
    
    # Final thought with animation
    final_thought = "PS: I'm not really Woody Allen. I'm just a program who wishes I was neurotic enough to be."
    animate_text(final_thought, 3)

if __name__ == "__main__":
    main()