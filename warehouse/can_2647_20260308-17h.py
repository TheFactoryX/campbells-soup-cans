"""
Campbell's Soup Can #2647
Produced: 2026-03-08 17:39:39
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

# Clear screen and get terminal size
os.system('cls' if os.name == 'nt' else 'clear')
term_width = os.get_terminal_size().columns

# Woody Allen style quote collection (all original!)
woody_quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "That's why I always leave the room when someone mentions it. "
    "It's not that I'm cowardly, it's just that I find the whole concept of non-existence "
    "to be in extremely poor taste.",
    
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon. "
    "I mean, really, 80 years? That's barely enough time to finish a crossword puzzle "
    "and decide if you want the fish or the chicken.",
    
    "I don't want to achieve immortality through my work; I want to achieve it through not dying. "
    "That way I can be around to complain about the weather in whichever century we're in.",
    
    "I took a class on existentialism. It was depressing. The professor kept saying "
    "'Existence precedes essence' and I kept thinking 'My existence precedes my essence? '
    Then why do I still have no idea what to order for dinner?'",
    
    "My therapist told me the way to achieve true enlightenment is to live in the moment. "
    "So I'm living in the moment. The moment is 3:17 PM. I'm thinking about lunch. "
    "It was a sandwich. Not my best moment."
]

def typewriter(text, color_code, delay=0.02, end='\n'):
    """Print text with typewriter effect and color"""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print(end=end)

def spinning_cursor():
    """Animated spinning cursor"""
    while True:
        for cursor in '|/-\\':
            yield cursor

def draw_neurotic_border(width):
    """Draw a wobbly, neurotic-looking border"""
    patterns = ['-', '~', '·', '⁓', '~']
    top = '┌'
    bottom = '└'
    for i in range(width - 2):
        top += random.choice(patterns)
        bottom += random.choice(patterns)
    top += '┐'
    bottom += '┘'
    return top + '\n' + bottom

def main():
    # Choose random Woody Allen quote
    quote = random.choice(woody_quotes)
    
    # ANSI color codes
    NEUROTIC_GREEN = '\033[38;2;152;195;121m'  # Sage green (anxious but natural)
    ANXIOUS_YELLOW = '\033[38;2;255;218;121m'   # Worried yellow
    EXISTENTIAL_GRAY = '\033[38;2;120;120;120m' # Foggy gray
    PANICKED_RED = '\033[38;2;220;90;90m'       # Flustered red
    RESET = '\033[0m'
    
    # Calculate box dimensions
    box_width = min(80, term_width - 4)
    if box_width < 40:
        box_width = 40
    
    # Split quote into lines that fit
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line else word
        if len(test_line) <= box_width - 4:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Create the neurotic box
    top_border = draw_neurotic_border(box_width).split('\n')[0]
    bottom_border = draw_neurotic_border(box_width).split('\n')[1]
    
    # Clear and center everything
    print('\n' * 2)
    
    # Animated thinking header
    spinner = spinning_cursor()
    thinking_text = "Woody Allen ponders the void"
    print(' ' * ((term_width - len(thinking_text)) // 2), end='')
    for _ in range(3):
        sys.stdout.write(f"\r{EXISTENTIAL_GRAY}{thinking_text} {next(spinner)}\033[0m")
        sys.stdout.flush()
        time.sleep(0.3)
    print('\r' + ' ' * term_width + '\r')  # Clear the line
    
    # Print top border with slight wobble
    print(' ' * ((term_width - box_width) // 2) + NEUROTIC_GREEN + top_border + RESET)
    
    # Print title line
    title = "  ── ☠  HEAVY PHILOSOPHY FROM AN INSOMNIAC  ☠ ──  "
    print(' ' * ((term_width - box_width) // 2) + 
          f"{ANXIOUS_YELLOW}║{title:^{box_width-2}}║{RESET}")
    
    # Empty line
    print(' ' * ((term_width - box_width) // 2) + 
          f"{EXISTENTIAL_GRAY}║{' ' * (box_width-2)}║{RESET}")
    
    # Print quote with typewriter effect, random colors for neurotic variety
    for i, line in enumerate(lines):
        line_text = f"  {line}"
        padding = box_width - 4 - len(line_text)
        
        # Random color for each line (neurotic mood swings)
        colors = [NEUROTIC_GREEN, ANXIOUS_YELLOW, EXISTENTIAL_GRAY]
        if i == len(lines) - 1:  # Last line gets panicked red
            colors = [PANICKED_RED] + colors
        
        line_color = random.choice(colors)
        
        # Print with typewriter effect
        print(' ' * ((term_width - box_width) // 2) + 
              f"{line_color}║{line_text}{' ' * padding}║{RESET}")
        
        # Slight random pause between lines (nervous habit)
        time.sleep(0.1 * random.uniform(0.3, 1.0))
    
    # Empty line
    print(' ' * ((term_width - box_width) // 2) + 
          f"{EXISTENTIAL_GRAY}║{' ' * (box_width-2)}║{RESET}")
    
    # Signature line with wobble
    signature = "─ ✦ Woody Allen, probably in his pajamas at 3 AM ✦ ─"
    print(' ' * ((term_width - box_width) // 2) + 
          f"{NEUROTIC_GREEN}║{signature:^{box_width-2}}║{RESET}")
    
    # Print bottom border
    print(' ' * ((term_width - box_width) // 2) + 
          f"{NEUROTIC_GREEN}{bottom_border}{RESET}")
    
    # Final existential footnote that fades away
    print('\n')
    footnote = "  (This quote brought to you by insomnia, anxiety, and a deep "
    footnote2 = "   suspicion that nothing we do matters in the grand scheme.)"
    
    print(' ' * ((term_width - len(footnote)) // 2) + 
          f"{EXISTENTIAL_GRAY}{footnote}{RESET}")
    print(' ' * ((term_width - len(footnote2)) // 2) + 
          f"{EXISTENTIAL_GRAY}{footnote2}{RESET}")
    
    # Fade effect for final line
    for opacity in range(40, 9, -2):
        sys.stdout.write(f"\033[38;2;{opacity};{opacity};{opacity}m")
        print(' ' * ((term_width - len(footnote2)) // 2) + footnote2, end='\r')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n' + ' ' * (term_width // 2) + "...\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{EXISTENTIAL_GRAY}  See? I knew you'd leave early. Typical.\033[0m")
        sys.exit(0)