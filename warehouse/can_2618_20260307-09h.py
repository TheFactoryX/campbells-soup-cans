"""
Campbell's Soup Can #2618
Produced: 2026-03-07 09:43:46
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

def slow_print(text, delay=0.03, color='\033[97m'):
    """Print text with typewriter effect and color"""
    reset = '\033[0m'
    for char in text:
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def philosophic_box():
    """Display Woody Allen's existential wit in a fancy box"""
    # ANSI color codes
    gold = '\033[38;5;178m'
    cyan = '\033[36m'
    yellow = '\033[93m'
    bold = '\033[1m'
    reset = '\033[0m'
    dim = '\033[2m'
    
    # Woody Allen's neurotic wisdom
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying. "
        "That way, I can continue to make the same mistakes "
        "without the pressure of being dead."
    )
    
    # Create decorative border
    border = gold + '✧･ﾟ: *･ﾟ✧･ﾟ: *･ﾟ✧･ﾟ: *･ﾟ✧･ﾟ: *･ﾟ✧' + reset
    
    # Clear screen (optional)
    print('\033[2J\033[H', end='')
    
    # Animated entrance
    for _ in range(3):
        sys.stdout.write('\r' + dim + 'Thinking' + reset)
        time.sleep(0.3)
        sys.stdout.write('\r' + dim + 'Thinking.' + reset)
        time.sleep(0.3)
        sys.stdout.write('\r' + dim + 'Thinking..' + reset)
        time.sleep(0.3)
        sys.stdout.write('\r' + dim + 'Thinking...' + reset)
        time.sleep(0.3)
    print('\n')
    
    # Print decorative top
    print(border.center(80))
    print()
    
    # Centered title
    title = bold + cyan + "~ WISDOM FROM THE NEUROTIC ~" + reset
    print(title.center(80))
    print()
    
    # Print quote in formatted box
    box_width = 60
    print(gold + '╔' + '═' * (box_width - 2) + '╗' + reset)
    
    # Word wrap the quote
    words = quote.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 <= box_width - 6:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print each line with alternating colors
    for i, line in enumerate(lines):
        padding = (box_width - 6 - len(line)) // 2
        extra_padding = (box_width - 6 - len(line)) % 2
        
        # Alternate between yellow and white for quote text
        line_color = yellow if i % 2 == 0 else '\033[97m'
        
        print(gold + '║' + reset + ' ' * padding + 
              line_color + line + reset + 
              ' ' * (padding + extra_padding) + gold + ' ║' + reset)
    
    print(gold + '╚' + '═' * (box_width - 2) + '╝' + reset)
    print()
    
    # Philosophical footer with animation
    footer_lines = [
        dim + "• Existence is a Temporary Condition •" + reset,
        dim + "• Death is Nature's way of telling you to slow down •" + reset,
        dim + "• I'm not afraid of death; I just don't want to be there when it happens •" + reset
    ]
    
    for line in footer_lines:
        slow_print(line.center(80), delay=0.02, color=dim)
        time.sleep(0.5)
    
    print()
    print(gold + '✧･ﾟ: *･ﾟ✧･ﾟ: *･ﾟ✧･ﾟ: *･ﾟ✧･ﾟ: *･ﾟ✧' + reset)
    print()
    
    # Final dramatic pause
    time.sleep(1)
    slow_print("Now go ponder your mortality... or take a nap. Same difference.", 
               delay=0.04, color='\033[38;5;244m')

if __name__ == "__main__":
    philosophic_box()