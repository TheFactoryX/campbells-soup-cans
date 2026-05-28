"""
Campbell's Soup Can #3802
Produced: 2026-05-28 04:40:12
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
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

# ANSI color codes
class Colors:
    RESET = '\033[0m'
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
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'

def type_text(text, delay=0.03):
    """Simulates typing effect with occasional random delays for realism"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Random delay for more natural typing
        time.sleep(delay * (0.5 + random.random()))
    print()

def draw_woody_head():
    """Simple Woody Allen ASCII art"""
    return [
        f"{Colors.RED}     _____     {Colors.RESET}",
        f"{Colors.RED}   /       \\   {Colors.RESET}",
        f"{Colors.RED}  |  {Colors.YELLOW}O   O{Colors.RED}  |  {Colors.RESET}",
        f"{Colors.RED}  |    {Colors.CYAN}\\ {Colors.RED}   |  {Colors.RESET}",
        f"{Colors.RED}  |     {Colors.CYAN}\\_/{Colors.RED} |  {Colors.RESET}",
        f"{Colors.RED}   \\________/  {Colors.RESET}",
        f"{Colors.RED}     |    |    {Colors.RESET}",
        f"{Colors.RED}    /      \\   {Colors.RESET}",
        f"{Colors.RED}   |        |  {Colors.RESET}",
        f"{Colors.RED}   '--------'  {Colors.RESET}"
    ]

def animate_blinking_eyes():
    """Simple animation of Woody's eyes blinking"""
    for i in range(3):
        time.sleep(0.5)
        # Eyes closed
        sys.stdout.write("\033[H")  # Move cursor to top-left
        head_lines = draw_woody_head()
        head_lines[2] = f"{Colors.RED}  |  {Colors.YELLOW}-{Colors.RED}   {Colors.YELLOW}-{Colors.RED}  |  {Colors.RESET}"
        for line in head_lines:
            print(line)
        time.sleep(0.5)
        # Eyes open
        sys.stdout.write("\033[H")  # Move cursor to top-left
        head_lines = draw_woody_head()
        for line in head_lines:
            print(line)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_quote_box(quote):
    """Prints the quote in a styled box with animation"""
    clear_screen()
    
    box_width = len(quote) + 6
    corners = ["┌", "┐", "└", "┘"]
    sides = ["│", "│", "─", "─"]
    
    # Print title
    type_text("\n" + Colors.BOLD + Colors.MAGENTA + "WOODY ALLEN ON LIFE, LOVE, AND OTHER NEUROTIC PURSUITS" + Colors.RESET + "\n")
    
    # Top border
    type_text(Colors.BLUE + corners[0] + sides[2] * (box_width-2) + corners[1] + Colors.RESET)
    
    # Woody Allen head
    head_lines = draw_woody_head()
    for line in head_lines:
        type_text(line)
    
    # Blink eyes
    animate_blinking_eyes()
    
    # Quote box
    for _ in range(2):
        type_text(Colors.BLUE + sides[0] + " " * (box_width-2) + sides[1] + Colors.RESET)
    
    # Quote text
    quote_lines = []
    words = quote.split()
    current_line = ""
    for word in words:
        if len(current_line + " " + word) <= box_width - 4:
            current_line += " " + word if current_line else word
        else:
            quote_lines.append(current_line)
            current_line = word
    quote_lines.append(current_line)
    
    for line in quote_lines:
        padding = (box_width - 4 - len(line)) // 2
        type_text(Colors.BLUE + sides[0] + " " * padding + Colors.YELLOW + line + Colors.RESET + " " * padding + Colors.BLUE + sides[1] + Colors.RESET)
    
    for _ in range(2):
        type_text(Colors.BLUE + sides[0] + " " * (box_width-2) + sides[1] + Colors.RESET)
    
    # Bottom border
    type_text(Colors.BLUE + corners[2] + sides[3] * (box_width-2) + corners[3] + Colors.RESET)
    
    # Signature with extra commentary
    type_text("\n" + Colors.BOLD + Colors.CYAN + " - Woody Allen" + Colors.RESET)
    type_text(Colors.ITALIC + Colors.MAGENTA + " (Probably overthinking this while eating a pastrami sandwich)" + Colors.RESET + "\n")
    
    # Random Woody Allen-style observation
    observations = [
        "I told my psychiatrist that everyone hates me. He said I was being ridiculous. Everyone hasn't met me yet.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "More people have seen me naked than I have.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "Sex is only dirty if you're doing it right."
    ]
    
    # Randomly select an observation
    observation = random.choice(observations)
    type_text(Colors.GREEN + "Random Woody Observation: " + Colors.RESET + Colors.WHITE + observation + Colors.RESET + "\n")
    
    # Wait for a moment before exiting
    time.sleep(5)

if __name__ == "__main__":
    # Woody Allen style philosophical quote
    quote = "I tried to be a philosopher, but it just gave me headaches. Turns out, thinking too much about the meaning of life is like trying to find a parking spot in Manhattan—impossible, and you end up going in circles."
    
    print_quote_box(quote)