"""
Campbell's Soup Can #1720
Produced: 2026-01-19 22:37:59
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
import random
from math import sin, pi

def colored_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return colors.get(color, '') + text + colors['reset']

def type_text(text, delay=0.03, color='white'):
    for char in text:
        sys.stdout.write(colored_text(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def jittery_text(text, color='yellow', jitter_chance=0.3):
    for char in text:
        if random.random() < jitter_chance:
            time.sleep(random.uniform(0.05, 0.15))
        sys.stdout.write(colored_text(char, color))
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def draw_box(text, border_color='cyan', text_color='white'):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    
    print(colored_text('╔' + '═' * (max_length + 2) + '╗', border_color))
    
    for line in lines:
        padding = ' ' * (max_length - len(line))
        print(colored_text('║ ' + colored_text(line, text_color) + padding + ' ║', border_color))
    
    print(colored_text('╚' + '═' * (max_length + 2) + '╝', border_color))

def animated_skeleton():
    frames = [
        "     _.--\"\"--._\n    /          \\\n   |            |\n   |            |\n    \\          /\n     `--..--'",
        "     _.--\"\"--._\n    /          \\\n   |    O    O  |\n   |            |\n    \\          /\n     `--..--'",
        "     _.--\"\"--._\n    /          \\\n   |    O    O  |\n   |      ~     |\n    \\          /\n     `--..--'",
        "     _.--\"\"--._\n    /          \\\n   |    X    X  |\n   |      ~     |\n    \\          /\n     `--..--'"
    ]
    
    for _ in range(2):
        for frame in frames:
            print(colored_text(frame, 'green'))
            time.sleep(0.5)
            print('\033[4A\033[J', end='')

def main():
    print('\033[2J\033[H', end='')
    
    type_text("WOODY ALLEN'S GUIDE TO EXISTENTIAL ANXIETY", 0.04, 'yellow')
    draw_line('=', 80, 'cyan')
    
    quote = """I'm not afraid of death,
I'm just afraid that if there's an afterlife,
I'll have to make small talk with strangers for eternity."""
    
    draw_box(quote, 'magenta', 'white')
    
    print()
    animated_skeleton()
    print()
    
    jittery_text("You know, it's not that I'm afraid of dying...", 'cyan')
    time.sleep(0.5)
    jittery_text("It's just that I don't want to be there when it happens.", 'red')
    
    print()
    draw_line('-', 60, 'blue')
    type_text("Life is full of misery, loneliness, and suffering -", 0.03, 'red')
    type_text("and it's all over much too soon.", 0.03, 'magenta')
    draw_line('-', 60, 'blue')
    
    print()
    print(colored_text("I don't want to achieve immortality through my work;", 'yellow'))
    print(colored_text("I want to achieve it through not dying.", 'cyan'))
    
    print()
    print(colored_text("                             -- Woody Allen", 'white'))
    print()
    
    type_text("Remember: Death is nature's way of telling you to slow down.", 0.05, 'green')

def draw_line(char, length, color='white'):
    line = char * length
    print(colored_text(line, color))

if __name__ == "__main__":
    main()