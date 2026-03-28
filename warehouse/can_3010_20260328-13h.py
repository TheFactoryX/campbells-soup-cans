"""
Campbell's Soup Can #3010
Produced: 2026-03-28 13:19:02
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random
import os

# Clear screen and hide cursor
def init_screen():
    sys.stdout.write('\033[2J\033[?25l')
    sys.stdout.flush()

# Show cursor again
def cleanup():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright versions
    BR_BLACK = '\033[90m'
    BR_RED = '\033[91m'
    BR_GREEN = '\033[92m'
    BR_YELLOW = '\033[93m'
    BR_BLUE = '\033[94m'
    BR_MAGENTA = '\033[95m'
    BR_CYAN = '\033[96m'
    BR_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Woody Allen style quotes (original creations)
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "The seating is terrible and the previews are endless.",
    
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon. "
    "Like a bad meal at a restaurant that charges you for the ambiance of your own regret.",
    
    "I don't want to achieve immortality through my work; I want to achieve it through not dying. "
    "That way I can finally get around to reading all those books I keep buying "
    "and immediately using as coasters.",
    
    "What if everything is meaningless? Then I wasted a lot of time worrying about it. "
    "On the other hand, if it's meaningful, I still wasted a lot of time. "
    "It's a lose-lose, like my relationship with my therapist.",
    
    "I took a course on happiness. It was okay. The syllabus was good, "
    "but the attendance policy was ridiculous. You had to be happy to get credit.",
    
    "My therapist says I have a fear of commitment. I'd commit to that, "
    "but I'm worried it might get serious.",
    
    "The universe is 93 billion light-years across and I still can't find a decent pair of socks. "
    "Either the cosmos is against me or my laundry room is a black hole.",
    
    "I'm not neurotic, I'm just... wait, did I lock the door? "
    "Is the stove still on? Did I remember to be anxious about the right things today?",
]

def typewriter(text, color=Colors.WHITE, delay=0.03, end='\n'):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write(end)
    sys.stdout.flush()

def draw_wobbly_box(text, width=50):
    """Draw a wobbly hand-drawn style box"""
    top = '╭' + '─' * (width - 2) + '╮'
    bottom = '╰' + '─' * (width - 2) + '╯'
    
    sys.stdout.write(Colors.BR_CYAN + top + Colors.RESET + '\n')
    
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        if sum(len(w) for w in current_line) + len(word) + len(current_line) <= width - 4:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    for line in lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        sys.stdout.write(Colors.BR_CYAN + '│' + Colors.RESET)
        sys.stdout.write(' ' * left_pad + Colors.BR_YELLOW + line + Colors.RESET + ' ' * right_pad)
        sys.stdout.write(Colors.BR_CYAN + '│' + Colors.RESET + '\n')
    
    sys.stdout.write(Colors.BR_CYAN + bottom + Colors.RESET + '\n')

def spinning_cursor():
    """Generator for spinning cursor animation"""
    while True:
        for cursor in '|/-\\':
            yield cursor

def main():
    init_screen()
    
    try:
        # Animated header
        title = "WOODY ALLEN PHILOSOPHY"
        spinner = spinning_cursor()
        
        sys.stdout.write('\n' * 3)
        for i, char in enumerate(title):
            sys.stdout.write(f"\r{' ' * 20}{Colors.BR_MAGENTA}{Colors.BOLD}")
            for j, c in enumerate(title[:i+1]):
                color = Colors.BR_RED if j == i else Colors.BR_YELLOW
                sys.stdout.write(color + c + Colors.RESET)
                sys.stdout.flush()
                time.sleep(0.05)
            sys.stdout.write(f" {next(spinner)}{Colors.RESET}")
            time.sleep(0.1)
        sys.stdout.write('\n' * 2)
        
        # Randomly select a quote
        quote = random.choice(QUOTES)
        
        # Draw the quote in a wobbly box with typewriter effect
        draw_wobbly_box(quote, width=60)
        time.sleep(0.5)
        
        # Add some existential flourishes
        sys.stdout.write('\n')
        typewriter("          ...or so he tells his therapist.", 
                  Colors.BR_BLUE + Colors.DIM, delay=0.06)
        sys.stdout.write('\n')
        
        # Animated existential dots
        for _ in range(3):
            sys.stdout.write(f"\r{' ' * 30}{Colors.BR_RED}...{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write(f"\r{' ' * 30}{Colors.BR_RED}... {Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write(f"\r{' ' * 30}{Colors.BR_RED}....{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write('\r' + ' ' * 35 + '\n')
        
        # Final flourish
        time.sleep(0.8)
        typewriter("  (The universe is indifferent. Also, your shoes are untied.)",
                  Colors.BR_GREEN + Colors.ITALIC, delay=0.04)
        
        sys.stdout.write('\n\n')
        time.sleep(1)
        
    finally:
        cleanup()

if __name__ == "__main__":
    main()