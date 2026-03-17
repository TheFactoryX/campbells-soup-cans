"""
Campbell's Soup Can #2812
Produced: 2026-03-17 10:09:22
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
import random
import sys
from itertools import cycle

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
    FG_BLACK = '\033[30m'
    FG_RED = '\033[31m'
    FG_GREEN = '\033[32m'
    FG_YELLOW = '\033[33m'
    FG_BLUE = '\033[34m'
    FG_MAGENTA = '\033[35m'
    FG_CYAN = '\033[36m'
    FG_WHITE = '\033[37m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Bright variants
    FG_LIGHTRED = '\033[91m'
    FG_LIGHTGREEN = '\033[92m'
    FG_LIGHTYELLOW = '\033[93m'
    FG_LIGHTBLUE = '\033[94m'
    FG_LIGHTMAGENTA = '\033[95m'
    FG_LIGHTCYAN = '\033[96m'
    FG_LIGHTWHITE = '\033[97m'

# Woody Allen style quotes (original creation)
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens. " 
    "The things I'm afraid of are much worse - like my accountant calling.",
    
    "Life is divided into the horrible and the miserable. "
    "The horrible are the people with terminal illnesses. "
    "The miserable are everyone else. I'm miserable, you're miserable... "
    "heck, even my therapist is miserable!",
    
    "I don't want to achieve immortality through my work; "
    "I want to achieve it through not dying. "
    "But my publisher says that's not a marketable strategy.",
    
    "Existentialism is the philosophy that says life has no meaning, "
    "which explains why my coffee tastes like despair and my plants are suicidal.",
    
    "What a absurd world we live in! "
    "I spend half my time worrying about death and the other half "
    "worrying about whether I locked the door. "
    "Spoiler: I didn't.",
    
    "They say you can't take it with you. "
    "But what if I just carry it? "
    "My neuroses are lightweight and fold neatly into a carry-on.",
    
    "My therapist told me I have a fear of commitment. "
    "I said, 'Let's talk about that sometime.' "
    "She hasn't called back in three weeks.",
    
    "The universe is expanding, my waistline is expanding, "
    "and my chances of finding true love are contracting. "
    "Somehow this feels like a fair trade."
]

def clear_screen():
    """Clear terminal screen."""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def typing_effect(text, color, delay=0.03, end='\n'):
    """Print text with typing effect."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write(end)
    sys.stdout.flush()

def spinning_cursor(duration=3):
    """Show a spinning cursor for given duration."""
    spinner = cycle(['|', '/', '-', '\\'])
    start = time.time()
    while time.time() - start < duration:
        sys.stdout.write(f'\r{Colors.FG_CYAN}Thinking{Colors.RESET} ' + next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

def fade_in_text(text, color, steps=10, delay=0.05):
    """Gradually fade in text."""
    for i in range(steps + 1):
        alpha = i / steps
        brightness = int(255 * alpha)
        # Using 24-bit color (RGB) for smooth fade
        sys.stdout.write(f'\033[38;2;{brightness};{brightness};{brightness}m')
        sys.stdout.write(text + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()

def draw_neurotic_border(width=60):
    """Draw a wobbly, neurotic border."""
    border_chars = ['+', '-', '~', '.', '*', ';']
    top = random.choice(border_chars) * (width - 2)
    bottom = random.choice(border_chars) * (width - 2)
    
    print(Colors.FG_LIGHTRED)
    print(' ' + top)
    print(Colors.RESET, end='')
    return width

def main():
    clear_screen()
    
    # Dramatic pause with spinning cursor
    print(f"\n{Colors.FG_LIGHTYELLOW}{Colors.ITALIC}Searching for wisdom in the void...{Colors.RESET}")
    spinning_cursor(2)
    
    # Select random quote
    quote = random.choice(QUOTES)
    words = quote.split()
    
    # Wrap text to fit in box
    lines = []
    current_line = []
    current_len = 0
    max_width = 58  # Leave 2 for borders
    
    for word in words:
        if current_len + len(word) + (1 if current_line else 0) <= max_width:
            current_line.append(word)
            current_len += len(word) + (1 if current_line else 0)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_len = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Draw fancy border
    box_width = max(len(line) for line in lines) + 4
    draw_neurotic_border(box_width)
    
    # Print quote with dramatic effects
    time.sleep(0.5)
    
    for i, line in enumerate(lines):
        if i == 0:  # First line gets special treatment
            fade_in_text(line.center(box_width - 2), Colors.FG_LIGHTWHITE + Colors.BOLD)
        elif i == len(lines) - 1:  # Last line gets ellipsis effect
            sys.stdout.write(f"{Colors.FG_LIGHTWHITE}| {line}")
            for _ in range(3):
                sys.stdout.write(f"{Colors.FG_LIGHTRED}...")
                sys.stdout.flush()
                time.sleep(0.3)
                sys.stdout.write('\b\b\b   \b\b\b')
                sys.stdout.flush()
            print(f"{Colors.RESET} |")
        else:
            typing_effect(line.center(box_width - 2), 
                         random.choice([Colors.FG_WHITE, Colors.FG_LIGHTWHITE, Colors.FG_LIGHTCYAN]),
                         delay=0.04)
    
    time.sleep(0.5)
    draw_neurotic_border(box_width)
    
    # Philosophical footer
    time.sleep(1)
    footer = random.choice([
        "∴ Nothing is certain except death, taxes, and my dentist's bills",
        "※ All phenomena are interrelated, except my laundry schedule",
        "⍨ I think, therefore I'm confused"
    ])
    
    print(f"\n{Colors.FG_LIGHTMAGENTA}{Colors.DIM}{footer}{Colors.RESET}\n")
    
    # Final dramatic pause
    time.sleep(1)
    print(f"{Colors.FG_LIGHTRED}...and then I remembered I left the stove on.{Colors.RESET}")
    time.sleep(2)
    print(f"{Colors.FG_GREEN}Just kidding. (I hope.){Colors.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FG_YELLOW}Ah, existential crisis aborted. "
              f"Same time tomorrow?{Colors.RESET}")
        sys.exit(0)