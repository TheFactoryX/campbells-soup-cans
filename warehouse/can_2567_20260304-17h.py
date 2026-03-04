"""
Campbell's Soup Can #2567
Produced: 2026-03-04 17:03:06
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

def typewriter(text, delay=0.03, color='\033[36m'):
    """Print text with typewriter effect in specified color"""
    for char in text:
        sys.stdout.write(color + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print()

def philosophical_quote_box():
    """Display a Woody Allen style quote in a fancy animated box"""
    
    # Original Woody Allen-esque quote
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying. "
        "It's much less work, and frankly, I'm lazy. "
        "Existentially speaking, I'm a collection of anxieties "
        "trying to find the meaning in my own sitcom."
    )
    
    # Box dimensions
    width = 70
    quote_lines = []
    words = quote.split()
    current_line = ""
    
    # Wrap quote to box width
    for word in words:
        if len(current_line + word) + 1 <= width - 4:  # Account for borders/padding
            current_line += (" " if current_line else "") + word
        else:
            quote_lines.append(current_line)
            current_line = word
    if current_line:
        quote_lines.append(current_line)
    
    # Animation phases for the box
    border_chars = ['░', '▒', '▓', '█', '▓', '▒', '░']
    animate_frames = 5
    
    # Get terminal width for centering
    try:
        import shutil
        term_width = shutil.get_terminal_size().columns
    except:
        term_width = 80
    
    # Center the box
    box_width = width + 4
    left_padding = max(0, (term_width - box_width) // 2)
    
    for frame in range(animate_frames):
        # Clear previous output (works in most terminals)
        sys.stdout.write('\033[2K\033[1G' * (len(quote_lines) + 6))
        sys.stdout.flush()
        
        # Print top border with animation
        print(' ' * left_padding + '\033[33m' + '█' * box_width + '\033[0m')
        
        # Title line
        title = " WOODY ALLEN'S DEEP THOUGHTS (FOR Lazy People) "
        print(' ' * left_padding + '\033[33m█\033[0m' + 
              '\033[1;33m' + title.center(width) + '\033[0m' + 
              '\033[33m█\033[0m')
        
        # Separator
        print(' ' * left_padding + '\033[33m█' + '─' * width + '█\033[0m')
        
        # Quote lines with typewriter effect on final frame
        for i, line in enumerate(quote_lines):
            padded_line = line.ljust(width)
            
            # Wobble effect on intermediate frames
            if frame < animate_frames - 1:
                wobble = random.choice(['', '\033[2m', '\033[4m'])
                sys.stdout.write(' ' * left_padding + '\033[33m█\033[0m ' + 
                               wobble + '\033[36m' + padded_line + '\033[0m' + 
                               wobble + ' \033[33m█\033[0m\n')
            else:
                # Final frame: typewriter effect
                sys.stdout.write(' ' * left_padding + '\033[33m█\033[0m ')
                typewriter(padded_line, delay=0.02, color='\033[36m')
                sys.stdout.write(' ' * left_padding + '\033[33m█\033[0m\n')
        
        # Bottom separator
        print(' ' * left_padding + '\033[33m█' + '─' * width + '█\033[0m')
        
        # Footer with animated dots
        footer = "...or maybe I'm just overthinking it"
        footer_dots = '.' * ((frame % 3) + 1)
        print(' ' * left_padding + '\033[33m█\033[0m' + 
              '\033[2;37m' + footer.center(width - len(footer_dots)) + 
              '\033[1;33m' + footer_dots + '\033[0m' + 
              '\033[33m█\033[0m')
        
        # Bottom border
        print(' ' * left_padding + '\033[33m' + '█' * box_width + '\033[0m')
        
        if frame < animate_frames - 1:
            time.sleep(0.3)
    
    # Final dramatic pause
    time.sleep(1.5)
    print('\n' + ' ' * left_padding + '\033[2;37m⟨ Fin ∽ Ambient jazz plays ⟩\033[0m\n')

# Woody Allen's existential crisis begins here
if __name__ == "__main__":
    try:
        philosophical_quote_box()
    except KeyboardInterrupt:
        print("\n\033[31m(Ctrl+C detected. Even my philosophical output has commitment issues.)\033[0m")
        sys.exit(0)