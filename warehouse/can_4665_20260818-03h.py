"""
Campbell's Soup Can #4665
Produced: 2026-08-18 03:57:42
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
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

# ANSI Color Codes
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    
    # Foreground
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;213m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Woody Allen ASCII Art
WOODY_ART = f"""
{C.CYAN}        ╭─────────────────────────╮
        │  {C.YELLOW}█████████████████████████████████{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}█ {C.BLUE}╭─────────────────╮ {C.WHITE}█ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}█ {C.BLUE}│  {C.MAGENTA}◉{C.BLUE}           {C.MAGENTA}◉{C.BLUE}  │ {C.WHITE}█ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}█ {C.BLUE}│    {C.YELLOW}┌───┐    {C.BLUE}│ {C.WHITE}█ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}█ {C.BLUE}│    {C.YELLOW}│   │    {C.BLUE}│ {C.WHITE}█ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}█ {C.BLUE}│    {C.YELLOW}└───┘    {C.BLUE}│ {C.WHITE}█ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}█ {C.BLUE}╰─────────────────╯ {C.WHITE}█ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█ {C.WHITE}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ {C.YELLOW}█{C.CYAN}  │
        │  {C.YELLOW}█████████████████████████████████{C.CYAN}  │
        ╰─────────────────────────╯{C.RST}
"""

# The Quote
QUOTE = "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia."
ATTRIBUTION = "— Woody Allen (probably)"

# Decorative elements
STARS = ["✦", "✧", "★", "☆", "✶", "✷", "✸", "✹"]
SPARKLES = [C.YELLOW, C.MAGENTA, C.CYAN, C.PINK, C.ORANGE]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.WHITE, delay=0.03, end='\n'):
    for char in text:
        print(f"{color}{char}{C.RST}", end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def sparkle_animation(duration=2.0):
    """Background sparkle animation"""
    start = time.time()
    cols = 80
    rows = 20
    while time.time() - start < duration:
        x = random.randint(2, cols - 2)
        y = random.randint(2, rows - 2)
        star = random.choice(STARS)
        color = random.choice(SPARKLES)
        move_cursor(y, x)
        print(f"{color}{star}{C.RST}", end='', flush=True)
        time.sleep(0.05)
        move_cursor(y, x)
        print(" ", end='', flush=True)

def draw_box(lines, width=70, color=C.CYAN, title=""):
    """Draw a fancy box around text"""
    inner_width = width - 4
    top = f"{color}╭{'─' * (width - 2)}╮{C.RST}"
    bottom = f"{color}╰{'─' * (width - 2)}╯{C.RST}"
    
    print(top)
    if title:
        title_line = f" {title} "
        padding = (inner_width - len(title_line)) // 2
        print(f"{color}│{C.RST}{' ' * padding}{C.BOLD}{C.YELLOW}{title_line}{C.RST}{' ' * (inner_width - padding - len(title_line))}{color}│{C.RST}")
        print(f"{color}├{'─' * (width - 2)}┤{C.RST}")
    
    for line in lines:
        # Strip ANSI codes for length calculation
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = inner_width - len(clean)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{color}│{C.RST}{' ' * left_pad}{line}{' ' * right_pad}{color}│{C.RST}")
    
    print(bottom)

def main():
    clear_screen()
    hide_cursor()
    
    try:
        # Phase 1: Show Woody ASCII art with fade-in
        print(WOODY_ART)
        time.sleep(1.5)
        
        # Phase 2: Sparkle burst
        for _ in range(15):
            x = random.randint(10, 70)
            y = random.randint(2, 12)
            star = random.choice(STARS)
            color = random.choice(SPARKLES)
            move_cursor(y, x)
            print(f"{color}{C.BOLD}{star}{C.RST}", end='', flush=True)
            time.sleep(0.08)
        
        time.sleep(0.5)
        
        # Phase 3: Clear and show quote in fancy box
        clear_screen()
        
        # Build quote lines with styling
        quote_words = QUOTE.split(' ')
        lines = []
        current_line = ""
        
        for word in quote_words:
            test_line = current_line + (" " if current_line else "") + word
            if len(test_line) > 55:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        if current_line:
            lines.append(current_line)
        
        # Style each line
        styled_lines = []
        for i, line in enumerate(lines):
            if i == 0:
                styled_lines.append(f"{C.BOLD}{C.WHITE}{line}{C.RST}")
            elif i == len(lines) - 1:
                styled_lines.append(f"{C.ITALIC}{C.YELLOW}{line}{C.RST}")
            else:
                styled_lines.append(f"{C.CYAN}{line}{C.RST}")
        
        # Add attribution
        styled_lines.append("")
        styled_lines.append(f"{C.DIM}{C.GRAY}{ATTRIBUTION}{C.RST}")
        
        # Draw the box
        draw_box(styled_lines, width=70, color=C.MAGENTA, title="WOODY'S WISDOM")
        
        # Phase 4: Typewriter effect for the quote (reprint inside box)
        time.sleep(0.5)
        
        # Move to first quote line position (approximately line 6)
        move_cursor(6, 5)
        
        # Retype with typewriter effect
        full_quote = QUOTE
        for i, char in enumerate(full_quote):
            move_cursor(6 + i // 55, 5 + i % 55)
            if i < len(full_quote) * 0.3:
                print(f"{C.BOLD}{C.WHITE}{char}{C.RST}", end='', flush=True)
            elif i < len(full_quote) * 0.7:
                print(f"{C.CYAN}{char}{C.RST}", end='', flush=True)
            else:
                print(f"{C.ITALIC}{C.YELLOW}{char}{C.RST}", end='', flush=True)
            time.sleep(0.02)
        
        # Type attribution
        time.sleep(0.3)
        move_cursor(6 + len(lines) + 1, 5)
        typewriter(ATTRIBUTION, color=C.DIM + C.GRAY, delay=0.04)
        
        # Phase 5: Final sparkle flourish
        time.sleep(0.5)
        for _ in range(20):
            x = random.randint(5, 75)
            y = random.randint(3, 18)
            star = random.choice(STARS)
            color = random.choice(SPARKLES)
            move_cursor(y, x)
            print(f"{color}{C.BOLD}{star}{C.RST}", end='', flush=True)
            time.sleep(0.04)
        
        # Final pause
        move_cursor(22, 0)
        time.sleep(2)
        
    finally:
        show_cursor()
        print(C.RST)

if __name__ == "__main__":
    main()