"""
Campbell's Soup Can #382
Produced: 2025-11-19 15:32:39
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
from itertools import cycle

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

# Woody Allen ASCII art
WOODY = f"""
{Colors.YELLOW}    ___
   /   \\{Colors.END}
  |  O  |{Colors.GREEN}  I'm not afraid of death;
   \\___/   {Colors.YELLOW}I just don't want to be there
 {Colors.BLUE}   ||||{Colors.END}       when it happens, and also
 {Colors.BLUE}   ||||{Colors.END}       could someone make sure
 {Colors.BLUE}  {Colors.YELLOW}||||||{Colors.BLUE}      my Netflix account gets
 {Colors.BLUE}  {Colors.YELLOW}||||||{Colors.BLUE}      cancelled? I don't want
 {Colors.BLUE}   ||||{Colors.END}       my family to have to
{Colors.RED}   /----\\{Colors.END}       deal with that on top of
{Colors.RED}  |      |{Colors.END}       everything else.
{Colors.RED}  \\______/{Colors.END}
"""

def typewriter_effect(text, delay=0.05, color=Colors.WHITE):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.END + "\n")

def draw_border(width, height, char="="):
    """Draw a decorative border"""
    corners = {
        'top_left': '+',
        'top_right': '+',
        'bottom_left': '+',
        'bottom_right': '+',
        'horizontal': '-',
        'vertical': '|'
    }
    
    # Top border
    print(f"{Colors.CYAN}{corners['top_left']}{corners['horizontal'] * width}{corners['top_right']}{Colors.END}")
    
    # Middle (empty)
    for _ in range(height):
        print(f"{Colors.CYAN}{corners['vertical']}{' ' * width}{corners['vertical']}{Colors.END}")
    
    # Bottom border
    print(f"{Colors.CYAN}{corners['bottom_left']}{corners['horizontal'] * width}{corners['bottom_right']}{Colors.END}")

def main():
    # Clear screen
    print("\033c", end="")
    
    # Title with pulsing effect
    title_colors = cycle([Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.BLUE, Colors.MAGENTA])
    for i in range(5):
        color = next(title_colors)
        print(f"\033[{20 + i};40H{color}{Colors.BOLD}WOODY ALLEN PHILOSOPHY{Colors.END}")
        time.sleep(0.3)
    
    # Draw border around Woody character
    woody_lines = WOODY.split('\n')
    max_width = max(len(line) for line in woody_lines)
    draw_border(max_width, len(woody_lines))
    
    # Print Woody character in the middle
    for line in woody_lines:
        print(f"\033[{25 + woody_lines.index(line)};40H{line}")
    
    # Wait a moment
    time.sleep(2)
    
    # Print the quote with typewriter effect
    quote = """
I've analyzed my life and I've come to a conclusion:
I'm not saying life is meaningless, but I've looked under 
the couch cushions and found more purpose than in my entire existence.
At least with dust bunnies, you know they're eventually going to get 
vacuumed up - there's a certain dignity in that.
"""
    
    # Position for quote
    print("\n\n")
    typewriter_effect(quote, delay=0.03, color=Colors.WHITE)
    
    # Add philosophical flourish
    time.sleep(1)
    print(f"\n{Colors.MAGENTA}    - Woody Allen{Colors.END}")
    
    # Existential footer
    time.sleep(1)
    print(f"\n{Colors.YELLOW}P.S. I'm not worried about the afterlife. I've already{Colors.END}")
    typewriter_effect("experienced a three-hour meeting with my accountant.", delay=0.05, color=Colors.YELLOW)
    
    # Reset cursor position
    print("\033[40;0H")

if __name__ == "__main__":
    main()