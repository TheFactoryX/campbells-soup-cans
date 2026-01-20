"""
Campbell's Soup Can #1727
Produced: 2026-01-20 07:42:54
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
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

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def move_cursor(x, y):
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.flush()

def print_color(text, color_code):
    sys.stdout.write(color_code + text + "\033[0m")
    sys.stdout.flush()

def typewriter(text, delay=0.03, color="\033[93m"):
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.02))

def print_boxed_quote():
    quote = "I can't even decide what to have for breakfast, yet I'm expected to choose a purpose for eternity. The cosmic menu is overwhelming and there's no waiter to explain the specials."
    author = "- Woody Allen-esque Anxious Thinker"
    
    lines = quote.split('. ')
    max_length = max(len(line) for line in lines)
    padding = 4
    
    clear_screen()
    
    # Create color gradient background
    colors = [41, 42, 43, 44, 45, 46, 47]
    for y in range(1, 25):
        for x in range(1, 80):
            move_cursor(x, y)
            print_color(" ", "\033[48;5;{}m".format(colors[(x+y) % 7]))
    
    # Calculate box position
    box_width = max_length + padding * 2
    box_height = len(lines) + 4
    start_x = (80 - box_width) // 2
    start_y = (24 - box_height) // 2
    
    # Draw box
    border_color = "\033[1;36m"
    move_cursor(start_x, start_y)
    typewriter("╭" + "─"*(box_width-2) + "╮", 0.001, border_color)
    
    for i in range(box_height-2):
        move_cursor(start_x, start_y + 1 + i)
        typewriter("│" + " "*(box_width-2) + "│", 0.001, border_color)
    
    move_cursor(start_x, start_y + box_height - 1)
    typewriter("╰" + "─"*(box_width-2) + "╯", 0.001, border_color)
    
    # Print quote
    text_color = "\033[1;93m\033[44m"
    for idx, line in enumerate(lines):
        pos_y = start_y + 2 + idx
        indent = "  " if idx == 0 else ""
        formatted_line = f"{indent}{line}{'.' if idx < len(lines)-1 else ''}"
        move_cursor(start_x + 2, pos_y)
        typewriter(formatted_line, 0.03, text_color)
    
    # Print author
    author_color = "\033[1;91m\033[45m"
    author_line = author.rjust(box_width-4)
    move_cursor(start_x + 2, start_y + box_height - 3)
    typewriter(author_line, 0.02, author_color)
    
    # Sparkle effect
    sparkle_pos = [(random.randint(start_x+1, start_x+box_width-2), 
                   random.randint(start_y+1, start_y+box_height-2)) 
                   for _ in range(30)]
    
    for _ in range(3):
        for x, y in sparkle_pos:
            move_cursor(x, y)
            print_color("*", "\033[1;37m")
        time.sleep(0.4)
        for x, y in sparkle_pos:
            move_cursor(x, y)
            print(" ")
    
    move_cursor(1, 25)

if __name__ == "__main__":
    print_boxed_quote()
    time.sleep(2)
    move_cursor(1, 25)
    print("\n")