"""
Campbell's Soup Can #2783
Produced: 2026-03-15 14:49:46
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def philosophical_woody():
    # Woody Allen-style quote (original creation)
    quote = (
        "I'm not an existentialist, I'm a non-existententialist. "
        "It's the same thing but with more apathy and better therapy bills."
    )
    
    # Box drawing characters
    chars = {
        'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝',
        'h': '═', 'v': '║', 'x': '╬'
    }
    
    # ANSI colors (terminal safe)
    colors = {
        'yellow': '\033[93m',
        'cyan': '\033[96m',
        'magenta': '\033[95m',
        'green': '\033[92m',
        'reset': '\033[0m',
        'bold': '\033[1m'
    }
    
    # Calculate dimensions
    width = max(60, len(quote) + 10)
    height = 7
    
    # Clear screen and hide cursor
    sys.stdout.write('\033[?25l\033[2J\033[H')
    
    try:
        # Animated box construction
        for i in range(width + 2):
            # Top border
            sys.stdout.write(f'\033[{1};{i+1}H{colors["yellow"]}{chars["h"] if i < width else chars["tr"]}')
            time.sleep(0.01)
        
        for j in range(2, height + 1):
            # Left and right borders
            sys.stdout.write(f'\033[{j};1H{colors["cyan"]}{chars["v"]}')
            sys.stdout.write(f'\033[{j};{width+1}H{colors["cyan"]}{chars["v"]}')
            time.sleep(0.02)
        
        for i in range(width + 2):
            # Bottom border
            sys.stdout.write(f'\033[{height+1};{i+1}H{colors["yellow"]}{chars["h"] if i < width else chars["br"]}')
            time.sleep(0.01)
        
        # Corners
        sys.stdout.write(f'\033[1;1H{colors["magenta"]}{chars["tl"]}')
        sys.stdout.write(f'\033[1;{width+1}H{colors["magenta"]}{chars["tr"]}')
        sys.stdout.write(f'\033[{height+1};1H{colors["magenta"]}{chars["bl"]}')
        sys.stdout.write(f'\033[{height+1};{width+1}H{colors["magenta"]}{chars["br"]}')
        
        # Pulsing title
        title = " WOODY ALLEN'S PHILOSOPHICAL CORNER "
        title_x = (width - len(title)) // 2 + 1
        for _ in range(3):
            sys.stdout.write(f'\033[2;{title_x}H{colors["bold"]}{colors["green"]}{title}{colors["reset"]}')
            time.sleep(0.5)
            sys.stdout.write(f'\033[2;{title_x}H{" " * len(title)}')
            time.sleep(0.3)
        sys.stdout.write(f'\033[2;{title_x}H{colors["bold"]}{colors["green"]}{title}{colors["reset"]}')
        
        # Quote animation with neurotic wiggle
        words = quote.split()
        lines = []
        current_line = []
        current_len = 0
        
        # Word wrap
        for word in words:
            if current_len + len(word) + 1 <= width - 4:
                current_line.append(word)
                current_len += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_len = len(word)
        if current_line:
            lines.append(' '.join(current_line))
        
        # Animate quote with random wobbles
        start_y = 4
        for line_num, line in enumerate(lines):
            line_x = (width - len(line)) // 2 + 2
            
            for char_idx, char in enumerate(line):
                # Neurotic random horizontal jitter
                jitter = random.choice([0, 0, 0, 1, -1])
                wobble_x = line_x + char_idx + jitter
                
                # Random delay to simulate thinking
                time.sleep(random.uniform(0.02, 0.08))
                
                # Type with color oscillation
                color = colors['yellow'] if char_idx % 2 == 0 else colors['cyan']
                sys.stdout.write(f'\033[{start_y + line_num};{wobble_x}H{color}{char}{colors["reset"]}')
                sys.stdout.flush()
        
        # Blinking cursor at end
        cursor_y = start_y + len(lines) + 1
        cursor_x = (width // 2) + 1
        for _ in range(5):
            sys.stdout.write(f'\033[{cursor_y};{cursor_x}H{colors["magenta"]}█')
            sys.stdout.flush()
            time.sleep(0.3)
            sys.stdout.write(f'\033[{cursor_y};{cursor_x}H ')
            time.sleep(0.2)
        
        # Footer with existential footnote
        footnote = "(* This thought brought to you by crippling self-doubt)"
        footnote_x = (width - len(footnote)) // 2 + 1
        sys.stdout.write(f'\033[{height+2};{footnote_x}H{colors["green"]}{footnote}{colors["reset"]}')
        
        # Add some random philosophical particles
        for _ in range(20):
            y = random.randint(2, height)
            x = random.randint(2, width+1)
            particle = random.choice(['·', '•', '◦', '◉'])
            color = random.choice([colors['yellow'], colors['cyan'], colors['magenta']])
            sys.stdout.write(f'\033[{y};{x}H{color}{particle}{colors["reset"]}')
        
        sys.stdout.flush()
        
        # Wait for keypress
        sys.stdout.write(f'\033[{height+4};1H{colors["bold"]}Press any key to accept the absurdity...{colors["reset"]}')
        sys.stdout.flush()
        sys.stdin.read(1)
        
    finally:
        # Show cursor and reset
        sys.stdout.write('\033[?25h\033[0m\n')

if __name__ == "__main__":
    philosophical_woody()