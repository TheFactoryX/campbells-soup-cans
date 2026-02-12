"""
Campbell's Soup Can #2188
Produced: 2026-02-12 20:51:37
Worker: Google: Gemini 3 Pro Preview (google/gemini-3-pro-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hide_cursor():
    sys.stdout.write("\033[?25l")

def show_cursor():
    sys.stdout.write("\033[?25h")

def get_color(color_name):
    colors = {
        'RESET': '\033[0m',
        'BOLD': '\033[1m',
        'DIM': '\033[2m',
        'ITALIC': '\033[3m',
        'CYAN': '\033[96m',
        'YELLOW': '\033[93m',
        'WHITE': '\033[97m',
        'GREY': '\033[90m',
        'RED': '\033[91m'
    }
    return colors.get(color_name, '\033[0m')

def nervous_typewriter(text, indent="    ", color_code=''):
    """Prints text with a 'neurotic' stuttering effect."""
    sys.stdout.write(color_code)
    
    # Split text into words to handle primitive wrapping visually
    words = text.split(' ')
    line_length = 0
    max_width = 60
    
    sys.stdout.write(indent)
    
    for word in words:
        if line_length + len(word) > max_width:
            sys.stdout.write("\n" + indent)
            line_length = 0
            time.sleep(0.3) # Pause at line break
            
        for char in word:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            # Neurotic timing logic
            delay = random.uniform(0.04, 0.09)
            
            # Hesitate on punctuation
            if char in ',;-':
                delay += 0.3
            elif char in '.?!':
                delay += 0.6
                
            # Random anxiety pause
            if random.random() < 0.02:
                time.sleep(0.4)
                
            time.sleep(delay)
            
        sys.stdout.write(" ")
        sys.stdout.flush()
        line_length += len(word) + 1
        time.sleep(random.uniform(0.02, 0.05))

    sys.stdout.write(get_color('RESET') + "\n")

def main():
    try:
        hide_cursor()
        clear_screen()
        
        # Colors
        C_GLASSES = get_color('CYAN') + get_color('BOLD')
        C_FACE = get_color('WHITE')
        C_QUOTE = get_color('YELLOW') + get_color('ITALIC')
        C_AUTHOR = get_color('GREY')
        C_RESET = get_color('RESET')

        # Iconic thick-rimmed glasses ASCII Art
        glasses_art = [
            f"{C_FACE}          .   ,           ",
            f"{C_FACE}        _ |\\ /| _         ",
            f"{C_GLASSES}      .'  o   o  `.       ",
            f"{C_GLASSES}     |   _     _   |      ",
            f"{C_GLASSES}     |  ( )   ( )  |      ",
            f"{C_GLASSES}      `._________.'       ",
            f"{C_FACE}         |___|            ",
            f"{C_FACE}        /     \\           "
        ]

        # Intro Animation
        print("\n\n")
        for line in glasses_art:
            print("        " + line)
            time.sleep(0.1)
        
        print("\n")
        
        # The Quote
        quote = "I was thrown out of college for cheating on the metaphysics exam; I looked into the soul of the boy sitting next to me."
        
        # Nervous intro (clearing throat)
        time.sleep(0.5)
        sys.stdout.write("        " + get_color('DIM') + "*cough*" + C_RESET + "\n")
        time.sleep(0.5)
        sys.stdout.write("        " + get_color('DIM') + "Is this thing on? Alright..." + C_RESET + "\n\n")
        time.sleep(0.8)

        # Print the quote with neurotic stutter
        nervous_typewriter(quote, indent="        ", color_code=C_QUOTE)
        
        # Attribution
        time.sleep(1)
        print("\n" + get_color('RED') + "                  -- Woody Allen" + C_RESET)
        print("\n\n")

    except KeyboardInterrupt:
        sys.stdout.write(get_color('RESET') + "\n\nOkay, okay, I'm leaving!\n")
    finally:
        show_cursor()

if __name__ == "__main__":
    main()