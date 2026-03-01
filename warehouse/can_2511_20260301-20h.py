"""
Campbell's Soup Can #2511
Produced: 2026-03-01 20:42:19
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

def colored_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'end': '\033[0m'
    }
    return colors.get(color, '') + text + colors['end']

def woody_allen_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens. It's like being at a party where you don't know anyone and the food is bad. You'd rather not go at all, but if you must, you'd prefer it to be over quickly."
    author = "— Woody Allen"
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Animated intro with Woody's anxiety
    intro = "You know, I've been thinking... which is always dangerous..."
    for char in intro:
        if char == ' ':
            print(' ', end='')
        else:
            color = ['red', 'magenta', 'cyan'][hash(char) % 3]
            print(colored_text(char, color), end='')
        sys.stdout.flush()
        time.sleep(0.03)
    
    print("\n\n")
    time.sleep(1)
    
    # Animated quote with varying speeds
    words = quote.split()
    neurotic_speeds = [0.01, 0.02, 0.03, 0.05, 0.1]
    
    for i, word in enumerate(words):
        color = ['red', 'magenta', 'cyan', 'green', 'yellow'][i % 5]
        print(colored_text(word + " ", color), end='')
        
        # Neurotic timing - sometimes fast, sometimes slow
        speed = random.choice(neurotic_speeds)
        if i % 5 == 0:  # Occasional dramatic pause
            speed *= 3
        
        time.sleep(speed)
        sys.stdout.flush()
    
    print("\n\n")
    
    # Author with pulsing effect
    for i in range(15):
        intensity = int(127 + 127 * math.sin(i * 0.4))
        color = f'\033[38;2;{intensity};{intensity//2};{intensity//3}m'
        print(color + author + '\033[0m', end='\r')
        time.sleep(0.1)
    
    # Final display in a decorative frame
    print("\033[2J\033[H", end="")
    
    # Create frame with gradient
    frame_width = 75
    frame_top = "╔" + "═" * (frame_width - 2) + "╗"
    frame_bottom = "╚" + "═" * (frame_width - 2) + "╝"
    frame_side = "║"
    
    # Gradient effect for frame
    for i in range(3):
        r = int(255 * i / 2)
        g = int(150 * (1 - i / 2))
        b = int(200 * (1 - i / 2))
        color = f'\033[38;2;{r};{g};{b}m'
        print(color + frame_top + '\033[0m')
    
    # Quote display with word wrap
    words = quote.split()
    lines = []
    current_line = ""
    line_colors = ['red', 'magenta', 'cyan', 'green', 'yellow']
    
    for word in words:
        if len(current_line + word) <= frame_width - 4:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    if current_line:
        lines.append(current_line)
    
    # Display lines with alternating colors
    for i, line in enumerate(lines):
        color = line_colors[i % len(line_colors)]
        print('\033[95m' + frame_side + " " + colored_text(line.center(frame_width - 4), color) + " " + '\033[95m' + frame_side)
    
    # Bottom of frame with gradient
    for i in range(3):
        r = int(255 * (1 - i / 2))
        g = int(150 * (i / 2))
        b = int(200 * (i / 2))
        color = f'\033[38;2;{r};{g};{b}m'
        print(color + frame_bottom + '\033[0m')
    
    # Author attribution
    print('\033[96m' + author.center(frame_width) + '\033[0m')

if __name__ == "__main__":
    woody_allen_quote()