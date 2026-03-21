"""
Campbell's Soup Can #2877
Produced: 2026-03-21 02:47:23
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
import math

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

def typewriter_effect(text, color=Colors.WHITE, delay=0.03):
    """Print text with a typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.END + '\n')

def draw_woody():
    """Draw a simple Woody Allen ASCII art"""
    woody = [
        "    __/\\__/\\__",
        "   |  O    O  |",
        "   |     ~    |",
        "   |    ___   |",
        "   |   /   \\  |",
        "  /|  |     | |\\",
        " / |  |     | | \\",
        "/__|__|_____|_|__\\"
    ]
    return '\n'.join(woody)

def draw_frame(width, height):
    """Draw a decorative frame around the quote"""
    frame = []
    # Top border
    frame.append(Colors.YELLOW + "+" + "-" * (width - 2) + "+" + Colors.END)
    # Empty lines
    for _ in range(height):
        frame.append(Colors.YELLOW + "|" + " " * (width - 2) + "|" + Colors.END)
    # Bottom border
    frame.append(Colors.YELLOW + "+" + "-" * (width - 2) + "+" + Colors.END)
    return '\n'.join(frame)

def main():
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Title
    typewriter_effect(Colors.BOLD + Colors.MAGENTA + "WOODY ALLEN ON EXISTENTIALISM" + Colors.END, delay=0.05)
    time.sleep(0.5)
    
    # Draw Woody Allen
    print(Colors.CYAN + draw_woody() + Colors.END)
    time.sleep(0.5)
    
    # The quote
    quote = "To be, or not to be? That is the question. But honestly, I'd rather be at home watching old movies. Life's too short for all this philosophical drama."
    
    # Calculate frame dimensions
    quote_lines = []
    line = ""
    max_width = 60
    for word in quote.split():
        if len(line + word) + 1 > max_width:
            quote_lines.append(line)
            line = word
        else:
            if line:
                line += " "
            line += word
    quote_lines.append(line)
    
    # Draw frame with quote
    frame_height = len(quote_lines) + 4
    frame = draw_frame(max_width + 4, frame_height)
    frame_lines = frame.split('\n')
    
    # Insert quote into frame
    for i, line in enumerate(quote_lines):
        frame_lines[i + 2] = frame_lines[i + 2][:-1] + Colors.WHITE + "  " + line + Colors.YELLOW + "  " + Colors.END + frame_lines[i + 2][-1]
    
    # Print frame
    sys.stdout.write(Colors.YELLOW)
    for line in frame_lines:
        typewriter_effect(line, delay=0.01)
    sys.stdout.write(Colors.END)
    
    # Add a small disclaimer
    time.sleep(0.5)
    typewriter_effect(Colors.BLUE + "\n*Typing nervously while adjusting glasses*" + Colors.END, delay=0.02)
    
    # Add a pulsating effect to the signature
    for i in range(3):
        time.sleep(0.3)
        sys.stdout.write(Colors.CYAN + "\n\n      - Woody" + Colors.END)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * 20 + "\r")
        sys.stdout.flush()
    
    typewriter_effect(Colors.CYAN + "\n      - Woody" + Colors.END, delay=0.02)
    
    # Final thought
    time.sleep(1)
    typewriter_effect(Colors.RED + "\n...and I'm not even sure if that's a real quote or if I just made it up. See? This is why I can't have nice things." + Colors.END, delay=0.02)

if __name__ == "__main__":
    main()