"""
Campbell's Soup Can #1459
Produced: 2026-01-07 20:40:44
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys
import time
from shutil import get_terminal_size

# ANSI escape codes for colors and styles
class Style:
    ORANGE = '\033[38;5;208m'
    TAN = '\033[38;5;223m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def centered_box(quote, author, width=70):
    """Generate ASCII art box with centered text"""
    top = Style.ORANGE + '╔' + '═' * (width-2) + '╗' + Style.RESET
    bottom = Style.ORANGE + '╚' + '═' * (width-2) + '╝' + Style.RESET
    side = Style.ORANGE + '║' + Style.RESET
    empty_line = side + ' ' * (width-2) + side
    
    lines = []
    words = quote.split(' ')
    current_line = ''
    
    # Wrap text to specified width
    for word in words:
        if len(current_line) + len(word) + 1 < width-4:
            current_line += (' ' + word).strip()
        else:
            lines.append(current_line.center(width-4))
            current_line = word
    lines.append(current_line.center(width-4))

    # Add some existential wings to the box
    art = [
        top,
        empty_line,
        *[side + ' ' + Style.BOLD + Style.TAN + line + Style.RESET + ' ' * (width - len(line) - 4) + ' ' + side for line in lines],
        empty_line,
        side + ' ' * ((width - len(author) - 6) // 2) + Style.ORANGE + '* ' + Style.TAN + author + Style.ORANGE + ' *' + ' ' * ((width - len(author) - 5) // 2) + side,
        bottom,
        '',
        Style.ORANGE + ' “' + Style.RESET,
        '   ' + Style.ORANGE + '\\' + Style.RESET,
        '    ' + Style.ORANGE + '\\' + Style.RESET + ' ' + Style.ORANGE + '/\\_/\\' + Style.RESET,
        '     ' + Style.ORANGE + '>^-^<' + Style.RESET + Style.ORANGE + '  The meaning of life? I think I left it here somewhere..."' + Style.RESET
    ]
    
    return '\n'.join(art)

def main():
    clear_screen()
    try:
        cols = get_terminal_size().columns
    except:
        cols = 80
    
    quote = "Life is meaningless, but have you tried their decaf? It's almost worse than the existential dread."
    author = "Woody Allen (probably)"
    
    # Make sure our box isn't too wide for the terminal
    box_width = min(70, cols - 10) if cols > 80 else 70
    
    # Make it slowly appear for dramatic effect
    animation = centered_box(quote, author, box_width)
    typewriter(animation, delay=0.008)
    time.sleep(1)
    
    # Flash the punchline for extra neurotic effect
    sys.stdout.write('\033[5A')  # Move cursor up 5 lines
    sys.stdout.write(Style.ORANGE + Style.BOLD + "    zZ^Z^zZzZz     " + Style.RESET)
    time.sleep(0.2)
    sys.stdout.write('\r' + ' ' * 30 + '\r')  # Clear the sleeping animation
    print(Style.RESET)  # Ensure colors reset

if __name__ == "__main__":
    main()