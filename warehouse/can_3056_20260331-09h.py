"""
Campbell's Soup Can #3056
Produced: 2026-03-31 09:17:56
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
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03, color_code=''):
    for char in text:
        sys.stdout.write(color_code + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color_cycle(text, delay=0.05):
    colors = [
        '\033[91m',  # Red
        '\033[92m',  # Green
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
    ]
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(BOLD + color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_quote():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    
    # ASCII art Woody Allen
    woody_art = [
        f"{BOLD}{BLUE}      __",
        f"     /  \\",
        f"    | () |",
        f"    | >< |  {RED}I'm not afraid of death,",
        f"     \\__/   {YELLOW}I'm just afraid that",
        f"      ||     {GREEN}there won't be good snacks",
        f"     {MAGENTA}||{RESET}        {CYAN}in the afterlife.{RESET}"
    ]
    
    # Frame decorations
    top_frame = f"{BOLD}{YELLOW}╔{'═' * 70}╗{RESET}"
    bottom_frame = f"{BOLD}{YELLOW}╚{'═' * 70}╝{RESET}"
    side_frame = f"{BOLD}{YELLOW}║{RESET}"
    
    clear_screen()
    
    # Display Woody Allen ASCII art with typing effect
    print(f"{BOLD}{BLUE}")
    for line in woody_art:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        print()
    print(f"{RESET}")
    
    # Display the quote with animation
    time.sleep(1)
    print(f"\n{top_frame}\n")
    
    # Main quote with color cycling
    quote = f"{BOLD}I was going to conquer the world, but then I remembered I had to return my library books.{RESET}"
    quote2 = f"{BOLD}Existential dread can wait, but late fees? That's true terror.{RESET}"
    
    # Create an animated frame with random colors
    frame_width = len(quote) + 10
    animated_frame = []
    for i in range(3):
        line = f"{side_frame}"
        for j in range(frame_width):
            line += random.choice([" ", "~", "*", "◊", "♥", "♦"])
        line += f"{side_frame}"
        animated_frame.append(line)
    
    # Print the animated frame
    for line in animated_frame:
        print(line)
        time.sleep(0.1)
    
    # Print the quote with typing effect
    type_text(f"{CYAN}I was going to conquer the world, but then I remembered I had to return my library books.{RESET}\n", 0.03)
    time.sleep(0.5)
    
    # Color cycle the second part
    color_cycle("Existential dread can wait, but late fees? That's true terror.")
    
    # Print the bottom frame
    print(f"\n{bottom_frame}")
    
    # Add a self-deprecating comment with animation
    time.sleep(1)
    type_text(f"\n{YELLOW}Woody Allen would probably spend an hour worrying about whether this joke was funny enough.{RESET}\n", 0.02)
    
    # Add a philosophical footer with random colors
    time.sleep(1)
    footer_quotes = [
        f"{BOLD}\"Life is divided into the horrible and the miserable.{RESET}",
        f"{BOLD}\"I don't want to achieve immortality through my work; I want to achieve it through not dying.{RESET}",
        f"{BOLD}\"More than any time in recent history, humanity's fate is in the hands of humanity.{RESET}"
    ]
    
    for quote in random.sample(footer_quotes, k=2):
        type_text(quote, 0.04)
        time.sleep(0.5)
    
    print(f"\n{BOLD}{ITALIC}{RED}- Woody Allen (probably){RESET}\n")

if __name__ == "__main__":
    woody_quote()