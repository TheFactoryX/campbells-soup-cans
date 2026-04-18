"""
Campbell's Soup Can #3336
Produced: 2026-04-18 07:35:01
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
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_quote():
    # Define colors using ANSI codes
    colors = [
        "31",  # Red
        "32",  # Green
        "33",  # Yellow
        "34",  # Blue
        "35",  # Magenta
        "36",  # Cyan
        "91",  # Bright Red
        "92",  # Bright Green
        "93",  # Bright Yellow
        "94",  # Bright Blue
        "95",  # Bright Magenta
        "96",  # Bright Cyan
        "97",  # White
    ]
    
    # Woody Allen quote
    quote = "I tried to be a philosopher once, but my mind kept wandering back to the refrigerator. I guess that's why I'm a neurotic comedian instead of a dead philosopher—at least with humor, you get punchlines. With philosophy, you just get... well, philosophy."
    
    # Split quote into multiple lines for better display
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 70:  # 70 chars per line approx
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    
    # Print with animation
    clear_screen()
    
    # Print animated border top
    border_top = "╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮"
    for i in range(len(border_top)):
        char = border_top[i]
        color = colors[i % len(colors)]
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(0.01)
    
    print()
    
    # Print animated quote
    for line_idx, line in enumerate(lines):
        # Print left border
        sys.stdout.write(colored("│", "97"))
        sys.stdout.flush()
        
        # Print line with alternating colors
        for i, char in enumerate(line):
            color_idx = (line_idx + i) % len(colors)
            sys.stdout.write(colored(char, colors[color_idx]))
            sys.stdout.flush()
            time.sleep(0.02)
        
        # Print right border
        print(colored("│", "97"))
    
    # Print animated border bottom
    border_bottom = "╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯"
    for i in range(len(border_bottom)):
        char = border_bottom[i]
        color = colors[i % len(colors)]
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(0.01)
    
    print()
    
    # Print signature with animation
    signature = " - Woody Allen"
    for i, char in enumerate(signature):
        color_idx = (i + len(colors)//2) % len(colors)
        sys.stdout.write(colored(char, colors[color_idx]))
        sys.stdout.flush()
        time.sleep(0.05)
    
    print("\n")
    
    # Add a small animated element (Woody's neurotic thinking)
    thoughts = ["To be or not to be...", "Is this all there is?", "What if I'm wrong?"]
    for thought in thoughts:
        sys.stdout.write("\033[96m" + thought + "\033[0m")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\r\033[K")  # Clear the line
        sys.stdout.flush()
    
    # Final neurotic thought
    final_thought = colored("I should've written a shorter quote...", "93")
    print("\n" + final_thought.center(80))
    time.sleep(2)
    
    # Clear screen and exit
    clear_screen()

if __name__ == "__main__":
    print_quote()