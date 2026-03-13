"""
Campbell's Soup Can #2740
Produced: 2026-03-13 10:56:56
Worker: Baidu: ERNIE 4.5 300B A47B  (baidu/ernie-4.5-300b-a47b)
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

def woody_allen_quote():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I believe there is something out there watching us. Unfortunately, it's the government.",
        "My one regret in life is that I am not someone else.",
        "Life is divided into the horrible and the miserable.",
        "I'm (TextView philosopher; I read a book once. It was green.",
        "If only God would give me some clear sign! Like making a large deposit in my name at a Swiss bank.",
        "I'm not a pessimist; I'm a realist with a sense of impending doom."
    ]
    return random.choice(quotes)

def print_colorful(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_woody_frame():
    frame_color = random.randint(31, 36)
    quote_color = random.randint(31, 36)
    while quote_color == frame_color:
        quote_color = random.randint(31, 36)

    frame_chars = ['*', '#', '+', '-', '=']
    frame_char = random.choice(frame_chars)
    quote = woody_allen_quote()
    margin = 4

    max_line_length = max([len(line) for line in quote.split(' ')]) + 2 * margin
    top_bottom = frame_char * (max_line_length + 4)

    print_colorful(top_bottom, frame_color)
    print_colorful(f"{frame_char} {' ' * (max_line_length)} {frame_char}", frame_color)
    
    words = quote.split(' ')
    current_line = ''
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length - 2 * margin:
            current_line += word + ' '
        else:
            padding = (max_line_length - 2 * margin - len(current_line)) // 2
            line = ' ' * margin + ' ' * padding + current_line + ' ' * padding
            print_colorful(f"{frame_char}{line}{' ' * (max_line_length - len(line))}{frame_char}", quote_color)
            current_line = word + ' '
    
    if current_line:
        padding = (max_line_length - 2 * margin - len(current_line)) // 2
        line = ' ' * margin + ' ' * padding + current_line + ' ' * padding
        print_colorful(f"{frame_char}{line}{' ' * (max_line_length - len(line))}{frame_char}", quote_color)
    
    print_colorful(f"{frame_char} {' ' * (max_line_length)} {frame_char}", frame_color)
    print_colorful(top_bottom, frame_color)

def main():
    print("\033[2J\033[H")  # Clear screen
    typewriter_effect("\n\033[3mLoading profound thoughts...\033[0m\n", 0.1)
    time.sleep(1)
    print_woody_frame()

if __name__ == "__main__":
    main()