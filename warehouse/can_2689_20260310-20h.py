"""
Campbell's Soup Can #2689
Produced: 2026-03-10 20:49:36
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

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
}

def slow_print(text, delay=0.03, color='white', end='\n', flush=True):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        if flush:
            sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write(end)
    if flush:
        sys.stdout.flush()

def neurotic_wobble(text, iterations=3):
    """Make text wobble nervously"""
    original = text
    wobble_chars = ['|', '/', '-', '\\']
    for _ in range(iterations):
        for char in wobble_chars:
            sys.stdout.write(f"\r{COLORS['yellow']}{char * len(original)}{COLORS['reset']}")
            time.sleep(0.05)
    sys.stdout.write(f"\r{text}")
    sys.stdout.flush()

def existential_crisis_box():
    """Display Woody Allen quote in a neurotic box"""
    quote = "I don't want to achieve immortality through my work. " \
            "I want to achieve it through not dying. " \
            "That way, if my work is forgotten, at least I'll still be here " \
            "to be disappointed about it."
    
    author = "— Woody Allen (probably oversharing)"
    
    # Box dimensions
    width = 70
    inner_width = width - 4
    
    # Clear screen and move cursor up a bit
    sys.stdout.write("\033[2J\033[3J\033[H")
    sys.stdout.write("\n" * 3)
    
    # Top border with nervous dots
    slow_print(f"{COLORS['dim']}·{COLORS['reset']}" * (width - 2), delay=0.01, color='dim')
    time.sleep(0.2)
    slow_print(f"{COLORS['cyan']}╔{'═' * (width - 2)}╗{COLORS['reset']}", delay=0.005)
    
    # Title with existential dread
    title = "EXISTENTIAL WISDOM FROM A NEUROTIC JEW"
    sys.stdout.write(f"{COLORS['bg_blue']}{COLORS['white']}{COLORS['bold']}")
    sys.stdout.write(f"║{title.center(width - 2)}║\n")
    sys.stdout.write(f"{COLORS['reset']}")
    time.sleep(0.3)
    
    # Separator that looks like a nervous heartbeat
    heartbeat = [COLORS['red'] + '♥' + COLORS['reset'], 
                 COLORS['dim'] + '♡' + COLORS['reset']]
    for _ in range(3):
        for beat in heartbeat:
            sys.stdout.write(f"\r{COLORS['dim']}║{beat * (width // 2)}{COLORS['reset']}")
            time.sleep(0.1)
    sys.stdout.write(f"\r{COLORS['dim']}╠{'═' * (width - 2)}╣{COLORS['reset']}\n")
    time.sleep(0.2)
    
    # Print quote with colors and line breaks
    words = quote.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= inner_width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print each line with alternating colors and nervous animation
    for i, line in enumerate(lines):
        # Color cycling
        line_color = ['cyan', 'yellow', 'magenta', 'green'][i % 4]
        
        # Add some neurotic spaces
        padding = random.randint(0, 2)
        padded_line = ' ' * padding + line
        
        sys.stdout.write(f"{COLORS['dim']}║{COLORS['reset']}")
        
        # Typewriter effect with color changes
        for j, char in enumerate(padded_line):
            # Occasionally change color mid-word for neurotic effect
            if random.random() < 0.1:
                line_color = random.choice(['cyan', 'yellow', 'magenta', 'green'])
            
            sys.stdout.write(f"{COLORS[line_color]}{char}{COLORS['reset']}")
            sys.stdout.flush()
            time.sleep(0.02 if char != ' ' else 0.01)
        
        # Right padding to fill line
        remaining = inner_width - len(padded_line)
        sys.stdout.write(' ' * remaining)
        
        sys.stdout.write(f"{COLORS['dim']}║{COLORS['reset']}\n")
        time.sleep(0.15)
        
        # Occasional nervous twitch
        if random.random() < 0.3:
            sys.stdout.write(f"\r{COLORS['dim']}║{' ' * (random.randint(0, inner_width))}║{COLORS['reset']}\n")
            time.sleep(0.05)
            sys.stdout.write(f"\033[F")  # Move cursor up
    
    time.sleep(0.3)
    
    # Separator that looks like it's questioning existence
    slow_print(f"{COLORS['dim']}╠{' ' * (width - 2)}╣{COLORS['reset']}", delay=0.01)
    
    # Author line with self-deprecating animation
    sys.stdout.write(f"{COLORS['dim']}║{COLORS['reset']}")
    neurotic_wobble(author, iterations=2)
    sys.stdout.write(f"{COLORS['dim']}║{COLORS['reset']}\n")
    time.sleep(0.2)
    
    # Bottom border with fading dots
    for i in range(width - 2):
        if i % 7 == 0:
            sys.stdout.write(f"{COLORS['dim']}·{COLORS['reset']}")
        else:
            sys.stdout.write(f"{COLORS['cyan']}═{COLORS['reset']}")
        time.sleep(0.005)
    sys.stdout.write(f"\n{COLORS['cyan']}╚{'═' * (width - 2)}╝{COLORS['reset']}")
    
    # Final message with nervous blinking
    time.sleep(0.5)
    sys.stdout.write(f"\n\n{COLORS['italic']}{COLORS['dim']}(press any key to continue being anxious...){COLORS['reset']}")
    sys.stdout.flush()
    try:
        # Wait for keypress with blinking cursor
        for _ in range(5):
            sys.stdout.write(f"\r{COLORS['dim']}_ {COLORS['reset']}")
            time.sleep(0.3)
            sys.stdout.write(f"\r{COLORS['dim']}‗{COLORS['reset']}")
            time.sleep(0.3)
        input()
    except:
        pass

if __name__ == "__main__":
    existential_crisis_box()