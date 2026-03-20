"""
Campbell's Soup Can #2873
Produced: 2026-03-20 20:49:53
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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
from itertools import cycle

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'grey': '\033[90m',
}

# Woody Allen-style philosophical quote
quote = (
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "It's not that I'm afraid of dying, it's that I don't want to miss a single episode of anything. "
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon. "
    "I don't want to achieve immortality through my work; I want to achieve it through not dying."
)

# Artistic box drawing characters
BOX_CHARS = {
    'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝',
    'h': '═', 'v': '║', 'vl': '╠', 'vr': '╣', 'th': '╦', 'bh': '╩'
}

def typewriter(text, color='yellow', delay=0.03, end='\n'):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print(end=end)

def draw_box(lines, width, title=None):
    """Draw a fancy box around text"""
    # Calculate actual width needed
    max_len = max(len(line) for line in lines) if lines else 0
    box_width = max(max_len + 4, width)
    
    # Top border
    print(f"{COLORS['cyan']}{BOX_CHARS['tl']}{BOX_CHARS['h'] * (box_width-2)}{BOX_CHARS['tr']}{COLORS['reset']}")
    
    # Optional title line
    if title:
        title_text = f" {title} "
        padding = (box_width - len(title_text) - 2) // 2
        extra = (box_width - len(title_text) - 2) % 2
        print(f"{COLORS['cyan']}{BOX_CHARS['v']}{' ' * padding}"
              f"{COLORS['bold']}{COLORS['white']}{title_text}{COLORS['reset']}"
              f"{' ' * (padding + extra)}{COLORS['cyan']}{BOX_CHARS['v']}{COLORS['reset']}")
        print(f"{COLORS['cyan']}{BOX_CHARS['vl']}{BOX_CHARS['h'] * (box_width-2)}{BOX_CHARS['vr']}{COLORS['reset']}")
    
    # Content lines
    for line in lines:
        padding = box_width - len(line) - 2
        print(f"{COLORS['cyan']}{BOX_CHARS['v']}{COLORS['reset']} {line}{' ' * padding} {COLORS['cyan']}{BOX_CHARS['v']}{COLORS['reset']}")
    
    # Bottom border
    print(f"{COLORS['cyan']}{BOX_CHARS['bl']}{BOX_CHARS['h'] * (box_width-2)}{BOX_CHARS['br']}{COLORS['reset']}")

def spinning_cursor(duration=2):
    """Show a spinning cursor animation"""
    cursor = cycle(['|', '/', '-', '\\'])
    start = time.time()
    while time.time() - start < duration:
        sys.stdout.write(f"\r{COLORS['grey']}Thinking{next(cursor)}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')

def philosophical_display():
    """Main display function with multiple visual effects"""
    
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[1;1H")
    sys.stdout.flush()
    
    # Animated header
    print(f"\n{COLORS['magenta']}{'='*60}{COLORS['reset']}")
    time.sleep(0.3)
    print(f"{COLORS['bold']}{COLORS['white']}  WISDOM FROM THE NEUROTIC MASTER{COLORS['reset']}")
    print(f"{COLORS['magenta']}{'='*60}{COLORS['reset']}\n")
    time.sleep(0.5)
    
    # Spinner while "generating" wisdom
    spinning_cursor(1.5)
    
    # Process quote into lines
    words = quote.split()
    lines = []
    current_line = []
    current_len = 0
    
    for word in words:
        if current_len + len(word) + (1 if current_line else 0) <= 65:
            current_line.append(word)
            current_len += len(word) + (1 if current_line else 0)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_len = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Draw the quote in a fancy box
    draw_box(lines, 70, title="WOODY ALLEN ON EXISTENCE")
    
    # Animated signature
    time.sleep(0.5)
    print(f"\n{COLORS['grey']}   — An existential thought, probably{COLORS['reset']}")
    time.sleep(0.3)
    
    # Final whimsical touch
    print(f"\n{COLORS['cyan']}{'·' * 40}{COLORS['reset']}")
    typewriter("(Pause for neurotic reflection...)", color='green', delay=0.1)
    
    # Quick color flash at the end
    for color in ['red', 'yellow', 'blue', 'magenta']:
        sys.stdout.write(f"\r{COLORS[color]} existential dread? Maybe later. {COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

if __name__ == "__main__":
    try:
        philosophical_display()
    except KeyboardInterrupt:
        print(f"\n{COLORS['red']}\nInterrupted! But hey, I was just getting to the good part.{COLORS['reset']}")
        sys.exit(0)