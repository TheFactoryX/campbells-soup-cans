"""
Campbell's Soup Can #1612
Produced: 2026-01-14 22:40:20
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
from math import sin

def woody_quote():
    # ANSI color codes
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    # Define the quote
    quote = "I've been analyzing my fear of commitment, and I've concluded that my fear of commitment is much more committed than I am to any relationship."
    author = "- Woody Allen"
    
    # Create a frame with ASCII art
    def create_frame(color_intensity):
        frame = [
            "╔" + "═" * 70 + "╗",
            "║" + " " * 70 + "║",
            "║",
            "║",
            "║",
            "║",
            "║",
            "║",
            "║",
            "║",
            "║",
            "╚" + "═" * 70 + "╝"
        ]
        
        # Add the quote to the frame with color
        quote_lines = []
        line_length = 45
        
        # Split quote into multiple lines
        for i in range(0, len(quote), line_length):
            quote_lines.append(quote[i:i+line_length])
            
        # Add quote lines to the frame
        frame[2] = f"║    {quote_lines[0]}"
        frame[3] = f"║    {quote_lines[1]}"
        frame[4] = f"║"
        frame[5] = f"║"
        frame[6] = f"║    {GREEN}{author}{END}"
        
        # Apply color with intensity variation
        colored_frame = []
        for line in frame:
            if "commitment" in line.lower():
                colored_line = line.replace("commitment", f"{color_intensity}commitment{END}")
            else:
                colored_line = line
            colored_frame.append(colored_line)
            
        return colored_frame
    
    # Animation loop
    for i in range(20):
        # Calculate color intensity (simulating a blinking/waving effect)
        intensity = int(127 * (0.5 + 0.5 * sin(i * 0.5)))
        color = f"\033[38;2;{intensity};{255-intensity};{intensity//2}m"
        
        # Create and print the frame
        frame = create_frame(color)
        for line in frame:
            print(line)
        
        # Add a footer with some neurotic thoughts
        footer = [
            f"    {RED}{'*' * 70}{END}",
            f"    {YELLOW}I mean, what if I commit to this quote and then find a better one?{END}",
            f"    {BLUE}{'*' * 70}{END}"
        ]
        
        for line in footer:
            print(line)
            
        # Sleep for a moment between frames
        time.sleep(0.2)
        
        # Clear the screen (ANSI escape sequence)
        sys.stdout.write("\033[H\033[J")
    
    # Final static frame
    final_frame = create_frame(YELLOW)
    for line in final_frame:
        print(line)
    
    # Add some decorative elements
    print(f"\n{BOLD}{BLUE}{'#' * 70}{END}")
    print(f"{BOLD}{YELLOW}    Existential crisis: 50% off today only!{END}")
    print(f"{BOLD}{BLUE}{'#' * 70}{END}\n")

# Run the function
woody_quote()