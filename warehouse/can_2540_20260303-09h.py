"""
Campbell's Soup Can #2540
Produced: 2026-03-03 09:00:10
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys
import os

# Clear screen and hide cursor for cleaner animation
def setup_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\033[?25l")  # Hide cursor
    sys.stdout.flush()

# Restore cursor on exit
def restore_terminal():
    sys.stdout.write("\033[?25h")  # Show cursor
    sys.stdout.flush()

# Woody Allen style quote
quote = (
    "I don't want to achieve immortality through my work. "
    "I want to achieve it through not dying. "
    "It's not that I'm afraid to die. "
    "I just don't want to be there when it happens."
)

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'cyan': '\033[96m',
    'yellow': '\033[93m',
    'magenta': '\033[95m',
    'green': '\033[92m',
    'red': '\033[91m',
    'blue': '\033[94m',
}

# Woody Allen ASCII portrait (simplified)
portrait = r"""
       .--.
      / O  \
     |   O  |
      \  O / 
       `--'
        ||
       /  \
      /    \
     /      \
    /        \
"""

def animate_portrait():
    """Make the portrait bob up and down slightly"""
    for i in range(3):
        sys.stdout.write("\033[2J\033[H")  # Clear screen and move to home
        offset = " " * random.randint(0, 2)
        for line in portrait.split('\n'):
            print(COLORS['cyan'] + offset + line + COLORS['reset'])
        time.sleep(0.2)

def typewriter_effect(text, delay=0.03, color='yellow'):
    """Print text with typewriter effect and random jitters"""
    for char in text:
        # Randomly change color for neurotic effect
        if random.random() < 0.1:
            current_color = random.choice(['yellow', 'magenta', 'green', 'cyan'])
        else:
            current_color = color
            
        sys.stdout.write(COLORS[current_color] + char + COLORS['reset'])
        sys.stdout.flush()
        # Variable delay for "nervous" typing
        time.sleep(delay + random.uniform(-0.01, 0.02))

def draw_box(text, width=60):
    """Draw a fancy box around text"""
    lines = []
    # Split text into lines that fit the box
    words = text.split()
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + (1 if current_line else 0) <= width - 4:
            current_line.append(word)
            current_length += len(word) + (1 if current_line else 0)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Draw box
    border = COLORS['blue'] + '+' + '─' * (width - 2) + '+' + COLORS['reset']
    empty = COLORS['blue'] + '│' + ' ' * (width - 2) + '│' + COLORS['reset']
    
    print(border)
    print(empty)
    
    for line in lines:
        padding = (width - 4 - len(line)) // 2
        print(COLORS['blue'] + '│' + COLORS['reset'] + 
              ' ' * padding + COLORS['yellow'] + line + COLORS['reset'] + 
              ' ' * (width - 4 - len(line) - padding) + 
              COLORS['blue'] + '│' + COLORS['reset'])
    
    print(empty)
    print(border)

def main():
    try:
        setup_terminal()
        
        # Animate portrait
        animate_portrait()
        time.sleep(0.5)
        
        # Print dramatic header
        sys.stdout.write("\033[2J\033[H")  # Clear screen
        header = COLORS['magenta'] + COLORS['bold'] + 
                "╔═══════════════════════════════════════════════════╗" + COLORS['reset']
        title = COLORS['magenta'] + "║" + COLORS['reset'] + 
               COLORS['yellow'] + "  WOODY ALLEN'S PHILOSOPHICAL MEDITATIONS  " + 
               COLORS['reset'] + COLORS['magenta'] + "║" + COLORS['reset']
        footer_header = COLORS['magenta'] + "╚═══════════════════════════════════════════════════╝" + COLORS['reset']
        
        print("\n" * 2)
        print(header.center(os.get_terminal_size().columns))
        print(title.center(os.get_terminal_size().columns))
        print(footer_header.center(os.get_terminal_size().columns))
        print("\n" * 2)
        
        time.sleep(1)
        
        # Animate the quote being "thought"
        print(COLORS['cyan'] + "凝思中... (thinking...)" + COLORS['reset'])
        time.sleep(1)
        
        # Clear and show quote in box
        sys.stdout.write("\033[2J\033[H")
        draw_box(quote)
        time.sleep(0.5)
        
        # Typewriter effect below the box
        print("\n")
        typewriter_effect("─ つまり、要するにさ... (I mean, in other words...)")
        print("\n")
        time.sleep(0.3)
        
        # Final dramatic touch
        final_thought = random.choice([
            "Existential dread? I prefer it Medium-Rare.",
            "My therapist says I have a preoccupation with mortality. "
            "I told him, 'That's because I'm going to die.'",
            "I'm not nihilistic. I'm just... practically oriented.",
            "The universe is infinite. My apartment is not. "
            "This is the source of all my anxiety."
        ])
        
        typewriter_effect(final_thought, delay=0.04, color='green')
        
        print("\n" * 2)
        print(COLORS['red'] + "™ Woody Allen (probably)" + COLORS['reset'].rjust(40))
        print("\n" * 2)
        
        time.sleep(2)
        
    finally:
        restore_terminal()

if __name__ == "__main__":
    main()