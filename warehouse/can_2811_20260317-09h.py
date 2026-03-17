"""
Campbell's Soup Can #2811
Produced: 2026-03-17 09:08:47
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys
import os

# Woody Allen style quote
quote = (
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon. "
    "I don't want to achieve immortality through my work; I want to achieve it through not dying."
)

def typewriter(text, delay=0.03, color_code='\033[96m'):
    """Print text with typewriter effect and color"""
    sys.stdout.write(color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    sys.stdout.write('\033[0m\n')

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_woody_allen():
    clear_screen()
    
    # Terminal width detection with fallback
    try:
        term_width = os.get_terminal_size().columns
    except:
        term_width = 80
    
    # Box styling
    border_chars = ['╔', '╚', '╝', '╠', '╣', '╩', '╦', '═', '║']
    box_width = min(term_width - 4, 70)
    
    # Random colors for each run
    colors = [
        '\033[92m',  # Green
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
    ]
    primary_color = random.choice(colors)
    accent_color = '\033[1;33m'  # Bold yellow
    
    # Print decorative header with animation
    print("\n" * 2)
    
    # Animated "thought bubble" dots
    for i in range(3):
        sys.stdout.write('\033[?25l')  # Hide cursor
        for dots in ['   ', '.  ', '.. ', '...']:
            sys.stdout.write(f'\r{accent_color}Thinking...{dots}\033[0m')
            sys.stdout.flush()
            time.sleep(0.2)
    print('\r' + ' ' * 20 + '\r')  # Clear the line
    sys.stdout.write('\033[?25h')  # Show cursor
    
    # Draw top border with animation
    print(primary_color + border_chars[0] + border_chars[7] * (box_width - 2) + border_chars[1] + '\033[0m')
    
    # Empty decorative line
    print(primary_color + border_chars[8] + ' ' * (box_width - 2) + border_chars[8] + '\033[0m')
    
    # Format quote into wrapped lines
    words = quote.split()
    lines = []
    current_line = []
    current_len = 0
    
    for word in words:
        if current_len + len(word) + 1 <= box_width - 8:
            current_line.append(word)
            current_len += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_len = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print quote with alternating colors for variety
    for i, line in enumerate(lines):
        # Alternate between primary and accent color for emphasis
        line_color = primary_color if i % 2 == 0 else accent_color
        
        # Center the line with padding
        padding = (box_width - len(line) - 4) // 2
        padded_line = ' ' * padding + line + ' ' * (box_width - len(line) - padding - 4)
        
        # Animate line appearance
        sys.stdout.write(primary_color + border_chars[8] + '\033[0m')
        sys.stdout.write(' ' * 2)
        
        # Typewriter effect for this line
        typewriter(padded_line, delay=0.01, color_code=line_color)
        
        # Print right border (already on next line from typewriter's \n)
        sys.stdout.write(primary_color + border_chars[8] + '\033[0m\n')
    
    # Decorative empty line
    print(primary_color + border_chars[8] + ' ' * (box_width - 2) + border_chars[8] + '\033[0m')
    
    # Bottom border with animated construction
    bottom = border_chars[2] + border_chars[7] * (box_width - 2) + border_chars[3]
    for char in bottom:
        sys.stdout.write(primary_color + char)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\033[0m')
    
    # Signature with wobble effect
    print()
    signature = "— Woody Allen (probably)"
    for _ in range(3):
        for offset in [-1, 0, 1]:
            sys.stdout.write(f'\r{" " * ((term_width - len(signature)) // 2 + offset)}{accent_color}{signature}\033[0m')
            sys.stdout.flush()
            time.sleep(0.05)
    print('\n')
    
    # Final dramatic pause with blinking cursor
    print('\033[5m' + ' ' * ((term_width - 3) // 2) + '...' + '\033[0m\n')

if __name__ == "__main__":
    try:
        print_woody_allen()
    except KeyboardInterrupt:
        print("\n\n\033[93m⟨Even interruption is philosophically interesting⟩\033[0m")
        sys.exit(0)